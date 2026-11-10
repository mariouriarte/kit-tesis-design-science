#!/usr/bin/env python3
"""Maqueta entrega_alsie/IFI_ALSIE.md como IFI_ALSIE.docx (ALSIE, Carta, Arial 11).

Pasos: (1) preprocesa el Markdown (carátula, cuerpo, figuras), (2) pandoc con
plantilla institucional, (3) postproceso OOXML (tablas, secciones, numeración,
índices) y (4) dos pasadas con LibreOffice para obtener páginas reales.

No reescribe contenido científico. Las únicas exclusiones de texto están en
EXCLUSIONES y se informan en el informe de maquetación.
"""
import copy
import re
import shutil
import struct
import subprocess
import sys
import unicodedata
import zipfile
from pathlib import Path

from lxml import etree

ROOT = Path(__file__).resolve().parent.parent
REPO = ROOT.parent
FUENTE = REPO / "entrega_alsie" / "IFI_ALSIE.md"
BUILD = ROOT / "build"
FIG = ROOT / "figuras"
SALIDA = ROOT / "IFI_ALSIE.docx"

WNS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
RNS = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
NS = {"w": WNS, "r": RNS}


def q(tag):
    p, t = tag.split(":")
    return "{%s}%s" % ({"w": WNS, "r": RNS}[p], t)


# Fragmentos de trabajo que NO se imprimen (meta-narración, no contenido científico).
EXCLUSIONES = [
    " Representación Mermaid provisional para convertir en figura APA 7 conservando título y nota.",
]
PARRAFOS_EXCLUIDOS_PREFIJO = ["**Estado de revisión institucional:**"]

# Caja máxima de figura (cm): ancho útil 16,09; alto de reserva 17 (§6.1 del encargo)
CAJA_W, CAJA_H = 16.09, 17.0
ALTO_MAX = {1: 16.0}  # figura 1: reduce un poco para que su letra no supere 12 pt

ANCHO_UTIL = 9121  # twips


# ---------------------------------------------------------------------------
# 1. Preprocesado de Markdown
# ---------------------------------------------------------------------------
def dims_png(p):
    with open(p, "rb") as f:
        d = f.read(24)
    return struct.unpack(">II", d[16:24])


def leer_fuente():
    return FUENTE.read_text(encoding="utf8").split("\n")


def seccion(lineas, titulo):
    """Devuelve las líneas de contenido de un H1 `# titulo` (sin el encabezado)."""
    ini = next(i for i, l in enumerate(lineas) if l.strip() == f"# {titulo}")
    fin = next((i for i in range(ini + 1, len(lineas)) if lineas[i].startswith("# ")), len(lineas))
    return [l for l in lineas[ini + 1:fin]]


def caratula_md(lineas):
    c = [l.strip() for l in seccion(lineas, "Carátula") if l.strip()]
    # Estructura fija del IFI; se valida para no maquetar una carátula distinta
    esperado = ["**UNIVERSIDAD AUTÓNOMA DEL BENI**", "**«JOSÉ BALLIVIÁN»**", "**ALSIE CONSULTORES PEDAGÓGICOS**"]
    assert c[:3] == esperado, c[:3]
    logo = c[3]
    assert logo.startswith("[Logotipo"), logo
    titulo_rot, titulo = c[4], c[5]
    assert titulo_rot == "**TÍTULO**"
    grado, post, tutor, fecha, ciudad = c[6], c[7], c[8], c[9], c[10]
    sal = []

    def div(estilo, texto):
        sal.append(f'::: {{custom-style="{estilo}"}}\n{texto}\n:::\n')

    div("Caratula Universidad", c[0])
    div("Caratula Universidad", c[1])
    div("Caratula ALSIE", c[2])
    div("Caratula Logo", logo)
    div("Caratula Titulo", titulo_rot)
    div("Caratula Titulo", titulo)
    div("Caratula Campo", grado)
    div("Caratula Campo", post)
    div("Caratula Campo", tutor)
    div("Caratula Pie", fecha)
    div("Caratula Pie", ciudad)
    return "\n".join(sal)


def resumen_md(lineas):
    parrafos = [l for l in seccion(lineas, "Resumen") if l.strip()]
    assert len(parrafos) == 1
    return parrafos[0]


# Apartado reservado al tesista: el Markdown no trae un texto personal y no se redacta uno en su nombre.
# Para publicarlo, reemplazar este marcador por el texto de agradecimientos.
TEXTO_AGRADECIMIENTOS = "[Texto de agradecimientos pendiente: lo aporta el tesista]\n"

SECT_PLACEHOLDER = "@@SECT_{}@@"


def openxml(xml):
    return "```{=openxml}\n" + xml + "\n```\n"


def sect_par(n):
    return openxml(f"<w:p><w:pPr><w:pStyle w:val=\"Normal\"/></w:pPr><w:r><w:t>{SECT_PLACEHOLDER.format(n)}</w:t></w:r></w:p>")


def frontales_md(lineas):
    p = []
    p.append(caratula_md(lineas))
    p.append('\n::: {custom-style="Apartado"}\nAgradecimientos\n:::\n')
    p.append(TEXTO_AGRADECIMIENTOS)
    p.append('\n::: {custom-style="Apartado"}\nResumen\n:::\n')
    p.append(resumen_md(lineas))
    p.append('\n::: {custom-style="Apartado"}\nÍndice\n:::\n')
    p.append(openxml("<w:p><w:r><w:t>@@TOC@@</w:t></w:r></w:p>"))
    p.append('\n::: {custom-style="Apartado"}\nÍndice de tablas y figuras\n:::\n')
    p.append('\n::: {custom-style="Subapartado de índice"}\nTablas\n:::\n')
    p.append(openxml("<w:p><w:r><w:t>@@TOT@@</w:t></w:r></w:p>"))
    p.append('\n::: {custom-style="Subapartado de índice"}\nFiguras\n:::\n')
    p.append(openxml("<w:p><w:r><w:t>@@TOF@@</w:t></w:r></w:p>"))
    p.append(sect_par(1))
    return "\n".join(p)


def cuerpo_md(lineas):
    ini = next(i for i, l in enumerate(lineas) if l.startswith("# 1. Introducción"))
    out = []
    en_fence = False
    fig_n = 0
    modo_mermaid = False
    fence_len = 3
    region_anexo_a12 = False
    sect2_insertada = False
    for l in lineas[ini:]:
        mf = re.match(r"^(`{3,})(.*)$", l)
        if mf and (not en_fence or (re.fullmatch(r"`{%d,}\s*" % fence_len, l) is not None)):
            if en_fence:
                en_fence = False
                if modo_mermaid:
                    fig_n += 1
                    png = FIG / f"figura_{fig_n}.png"
                    w, h = dims_png(png)
                    alto = ALTO_MAX.get(fig_n, CAJA_H)
                    ancho = alto * w / h
                    if ancho > CAJA_W:
                        ancho = CAJA_W
                        alto = ancho * h / w
                    out.append('::: {custom-style="Imagen"}')
                    out.append(f"![Figura {fig_n}](figuras/figura_{fig_n}.png){{width={ancho:.2f}cm height={alto:.2f}cm}}")
                    out.append(":::")
                    modo_mermaid = False
                    continue
                out.append(l)
                continue
            en_fence = True
            fence_len = len(mf.group(1))
            modo_mermaid = l.strip() == "```mermaid"
            if modo_mermaid:
                continue
            out.append(l)
            continue
        if en_fence:
            if not modo_mermaid:
                out.append(l)
            continue

        # fuera de bloques de código
        m = re.match(r"^# (\d+)\. (.+)$", l)
        if m:
            titulo = m.group(2)
            if titulo == "Referencias bibliográficas":
                # fin de la numeración de páginas: sección 2 termina antes de Referencias
                out.append("")
                out.append(sect_par(2))
            out.append(f"# {titulo}")
            continue
        if re.match(r"^## Anexo [A-D]\.", l):
            region_anexo_a12 = l.startswith("## Anexo A.")
        if l.startswith("# ") and not re.match(r"^# (Introducción|Capítulo|Conclusiones|Recomendaciones|Referencias|Anexos)", l):
            # H1 interno de documentos transcritos en los anexos
            nivel = 1
            out.append("#" * min(nivel + 3, 6) + l[1:])
            continue
        mh = re.match(r"^(#{2,6}) (.*)$", l)
        if mh and region_anexo_a12:
            nivel, txt = len(mh.group(1)), mh.group(2)
            estructural = re.match(r"^(A\.\d+\.|Anexo [A-D]\.)", txt)
            if not estructural:
                out.append("#" * min(nivel + 3, 6) + " " + txt)
                continue
        out.append(l)
    texto = "\n".join(out)
    for frag in EXCLUSIONES:
        assert frag in texto, f"fragmento a excluir no encontrado: {frag!r}"
        texto = texto.replace(frag, "")
    lines = texto.split("\n")
    lines = [x for x in lines if not any(x.startswith(pf) for pf in PARRAFOS_EXCLUIDOS_PREFIJO)]
    return "\n".join(lines)


def construir_md():
    lineas = leer_fuente()
    frontal = frontales_md(lineas)
    cuerpo = cuerpo_md(lineas)
    md = frontal + "\n\n" + cuerpo + "\n"
    (BUILD / "ifi_maquetado.md").write_text(md, encoding="utf8")
    return md


# ---------------------------------------------------------------------------
# 2. pandoc
# ---------------------------------------------------------------------------
def pandoc():
    ent = BUILD / "ifi_maquetado.md"
    sal = BUILD / "raw.docx"
    subprocess.run([
        "pandoc", str(ent),
        "-f", "markdown-smart-tex_math_dollars-tex_math_single_backslash-auto_identifiers-implicit_figures-raw_tex-yaml_metadata_block",
        "-t", "docx",
        "--reference-doc", str(BUILD / "referencia.docx"),
        "--lua-filter", str(ROOT / "scripts" / "filtro.lua"),
        "--syntax-highlighting=" + str(ROOT / "scripts" / "tema_codigo.theme"),
        "--resource-path", str(ROOT),
        "-o", str(sal),
    ], check=True, cwd=ROOT)
    return sal


# ---------------------------------------------------------------------------
# 3. Postproceso OOXML
# ---------------------------------------------------------------------------
def norm(s):
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", " ", s.lower()).strip()


def ptext(p):
    return "".join(t.text or "" for t in p.iter(q("w:t")))


def pstyle(p):
    e = p.find("w:pPr/w:pStyle", NS)
    return e.get(q("w:val")) if e is not None else None


def set_pstyle(p, sid):
    ppr = p.find("w:pPr", NS)
    if ppr is None:
        ppr = etree.SubElement(p, q("w:pPr"))
        p.insert(0, ppr)
    e = ppr.find("w:pStyle", NS)
    if e is None:
        e = etree.Element(q("w:pStyle"))
        ppr.insert(0, e)
    e.set(q("w:val"), sid)


def ppr_of(p):
    ppr = p.find("w:pPr", NS)
    if ppr is None:
        ppr = etree.Element(q("w:pPr"))
        p.insert(0, ppr)
    return ppr


ORDEN_PPR = ["pStyle", "keepNext", "keepLines", "pageBreakBefore", "widowControl", "numPr", "pBdr", "shd", "tabs",
             "spacing", "ind", "jc", "outlineLvl", "rPr", "sectPr"]


def put_ppr(p, tag, attrs=None):
    ppr = ppr_of(p)
    e = ppr.find(f"w:{tag}", NS)
    if e is None:
        e = etree.SubElement(ppr, q(f"w:{tag}"))
    for k, v in (attrs or {}).items():
        e.set(q(f"w:{k}"), v)
    hijos = sorted(list(ppr), key=lambda x: ORDEN_PPR.index(etree.QName(x).localname) if etree.QName(x).localname in ORDEN_PPR else 99)
    for h in list(ppr):
        ppr.remove(h)
    for h in hijos:
        ppr.append(h)
    return e


ORDEN_RPR = ["rStyle", "rFonts", "b", "bCs", "i", "iCs", "caps", "smallCaps", "strike", "dstrike", "outline", "shadow",
             "emboss", "imprint", "noProof", "snapToGrid", "vanish", "webHidden", "color", "spacing", "w", "kern",
             "position", "sz", "szCs", "highlight", "u", "effect", "bdr", "shd", "fitText", "vertAlign", "lang"]


def ordenar_rpr(rpr):
    hijos = sorted(list(rpr), key=lambda x: ORDEN_RPR.index(etree.QName(x).localname)
                   if etree.QName(x).localname in ORDEN_RPR else 99)
    for h in list(rpr):
        rpr.remove(h)
    for h in hijos:
        rpr.append(h)


def run_rpr(r):
    rpr = r.find("w:rPr", NS)
    if rpr is None:
        rpr = etree.Element(q("w:rPr"))
        r.insert(0, rpr)
    return rpr


def sectpr_xml(tipo, header_rid=None, pg_start=None):
    h = f'<w:headerReference w:type="default" r:id="{header_rid}"/>' if header_rid else ""
    pg = f'<w:pgNumType w:start="{pg_start}"/>' if pg_start else ""
    return (
        f'<w:sectPr xmlns:w="{WNS}" xmlns:r="{RNS}">{h}<w:type w:val="nextPage"/>'
        f'<w:pgSz w:w="12240" w:h="15840"/>'
        f'<w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1701" w:header="709" w:footer="709" w:gutter="0"/>'
        f'{pg}</w:sectPr>'
    )


HDR_BODY = (
    f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f'<w:hdr xmlns:w="{WNS}" xmlns:r="{RNS}"><w:p><w:pPr><w:pStyle w:val="Header"/><w:jc w:val="right"/></w:pPr>'
    f'<w:r><w:fldChar w:fldCharType="begin"/></w:r><w:r><w:instrText xml:space="preserve"> PAGE </w:instrText></w:r>'
    f'<w:r><w:fldChar w:fldCharType="separate"/></w:r><w:r><w:t>1</w:t></w:r><w:r><w:fldChar w:fldCharType="end"/></w:r>'
    f'</w:p></w:hdr>'
)
HDR_VACIO = (
    f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
    f'<w:hdr xmlns:w="{WNS}" xmlns:r="{RNS}"><w:p><w:pPr><w:pStyle w:val="Header"/></w:pPr></w:p></w:hdr>'
)


def tabla_a_formato(tbl):
    """Aplica ancho útil, bordes APA, encabezado repetido y tamaño de letra."""
    filas = tbl.findall("w:tr", NS)
    ncol = len(tbl.findall("w:tblGrid/w:gridCol", NS))
    pt = 10 if ncol <= 3 else (9 if ncol <= 5 else 8)
    sz = str(pt * 2)

    # pesos de columna: texto total + palabra más larga (ancho mínimo para no partir palabras)
    pesos = [0.0] * ncol
    palabra = [0] * ncol
    for ri_, tr in enumerate(filas):
        for i, tc in enumerate(tr.findall("w:tc", NS)):
            if i < ncol:
                txt = "".join(t.text or "" for t in tc.iter(q("w:t")))
                pesos[i] = max(pesos[i], min(len(txt), 70)) * 0.35 + pesos[i] * 0.65
                mw = max((len(w_) for w_ in re.split(r"\s+", txt) if w_), default=0)
                palabra[i] = max(palabra[i], mw * (1.12 if ri_ == 0 else 1.0))
    minimos = [int(palabra[i] * pt * 10.6 + 150) for i in range(ncol)]
    if sum(minimos) > ANCHO_UTIL:
        # columnas rígidas (códigos/ID de pocas letras) conservan su mínimo; el resto se reduce
        rig = [i for i in range(ncol) if palabra[i] <= 7]
        fijo = sum(minimos[i] for i in rig)
        resto = sum(minimos[i] for i in range(ncol) if i not in rig)
        k = max((ANCHO_UTIL - fijo) / resto, 0.3) if resto else 1
        minimos = [minimos[i] if i in rig else int(minimos[i] * k) for i in range(ncol)]
    pesos = [max(p, 9.0) for p in pesos]
    tot = sum(pesos)
    anchos = [max(int(ANCHO_UTIL * p / tot), minimos[i]) for i, p in enumerate(pesos)]
    # reajuste para sumar exactamente el ancho útil: quitar exceso de las columnas más anchas
    exceso = sum(anchos) - ANCHO_UTIL
    while exceso > 0:
        j = max(range(ncol), key=lambda c: anchos[c] - minimos[c])
        if anchos[j] - minimos[j] <= 0:
            break
        d = min(exceso, max(1, (anchos[j] - minimos[j]) // 2))
        anchos[j] -= d
        exceso -= d
    anchos[-1] += ANCHO_UTIL - sum(anchos)

    tblpr = tbl.find("w:tblPr", NS)
    for e in list(tblpr):
        if etree.QName(e).localname in ("tblW", "tblLayout", "tblBorders", "tblLook", "tblCellMar"):
            tblpr.remove(e)
    tw = etree.SubElement(tblpr, q("w:tblW"))
    tw.set(q("w:w"), str(ANCHO_UTIL))
    tw.set(q("w:type"), "dxa")
    b = etree.SubElement(tblpr, q("w:tblBorders"))
    for lado in ("top", "bottom"):
        x = etree.SubElement(b, q(f"w:{lado}"))
        x.set(q("w:val"), "single"); x.set(q("w:sz"), "8"); x.set(q("w:space"), "0"); x.set(q("w:color"), "000000")
    lay = etree.SubElement(tblpr, q("w:tblLayout")); lay.set(q("w:type"), "fixed")
    cm = etree.SubElement(tblpr, q("w:tblCellMar"))
    for lado, v in (("top", 20), ("left", 60), ("bottom", 20), ("right", 60)):
        x = etree.SubElement(cm, q(f"w:{lado}")); x.set(q("w:w"), str(v)); x.set(q("w:type"), "dxa")

    grid = tbl.find("w:tblGrid", NS)
    for gc, a in zip(grid.findall("w:gridCol", NS), anchos):
        gc.set(q("w:w"), str(a))

    for ri, tr in enumerate(filas):
        trpr = tr.find("w:trPr", NS)
        if trpr is None:
            trpr = etree.Element(q("w:trPr"))
            tr.insert(0, trpr)
        for e in list(trpr):
            if etree.QName(e).localname in ("cantSplit", "tblHeader"):
                trpr.remove(e)
        etree.SubElement(trpr, q("w:cantSplit"))
        if ri == 0:
            etree.SubElement(trpr, q("w:tblHeader"))
        for ci, tc in enumerate(tr.findall("w:tc", NS)):
            tcpr = tc.find("w:tcPr", NS)
            if tcpr is None:
                tcpr = etree.Element(q("w:tcPr"))
                tc.insert(0, tcpr)
            for e in list(tcpr):
                if etree.QName(e).localname in ("tcW", "tcBorders"):
                    tcpr.remove(e)
            w = etree.Element(q("w:tcW"))
            w.set(q("w:w"), str(anchos[min(ci, ncol - 1)])); w.set(q("w:type"), "dxa")
            tcpr.insert(0, w)
            if ri == 0:
                bd = etree.Element(q("w:tcBorders"))
                x = etree.SubElement(bd, q("w:bottom"))
                x.set(q("w:val"), "single"); x.set(q("w:sz"), "6"); x.set(q("w:space"), "0"); x.set(q("w:color"), "000000")
                tcpr.insert(1, bd)
            for p in tc.findall("w:p", NS):
                set_pstyle(p, "CeldaTabla")
                for r in p.iter(q("w:r")):
                    rpr = run_rpr(r)
                    for e in list(rpr):
                        if etree.QName(e).localname in ("sz", "szCs", "rFonts"):
                            rpr.remove(e)
                    # orden: rFonts, b, i, ..., sz
                    rf = etree.Element(q("w:rFonts"))
                    for a in ("ascii", "hAnsi", "cs"):
                        rf.set(q(f"w:{a}"), "Arial")
                    rpr.insert(0, rf)
                    s = etree.SubElement(rpr, q("w:sz")); s.set(q("w:val"), sz)
                    s2 = etree.SubElement(rpr, q("w:szCs")); s2.set(q("w:val"), sz)
                    if ri == 0 and rpr.find("w:b", NS) is None:
                        etree.SubElement(rpr, q("w:b"))
                    ordenar_rpr(rpr)


def estructura_docx(raw, destino, paginas=None):
    """Postprocesa raw.docx -> destino.

    paginas: dict con 'toc', 'tot', 'tof' -> lista de números ya calculados
    (misma longitud que las entradas), o None para usar 0 como marcador.
    Devuelve las entradas del índice para el cálculo de páginas.
    """
    tmp = BUILD / "x"
    if tmp.exists():
        shutil.rmtree(tmp)
    with zipfile.ZipFile(raw) as z:
        z.extractall(tmp)

    doc_path = tmp / "word" / "document.xml"
    tree = etree.parse(str(doc_path))
    body = tree.getroot().find("w:body", NS)

    # --- Referencias y anexos
    ps = list(body.iter(q("w:p")))
    idx = {}
    for i, p in enumerate(ps):
        st = pstyle(p)
        if st == "Heading1":
            idx[norm(ptext(p))] = i
    i_ref = idx[norm("Referencias bibliográficas")]
    i_anx = idx[norm("Anexos")]
    for p in ps[i_ref + 1:i_anx]:
        if pstyle(p) in ("BodyText", "FirstParagraph") and not ptext(p).startswith(("Incorporaciones posteriores", "Las referencias corresponden")):
            set_pstyle(p, "Referencia")
    # Anexos: interlineado sencillo, sin sangría de primera línea
    for p in ps[i_anx + 1:]:
        st = pstyle(p)
        if st in ("BodyText", "FirstParagraph", "Compact", "BlockText"):
            put_ppr(p, "spacing", {"before": "60", "after": "120", "line": "276", "lineRule": "auto"})
            put_ppr(p, "ind", {"firstLine": "0"} if st != "BlockText" else {"left": "737", "firstLine": "0"})
            if st == "Compact":
                ppr = p.find("w:pPr", NS)
    # Cada Anexo (A–D) en hoja nueva, centrado y en mayúscula sostenida
    for p in ps[i_anx + 1:]:
        if pstyle(p) == "Heading2" and re.match(r"^Anexo [A-D]\.", ptext(p)):
            put_ppr(p, "pageBreakBefore")
            put_ppr(p, "jc", {"val": "center"})
            for r in p.iter(q("w:r")):
                rpr = run_rpr(r)
                if rpr.find("w:caps", NS) is None:
                    etree.SubElement(rpr, q("w:caps"))
                ordenar_rpr(rpr)

    # --- Código resaltado: fondo claro y borde fino en todo bloque con fichas de sintaxis
    # (rStyle *Tok distinto de NormalTok). Los bloques sin resaltado (transcripciones) no se tocan.
    for p in body.iter(q("w:p")):
        if pstyle(p) != "SourceCode":
            continue
        est = {e.get(q("w:val")) for e in p.iter(q("w:rStyle"))}
        if any(x.endswith("Tok") and x != "NormalTok" for x in est):
            put_ppr(p, "shd", {"val": "clear", "color": "auto", "fill": "F6F8FA"})
            bd = etree.Element(q("w:pBdr"))
            for lado in ("top", "left", "bottom", "right"):
                x = etree.SubElement(bd, q(f"w:{lado}"))
                x.set(q("w:val"), "single"); x.set(q("w:sz"), "4"); x.set(q("w:space"), "4"); x.set(q("w:color"), "D0D7DE")
            ppr_of(p).append(bd)
            put_ppr(p, "pBdr")  # reordena respetando el orden del esquema
            put_ppr(p, "ind", {"left": "113", "right": "113"})

    # --- Código en línea (fuera de bloques): monoespaciado a 10 pt para no verse diminuto en Arial 11
    for p in body.iter(q("w:p")):
        if pstyle(p) == "SourceCode":
            continue
        for r in p.iter(q("w:r")):
            rs = r.find("w:rPr/w:rStyle", NS)
            if rs is not None and rs.get(q("w:val")) == "VerbatimChar":
                rpr = run_rpr(r)
                for e in rpr.findall("w:sz", NS) + rpr.findall("w:szCs", NS):
                    rpr.remove(e)
                for tag in ("sz", "szCs"):
                    x = etree.SubElement(rpr, q(f"w:{tag}")); x.set(q("w:val"), "20")
                ordenar_rpr(rpr)

    # --- Tablas
    for tbl in body.iter(q("w:tbl")):
        tabla_a_formato(tbl)

    # --- Párrafos de imagen: asegurar alineación centrada y mantener con rótulo
    # (ya definidos por el estilo 'Imagen')

    # --- Marcadores de sección
    ps = list(body.iter(q("w:p")))
    sect_pars = {}
    for p in ps:
        t = ptext(p)
        m = re.fullmatch(r"@@SECT_(\d)@@", t)
        if m:
            sect_pars[int(m.group(1))] = p
    for n, p in sect_pars.items():
        for r in list(p.findall("w:r", NS)):
            p.remove(r)
        ppr = ppr_of(p)
        if n == 1:
            sx = etree.fromstring(sectpr_xml("nextPage"))
        else:
            sx = etree.fromstring(sectpr_xml("nextPage", header_rid="rIdHdrBody", pg_start=None))
        # la sección 2 reinicia la numeración en 1 (Introducción)
        if n == 2:
            pass
        ppr.append(sx)

    # La sección 1 (frontal) no lleva encabezado; la 2 (Introducción→Recomendaciones) sí, desde 1.
    # sectPr de la sección 2: reinicio de numeración en 1
    sx2 = sect_pars[2].find("w:pPr/w:sectPr", NS)
    pg = etree.SubElement(sx2, q("w:pgNumType")); pg.set(q("w:start"), "1")
    # pgNumType debe ir tras pgMar: ya está al final -> correcto.
    # Sección 3 final (Referencias, Anexos): encabezado vacío y numeración continua.
    final = body.find("w:sectPr", NS)
    if final is not None:
        body.remove(final)
    final = etree.fromstring(sectpr_xml("nextPage", header_rid="rIdHdrEmpty"))
    body.append(final)
    # La sección 2 debe iniciar su numeración en 1, pero su sectPr describe la sección que TERMINA
    # en ese párrafo (Introducción→Recomendaciones). Ver nota: pgNumType va en esa misma sectPr.
    # La sección 1 (frontal) usa encabezado vacío para no heredar numeración.
    s1 = sect_pars[1].find("w:pPr/w:sectPr", NS)
    # sin headerReference: la primera sección no hereda nada

    # --- Entradas de índice y marcadores
    entradas_toc, entradas_tot, entradas_tof = [], [], []
    bm_id = 100
    ps = list(body.iter(q("w:p")))
    en_cuerpo = False
    for p in ps:
        st = pstyle(p)
        t = ptext(p)
        if st == "Heading1" and norm(t) == norm("Introducción"):
            en_cuerpo = True
        if not en_cuerpo:
            continue
        clase = None
        if st in ("Heading1", "Heading2", "Heading3"):
            clase = ("toc", int(st[-1]))
        elif st == "RotuloTabla":
            clase = ("tot", 1)
        elif st == "RotuloFigura":
            clase = ("tof", 1)
        if clase is None:
            continue
        bm_id += 1
        nombre = f"_Toc{bm_id:06d}"
        bs = etree.Element(q("w:bookmarkStart")); bs.set(q("w:id"), str(bm_id)); bs.set(q("w:name"), nombre)
        be = etree.Element(q("w:bookmarkEnd")); be.set(q("w:id"), str(bm_id))
        ppr = p.find("w:pPr", NS)
        pos = 1 if ppr is not None else 0
        p.insert(pos, bs)
        p.append(be)
        if clase[0] == "toc":
            titulo = t.strip()
            if st == "Heading1":
                titulo = titulo.upper()
            entradas_toc.append((clase[1], titulo, nombre, st, t))
        else:
            # rótulo: "Tabla 2" (primer run) + salto + título
            runs = [r for r in p.iter(q("w:r")) if r.find("w:t", NS) is not None]
            etiq = "".join(x.text or "" for x in runs[0].findall("w:t", NS)).strip()
            tit = "".join("".join(x.text or "" for x in r.findall("w:t", NS)) for r in runs[1:]).strip()
            (entradas_tot if clase[0] == "tot" else entradas_tof).append((1, f"{etiq}. {tit}", nombre, st, etiq))

    def entrada_p(nivel, texto, bm, num, estilo):
        p = etree.Element(q("w:p"))
        ppr = etree.SubElement(p, q("w:pPr"))
        ps_ = etree.SubElement(ppr, q("w:pStyle")); ps_.set(q("w:val"), estilo)
        h = etree.SubElement(p, q("w:hyperlink")); h.set(q("w:anchor"), bm); h.set(q("w:history"), "1")
        r = etree.SubElement(h, q("w:r")); tt = etree.SubElement(r, q("w:t")); tt.text = texto
        tt.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        r2 = etree.SubElement(h, q("w:r")); etree.SubElement(r2, q("w:tab"))
        r3 = etree.SubElement(h, q("w:r")); t3 = etree.SubElement(r3, q("w:t")); t3.text = str(num)
        return p

    def campo(entradas, instr, estilo_fn, paginas_lista):
        ps_out = []
        for i, (nivel, texto, bm, st, orig) in enumerate(entradas):
            num = paginas_lista[i] if paginas_lista else 0
            p = entrada_p(nivel, texto, bm, num, estilo_fn(nivel))
            ps_out.append(p)
        # campo complejo: begin en el primer párrafo, end en el último
        def fc(tipo):
            r = etree.Element(q("w:r")); f = etree.SubElement(r, q("w:fldChar")); f.set(q("w:fldCharType"), tipo); return r
        ri = etree.Element(q("w:r")); it = etree.SubElement(ri, q("w:instrText")); it.text = instr
        it.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        first = ps_out[0]
        ppr = first.find("w:pPr", NS)
        k = list(first).index(ppr) + 1
        first.insert(k, fc("begin")); first.insert(k + 1, ri); first.insert(k + 2, fc("separate"))
        ps_out[-1].append(fc("end"))
        return ps_out

    def reemplazar(marker, pars):
        for p in list(body.iter(q("w:p"))):
            if ptext(p) == marker:
                padre = p.getparent()
                pos = list(padre).index(p)
                padre.remove(p)
                for j, np_ in enumerate(pars):
                    padre.insert(pos + j, np_)
                return
        raise RuntimeError(marker)

    p_toc = paginas["toc"] if paginas else None
    p_tot = paginas["tot"] if paginas else None
    p_tof = paginas["tof"] if paginas else None
    reemplazar("@@TOC@@", campo(entradas_toc, ' TOC \\o "1-3" \\h \\z \\u ', lambda n: f"TOC{n}", p_toc))
    reemplazar("@@TOT@@", campo(entradas_tot, ' TOC \\h \\z \\t "Rotulo Tabla,1" ', lambda n: "TableofFigures", p_tot))
    reemplazar("@@TOF@@", campo(entradas_tof, ' TOC \\h \\z \\t "Rotulo Figura,1" ', lambda n: "TableofFigures", p_tof))

    tree.write(str(doc_path), xml_declaration=True, encoding="UTF-8", standalone=True)

    # --- Encabezados, relaciones y tipos de contenido
    (tmp / "word" / "header1.xml").write_text(HDR_BODY, encoding="utf8")
    (tmp / "word" / "header2.xml").write_text(HDR_VACIO, encoding="utf8")
    rels = tmp / "word" / "_rels" / "document.xml.rels"
    r = rels.read_text(encoding="utf8")
    r = r.replace("</Relationships>",
                  '<Relationship Id="rIdHdrBody" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header1.xml"/>'
                  '<Relationship Id="rIdHdrEmpty" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/header" Target="header2.xml"/>'
                  '</Relationships>')
    r = r.replace("</Relationships>",
                  '<Relationship Id="rIdSettings" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/settings" Target="settings.xml"/></Relationships>')
    rels.write_text(r, encoding="utf8")
    # Word recalcula índices y números de página al abrir (pregunta una vez; aceptar con «Sí»)
    (tmp / "word" / "settings.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8" standalone="yes"?><w:settings xmlns:w="{WNS}">'
        '<w:updateFields w:val="true"/></w:settings>', encoding="utf8")
    ct = tmp / "[Content_Types].xml"
    c = ct.read_text(encoding="utf8")
    if 'Extension="png"' not in c:
        c = c.replace("<Override", '<Default Extension="png" ContentType="image/png"/><Override', 1)
    c = c.replace("</Types>",
                  '<Override PartName="/word/settings.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.settings+xml"/>'
                  '<Override PartName="/word/header1.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
                  '<Override PartName="/word/header2.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.header+xml"/>'
                  '</Types>')
    ct.write_text(c, encoding="utf8")

    # --- Metadatos básicos (datos de la carátula del propio IFI)
    (tmp / "docProps" / "core.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
        'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
        'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
        '<dc:title>Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones heredadas modelo-vista-controlador</dc:title>'
        '<dc:creator>Mario Arturo Uriarte Marin</dc:creator><dc:language>es-BO</dc:language>'
        '</cp:coreProperties>', encoding="utf8")
    zip_dir(tmp, destino)
    return entradas_toc, entradas_tot, entradas_tof


def zip_dir(src, destino):
    if Path(destino).exists():
        Path(destino).unlink()
    with zipfile.ZipFile(destino, "w", zipfile.ZIP_DEFLATED) as z:
        ct = src / "[Content_Types].xml"
        z.write(ct, "[Content_Types].xml")
        for p in sorted(src.rglob("*")):
            if p.is_file() and p != ct:
                z.write(p, p.relative_to(src).as_posix())


# ---------------------------------------------------------------------------
# 4. Páginas reales desde PDF (LibreOffice) y reconstrucción
# ---------------------------------------------------------------------------
def a_pdf(docx):
    subprocess.run(["soffice", "--headless", "--convert-to", "pdf", "--outdir", str(BUILD), str(docx)],
                   check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return BUILD / (Path(docx).stem + ".pdf")


def textos_paginas(pdf):
    out = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, check=True).stdout
    return out.split("\f")


def localizar(entradas, paginas, desde, intro_fisica):
    """Busca secuencialmente cada título (como línea de encabezado) en las páginas físicas."""
    res = []
    cur = desde
    for (_n, texto, _bm, st, orig) in entradas:
        clave = norm(orig)
        igual = st.startswith("Rotulo") or len(clave) <= 28
        pref = clave if igual else clave[:28]
        hallada = None
        for pg in range(cur, len(paginas)):
            for linea in paginas[pg].split("\n"):
                ln = norm(linea)
                if (ln == pref) if igual else ln.startswith(pref):
                    hallada = pg
                    break
            if hallada is not None:
                break
        if hallada is None:
            raise RuntimeError(f"No se localizó en PDF: {orig[:70]!r}")
        res.append(hallada - intro_fisica + 1)
        cur = hallada
    return res


def main():
    BUILD.mkdir(exist_ok=True)
    subprocess.run([sys.executable, str(ROOT / "scripts" / "crear_referencia.py")], check=True)
    construir_md()
    raw = pandoc()
    prov = BUILD / "paso1.docx"
    toc, tot, tof = estructura_docx(raw, prov, None)
    pdf = a_pdf(prov)
    pgs = textos_paginas(pdf)
    # página física de la Introducción: primera página cuyo texto contiene el encabezado y no es el índice
    intro_fisica = None
    for i, tx in enumerate(pgs):
        if any(norm(l) == "introduccion" for l in tx.split("\n")):
            intro_fisica = i
            break
    assert intro_fisica is not None, "No se halló la página de Introducción"
    d_toc = localizar(toc, pgs, intro_fisica, intro_fisica)
    d_tot = localizar(tot, pgs, intro_fisica, intro_fisica)
    d_tof = localizar(tof, pgs, intro_fisica, intro_fisica)
    estructura_docx(raw, SALIDA, {"toc": d_toc, "tot": d_tot, "tof": d_tof})
    pdf2 = a_pdf(SALIDA)
    pgs2 = textos_paginas(pdf2)
    print("páginas físicas:", len(pgs2) - (1 if not pgs2[-1].strip() else 0), "intro física:", intro_fisica + 1)
    print("TOC:", len(toc), "tablas:", len(tot), "figuras:", len(tof))


if __name__ == "__main__":
    main()
