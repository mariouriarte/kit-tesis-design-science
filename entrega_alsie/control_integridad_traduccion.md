# Control documental de integridad de la traducción

## 1. Alcance y criterio

Este control identifica contenido efectivamente incorporado al IFI y cotejado contra las fuentes. No certifica nuevas aplicaciones, resultados favorables o aprobación institucional. La traducción mantiene el cierre de E0–E10 en sus alcances, los seis objetivos originales, los cuatro equivalentes institucionales ratificados y PA1–PA3 con sus reservas.

**Alcance vigente, precisado por el tesista:** se revisan el IFI actual y las fuentes finales pertinentes, no el archivo histórico completo. Se excluyen de nuevas pasadas basura, descartados, duplicados, predefensas y borradores superados sin contenido final necesario. Los cotejos ya resueltos se conservan; solo una discrepancia concreta justifica reabrirlos. La integridad exige aprovechar el contenido sustantivo final, no desarrollar indiscriminadamente todos los documentos inventariados. §11 actualiza las valoraciones frente a los cortes anteriores.

La revisión se rige por la rúbrica vigente, la guía de contenido, los indicadores compatibles y APA 7. Para las exigencias que esas fuentes ya definen no se condiciona el avance a auxiliares externos. No se supone el contenido de dichos auxiliares ni se añaden requisitos porque una nota los mencione. Los vacíos restantes se describen como datos o decisiones verificables.

## 2. Transcripciones exactas incorporadas

Se comparó el texto de cada bloque con su origen. Para programas y salida JSON se cotejó el bloque completo; para los archivos íntegros se excluyó únicamente el salto final de línea al delimitar el bloque. Las huellas siguientes corresponden al contenido cotejado, no al archivo completo del IFI. Las rutas de A.6–A.15 y A.21–A.25 son relativas a `tesis_ds/`; A.16–A.20 y A.27 proceden del historial de SIGPP identificado en §§8/10. Se contabilizan veintidós bloques exactos en A.6–A.27: A.21 contiene dos, A.26 no contiene un bloque cercado y el programa interno de A.25 no se cuenta aparte. A.26 añade tres extractos literales de seguimiento, sin etiqueta de remitente, cotejados por separado.

| Destino | Fuente original | Contenido | SHA-256 cotejado |
|:--|:--|:--|:--|
| A.6 | `instrumento_i03_cierre_bisiesto_e6.md` | Programa B01/B02 completo. | `a91b7d552b844de8fc7cda63fa5b6b7aa1ea59422c1f30e01b94a36432aaee16` |
| A.7 | `comprobacion_ordinaria_pantalla_e6.md` | Programa O01–O05 y control completo. | `241d715f22884f98d50dcf145fcc6a5a3ea8e7bbca7fc61dfc2e7cabecf98d90` |
| A.8 | `comprobacion_cierre_mensual_e6.md` | Programa M08/M09 y control completo. | `acf71a6fc94bbb49b2dcadfbc5a54f8ce64a52dd94cda5cce1e40addd79aabbe` |
| A.9 | `comprobacion_o06_servidor_e6.md` | Programa O06 completo y condiciones de aislamiento. | `d9657e1f6cdc0af31427539c43d9e4157bbb426eda103a60c05bec2c965e9048` |
| A.10 | `comprobacion_formulario_temporal_e6.md` | Programa de formulario completo. | `c9ae37409c244a0b27fff0c5b066b5c7f28b361479a1dc8619295832908c05fc` |
| A.11 | `comprobacion_interacciones_fechas_gestion_e6.md` | Programa S31/S14/S16 completo. | `686066f45bf4ce627f001984d6aa794f22d5e1c9c274b2f96d1e5f28f3bc8c55` |
| A.12 | `cuestionario_planificacion_certificacion.md` | Cuestionario recibido completo: autorización, doce casos, seis aclaraciones, respuestas y cierre. | `d4928fb88f6e8d6c992f9cbb052aef98b2d356c597ef0e6d40e916ac8b06f341` |
| A.13 | `instrumento_observacion_aplicacion_metodo.md` | Esquema original completo de registro y sus instrucciones. | `cae3591d435ea27067a4110fbe477535e4bc6bec4b9260eab8cd9320035edea2` |
| A.14 | `mensaje_confirmacion_entrevista_2026-11-03.md` | Consulta preparada completa, identificada como propuesta posteriormente corregida. | `a040ebd387aa08133e9d7543a5ae64d5ae7ac77f191ed774181fcd7e7e0e3cff` |
| A.15 | `resultado_i03_cierre_bisiesto_e6.md` | Salida JSON original completa. | `88c32e2422cfc0aaf1b4f5a3a2cbdab1ff45a2b86aa54a174a5c0d9dc2b5fd91` |
| A.16 | SIGPP `docs/development/fecha-documental-tesis-evidencia.md` | Informe histórico completo, sin salto final; rótulo y tiempos originales aclarados fuera del bloque. | `43deb8a795c17db1ee10b3924759da9d85c86f40d2f65f476ff8f939eba648a7` |
| A.17 | SIGPP `docs/development/fecha-hora-i03-evidencia.md` | Informe histórico completo, sin salto final; distinción de propiedad funcional e indicador humano. | `911ba7d55fcb76c9c6f96de3acf8bacdf7da52b10d62462cc6d6778dade48c96` |
| A.18 | SIGPP `tests/Certificacion/CreateCertificacionServiceTest.php` | Archivo PHP completo, sin salto final; incluidos los dos métodos y su preparación. | `52db9264df33875df7a40b002153901842b239f6aec92f4bdf154e558dd695bf` |
| A.19 | SIGPP `tests/Certificacion/RestrictionSelectionFixture.php` | Auxiliar PHP completo, sin salto final; se conserva gestión 2025. | `556887c3449d0584ecc6ef8d68f28da53032b66229756d4c08b2435f2de73c9a` |
| A.20 | SIGPP `tests/Certificacion/RestrictionSelectionCharacterizationTest.php` | Archivo PHP completo, sin salto final; instrumento común de trece casos. | `c6e3c89b578ad93e79f1ac6726f4327ee41c4826612c69a12fb569b03713cfd2` |
| A.21, Python | `comparacion_extraccion_restriccion_2026-10-29.md`, §6 | Programa completo de carga histórica, sin ejecutarlo. | `1ec7a8cbdbee7722ef5831cdf4887ac2f61433322cf0da894ca85f45abc52844` |
| A.21, Bash | Misma fuente y sección | Comando completo del estado posterior, sin ejecutarlo. | `25e69f994808f3c4698914ce11d9875973b202b19c41b06e75f829b03bef3a7b` |
| A.22 | `bitacora_i03_cierre_bisiesto_e6.md` | Archivo completo, sin salto final; incluye todos los intentos, cierres, reformulaciones y consolidación. | `20fb9541cf242af916dc36ca40c190389c9e09ae57491f79f6230705b43fc1cc` |
| A.23 | `propuesta_actividad_i03_cierre_bisiesto_e6.md` | Instrucciones completas de la actividad humana A/B/C, sin salto final. | `4e9f3105b9bab676996798674abd632ceb9dae89ad54f3b83becce0a8ae41da7` |
| A.24 | `matriz_escenarios_temporales_e6.md` | Matriz completa, sin salto final; estados históricos conservados con precedencia explícita. | `1e6ed569d29aa0e93c906c681a9ee199feafe20f2569cadd61bb159ba9b954c6` |
| A.25 | `instrumento_i03_cierre_bisiesto_e6.md` | Documento completo, sin salto final, incluido el programa ya transcrito en A.6. | `5e6f583a0f0548cb2cad9f184dab4a904753d2e95cb48109c6cfbf4abda685e1` |
| A.27 | SIGPP `5e0fec3d854f0cf74feaa4935caeb19736b40bbb:tmp/propuesta-tesis.md`, §2.5 | Sección completa de 76 líneas, sin saltos finales; cuatro matrices originales y métricas pendientes diferenciadas. | `a8b8fd15985afbfdbb1d594ed6123b3cd03e254bad7cc6de7b5451a8cb5097b5` |

Las transcripciones de programas, archivos PHP y comandos no fueron ejecutadas. La comparación fue textual; no se valida de nuevo su compatibilidad con un entorno actual ni se presume disponibilidad de imágenes históricas. Los estados intermedios, resultados fallidos, controles separados y limitaciones de capas conservan sus fechas y fuentes. Reproducir documentalmente un bloque no constituye otro caso de evaluación. Los dos bloques de A.21 se cotejan literalmente con los bloques Python y Bash de `comparacion_extraccion_restriccion_2026-10-29.md`, §6; sus huellas figuran en esta tabla y su alcance en §8.

## 3. Destino del resto de productos principales

| Conjunto de fuentes | Destino y control actual |
|:--|:--|
| `00_estado.md` y control final de coherencia | Vigencia, identidad, precedencia de formulaciones y límites; mapa y perfil institucional. Los pendientes históricos no reabren cierres. |
| E1–E3: áreas, delimitación y perfil | Contexto, situación/brecha, objeto/campo y compromisos; §§1–2 y tabla 23 preservan seis objetivos y resultados parciales. |
| E4/E5, mapa D01–D09 y referencias | Capítulo II: fuentes, decisiones y siete comparadores originales; complemento regional/nacional separado cronológicamente. |
| E6 y matrices/registros citados | Capítulo I y Anexo A: cuatro indicadores, expectativas, fallos, fuentes funcionales, I03 descriptivo e I04 no medido. |
| E7a–E7c | Alternativas, catorce requisitos, diseño, roles, relaciones y dos diagramas operativos; capítulos III–IV. |
| E7d/E7e | Producto mínimo, plan V1–V3, riesgos, cronología y verificación; §5.6, sin atribuir construcción histórica al método. |
| E7f y manual M-R1 | Guía de ocho pasos y ficha reproducible; §5.4 y Anexo B. |
| E8, revisiones P01/P02/importe y rediseño | §§5.7–5.9/5.11: episodios, cuatro ajustes, resultados por fuente, ayudas, distintos alcances de integración y amenazas. |
| E9 | Matriz vigente T01–T14 y cobertura R1–R14 íntegras en §5.10; grados negativos/no medidos conservados. |
| E10 y balance global | Relaciones PA1–PA3, respaldo/condiciones/amenazas, conclusiones y recomendaciones. Cinco candidatos anteriores identificados como historia, no conjunto final concurrente. |
| Arquitectura de referencia y ejemplo de importe | §5.5/5.9 y Anexo D; no otra aplicación o muestra independiente. |

Esta tabla registra los destinos principales, no demuestra por sí sola aprovechamiento línea por línea de todos los auxiliares. El inventario específico `inventario_instrumentos_diagnostico.md` coteja 25 fuentes locales directas y seis fuentes Git, con aspectos, resultados y destinos. Se diferencia ese alcance de los veintidós bloques literales y del aprovechamiento completo del resto del corpus. No se utiliza la extensión como prueba de integridad.

## 4. Exclusiones justificadas y límites restantes

- `ficha_validacion_funcional_certificacion.md` se identifica como instrumento preparado, no aplicado y sin respuestas. No se transforma en una aplicación adicional ni se publica su identificación nominal como si estuviera autorizada por el consentimiento posterior limitado al cargo. El cuestionario efectivamente recibido está completo en A.12.
- X01–X06 e I04 son expectativas aceptadas de una capacidad no construida; A.4 conserva condiciones y resultados esperados, no salidas inventadas. No existe un programa ejecutado que deba fabricarse para completar un anexo.
- Las rutas de los dos informes iniciales no estaban presentes en el directorio de trabajo consultado. Esa ausencia dejó de ser una reserva de disponibilidad al recuperarse ambos objetos originales del historial de SIGPP, revisión `7c0bca084b05c462137fd62c24e6b025bb09a12c`. Se transcribieron íntegros en A.16–A.17, junto a los archivos de prueba y preparación en A.18–A.20. No se describen como perdidos ni se solicitan al tesista.
- Los resultados de esos dos ensayos siguen siendo los originales reportados e inspeccionados en E6/tabla 3. La recuperación confirma su soporte documental, no reproduce la ejecución. Se mantienen discrepancia del auxiliar, fallo de expectativa, limitación de reloj y corrección de los rótulos históricos. El original no fue reconstruido ni corregido para hacerlo parecer metodológicamente uniforme.
- Los formularios operativos nominales de P01/P02 y los originales sensibles conservan referencias y revisión pública acotada; las transcripciones no autorizan publicar identidades o datos institucionales. No se confunde el esquema original A.13 con todos los formularios diligenciados externos.
- Persisten revisión de exhaustividad de los auxiliares y cotejo de todo dato/figura de origen frente al IFI. Es una tarea documental pendiente, no motivo para pedir nuevas aplicaciones o completar metas mediante ingeniería adicional.

## 5. Consecuencias para la autoevaluación

ANX-1 conserva Bien, 1/1, por originales identificados completos; no por volumen o reproducción nueva. Se mantienen límites de comandos y código medido sin exigir una ejecución adicional. CI-3 se reexamina en Bien, 3/3: las tablas 1–4 y anexos contienen resultados de los instrumentos aplicados, incluidos errores, negativos, controles y medidas ausentes. El criterio no exige auditar descartes o todo el archivo histórico; esa penalización añadida se retira. El total actual es 92,40/100, sin cambios de resultados o conclusiones científicas. Los cortes anteriores se conservan como registro, no como pendientes activos.

V06 deja de ser una solicitud de documentos externos para requisitos ya definidos. Esto no agregó puntos a CIV-3, que ya estaba acreditado por estructura con autor y desarrollo. La incorporación de originales no cambió entonces HIP-1, POB-1, CII-2 o REF-2. La posterior resolución de la formulación institucional de hipótesis se registra separadamente; ninguna de estas operaciones cambia evidencia científica, relaciones resueltas o reservas de generalización.

El IFI no se declara cerrado por estas transcripciones. Las consultas se refieren a datos reales, no a pedir auxiliares normativos externos o ratificar decisiones ya aceptadas. El tesista precisó dos mantenedores, incluido él, y confirmó que P01/P02 no integraban ese equipo: colaboraron para las actividades, con P01 en otro proyecto. Se conservan las funciones de cada episodio y la aplicación adicional del autor; no se infiere otra institución o proyecto actual de P02. No se vuelven a preguntar tamaño o pertenencia ya resueltos ni se equiparan con población técnica, censo, autonomía o independencia plena.

## 6. Precisión posterior de hipótesis y unidades

Se cotejaron HIP-1 y POB-1 con su texto normativo. El primero evalúa estructura afirmativa, novedad concreta y relación lógica causa-efecto; no se añade aprobación del tutor o experimento prospectivo como condición que no contiene. La exigencia de fundamentación y veracidad se mantiene: no se afirma causalidad aislada ni que una frase posterior fuera contrastada literalmente antes. Después de ajustar la redacción sin códigos o siglas, el tesista adoptó mediante «aceptado» la hipótesis de diseño del §1.5, derivada de las relaciones finales y sin reabrir PA1–PA3. V03 queda resuelto en cuanto a formulación institucional, no como comprobación causal nueva.

En la aplicación se observa cada paso aplicado a una tarea, como dice el instrumento original; técnicamente se examinan decisiones, consumidores y efectos. Tres familias fueron examinadas en el conjunto, dos en las aplicaciones y tres episodios documentados: P01/M-P01, P02/M-R1 e importe/M-R1 con suplemento. El diagnóstico temporal no pasa a ser otro episodio de aplicación. No se computan automáticamente ocho pasos por tres episodios como veinticuatro observaciones estadísticas independientes, ni aserciones como personas.

No se redefine la población después de los resultados como un conjunto censal de episodios. Se explicitan selección analítica y límites de cuantificación de la clase; POB-1 no se convierte en una obligación adicional de inventariar todo el código. La adopción de la hipótesis y las precisiones de unidades no modifican datos, escenarios, evaluación, contribución final, conclusiones u originales transcritos. La revisión de HIP-1 puntúa la formulación y fundamentación explícitas, no una supuesta evidencia empírica producida por aceptar el texto.

Atendiendo la observación del tesista, el enunciado adoptado se presenta sin identificadores de versión ni siglas; nombra el método y describe el mismo sistema institucional de planificación operativa y presupuesto. La trazabilidad de versiones permanece en el capítulo IV, sin renombrar oficialmente el sistema o sustituir materiales de episodios anteriores. La prohibición expresa de abreviaturas de TIT-1 no se amplía como regla general inexistente de HIP-1: la corrección responde a claridad y la aceptación se limita a esa formulación y su alcance declarado.

La reevaluación de HIP-1 distingue formulación y prueba. El enunciado adoptado cumple afirmación, solución concreta, características, finalidad y relación lógica causa-efecto; novedad incremental y fundamento contextual se explican junto a sus límites. Se valora Bien, 2/2, por ese contenido, no porque la respuesta del autor demuestre el efecto causal. Ese cambio de 0,80 a 2 situó el total entonces en 91,05/100; el inventario posterior actualiza únicamente ANX-1 según §5/§9. La etiqueta Excelente corresponde a la banda de la escala, no a un dictamen del tribunal o una recomendación efectiva de publicación. No se alteran resultados/conclusiones para obtener puntuación.

## 7. Cotejo bibliográfico posterior

`control_bibliografico_apa7.md` registra contraste de metadatos de once fuentes, con páginas primarias, registros depositados y versiones arXiv. La verificación impidió falsas correcciones: se mantiene Zou frente a una cubierta añadida con Zhou y la paginación 2:1–14 de Fischer frente al identificador de recurso a13. Los campos confirmados de Abbasi no se convierten en un número de artículo inventado o en lectura completa tras un acceso limitado.

No se añadieron fuentes o resultados al IFI, que conserva 29 referencias y el recuento de actualidad; REF-3 mantiene su observación por límites precisados. Esta operación no certifica renovación externa de todo el corpus ni sustituye el cotejo pendiente de auxiliares. La posterior recuperación de los dos informes se registra en §8, sin conservar su no localización como pendiente actual. En ese corte la puntuación era 91,05/100; el inventario posterior de §9 actualiza ANX-1. El cierre institucional continúa pendiente de las reservas efectivamente registradas.

## 8. Recuperación histórica y comparación retrospectiva

**Fecha de recuperación documental:** 8 de noviembre de 2026, posterior al corte científico. **Repositorio:** `/home/mario/dev/sf_projects/sipoa4`. **Revisión conservada:** `7c0bca084b05c462137fd62c24e6b025bb09a12c`; fecha de autor registrada `2026-10-30T16:03:14-04:00`; mensaje `test(certificacion): add characterization tests for documentary date rules`. La lectura se realizó mediante `git show REV:ruta` y la identificación de objetos mediante `git rev-parse REV:ruta`; sin cambiar rama, reconstruir archivos en SIGPP, instalar dependencias o ejecutar PHP/PHPUnit/Docker. La fecha del commit identifica conservación, no verifica independientemente cada marca temporal del relato.

| Destino | Objeto Git conservado | SHA-256 del archivo completo, incluido salto final |
|:--|:--|:--|
| A.16 | `8c3b0fdca7268bd6a89d924b133a928b547711a7` | `d6c89541aa294901ba461b37edc13c76d824234fe6abb4b2168e7d78a8b30e34` |
| A.17 | `21aff1b108fa5e765242e40fd6ab7cef3ee6ee0b` | `27124bf35e3920000639574debef13f6af91fb487c18d0da8111eb008cb6bd19` |
| A.18 | `808a0927a09ae06ece802a2e9ea63ae7bea3eb1f` | `2afcde36a886554563d84d91b7480ec888961972c2578aec81aa7d7358d6ead5` |
| A.19 | `c9cf8118f7f54b5afa3d36add1b43fd10e8c64b3` | `8858b9550ad0c5b44d31edc344d5825b200f4248a367e508e9022c2c73b95bd3` |
| A.20 | `21030cc458cdd9f8d6193b0964b703dd5ce06e1c` | `a07d03edff44961f199fa5b446df6dc1c00293bf6f3a216c2fff12b0ccfbe505` |

Los dos últimos archivos coinciden por su huella completa con los identificados en la comprobación retrospectiva del 29/10, `tesis_ds/comparacion_extraccion_restriccion_2026-10-29.md`, §6. El programa de carga histórica y el comando posterior de esa sección se conservaron en A.21; este último contiene dos bloques, no dos aplicaciones nuevas. La comparación conserva trece pruebas/65 aserciones por estado, entorno actual y adaptación de carga en memoria: no identidad de entornos históricos, integración completa, evidencia prospectiva de desarrollo dirigido por pruebas o mejora de esfuerzo.

Los informes conservan una prueba/una aserción/un fallo y tres pruebas/cinco aserciones/un fallo. Sus comandos, salidas, marcas y reservas fueron cotejados con E6. «I03» en el segundo título es un identificador histórico de propiedad funcional, distinto del indicador vigente de minutos humanos; la corrección se coloca fuera de la transcripción. No se añade un cuarto episodio ni se computan 178 segundos o dieciséis segundos del agente como esfuerzo humano. El archivo PHP combinado es el conservado después de ambas adiciones, no prueba de que todo su contenido estuviera presente idéntico antes de cada ensayo. Las indicaciones operativas internas se conservan como registro, no como instrucciones actuales o reglas institucionales.

**Verificación del corte de recuperación:** diecisiete bloques literales, veintiún apartados A indexados, mapa/Anexo C iguales salvo encabezados, 44 criterios/91,05 puntos, resumen235,24 tablas y catorce filas T01–T14,29 referencias,cercas equilibradas y tres respaldos intactos. Ese corte precede al inventario y ampliación de §9; no describe el número actual de bloques/apartados. No se ejecutaron las pruebas transcritas.

## 9. Inventario específico y correcciones del diagnóstico

El primer corte de `inventario_instrumentos_diagnostico.md` registró D01–D25 y G01–G05; después se agregó G06 según §10. Distingue instrumentos aplicados, preparados/no aplicados, inspecciones, antecedentes, continuidad y evaluación posterior. Los catorce documentos del contexto constan como inventario de la revisión del tesista; no fueron inspeccionados nuevamente en binario durante este control ni se convierten en catorce normas CPS. No se certifica aprovechamiento completo de los auxiliares E4–E10.

Se añadió el contenido íntegro de A.22–A.25 y los tres extractos de A.26, cotejados literalmente. La referencia MDN de A.22 y las instrucciones internas permanecen dentro del original como metadatos históricos, no como nueva consulta o fuente teórica directa del IFI. Las notas superadas de etapas abiertas tienen aclaración externa; las fechas/casos/duraciones originales no se alteran.

La tabla 3 se amplió a los seis casos de formulario con fechas finales, envío/sincronización/validez/campo, excepción y error de transformación, y a los tres escenarios de servicio con sus interacciones. Se explicitaron identidad/fecha/total, relación con seguimiento, orden y contador anticipado; se preservaron primer intento interrumpido, discrepancias y ausencia de día operativo. En §2.5 se conservaron por separado los cierres 4,75/1,72/2,55 segundos de I03 y la consolidación única de C2/C3. En §2.4 se identificaron los once componentes del recuento inicial y la afirmación histórica superada sobre falta de prueba del servicio.

En ese corte, D20 conservó una reserva de procedencia porque el desglose no aparecía en los Markdown del kit cotejados. La búsqueda posterior en versiones Git de SIGPP recuperó el registro y resolvió su localización, sin solicitarlo al tesista o fabricarlo. No se impone automatización como condición de una medición que pudo ser manual. El límite actual de comandos, fecha y código medido se distingue de la disponibilidad ya acreditada del registro.

**Estado del corte previo a G06:** veintiún bloques, tres extractos, veintiséis apartados A; 44 criterios, 91,40/100, ANX-1 0,75/1 y CI-3 2,25/3. §10 registra el estado actualizado. Este avance no modifica indicadores, episodios, muestra, PA1–PA3, contribución o conclusiones.

## 10. Recuperación del registro de recuentos iniciales

La revisión adicional de `tmp/propuesta-tesis.md` en tres estados del historial de SIGPP encontró su §2.5 en `5e0fec3d854f0cf74feaa4935caeb19736b40bbb` —archivo de 458 líneas—, no en los ejemplares de 315 líneas de `5313c0e150859d86dd9d82b1df21f719d2242076` y `7ef29a4f438e5d2474d39b67f530cb940c922e76`. Objeto recuperado `2f8b2bbaedb148206f4525d00f5c9c4ee1b3ede0`; SHA-256 completo `7c72cdfdf685e9e7c722c986a1eb869c55d113a47b54b92db14da10f4f7173d4`. La sección íntegra de 76 líneas se transcribe en A.27 y su huella figura en §2. El encabezado aparece una sola vez; la búsqueda no descubrió dos matrices independientes duplicadas.

La tabla 3 incorpora sus once filas de tamaño/métodos públicos, ocho anotaciones de ruta, cuatro grupos por nombre y seis búsquedas en pruebas; los seis agregados resumidos anteriormente permanecen en el análisis previo. La suma de líneas de las once filas coincide con 4177; es comprobación aritmética documental, no nueva medición de SIGPP. Los grupos nominales no se suman como conjuntos disjuntos y las ocurrencias textuales no se convierten en casos, cobertura o calidad. El cero histórico de referencias al servicio fue superado por la inspección del 18/10. Los objetivos preliminares de medir complejidad/cobertura/esfuerzo no se transforman en resultados obtenidos.

Se resuelve la localización del registro, no la trazabilidad exacta de comandos, fecha y código medido que este no contiene. Se conservan tales límites sin exigir al tesista reconstrucción de memoria, un programa inexistente o repetición actual que se presente como pasada. La revisión del contexto/otros auxiliares sigue pendiente y no se confunde con omitir instrumentos originales ya incorporados.

**Estado al incorporar A.27:** inventario D01–D25/G01–G06; veintidós bloques exactos, tres extractos y veintisiete apartados A indexados; 44 criterios, ANX-1 1/1 y total entonces de 91,65/100. §11 registra el reexamen posterior de CI-3. No se ejecutaron nuevas pruebas ni se modificó `tesis_ds/` o SIGPP.

**Verificación final de este corte:** literalidad de los veintidós bloques y tres extractos, veintidós huellas del manifiesto, índice A.1–A.27, mapa/Anexo C idénticos salvo nivel de encabezados, 44 códigos/pesos/factores y evidencias textuales cotejados. Total 91,65/100: 34 Bien, siete con observaciones y tres que requieren mejora; subtotal del elemento 11 de 4,55/6. Se mantienen resumen de 235 palabras, 24 tablas principales, 37 filas de resultados en tabla 3, catorce filas T01–T14 y 29 referencias. Coinciden aritméticamente las 4177 líneas del registro y los 1593,87 segundos del autoinforme, sin convertir ese cotejo en medición nueva. Se preservan tres huellas del respaldo, cercas Markdown equilibradas y ausencia de cambios Git informados en `tesis_ds/` y SIGPP. La comprobación mecánica no reemplaza la revisión contextual y visual pendiente.

## 11. Revisión final limitada al documento pertinente

El tesista señaló el costo de revisar históricos y descartes que no entrarán al IFI. Se retiró el pendiente genérico de recorrer todos los auxiliares o desarrollar obligatoriamente catorce documentos de contexto. Se preserva el cotejo ya realizado, sin volver a abrir esos archivos o borrar evidencia incorporada. La siguiente revisión debe indicar un apartado vigente, un criterio y una corrección concreta.

CI-3 se cotejó con el texto exacto de la rúbrica: exige presentar los resultados de todos los instrumentos aplicados y aspectos medidos. Las tablas 1–4 y anexos ya cumplen esa exigencia en el conjunto identificado. La observación anterior se apoyaba en una auditoría histórica indiscriminada, no en un resultado omitido identificado; por ello se corrige de 2,25 a 3/3. El total queda en 92,40/100: 35 Bien, seis con observaciones y tres que requieren mejora. La corrección no acredita éxito de I01–I04, causalidad o efectos no medidos.

Se verifican solo el cambio de criterio, sus evidencias, subtotales y sincronización del mapa/Anexo C. Se mantienen los controles previos de originales sin repetirlos; solo se reabrirían ante discrepancia concreta. Persisten pendientes normativos de bibliografía, presentación y población/muestra, y limitaciones científicas que no se resuelven mediante nuevas construcciones o eliminación retórica de reservas.
