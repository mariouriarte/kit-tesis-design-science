# Método de refactorización arquitectónica incremental — M-R1

**Estado:** versión rediseñada y aprobada por el tesista después de P01; aún no evaluada en una aplicación posterior. **Identificador:** M-R1. **Fecha de formalización:** 6 de noviembre de 2026, America/La_Paz. No sustituye retrospectivamente la versión que recibió P01 ni convierte sus pendientes en pasos cumplidos.

## 1. Propósito y alcance

El método orienta intervenciones acotadas sobre decisiones funcionales distribuidas en subcircuitos de aplicaciones MVC heredadas. Su producto no es necesariamente una nueva clase: primero se justifica la necesidad, se delimita la decisión y se fija el comportamiento que se debe conservar o cambiar intencionalmente. La selección de una intervención debe considerar consumidores, dependencias y efectos, sin exigir una reescritura completa ni independencia total del marco existente.

M-R1 conserva los ocho pasos y la base del diseño documentada en `07c_diseno_artefacto.md`. Modifica únicamente las instrucciones de P3, P5, P7 y P8 aprobadas tras la aplicación P01. El registro de motivos y la comparación con la versión anterior están en `registro_redisenio_metodo_mr1.md`; no se reclama originalidad de prácticas heredadas por cambiar su redacción.

## 2. Entradas de una aplicación

La aplicación debe identificar una necesidad de cambio, el código de partida y los consumidores pertinentes. Antes de transformar se registran comportamiento observado, comportamiento requerido e intención del cambio: conservación, corrección o extensión. Cuando el comportamiento requerido no esté confirmado, se declara la incertidumbre y no se presenta una decisión del desarrollador como aprobación funcional.

También deben identificarse las condiciones de trabajo: referencia de código, herramientas, entorno, datos, asistencia y comprobaciones autorizadas. Las restricciones de acceso no prueban defectos del método ni autorizan declarar verificaciones no realizadas. Si se utiliza IA, se registran las ayudas relevantes y las decisiones revisadas por el practicante.

## 3. Pasos y condiciones

| Paso | Entradas | Productos | Condición de entrada | Condición de salida |
|:--|:--|:--|:--|:--|
| P1. Delimitar el incremento | Escenario de cambio | Decisión delimitada, consumidores y efectos, frontera justificada | Necesidad concreta que justifique examinar el incremento | Frontera y justificación identificables |
| P2. Caracterizar el comportamiento | Código actual y comportamiento accesible | Pruebas de caracterización y registro observado–requerido–intención | Decisión y consumidores localizados | Comportamiento pertinente fijado antes de mover lógica |
| P3. Hacer controlable la decisión | Decisión y dependencias identificadas | Inventario de datos y dependencias que determinan la decisión, forma de controlarlos y puntos de observación | Información necesaria y restricciones de control identificables | Decisión reproducible en el alcance declarado; dependencias no controlables y límites explícitos |
| P4. Migrar sin retirar el original | Destino justificado y caracterización previa | Implementación nueva en coexistencia temporal con la original | Comportamiento fijado antes de transformar | Nueva implementación disponible y original conservada durante la comprobación |
| P5. Comprobar comportamiento y efectos | Implementaciones coexistentes y escenarios definidos | Resultados observados y efectos permitidos/prohibidos para resultados normales, ausencia y fallos pertinentes | Puntos de observación y expectativas identificados | Conservación o cambio intencional respaldado en el conjunto examinado; discrepancias y límites registrados |
| P6. Retirar el original y ajustar dependencias | Implementaciones comprobadas | Duplicación retirada y conexiones/dependencias ajustadas | Comprobaciones pertinentes de P5 satisfactorias | Conexiones coherentes y dependencias transitorias declaradas |
| P7. Integrar y verificar | Cambio aislado y condiciones de integración | Evidencia separada de verificación local e integración en el entorno objetivo | Comprobaciones locales disponibles y condiciones de integración identificadas | Cumplimiento acreditado de ambas partes en su alcance; si una falta, estado parcial o no completado, no cumplimiento integral |
| P8. Documentar, versionar y registrar mediciones previstas | Productos, decisiones, diferencias y protocolo de medición aplicable | Versión identificada, pregunta de diseño, hallazgos, cambios, ayudas y límites; mediciones previstas o estado no medido | Evidencia disponible, sin reconstruir datos inexistentes | Trazabilidad documental completa y estado de cada medición declarado; medidas exigidas por una afirmación obtenidas antes de sostenerla |

## 4. P3: datos y dependencias propios de la decisión

Identifique qué información determina el resultado y de dónde proviene: entradas recibidas, configuración, consultas, estado previo u otras dependencias pertinentes. Explique cómo suministrarla o sustituirla de manera controlada y cómo observar el resultado. No se exige convertir toda entrada en valores escalares ni introducir una arquitectura nueva para cumplir este paso.

**El instante solo debe controlarse si la decisión depende del tiempo.** Gestión, fecha o zona horaria son ejemplos condicionados, no entradas obligatorias para todo incremento. Si el entorno impide controlar una dependencia necesaria, se registra qué parte del comportamiento queda sin comprobar; no se presenta una ejecución no controlada como evidencia equivalente.

## 5. P5: resultados y efectos, no rechazo obligatorio

Para cada escenario identifique qué resultado puede producir la decisión y qué consecuencias son permitidas o prohibidas. Distinga, cuando existan, resultado normal, ausencia de resultado y fallo: una consulta puede devolver ausencia sin que ello constituya un rechazo de dominio. Una excepción tampoco debe ocultarse como ausencia para favorecer la comprobación.

La lista de escenarios depende del comportamiento y de la intención aceptada. No se exige inventar un rechazo, una excepción o un efecto inexistentes para completar la tabla. Registre los observables y los límites de las pruebas: comprobar llamadas con dobles no acredita por sí solo persistencia real, atomicidad o ausencia universal de efectos.

## 6. P7: verificación local e integración diferenciadas

**P7-L, verificación local:** identifique y ejecute las comprobaciones autorizadas sobre el cambio aislado: pruebas pertinentes, sintaxis y revisión de conexiones, diferencias o dependencias según el incremento. Registre comandos, condiciones, resultados y omisiones. Una prueba omitida no se cuenta como satisfactoria.

**P7-I, integración en el entorno objetivo:** identifique qué debe comprobarse para que el cambio opere con los consumidores y el entorno previstos. Según el caso, puede incluir configuración de dependencias, compilación del contenedor de servicios, integración con persistencia o recorridos de aplicación; no toda intervención exige las mismas comprobaciones. Su selección y límites se definen antes de ejecutar la evaluación correspondiente, sin usar el resultado observado para reducir la exigencia.

Registre por separado el estado y la evidencia de P7-L y P7-I. Si solo se acredita la primera parte, P7 sigue **parcialmente verificado**; «completado con pendientes» no equivale a cumplimiento integral. No se autoriza intervenir producción, conectar servicios o mezclar ramas por el solo hecho de seguir este paso: si la integración necesaria no está permitida, se registra pendiente.

## 7. P8: trazabilidad obligatoria y medición explícita

Conserve la identificación de la versión y referencia, la pregunta de diseño, los productos, decisiones y alternativas, los hallazgos, las ayudas relevantes y las limitaciones. Esa trazabilidad es un producto del método aunque no exista medición de esfuerzo. Un commit puede contribuir a conservar la versión, pero no sustituye el razonamiento documentado ni es la única forma de identificarla.

Las mediciones de esfuerzo, tiempo, costo inicial o evolución posterior requieren actividades, unidades y reglas de cómputo fijadas antes de medir. Registre por separado las que correspondan y marque **no medido** cuando no existan datos; no reconstruya esfuerzo a partir del horario de una sesión ni asigne cero a datos ausentes. Los recuentos de archivos o líneas describen extensión del cambio, no equivalen automáticamente a costo o mantenibilidad.

Si una medición es requisito del estudio o sustenta una afirmación de mejora, sigue siendo necesaria para sostenerla: declararla no medida limita la conclusión, no satisface el requisito. Distinguir medición de documentación no elimina los compromisos previos de evaluación. El costo de incorporar una capacidad y el de modificarla posteriormente se mantienen separados cuando se estudian ambos.

## 8. Límites de esta versión

La aprobación de M-R1 acredita una decisión de diseño del tesista, no su efectividad. P01 aplicó la versión anterior con asistencia sustantiva de IA; no se le atribuirán las instrucciones nuevas ni se reinterpretarán sus resultados para probarlas. C01–C05 y los estados históricos de los indicadores I01–I04 permanecen sin cambios.

Antes de una evaluación posterior se debe fijar una tarea y un protocolo que examinen esta versión y permitan distinguir efecto del rediseño, aprendizaje del participante y ayuda recibida. No se ha ejecutado ese episodio ni se han definido aquí sus umbrales de éxito. Este archivo formaliza el artefacto rediseñado; no declara validado el método ni cerrada la tesis.
