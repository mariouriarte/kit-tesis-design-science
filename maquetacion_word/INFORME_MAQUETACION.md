# Informe de maquetación del IFI ALSIE

**Entregable:** `maquetacion_word/IFI_ALSIE.docx` (generado el 9 de noviembre de 2026).
**Fuente única de texto:** `entrega_alsie/IFI_ALSIE.md` en su versión vigente (commit `d537a62`, con glosas de códigos y tono impersonal), sin modificaciones. No existía un Word anterior versionado en el repositorio, por lo que no hubo versión que preservar.
**Estado:** composición editorial provisional, sujeta a la revisión visual del tesista en Word. No acredita aprobación institucional ni científica.

## 1. Qué se maquetó

| Elemento | Resultado |
|:--|:--|
| Página y márgenes | Carta; izquierdo 3,0 cm; superior, inferior y derecho 2,5 cm. |
| Cuerpo | Arial 11, justificado, interlineado doble, 12 pt antes y 8 pt después, sangría de primera línea de 1,27 cm. |
| Títulos | Apartados y capítulos: Arial 11, negrita, mayúscula sostenida, centrados, en hoja nueva. Epígrafes: negrita, mayúscula inicial, izquierda. Subepígrafes: negrita cursiva. Son estilos reales de Word (Título 1 a 3). |
| Carátula | Tahoma: universidad 16, ALSIE 14, rótulo y título 20, campos 14, fecha y ciudad 12. Sin numeración. |
| Orden | Carátula, Resumen, Índice, Índice de tablas y figuras, Introducción, Capítulos I–IV, Conclusiones, Recomendaciones, Referencias, Anexos A–D. |
| Índices | Campos TOC reales (contenido, tablas, figuras) con páginas calculadas sobre el render. Para actualizar en Word: seleccionar todo y pulsar F9. |
| Foliación | Arábiga, esquina superior derecha, desde la Introducción hasta Recomendaciones. Referencias y Anexos continúan la cuenta sin número visible. |
| Tablas | Ancho útil completo, bordes APA, encabezado repetido en continuaciones, filas sin cortar, Arial de 10, 9 u 8 pt según el número de columnas. |
| Figuras | Número en negrita y título en cursiva arriba; nota debajo, Arial 10, «Nota.» en cursiva. |
| Referencias | Sangría francesa de 1,27 cm, sin cambios en autores, años ni DOI. |
| Anexos | Cada anexo (A–D) en hoja nueva. Interlineado 1,15 y sin sangría de primera línea. |

## 2. Diagramas

Se renderizaron los cuatro bloques Mermaid con `@mermaid-js/mermaid-cli` 12.2.0 y Chromium del sistema, a escala 4 (`figuras/figura_1.png` a `figura_4.png`, con su fuente `.mmd`).

| Figura | Tamaño insertado | Letra física aproximada |
|:--|:--|:--|
| 1 | 13,55 × 16,00 cm | 11,7 pt |
| 2 | 9,46 × 17,00 cm | 8,8 pt |
| 3 | 16,09 × 7,84 cm | 9,3 pt |
| D1 | 16,09 × 5,15 cm | 9,3 pt |

La letra se calculó como tamaño CSS declarado en la fuente por el factor de escala de inserción, no a partir de píxeles. Inspección visual: la figura 2 muestra P1–P8 completos con el retorno a P2 y el nuevo incremento hacia P1. Las cuatro figuras aparecen sin recortes en el Word renderizado (según la foliación del documento: figura 1 en pág. 46, figura 2 en 58, figura 3 en 60 y figura D1 en 163).

## 3. Controles realizados

- Validación estructural del `.docx` con `validate.py` (esquemas OOXML): **aprobada**.
- Diferencias entre la fuente y el Markdown maquetado: solo prefijos numéricos de capítulo, bloques Mermaid sustituidos por imagen y las dos exclusiones del apartado 5.
- Ninguna palabra queda fuera de la caja útil en las 169 páginas (comprobación geométrica con `pdftotext -bbox`).
- Sin bloques Mermaid ni marcadores de trabajo impresos.
- Revisión visual de una muestra: carátula, resumen, índices, introducción, las cuatro figuras, tablas anchas (21, 4, 9, A1, A5), conclusiones, referencias, anexo A y bloques de código. **No se revisaron una por una las 169 páginas.**
- Conteo: **33 tablas** (24 principales y 9 de anexos) y **4 figuras** (1, 2, 3 y D1).
- Extensión de la Introducción: 11 páginas (1–11). Sobre el total del informe, que es el criterio literal de la guía («10 % del total de las páginas»), representa 6,7 % de las 163 páginas numeradas, o 6,5 % de las 169 totales: **cumple**. Si el total se acotara a Introducción–Recomendaciones (aprox. 76 páginas), sería cerca de 14,5 %: **no cumpliría**. No se recortó contenido para simular cumplimiento.

## 4. Pendientes y reservas

1. **Logotipo:** no existe archivo de logotipo en el repositorio. En la carátula permanece el marcador del Markdown: «[Logotipo institucional pendiente de incorporación y verificación]». Se requiere la imagen autorizada.
2. **Agradecimientos y Dedicatoria:** la página de **Agradecimientos** ya está incluida (hoja propia, entre la carátula y el Resumen) con el marcador «[Texto de agradecimientos pendiente: lo aporta el tesista]»; el Markdown no trae texto personal y no se redacta uno en su nombre. Para incorporarlo, reemplazar `TEXTO_AGRADECIMIENTOS` en `scripts/maquetar.py` y regenerar, o escribirlo directamente en Word. **Dedicatoria** sigue omitida.
3. **Paginación e índices:** calculados con LibreOffice. El documento lleva `updateFields`: al abrirlo, Word pregunta si actualizar los campos; responder **Sí** recalcula índice, índice de tablas y figuras y números de página. También se puede forzar con Ctrl+A y F9. La verificación final de páginas debe hacerse en Word.
4. **Tabla 21** (ocho columnas): a 8 pt algunas palabras largas se parten entre líneas. No se pierde contenido. Si se desea mejorarla, es decisión de composición (orientación horizontal u otro reparto).
5. **Código y transcripciones de anexos:** Courier New 8 pt (código en línea, 10 pt). Es una excepción a «Arial en todo el documento» (la guía no trata el código). Ver §6.
6. **Numeración de epígrafes:** se retiró solo el prefijo de trabajo delante del capítulo (p. ej. «2. Capítulo I» pasa a «Capítulo I»). Los números de epígrafe (1.1, 2.1, 3.1…) se conservaron porque el texto los cita (§1.3, sección 2.5). Los epígrafes del Capítulo I quedan numerados 2.x.
7. **Divergencias entre el encargo recibido y el repositorio.** Se siguió el repositorio (`encargo_composicion_final.md` y §6 de `referencia_presentacion_institucional.md`, derivado de la guía):
   - son **cuatro** diagramas (1, 2, 3 y D1), no tres;
   - sangría francesa de **1,27 cm**, no 0,5 cm;
   - títulos de nivel 2 y 3 en negrita.

## 5. Contenido de trabajo no impreso (requiere confirmación)

El Markdown contiene dos fragmentos que son meta-narración y no contenido científico. No se imprimieron:

- En la nota de la Figura 1: «Representación Mermaid provisional para convertir en figura APA 7 conservando título y nota.»
- Último párrafo del documento, «**Estado de revisión institucional:** …», que declara pendientes de la propia composición.

Además se omitieron las secciones «Agradecimientos» y «Dedicatoria» (ver punto 2) y las notas editoriales del «Índice» y de la lista de tablas y figuras del Markdown, sustituidas por campos automáticos. No se detectaron inconsistencias de contenido que obligaran a detener la maquetación. Quedan en el documento, por ser contenido del IFI, el párrafo «Incorporaciones posteriores autorizadas» (Referencias) y las notas de procedencia del Anexo C. Si desea impresos o suprimidos otros fragmentos, ajuste `EXCLUSIONES` en `scripts/maquetar.py`.

## 6. Código fuente con resaltado de sintaxis

- **Tema:** `scripts/tema_codigo.theme`, derivado de `tango` de pandoc con colores de mayor contraste para fondo claro (mínimo 4,99:1 sobre `#F6F8FA`): palabras clave azul `#0033b3` en negrita, cadenas verde `#067d17`, comentarios gris `#5c6670` en cursiva, números `#1750eb`, tipos `#1f6f8b`, variables `#001080`. Nunca hay texto claro sobre fondo claro.
- **Qué se resalta:** solo los bloques con lenguaje `php`, `bash`, `python` y `json` (15). Los bloques `markdown`, `text` y sin lenguaje son transcripciones literales de documentos: van en monoespaciado sin color (regla en `filtro.lua`, función `CodeBlock`). El tratamiento «más suave» para `markdown` fue ningún color: resaltar encabezados y negritas de un documento transcrito lo haría parecer código.
- **Caja:** los bloques resaltados llevan fondo `#F6F8FA` y borde fino `#D0D7DE` (postproceso en `maquetar.py`); los literales, no. Las líneas largas se ajustan dentro de los márgenes (0 palabras fuera de la caja útil en las 169 páginas).
- **Fuente:** Courier New 8 pt en bloques; 10 pt en código en línea. El render de LibreOffice sustituye Courier New por una métrica equivalente; en Word se usa Courier New.
- **Muestras visuales verificadas:** bloque PHP de pruebas (pág. física 123: palabras clave, cadenas, tipos y números legibles) y bloque bash/Node del Anexo A (pág. física 97, casi todo cadena, verde). El bloque `markdown` del Anexo A (pág. física 112) quedó en negro, sin color. El bloque JSON no se revisó visualmente.
- **Límite:** un bloque `bash` que contiene un programa completo entre comillas simples se colorea entero como cadena; es lo que el lexer reconoce, no un error.

## 7. Reproducción

```bash
cd maquetacion_word
# figuras (una por bloque; ya generadas en figuras/)
./node_modules/.bin/mmdc -p puppeteer.json -i figuras/diagrama_N.mmd -o figuras/figura_N.png -s 4 -b white
python3 scripts/maquetar.py          # genera IFI_ALSIE.docx (pandoc 3.11 + LibreOffice para páginas; el tema de código se carga de `scripts/tema_codigo.theme`)
```

Herramientas usadas: pandoc 3.10.2, `@mermaid-js/mermaid-cli` 12.2.0 (instalado solo en `maquetacion_word/node_modules`, ignorado por Git), Chromium del sistema, LibreOffice (`soffice`), `pdftotext`/`pdftoppm` (Poppler), Python con `lxml`. No se instaló nada global.
