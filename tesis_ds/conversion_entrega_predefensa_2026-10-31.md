# Conversión externa de los dos documentos solicitados para predefensa

**Fecha:** 31 de octubre de 2026. El trabajo original DSR ya está consolidado en `tesis_ds/TRABAJO_ORIGINAL_DSR_AVANCE_2026-10-31.md`. La fuente institucional separada es `entrega_alsie/IFI_ALSIE_AVANCE.md`. Ambos son avances con pendientes explícitos, no informes de investigación concluida; la conversión no cambia esa condición.

Los comandos siguientes se entregan como procedimiento Markdown y deben ejecutarse externamente por el tesista. Pandoc 3.11, XeLaTeX, LibreOffice y las fuentes DejaVu se identificaron en el equipo durante la preparación; no se ejecutó la generación PDF o Word. No se afirma revisión visual, carga en Google Drive o cumplimiento integral del formato institucional. Si un archivo de salida ya existe, cambie el nombre para no reemplazar una versión editada.

## 1. Trabajo original DSR: PDF

```bash
pandoc \
  "/home/mario/Documents/tesis/kit-tesis-design-science/tesis_ds/TRABAJO_ORIGINAL_DSR_AVANCE_2026-10-31.md" \
  --from=markdown \
  --pdf-engine=xelatex \
  --metadata=lang:es \
  --variable=papersize:a4 \
  --variable=geometry:margin=2.5cm \
  --variable=fontsize:11pt \
  --variable="mainfont:DejaVu Serif" \
  --variable="monofont:DejaVu Sans Mono" \
  --output="/home/mario/Documents/tesis/kit-tesis-design-science/tesis_ds/TRABAJO_ORIGINAL_DSR_AVANCE_2026-10-31.pdf"
```

La fuente contiene texto y tablas Markdown, sin bloques Mermaid que requieran renderizador adicional. Los márgenes, tamaño y tipografía son opciones prácticas de conversión, no parámetros institucionales aprobados. El análisis de Pandoc reconoció diecisiete tablas y ningún bloque de código; no equivale a comprobar su ajuste visual en PDF. Revise especialmente tablas de indicadores, referencias, tildes y símbolos antes de compartir.

## 2. Documento ALSIE actual: Word

```bash
pandoc \
  "/home/mario/Documents/tesis/kit-tesis-design-science/entrega_alsie/IFI_ALSIE_AVANCE.md" \
  --from=markdown \
  --to=docx \
  --output="/home/mario/Documents/tesis/kit-tesis-design-science/entrega_alsie/IFI_ALSIE_AVANCE_2026-10-31.docx"
```

El docente solicita documento final ALSIE; la fuente disponible continúa siendo un avance provisional. Conserve esa advertencia y no cambie su condición por el nombre del archivo. Revise carátula, tablas, índice y diagrama: el IFI conserva un bloque Mermaid que este comando no convierte automáticamente en figura. No se incorpora una plantilla Word institucional porque no fue recibida o validada para esta conversión.

## 3. Diapositivas y carga

El tesista declara sus diapositivas preparadas. No se regeneran en esta tarea: compruebe apertura y use su archivo final. En la carpeta compartida del mensaje docente, cree `Mario Arturo Uriarte Marin` y suba el PDF DSR, el Word ALSIE disponible y las diapositivas. La exigencia de tenerlos antes de presentar procede del mensaje de las 07:45 aportado por el tesista, no de una comprobación de acceso realizada por este asesor (L. R. Pérez Rios, comunicación personal, 31 de octubre de 2026).

- [ ] PDF DSR abierto y revisado; no confundirlo con el IFI ALSIE.
- [ ] Word ALSIE abierto y revisado, con límites documentales conservados.
- [ ] Diapositivas preparadas por el tesista abiertas y revisadas.
- [ ] Tres archivos cargados en la carpeta nominal y acceso comprobado.

## Referencia técnica

Pandoc. (s. f.). *Pandoc user's guide*. https://pandoc.org/MANUAL.html

Se reutiliza la consulta de documentación oficial mediante Context7 para motor XeLaTeX, variables de márgenes y fuentes y escritura DOCX. Los comandos no se han ejecutado para producir entregables binarios en esta asesoría. La comunicación personal se cita únicamente en el texto conforme a APA 7.
