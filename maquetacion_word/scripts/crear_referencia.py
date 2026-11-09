#!/usr/bin/env python3
"""Crea build/referencia.docx con los estilos institucionales ALSIE (Carta, Arial 11).

Parte de la plantilla por defecto de pandoc y reemplaza/añade estilos.
Medidas en twips (1 cm = 566,93 twips) y medios puntos (sz = pt * 2).
"""
import re
import shutil
import subprocess
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILD = ROOT / "build"
W = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'

# Ancho útil = 12240 - 1701 (3,0 cm) - 1418 (2,5 cm) = 9121 twips
ANCHO_UTIL = 9121


def estilo(sid, nombre, tipo="paragraph", base=None, sig=None, ppr="", rpr="", extra=""):
    b = f'<w:basedOn w:val="{base}"/>' if base else ""
    n = f'<w:next w:val="{sig}"/>' if sig else ""
    p = f"<w:pPr>{ppr}</w:pPr>" if ppr else ""
    r = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    return (
        f'<w:style w:type="{tipo}" w:customStyle="1" w:styleId="{sid}">'
        f'<w:name w:val="{nombre}"/>{b}{n}<w:qFormat/>{extra}{p}{r}</w:style>'
    )


def estilo_builtin(sid, nombre, base=None, sig=None, ppr="", rpr="", tipo="paragraph"):
    b = f'<w:basedOn w:val="{base}"/>' if base else ""
    n = f'<w:next w:val="{sig}"/>' if sig else ""
    p = f"<w:pPr>{ppr}</w:pPr>" if ppr else ""
    r = f"<w:rPr>{rpr}</w:rPr>" if rpr else ""
    return (
        f'<w:style w:type="{tipo}" w:styleId="{sid}">'
        f'<w:name w:val="{nombre}"/>{b}{n}<w:qFormat/>{p}{r}</w:style>'
    )


ARIAL = '<w:rFonts w:ascii="Arial" w:hAnsi="Arial" w:cs="Arial" w:eastAsia="Arial"/>'
TAHOMA = '<w:rFonts w:ascii="Tahoma" w:hAnsi="Tahoma" w:cs="Tahoma" w:eastAsia="Tahoma"/>'
SZ = lambda pt: f'<w:sz w:val="{int(pt*2)}"/><w:szCs w:val="{int(pt*2)}"/>'
DOBLE = '<w:spacing w:before="240" w:after="160" w:line="480" w:lineRule="auto"/>'
SIMPLE = '<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>'

ESTILOS = []

# --- Cuerpo ---------------------------------------------------------------
ESTILOS.append(estilo_builtin(
    "Normal", "Normal",
    ppr='<w:spacing w:before="0" w:after="0" w:line="240" w:lineRule="auto"/>',
    rpr=ARIAL + SZ(11) + '<w:lang w:val="es-BO" w:eastAsia="es-BO" w:bidi="ar-SA"/>',
))
ESTILOS.append(estilo_builtin(
    "BodyText", "Body Text", base="Normal", sig="BodyText",
    ppr=DOBLE + '<w:ind w:firstLine="720"/><w:jc w:val="both"/>',
))
ESTILOS.append(estilo_builtin(
    "FirstParagraph", "First Paragraph", base="BodyText", sig="BodyText",
))
ESTILOS.append(estilo_builtin(
    "Compact", "Compact", base="Normal",
    ppr='<w:spacing w:before="0" w:after="120" w:line="480" w:lineRule="auto"/><w:jc w:val="both"/>',
))
ESTILOS.append(estilo_builtin(
    "BlockText", "Block Text", base="BodyText", sig="BodyText",
    ppr='<w:ind w:left="737" w:right="0" w:firstLine="0"/><w:jc w:val="both"/>',
))
# --- Títulos --------------------------------------------------------------
ESTILOS.append(estilo_builtin(
    "Heading1", "heading 1", base="Normal", sig="BodyText",
    ppr='<w:keepNext/><w:keepLines/><w:pageBreakBefore/><w:spacing w:before="0" w:after="240" w:line="480" w:lineRule="auto"/>'
        '<w:jc w:val="center"/><w:outlineLvl w:val="0"/>',
    rpr=ARIAL + '<w:b/><w:bCs/><w:caps/>' + SZ(11),
))
ESTILOS.append(estilo_builtin(
    "Heading2", "heading 2", base="Normal", sig="BodyText",
    ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="160" w:line="480" w:lineRule="auto"/>'
        '<w:jc w:val="left"/><w:outlineLvl w:val="1"/>',
    rpr=ARIAL + '<w:b/><w:bCs/>' + SZ(11),
))
ESTILOS.append(estilo_builtin(
    "Heading3", "heading 3", base="Normal", sig="BodyText",
    ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="160" w:line="480" w:lineRule="auto"/>'
        '<w:jc w:val="left"/><w:outlineLvl w:val="2"/>',
    rpr=ARIAL + '<w:b/><w:bCs/><w:i/><w:iCs/>' + SZ(11),
))
for n in (4, 5, 6):
    ESTILOS.append(estilo_builtin(
        f"Heading{n}", f"heading {n}", base="Normal", sig="BodyText",
        ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="200" w:after="120" w:line="276" w:lineRule="auto"/>'
            f'<w:jc w:val="left"/><w:outlineLvl w:val="{n-1}"/>',
        rpr=ARIAL + ('<w:b/><w:bCs/>' if n == 4 else '<w:b/><w:bCs/><w:i/><w:iCs/>') + SZ(11),
    ))
# Apartados sin entrada en el índice (Resumen, Índice, etc.)
ESTILOS.append(estilo(
    "Apartado", "Apartado",
    base="Normal", sig="BodyText",
    ppr='<w:keepNext/><w:pageBreakBefore/><w:spacing w:before="0" w:after="240" w:line="480" w:lineRule="auto"/><w:jc w:val="center"/>',
    rpr=ARIAL + '<w:b/><w:bCs/><w:caps/>' + SZ(11),
))
ESTILOS.append(estilo(
    "SubapartadoIndice", "Subapartado de índice",
    base="Normal", sig="Normal",
    ppr='<w:keepNext/><w:spacing w:before="240" w:after="120" w:line="276" w:lineRule="auto"/><w:jc w:val="left"/>',
    rpr=ARIAL + '<w:b/><w:bCs/>' + SZ(11),
))
# --- Rótulos, notas e imágenes ---------------------------------------------
ESTILOS.append(estilo(
    "RotuloTabla", "Rotulo Tabla", base="Normal", sig="Normal",
    ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="120" w:line="276" w:lineRule="auto"/><w:jc w:val="left"/>',
    rpr=ARIAL + SZ(11),
))
ESTILOS.append(estilo(
    "RotuloFigura", "Rotulo Figura", base="Normal", sig="Normal",
    ppr='<w:keepNext/><w:keepLines/><w:spacing w:before="240" w:after="120" w:line="276" w:lineRule="auto"/><w:jc w:val="left"/>',
    rpr=ARIAL + SZ(11),
))
ESTILOS.append(estilo(
    "Nota", "Nota", base="Normal", sig="BodyText",
    ppr='<w:keepLines/><w:spacing w:before="80" w:after="240" w:line="360" w:lineRule="auto"/><w:jc w:val="left"/>',
    rpr=ARIAL + SZ(10),
))
ESTILOS.append(estilo(
    "Imagen", "Imagen", base="Normal", sig="Nota",
    ppr='<w:keepNext/><w:spacing w:before="0" w:after="60" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>',
    rpr=ARIAL + SZ(11),
))
ESTILOS.append(estilo(
    "CeldaTabla", "Celda de tabla", base="Normal",
    ppr='<w:spacing w:before="20" w:after="20" w:line="240" w:lineRule="auto"/><w:jc w:val="left"/>',
    rpr=ARIAL + SZ(9),
))
# --- Carátula ---------------------------------------------------------------
def car(sid, nombre, pt, bold, antes=0, despues=0):
    return estilo(
        sid, nombre, base="Normal", sig="Normal",
        ppr=f'<w:spacing w:before="{antes}" w:after="{despues}" w:line="276" w:lineRule="auto"/><w:jc w:val="center"/>',
        rpr=TAHOMA + ('<w:b/><w:bCs/>' if bold else '') + SZ(pt),
    )

ESTILOS += [
    car("CaratulaUniversidad", "Caratula Universidad", 16, True, 0, 60),
    car("CaratulaALSIE", "Caratula ALSIE", 14, True, 120, 240),
    car("CaratulaLogo", "Caratula Logo", 12, False, 360, 360),
    car("CaratulaTitulo", "Caratula Titulo", 20, True, 120, 240),
    car("CaratulaCampo", "Caratula Campo", 14, False, 120, 120),
    car("CaratulaPie", "Caratula Pie", 12, False, 120, 60),
]
# --- Código -------------------------------------------------------------------
ESTILOS.append(estilo_builtin(
    "SourceCode", "Source Code", base="Normal",
    ppr='<w:keepLines/><w:spacing w:before="60" w:after="60" w:line="240" w:lineRule="auto"/><w:ind w:left="0"/><w:jc w:val="left"/>',
    rpr='<w:rFonts w:ascii="Courier New" w:hAnsi="Courier New" w:cs="Courier New"/>' + SZ(8),
))
# --- Índices ------------------------------------------------------------------
TABS = (
    '<w:tabs><w:tab w:val="right" w:leader="dot" w:pos="%d"/></w:tabs>' % ANCHO_UTIL
)
for n, izq in ((1, 0), (2, 284), (3, 567)):
    ESTILOS.append(estilo_builtin(
        f"TOC{n}", f"toc {n}", base="Normal", sig="Normal",
        ppr=TABS + f'<w:spacing w:before="{80 if n == 1 else 0}" w:after="40" w:line="240" w:lineRule="auto"/>'
            f'<w:ind w:left="{izq + 284}" w:hanging="284"/><w:jc w:val="left"/>',
        rpr=ARIAL + SZ(11) + ('<w:b/><w:bCs/><w:caps/>' if n == 1 else ''),
    ))
ESTILOS.append(estilo_builtin(
    "TableofFigures", "table of figures", base="Normal", sig="Normal",
    ppr=TABS + '<w:spacing w:before="0" w:after="30" w:line="240" w:lineRule="auto"/><w:ind w:left="567" w:hanging="567"/><w:jc w:val="left"/>',
    rpr=ARIAL + SZ(11),
))
# Referencias: sangría francesa 1,27 cm
ESTILOS.append(estilo(
    "Referencia", "Referencia", base="Normal", sig="Referencia",
    ppr='<w:spacing w:before="0" w:after="120" w:line="480" w:lineRule="auto"/><w:ind w:left="720" w:hanging="720"/><w:jc w:val="left"/>',
    rpr=ARIAL + SZ(11),
))
ESTILOS.append(estilo_builtin(
    "Header", "header", base="Normal",
    ppr='<w:tabs><w:tab w:val="right" w:pos="%d"/></w:tabs><w:jc w:val="right"/>' % ANCHO_UTIL,
    rpr=ARIAL + SZ(11),
))
# Estilos de carácter
CAR = [
    ('VerbatimChar', 'Verbatim Char', ARIAL + SZ(10)),
    ('Hyperlink', 'Hyperlink', ''),
]


def main():
    BUILD.mkdir(exist_ok=True)
    src = BUILD / "ref_default"
    if src.exists():
        shutil.rmtree(src)
    base_docx = BUILD / "ref_default.docx"
    with open(base_docx, "wb") as f:
        subprocess.run(["pandoc", "--print-default-data-file", "reference.docx"], stdout=f, check=True)
    with zipfile.ZipFile(base_docx) as z:
        z.extractall(src)

    sp = src / "word" / "styles.xml"
    s = sp.read_text(encoding="utf8")

    # docDefaults: Arial 11 y español de Bolivia, sin temas
    s = re.sub(r"<w:docDefaults>.*?</w:docDefaults>",
               '<w:docDefaults><w:rPrDefault><w:rPr>' + ARIAL + SZ(11) +
               '<w:lang w:val="es-BO" w:eastAsia="es-BO" w:bidi="ar-SA"/></w:rPr></w:rPrDefault>'
               '<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>',
               s, flags=re.S)

    nuevos = {re.search(r'w:styleId="([^"]+)"', e).group(1): e for e in ESTILOS}
    # eliminar estilos existentes con el mismo id y añadir los nuevos
    def quitar(m):
        sid = re.search(r'w:styleId="([^"]+)"', m.group(0)).group(1)
        return "" if sid in nuevos else m.group(0)
    s = re.sub(r"<w:style\b.*?</w:style>", quitar, s, flags=re.S)
    # reajustar estilos de carácter pandoc (VerbatimChar y enlaces)
    s = re.sub(
        r'(<w:style w:type="character"[^>]*w:styleId="VerbatimChar".*?</w:style>)',
        '<w:style w:type="character" w:customStyle="1" w:styleId="VerbatimChar"><w:name w:val="Verbatim Char"/>'
        '<w:rPr>' + ARIAL + SZ(10) + '</w:rPr></w:style>', s, flags=re.S)
    s = re.sub(r'<w:style w:type="character"[^>]*w:styleId="Hyperlink".*?</w:style>', '<w:style w:type="character" w:styleId="Hyperlink"><w:name w:val="Hyperlink"/><w:rPr/></w:style>', s, flags=re.S)
    s = s.replace("</w:styles>", "".join(nuevos.values()) + "</w:styles>")
    sp.write_text(s, encoding="utf8")

    # Sección final: Carta + márgenes (se reescribe luego en el postproceso)
    dp = src / "word" / "document.xml"
    d = dp.read_text(encoding="utf8")
    d = re.sub(r"<w:sectPr>.*?</w:sectPr>",
               '<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
               '<w:pgMar w:top="1418" w:right="1418" w:bottom="1418" w:left="1701" w:header="709" w:footer="709" w:gutter="0"/>'
               '</w:sectPr>', d, flags=re.S)
    dp.write_text(d, encoding="utf8")

    out = BUILD / "referencia.docx"
    if out.exists():
        out.unlink()
    with zipfile.ZipFile(out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src.rglob("*")):
            if p.is_file():
                z.write(p, p.relative_to(src).as_posix())
    print("OK", out)


if __name__ == "__main__":
    main()
