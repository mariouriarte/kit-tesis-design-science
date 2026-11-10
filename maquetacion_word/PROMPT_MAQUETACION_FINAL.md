# Encargo de maquetación final del IFI ALSIE (para Claude)

> Este archivo es el encargo completo para regenerar y ajustar el Word del Informe Final de Investigación. Léelo entero antes de ejecutar.

## 1. Objetivo

Actualizar y regenerar el Word desde el Markdown vigente, aplicando la guía institucional [PDF 1], el resaltado de código, el logotipo y los textos de Agradecimientos/Dedicatoria recién incorporados. Es la versión actualizada del encargo anterior; ahora hay que incorporar estos ajustes nuevos.

**Nombre del entregable:** `IFI_ALSIE-mario-uriarte.docx` (y su PDF `IFI_ALSIE-mario-uriarte.pdf`).

## 2. Fuente única de texto

`entrega_alsie/IFI_ALSIE.md` (NO usar el `.docx` anterior como base). Este Markdown ya contiene:

- Glosas de códigos (P01/P02, I01–I04, E10/E8/E9, PA1–PA3, C01–C05, P1–P8, M-R1/M-P01).
- Limpieza de tono (se retiró «por WhatsApp», «se autorizó», «se adopta la hipótesis… para el IFI», etc.).
- **Agradecimientos** ya con texto: «A mi madre, Jaquelin, por creer siempre en mí, incluso en los momentos en que yo mismo dudaba.»
- **Dedicatoria** ya con texto: «A mi hija, Fernanda, mi mayor fuente de inspiración, por darme cada día un motivo para seguir creciendo y alcanzar mis metas.»

## 3. Guía institucional [PDF 1]

- **Ruta del PDF:** `tmp/1_Guía IFI_Ed 2_2023 Corrección Agosto 22, 2023.pdf`
- Léelo (si tienes lectura de PDF) y coteja su **sección B, páginas físicas 22–35**: papel, márgenes, tipografías, carátula, foliación, índices, tablas/figuras, notas, referencias y anexos.
- Las reglas ya están **extraídas** en `entrega_alsie/referencia_presentacion_institucional.md`, **§6** (con localizadores por página). Úsala como referencia de aplicación; el PDF es para confirmación visual. Donde la rúbrica vigente contradiga al PDF, manda la rúbrica; se mantiene APA 7.

## 4. Pipeline existente (reutilizar y extender)

`maquetacion_word/` ya contiene el pipeline funcional: `scripts/maquetar.py`, `scripts/crear_referencia.py`, `scripts/filtro.lua`, `scripts/tema_codigo.theme`, y las figuras en `maquetacion_word/figuras/`. Reutilízalo; no reconstruyas desde cero salvo defecto.

## 5. AJUSTES NUEVOS (obligatorios en esta pasada)

### 5.1. Logotipo automático

- El logotipo está en `maquetacion_word/figuras/logo.png` (105 KB).
- **Modifica `scripts/maquetar.py`** para que `caratula_md()` **inserte la imagen `figuras/logo.png`** en la carátula (centrada, tamaño moderado, encima del rótulo «TÍTULO:») en lugar de imprimir el texto marcador `[Logotipo institucional pendiente de incorporación y verificación]`.
- El marcador **no debe** aparecer impreso. Si el logo no se encuentra, detente y repórtalo (no imprimas el marcador ni inventes una imagen).

### 5.2. Agradecimientos y Dedicatoria

- Ya **no** se omiten: el Markdown trae el texto real de ambos. El pipeline debe **imprimirlos** (cada uno en su página, estilo de apartado preliminar, sin foliar).

### 5.3. Resaltado de código tipo IDE

- Ya existe `scripts/tema_codigo.theme` (paleta estilo GitHub). Verifica que el pipeline **aplique el resaltado de sintaxis** a los bloques con lenguaje (`php`, `bash`, `python`, `json`, `markdown`).
- Requisitos: **monospace** (Courier New o equivalente), **letra más pequeña que el cuerpo (8–9 pt)**, colores de buen contraste (que siga siendo legible).
- Los bloques ` ``` ` **sin** lenguaje (transcripciones literales de documentos) van en monospace **sin** resaltado.

## 6. Reglas de presentación (resumen operativo; prevalece §6)

| Elemento | Regla |
|:--|:--|
| Página | Carta; margen izquierdo 3 cm, resto 2,5 cm. |
| Cuerpo | Arial 11, justificado, interlineado doble, 12 pt antes / 8 pt después. |
| Carátula | Tahoma: universidad 16, ALSIE 14, rótulo/título 20, campos 14, fecha/ciudad 12; centrado; sin numerar. |
| Capítulos | Arial 11 negrita, mayúscula sostenida, centrados, hoja nueva. Epígrafes negrita a la izquierda; subepígrafes negrita cursiva. |
| Foliación | Arábiga, esquina superior derecha, desde Introducción hasta Recomendaciones. Referencias y Anexos continúan la cuenta sin número visible. |
| Figuras | Número en negrita y título en cursiva arriba; nota abajo en Arial 10. |
| Referencias | APA 7, sangría francesa 1,27 cm, orden alfabético. |
| Anexos | Cada anexo A–D en hoja nueva; interlineado 1,15 sin sangría. |

## 7. Restricciones

- No cambiar contenido científico, cifras, referencias, participantes ni limitaciones.
- Preservar las glosas y la limpieza de tono del Markdown (no revertirlas).
- No tocar ni recrear `entrega_alsie/figuras/` (fue eliminada; las figuras viven en `maquetacion_word/figuras/`).
- Índices (TOC) con campos reales; el tesista actualiza con F9 en Word.

## 8. Verificación obligatoria

- Renderizar el `.docx` a PDF y revisar **visualmente**: carátula con el logotipo, las 4 figuras (sobre todo la figura 2: P1–P8 y sus retornos), Agradecimientos/Dedicatoria, tablas anchas y una muestra de bloques de código con el resaltado.
- Confirmar que el código resaltado es legible (buen contraste).
- `git diff --check` limpio; no commitear binarios salvo indicación.

## 9. Entregable

Generar **dos archivos** en `maquetacion_word/`:

1. `IFI_ALSIE-mario-uriarte.docx` — Word final.
2. `IFI_ALSIE-mario-uriarte.pdf` — PDF generado desde el Word (render con LibreOffice), por si se necesita como copia de revisión/impresión.

Ambos deben quedar con la paginación y los campos de índice resueltos. Acompáñalos de un informe Markdown breve con: versión del Markdown usado, cambios aplicados al pipeline (logo automático, inclusión de preliminares, tema de resaltado), muestras verificadas y pendientes (paginación en Word, verificación con fuentes Arial/Tahoma reales).
