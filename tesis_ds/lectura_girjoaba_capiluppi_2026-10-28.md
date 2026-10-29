# E5: identificación y lectura del documento de Girjoaba y Capiluppi

## Identificación y versión

**Fecha:** 28 de octubre de 2026. El tesista aportó el adjunto «PDF 1», con texto de doce páginas y figuras. Coinciden título, autores, caso ASML, interfaces Q y objeto del estudio con la publicación identificada mediante DOI `10.1109/ICSME58944.2024.00079`. **La falta de acceso al contenido queda resuelta mediante el adjunto**; no volver a solicitarlo como si solo tuviéramos el resumen. No se afirma que el archivo se haya copiado a `tmp/docs/` ni que sea binariamente idéntico al PDF del repositorio.

La primera página contiene una plantilla ACM, DOI `XXXXXXX.XXXXXXX`, ISBN provisional y, en el cuerpo, identificadores como «XYZ» y «University of ABC». Son indicios de una versión editorial no finalizada; no se establece su condición exacta sin comparar versiones. Crossref volvió a confirmar autores, actas **IEEE**, pp. 753–764 y DOI de publicación. Se conserva esa referencia editorial para identificar la obra y se declara que los pasajes analizados proceden del manuscrito aportado, con paginación 1–12; no se copia el DOI provisional ni se atribuye ACM como editor definitivo.

## Procedimiento documentado

Girjoaba y Capiluppi (2024, manuscrito aportado, secs. 2.3–2.4 y 4–5) tratan interfaces C++ obsoletas cuya funcionalidad sigue necesitándose internamente. El procedimiento no consiste simplemente en borrar: investiga usos, encapsula funcionalidad, actualiza pruebas y dependencias y verifica integración. Se desarrolla mediante investigación-acción durante la refactorización de seis interfaces y se estabiliza hacia las últimas iteraciones. Estos elementos constituyen un antecedente directo de formalización de un procedimiento incremental, no una novedad que pueda reclamarse por cambiar nombres.

| Paso del ciclo | Contenido contrastado en pp. 5–6 |
|:--|:--|
| 1. Investigar interfaz. | Localizar referencias, funcionalidad y dependencias; proponer ubicación y solución, discutir con el arquitecto y revisar principios SOLID. |
| 2. Migrar funcionalidad. | Implementarla internamente sin eliminar todavía los archivos o métodos originales; dejar de llamar a la interfaz original. |
| 3. Probar comportamiento. | Ejecutar pruebas tras la migración, separando sus errores de los de eliminación posterior. |
| 4. Retirar archivos y ajustar dependencias. | Eliminar referencias y archivos innecesarios, incluidos cambios pertinentes de configuración de construcción. |
| 5. Probar configuración de dependencias. | Comprobar los efectos sobre código y pruebas después de modificar conexiones y construcción. |
| 6. Integrar en rama superior. | Incorporar el cambio a la rama que acumula interfaces refactorizadas. |
| 7. Probar integración. | Ejecutar una comprobación del sistema y sus componentes conjuntamente. |

La coexistencia temporal de implementaciones sirve como punto de comprobación, y las pruebas se adaptan junto con el código cuando cambian sus conexiones. No se trasladan a SIGPP sus tiempos de construcción, ramificación o herramientas C++. Las interfaces de tipo 1, no utilizadas, no requieren todas las fases: el propio documento limita la aplicación uniforme del ciclo. El patrón aprovechable es la separación de migración, retirada y comprobación de conexiones, sujeto al comportamiento del incremento local.

## Evaluación y cautelas

| Aspecto | Evidencia del manuscrito | Límite de interpretación |
|:--|:--|:--|
| Participantes y unidades. | Seis interfaces, dos por cada uno de tres tipos; refactorizaciones realizadas por el primer autor; un caso industrial. | Seis interfaces no son seis contextos independientes ni seis desarrolladores. |
| Tiempo. | Tiempo por interfaz expresado como proporción del total; valores absolutos omitidos por confidencialidad, secs. 2.4 y 6. | No convertir diferencias de proporciones en porcentajes de ahorro relativo ni adoptar sus valores como metas de SIGPP. |
| Fallos. | Intentos que obligan a volver a una versión anterior por errores difíciles de rastrear; se contabilizan mediante ramas/intentos, secs. 4.2 y 6.3. | No equivalen a defectos en producción ni a cantidad de pruebas fallidas. Una métrica análoga debe definirse por adelantado si se utiliza. |
| Contraste estadístico. | Sec. 6.4: exclusión del tipo 1; comparación de primeras/segundas interfaces de tipos 2–3, cuatro observaciones en total; prueba t no pareada bilateral y `p = 0.0496`. | Muestra muy pequeña, tareas no asignadas aleatoriamente y evolución del conocimiento del autor: no acredita efecto causal aislado del método. No adoptar cambiar a prueba unilateral después de ver el resultado para mejorar el valor p. |
| Revisión institucional. | Sec. 6.5: valoración del responsable de diseño y aceptación de documentación para trabajos posteriores. | Es revisión interna de la organización, no aplicación independiente del ciclo por otro equipo. |
| Transferencia. | Secs. 2.4 y 7.3–7.4: extracción/encapsulación en sistemas muy acoplados, necesidad de conocimiento del código y evaluación futura en otros contextos. | No demuestra de antemano funcionamiento en flujos MVC, PHP o certificación POA; tampoco prueba que no pueda adaptarse a ellos. |

El aprendizaje del ejecutor y el orden de las tareas son explicaciones rivales reconocidas en el texto. Cambiar a interfaces de otro tipo no elimina automáticamente ese efecto, aunque los autores defiendan que reduce su impacto. Las afirmaciones de no introducir errores o conservar cobertura deben leerse en el alcance de sus comprobaciones; mantener pruebas no demuestra ausencia universal de defectos. Esta cautela informa nuestra evaluación futura sin invalidar el valor práctico del antecedente.

## Consecuencia para E5 y siguiente contraste

El contenido ya permite comparar investigación de dependencias, migración conservadora, pruebas de comportamiento y conexión, retiro posterior y ajuste del ciclo a partir de experiencia. La tesis no puede reclamar esos elementos como originales por sí mismos. Falta precisar si la selección y verificación del incremento de ejecución POA necesita una adaptación concreta frente a este procedimiento, Feathers y ADD, y cómo se evaluaría. Diferencias de lenguaje o institución no bastan para demostrar esa necesidad; E5 permanece abierta, sin nueva implementación o evaluación propia.

## Referencia editorial y estado de verificación

Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079

**Verificación:** metadatos editoriales reconfirmados en Crossref el 28 de octubre de 2026; contenido analizado mediante el manuscrito de doce páginas aportado por el tesista. Correspondencia exacta con la versión final publicada **[por verificar]**. La identificación de la obra y la disponibilidad de su contenido no quedan pendientes por esa diferencia de versión.
