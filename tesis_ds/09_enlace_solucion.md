# E9. Enlace propuesta ↔ solución

## Estado vigente: E9 cerrada el 7 de noviembre de 2026

El tesista acepta mediante «acepto» la lectura de la matriz y el cierre de E9 como trazabilidad completa y explícita. La aceptación no convierte los catorce requisitos en satisfechos ni valida por sí sola PA1–PA3. Se conservan grados parciales, ausencia de medición y límites; posteriormente E10 adoptó la contribución acotada y su dictamen, con habilitación de traducción según el control final y `00_estado.md`. No se vuelve a solicitar aceptación de E9 ni de etapas o episodios ya resueltos.

E8 fue cerrada expresamente como evaluación realizada con resultados parciales. Esta revisión incorpora P01, el rediseño M-R1, P02 y la aplicación del autor sobre importe; no modifica objetivos o criterios ni convierte indicadores ausentes en éxitos. Las secciones históricas del 4 de noviembre se conservan al final y no acreditan por sí solas el cierre actual. El respaldo y alcance final de PA1–PA3 corresponden al dictamen adoptado en E10, no a que la matriz tenga todas sus filas.

## A. Fuentes de la cadena actual

| Código | Fuente y función |
|:--|:--|
| EV-D | `06_diagnostico.md`, matriz de escenarios y comprobaciones citadas allí: existencia del problema y resultados diagnósticos I01–I04. |
| EV-F | `revision_aplicacion_p01_2026-11-05.md`: aplicación formativa asistida, productos y verificación final, con P7 parcial. |
| EV-R | `registro_redisenio_metodo_mr1.md` y `metodo_refactorizacion_incremental_mr1.md`: hallazgos → decisiones aprobadas → cambios RD01–RD04/P3/P5/P7/P8. |
| EV-S | `revision_aplicacion_p02_2026-11-06.md`, sección 7: dictamen aceptado, productos y niveles de comprobación de la evaluación posterior. |
| EV-A | `revision_aplicacion_autor_importe_2026-11-07.md`, secciones 3–6 y 10: criterios A01–A05, estado final reproducido, decisiones y límites. |
| EV-B | `balance_global_evaluacion_2026-11-07.md`: objetivos, requisitos, candidatos PA1–PA3, contraste con antecedentes y cierre acotado E8. |

El anexo `anexo_ejemplo_aplicacion_importe.md` es una representación explicativa de EV-A, no una observación adicional ni un nuevo participante. EV-F/EV-S y EV-A corresponden a referencias y baterías diferentes; sus pruebas no se suman como si fueran una muestra común. Las fuentes permiten distinguir resultados reproducidos por la asesoría, secuencias relatadas y aspectos sin medición. Esa procedencia se conserva en los grados de cumplimiento.

## B. Matriz actual: problema → requisito → decisión → criterio → evidencia → grado → límite

| ID | Problema o necesidad | Requisito | Decisión de diseño | Criterio/indicador | Evidencia correspondiente | Grado de cumplimiento | Límite |
|:--|:--|:--|:--|:--|:--|:--|:--|
| T01 | Intervenir por estructura de archivos sin justificar necesidad/frontera. | R1, R2 | Delimitar decisión, consumidores, efectos y exclusiones; admitir revisión justificada de la frontera. | Escenario de cambio y delimitación identificables antes de transformar. | EV-S/P1; EV-A/P1–P4: dos consumidores en restricciones y decisión/observación/intervención diferenciadas en importe. | Respaldado en aplicaciones asistidas. | Tareas seleccionadas previamente; no selección autónoma entre riesgos ni frontera óptima demostrada. |
| T02 | Confundir preservación con corrección o capacidad nueva. | R3 | Registrar observado, requerido e intención; conservar cambios funcionales fuera de la extracción. | Transformación clasificada y expectativas por caso. | EV-R conserva intención de P01; EV-S/P2/P5; EV-A/A01–A05, umbral/mensajes mantenidos. | Respaldado en conservación acotada. | No demuestra aplicación evaluada a toda combinación de corrección/extensión. La regla temporal sigue sin corregirse. |
| T03 | Mover comportamiento sin una comprobación previa pertinente. | R4 | Caracterizar y comprobar antes de retirar el original. | Casos previos/posteriores y punto de observación declarado. | EV-S/P2/P4/P5; EV-A/P2/P5: comparación previa relatada y prueba final reproducida 5/25. | Respaldado con reserva de secuencia histórica. | Sin commits intermedios completos; comparador temporal de importe retirado y no reejecutado por revisión. No equivalencia universal. |
| T04 | Probar categorías ajenas o confundir ausencia y fallo; no observar efectos. | R5 | RD01/RD02: datos/dependencias pertinentes y escenarios según significado de resultados. | C01–C05 en restricciones; A01–A05 y rechazo previo a cuatro efectos en importe. | EV-R; EV-S/P3/P5; EV-A/prueba permanente: admisión/rechazo y expectativas de llamadas. | Respaldado para casos y niveles definidos. | Fallos mediante dobles y datos delimitados; no atomicidad o ausencia universal de efectos reales. No sustituye I02 temporal. |
| T05 | Desplazar dependencias sin declarar qué se mantiene. | R8 | Revisar componentes/consumidores y dependencias transitorias. | Dependencias conservadas y excepciones identificadas. | EV-S/P6: repositorios, recarga de tarea y estado conservados; EV-A/P6/P7: interfaz pública y colaboradores sin cambios. | Parcial. | No inventario exhaustivo de todas las excepciones del contrato; no independencia de Symfony/Doctrine. |
| T06 | Inferir atributos de calidad de recuentos favorables. | R9 | Evaluar por escenarios/condiciones y separar descripciones estructurales de resultados de atributos. | Conservación por casos; comparabilidad de esfuerzo y efectividad de pruebas cuando se afirmen. | EV-S/amenazas; EV-A/A01–A05 y conteos; EV-B/objetivos. | Parcial: conservación y límites explícitos. | Sin comparación equivalente de esfuerzo/efectividad; más pruebas o menos duplicación no prueban mantenibilidad mejorada. |
| T07 | Refactorizar el monolito mediante una migración arquitectónica total no justificada. | R11 | Mantener MVC y una intervención incremental; no imponer núcleo independiente o clase nueva. | Controlador/coordinación y separación de responsabilidades en el alcance seleccionado. | EV-S: selección centralizada usada por dos consumidores; EV-A: descomposición privada y cálculo reutilizado. | Parcial respecto del requisito completo. | No separación total de lecturas, reglas y efectos del subcircuito; importe es refactorización interna, no nueva frontera entre capas. |
| T08 | Autoridad temporal dispersa entre interfaz y servidor. | R12 | Decisión temporal única en servidor propuesta. | Regla temporal reutilizada por consumidores, sin duplicación de interfaz. | EV-D: discrepancias localizadas; EV-B: solución temporal no construida. | Cumplimiento no acreditado. | Centralizar restricciones o cálculo de importe no demuestra satisfacer R12. No se presenta diagnóstico como solución. |
| T09 | Correspondencia temporal y rechazo previo a efectos sin demostrar en todo el conjunto. | R13 | Conservar criterios I01/I02 sin sustituirlos por criterios locales de otras decisiones. | I01: 100 % del conjunto acordado; I02: 100 % de rechazos sin efectos acordados. | EV-D: discrepancia temporal y O06 con dobles; EV-B: persistencia de resultados parciales. | Parcial/no satisfactorio para el cumplimiento conjunto. | O06 no cubre todo el subconjunto ni persistencia real; C01–C05/A01–A05 no son medición sustitutiva de esos indicadores. |
| T10 | Atribuir modificabilidad a la extracción sin observar evolución posterior. | R6, R7, R13 | Priorizar variación existente y separar incorporación de capacidad de cambio posterior. | I04: ampliación acordada sin cambios de código; costos separados. | EV-D/EV-B: capacidad extraordinaria ausente e I04 no medido. EV-A: escenarios estructurales añadidos después, sin ejecución. | No medido/no acreditado. | Contar de dos a un lugar para editar una fórmula no cumple el escenario I04 ni mide costo de cambio. No se construye otra capacidad por esta matriz. |
| T11 | Afirmar ahorro sin esfuerzo activo comparable. | R7, R9, R14 | Registrar fases/esperas/automatización y declarar datos ausentes. | I03: esfuerzo activo por fase; costo inicial/posterior separado cuando corresponda. | EV-D: 26:33.87 descriptivo por autoinforme; EV-S/P8 y EV-A: esfuerzo no medido. | Descriptivo parcial, sin mejora acreditada. | Horarios de sesión no equivalen a esfuerzo. No comparación equivalente, ahorro o costo total del método. |
| T12 | Perder relación entre decisiones, versiones, ayudas y resultados. | R10 | Conservar versión, pregunta/hallazgo/cambio, referencias y evidencia por episodio. | Trazabilidad documental de versiones y decisiones. | EV-F → EV-R → EV-S; EV-A/registro por pasos y revisión personal confirmada. | Respaldado documentalmente. | IA produce registros; P1 retrospectivo/P3 registrado después de P2 en importe. No mejora de carga documental medida ni independencia del ejecutor. |
| T13 | Presentar iteración implícita o solo una prueba final como rediseño. | R10 | Documentar hallazgo → ajuste → versión → evaluación posterior. | Al menos un rediseño identificable y valoración posterior con criterios fijados. | EV-F/EV-R/EV-S; cierre E8 aceptado. | Respaldado como proceso evaluativo acotado. | No campo, causalidad o validación de toda la contribución por contar ciclos. |
| T14 | Confundir utilidad del artefacto con conocimiento transferible. | R9, R10; OE6 | Separar evidencia de aplicación, reglas de adaptación y antecedentes. | Contexto, mecanismo, evidencia y límites de cada afirmación de contribución. | EV-B/PA1–PA3 y contraste; adopción posterior y dictamen en E10. | Formulación y trazabilidad disponibles; respaldo contextual dictaminado en E10. | No inferir validación general, originalidad de prácticas de base o transferencia externa por completar esta fila. |

## C. Control de cobertura y afirmaciones

| Requisito | Filas de la matriz |
|:--|:--|
| R1 | T01 |
| R2 | T01 |
| R3 | T02 |
| R4 | T03 |
| R5 | T04 |
| R6 | T10 |
| R7 | T10, T11 |
| R8 | T05 |
| R9 | T06, T11, T14 |
| R10 | T12, T13, T14 |
| R11 | T07 |
| R12 | T08 |
| R13 | T09, T10 |
| R14 | T11 |

La cobertura de catorce requisitos significa que cada compromiso tiene destino trazable, no que los catorce estén satisfechos. Las filas sin evidencia de mejora declaran explícitamente ausencia de medición o incumplimiento: no se las convierte en «cumplidas con limitaciones». PA1–PA3 son interpretaciones posteriores del conjunto y no criterios usados retroactivamente para garantizar éxito. Se conservan las decisiones de congelar construcción temporal y de no solicitar otros participantes.

**Afirmaciones de solución respaldadas:** el método formalizado pudo aplicarse con asistencia en las tareas delimitadas; se conservó el comportamiento examinado de selección y de importe en sus niveles documentados; hubo rediseño trazable y referencias que permiten seguir decisiones, ayudas y resultados. No se reclama aquí aplicación autónoma o satisfacción de todo el flujo por esas observaciones. La recepción, reproducción y límites se encuentran en las revisiones de cada episodio. El original del ejemplo y su anexo derivado no constituyen dos evidencias independientes.

**Afirmaciones que no corresponden:** resolución completa de la decisión temporal, ahorro medido, mejora conjunta de modificabilidad/testabilidad/trazabilidad, ausencia universal de regresiones, mantenibilidad empírica o transferencia demostrada a otros sistemas. Tampoco «todo P7 fue igual» entre episodios: P01 parcial, P02 integración en alcance acordado e importe alcance diferente. La matriz impide usar un resultado de otro comportamiento para satisfacer un indicador pendiente. Estas restricciones forman parte del enlace de solución, no notas que puedan omitirse en las conclusiones.

## D. Demostración, evaluación y contribución

La demostración establece que el método puede aplicarse a las tareas documentadas y producir una intervención; no basta por sí sola para afirmar utilidad general. La evaluación contrasta escenarios y condiciones acordados y revela conservación acotada, integración parcial o delimitada y mediciones ausentes. La contribución exige un examen adicional de las reglas de adaptación y su respaldo, a resolver en E10. Este documento no convierte una refactorización que funciona en prueba automática de conocimiento original.

La aplicación de importe muestra observación desde el consumidor e intervención ampliada por un cálculo duplicado, con una alternativa de clase nueva descartada por el autor. Se conserva como ejemplo de decisión y evidencia, no como garantía de que dividir métodos sea la mejor solución en cualquier contexto. Los escenarios de cambio añadidos después describen lugares hipotéticos de edición; no son ensayos ejecutados ni metas prospectivas satisfechas. La reformulación de principios no puede borrar esa cronología.

## E. Revisión de las condiciones de E9

| Condición | Resultado de esta revisión |
|:--|:--|
| Matriz completa y sin eslabones sin destino. | R1–R14 cubiertos; cada fila identifica decisión, criterio, fuente, grado y límite, incluidos compromisos incumplidos o no medidos. |
| Cada afirmación positiva de solución tiene evidencia pertinente. | Se limitan a aplicación asistida, conservación en casos definidos y trazabilidad; referencias y procedencia diferenciadas. |
| Limitaciones declaradas. | Alcance de datos, IA, roles, secuencia histórica, integración, atributos no medidos y suficiencia de conocimiento explícitos. |

**Cierre de E9 aceptado por el tesista mediante «acepto»:** la cadena de trazabilidad permite informar qué se resolvió, qué quedó parcial y qué no se demostró, sin borrar requisitos. El cierre no significa cumplimiento integral de la solución o validación automática de PA1–PA3. E10 fue posteriormente adoptada con respaldo contextual y conclusiones acotadas; no se requiere repetir aplicaciones o aprobaciones previas. La habilitación documental de traducción se registra en el control final, no se deduce de esta matriz por sí sola.

## Registro histórico del 4 de noviembre de 2026

Las secciones inferiores conservan la matriz y aceptación de esa fecha. Sus estados y afirmaciones generales no prevalecen sobre la matriz actual: el diagnóstico temporal no se transforma en sumativa ni un criterio sin medición se da por satisfecho. Se mantiene el cierre histórico como antecedente, no como aceptación del nuevo cierre propuesto.

**Estado:** en curso. Esta etapa recorre la cadena problema → requisito → decisión de diseño → criterio → evidencia → grado de cumplimiento → limitación, para mostrar qué quedó resuelto, qué quedó parcial y qué no se midió. No se confunde «el sistema compila y las pruebas pasan» con «el problema está resuelto».

## 1. Matriz de trazabilidad

| Problema de diseño | Requisito | Decisión de diseño | Criterio/indicador | Evidencia | Grado | Limitación |
|:--|:--|:--|:--|:--|:--|:--|
| Selección de restricción duplicada entre controlador y servicio | R3, R4 | Centralización en `RestriccionSubPartidaResolver` (P4) | Prueba directa sobre la regla | `make test` 188/540; `tests/Certificacion` 37/305 | Cumplido parcial | Antecedente de 2025, no producido por el método formalizado |
| Decisión temporal distribuida entre interfaz y servidor | R2, R11, R12 | Frontera incremental + autoridad en servidor (P3–P4) | I01 (100 % de correspondencia) | Comprobaciones O01–O06, M08/M09 | Parcial: el límite 8/9 no se distingue | La corrección no se construyó |
| Rechazo que puede ocurrir después de efectos | R5 | Comprobación de efectos prohibidos (P5) | I02 (100 % sin efectos) | O06 de servidor, rechazo sin llamar a los cuatro efectos | Parcial: un caso con dobles | Sin persistencia real ni atomicidad |
| Costo de cambio en esfuerzo humano | R14 | Registro por fases (P8) | I03 (minutos activos) | Bitácora, 26:33.87 | Descriptivo | Autoinforme, no experimental independiente |
| Modificabilidad ante cambio posterior | R6, R7 | Reutilizar configuración existente (P6) | I04 (cero archivos de código) | No medido | Limitación declarada | La capacidad extraordinaria no existe; construirla sería fabricar evidencia |
| Falta de trazabilidad entre decisión, versión y resultado | R10 | Versionado y design rationale (P8) | Documentación por versión con pregunta y hallazgo | V1–V3 documentadas en E7d/E7e | Cumplido documental | No sustituye evaluación empírica |

## 2. Distinción entre demostración y evaluación

La evidencia disponible demuestra que la instanciación **puede aplicarse**: las pruebas pasan, la extracción de la restricción funciona y el rechazo de O06 se observa con dobles. Eso es **demostración** —el artefacto opera—, no **evaluación** —la comparación sistemática contra los objetivos.

La evaluación propiamente dicha muestra que el problema **no está resuelto**: I01 no se cumple al 100 % porque el límite 8/9 no se distingue. Decir «las pruebas pasan» no equivale a «resuelve el problema». La distinción se mantiene explícita para no inflar el resultado.

## 3. Eslabones sin huérfano

Cada requisito tiene una decisión de diseño que lo atiende; cada criterio tiene evidencia o una limitación declarada. No hay un requisito sin decisión ni un criterio sin destino. Los eslabones que no tienen evidencia de cumplimiento (I04) no se declaran «cumplidos»: se declaran limitación con su razón.

## 4. Gate de E9

El gate exige: matriz de trazabilidad completa sin eslabones huérfanos, cada afirmación de solución respaldada por evidencia, y limitaciones declaradas. La sección 1 propone ese cumplimiento. Corresponde al tesista validar o corregir, en particular si algún grado de cumplimiento le parece inexacto o si falta un eslabón que considere relevante.

**Cierre, 4 de noviembre de 2026:** el tesista valida la matriz —«esta perfecto»—. El gate de E9 se cumple: la matriz de trazabilidad está completa sin eslabones huérfanos, cada afirmación de solución está respaldada por evidencia y las limitaciones están declaradas.
