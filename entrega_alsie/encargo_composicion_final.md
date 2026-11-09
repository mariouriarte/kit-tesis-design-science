# Encargo de regeneración y control visual del IFI ALSIE

## Estado y alcance

Encargo preparado el 8 de noviembre de 2026 a solicitud del tesista. **Pendiente de ejecución por un proceso autorizado para generar imágenes y Word.** Este archivo no acredita regeneración, inspección visual o conformidad del documento final. El asesor DS entrega exclusivamente Markdown; no se ha invocado ni delegado automáticamente otro agente.

La investigación E0–E10 está cerrada en los alcances y con las limitaciones de `tesis_ds/00_estado.md`. La tarea es editorial: no reabrir la investigación ni cambiar resultados, criterios, participantes, principios PA1–PA3 o límites de las conclusiones.

## Fuentes obligatorias

- `entrega_alsie/IFI_ALSIE.md`: fuente vigente del contenido y de los cuatro diagramas Mermaid. No reconstruir el texto desde el Word anterior.
- `entrega_alsie/referencia_presentacion_institucional.md`, §6: especificación de composición documentada a partir de la guía aportada; contiene localizadores y reservas.
- `entrega_alsie/autoevaluacion_indicadores.md`: observaciones y controles pendientes; su puntuación documental no certifica la composición final.
- `entrega_alsie/IFI_ALSIE.docx`: versión anterior con recortes detectados. Conservarla antes de sustituirla y no presentarla como corregida.

La guía institucional está identificada en la especificación como Santos Santos, A. (2023), *Guía para la elaboración del informe final de investigación* (2.ª ed.), aportada por el tesista. Para este encargo se reutiliza la inspección documentada; no se declara una nueva verificación independiente del ejemplar.

## Secuencia de ejecución

1. Preservar el Word y las imágenes anteriores en una ubicación identificada antes de sustituirlos. Inspeccionar las herramientas disponibles; no instalar dependencias o cambiar la configuración global sin necesidad y autorización correspondiente.
2. Extraer los cuatro diagramas de la fuente vigente y regenerar las figuras 1, 2, 3 y D1. No reutilizar imágenes antiguas por coincidencia de nombre. Mantener textos, componentes, sentidos y conexiones; cualquier ajuste adicional del trazado debe conservar el contenido y quedar registrado.
3. Inspeccionar visualmente las cuatro imágenes completas y a su tamaño previsto de inserción. Corregir solapamientos, recortes y tamaños ilegibles antes de componer el documento. En la figura 2 deben aparecer P1–P8 y sus retornos completos.
4. Generar un Word nuevo desde el Markdown vigente con estilos institucionales explícitos. No repetir la conversión anterior con sus valores predeterminados. Preservar tablas, notas, referencias, anexos y remisiones; no incorporar este encargo ni otros documentos de trabajo al cuerpo del IFI.
5. Actualizar los índices y campos con paginación real. Renderizar el Word y revisar todas las páginas; utilizar archivos temporales de inspección cuando el proceso autorizado lo requiera, sin confundirlos con entregables aprobados.
6. Corregir los defectos encontrados, actualizar campos y volver a renderizar. Entregar el Word corregido solo con un informe Markdown que identifique versión, comprobaciones efectivamente realizadas y pendientes residuales. Si no se puede inspeccionar el resultado renderizado, declararlo provisional.

## Reglas de composición que no deben omitirse

La especificación completa de §6 prevalece sobre este resumen operativo.

| Elemento | Aplicación requerida |
|:--|:--|
| Página | Carta; margen izquierdo 3 cm y restantes 2,5 cm. |
| Cuerpo | Arial 11, justificado, interlineado doble; espaciados según §6. |
| Portada | Datos propios confirmados, sin comentarios de trabajo; Tahoma y tamaños según §6. No inventar ni copiar un logotipo no verificado. |
| Capítulos y epígrafes | Jerarquía institucional y capítulos I–IV; normalizar localizadores editoriales sin romper índices o remisiones. |
| Imágenes | Alto contraste y Arial; conservar proporción y limitar ancho y alto simultáneamente. Área de página útil de 16,09 × 22,94 cm, antes de rótulos, notas y espaciados. |
| Tamaño de figuras | Caja inicial máxima de imagen de 16,09 × 17 cm, ajustable al espacio real: 17 cm es una reserva operativa, no una exigencia institucional. Letra física entre 8 y 12 puntos. Si no cabe legiblemente, reorganizar el trazado, no reducirlo hasta hacerlo ilegible. |
| Rótulos y notas | Número y título arriba de la figura, nota debajo; mantener conjunto sin recortes. Formatos específicos según §6 y APA 7. |
| Tablas | Texto legible, ancho dentro de márgenes, encabezados reconocibles en continuaciones y ningún contenido perdido o recortado. |
| Referencias | APA 7; conservar datos, orden alfabético y sangría francesa de 1,27 cm. |
| Índices y foliación | Páginas reales, no estimadas. Numeración y alcance según §6; índices de tablas y figuras en hojas nuevas. |
| Anexos | Cada anexo comienza en hoja nueva; no limitar un anexo extenso a una sola página. |

## Criterios de aceptación y evidencia

| Control | Evidencia mínima que debe registrar el ejecutor |
|:--|:--|
| Cuatro figuras regeneradas | Correspondencia con cada bloque vigente, archivos producidos y comprobación visual individual. |
| Conservación de diagramas | Textos, componentes y conexiones cotejados con la fuente; P8 completo y retornos de figura 2 visibles. |
| Legibilidad física | Dimensiones de inserción y tamaño de letra resultante comprobados; declarar el procedimiento utilizado, no inferir puntos impresos desde píxeles CSS. |
| Composición sin recortes | Páginas renderizadas identificadas para cada figura y revisión de todas las tablas. Una imagen correcta fuera del Word no basta. |
| Aplicación institucional | Tamaño de página, márgenes, fuentes, interlineado, portada, encabezados, notas, referencias, foliación y saltos cotejados. |
| Integridad de contenido | Ninguna sección, tabla, figura, nota, referencia o anexo omitido; ausencia de bloques Mermaid sin convertir o comentarios de trabajo impresos. |
| Índices | Correspondencia de títulos y páginas después de la última recomposición. |
| Extensión de Introducción | Porcentaje calculado con la paginación final y criterio de cómputo explícito; contrastar límite de 10 % sin suprimir contenido científico para simular cumplimiento. |
| Logotipo | Identidad y autorización verificadas o pendiente expresamente declarado; un marcador no constituye portada final aprobada. |
| Resultado | Informe Markdown con controles satisfactorios, defectos corregidos y reservas. No declarar aprobación institucional o científica a partir de una revisión editorial. |

## Condiciones de entrega

El ejecutor debe indicar la ruta exacta del Word nuevo y la ubicación preservada del anterior; registrar herramientas y versiones efectivamente utilizadas, sin inventar ejecuciones. No efectuar commits, publicaciones o carga a servicios externos salvo solicitud expresa. Los originales y datos institucionales no deben publicarse para resolver la composición.

**Estado al preparar este encargo:** Word anterior localizado; fuente Markdown corregida; imágenes y Word nuevos no generados por este asesor; aceptación editorial final pendiente.
