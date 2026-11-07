# E8. Evaluación

## Estado vigente al 6 de noviembre de 2026: revisión de P02

Existe ya una aplicación posterior de M-R1 por P02; las notas inferiores que indicaban ausencia de episodio posterior conservan su sentido histórico, no el estado actual. El tesista confirma autorización durante la actividad para dejar efectos en la base local, con borrado anunciado para el final del día; no se registra ese borrado como realizado.

El dictamen está en `revision_aplicacion_p02_2026-11-06.md`, sección 7, y fue aceptado expresamente por el tesista el 6 de noviembre de 2026 mediante «aceptado». Se cierra la valoración del episodio: aplicación asistida acreditada en los ocho pasos y P7 integral en el alcance acordado —configuración, repositorio/servicio reales y controlador por invocación directa, no HTTP completo—. La IA produjo parte sustantiva del diseño, código, pruebas, procedimientos y registro; no se sostiene desempeño autónomo de P02.

| Evidencia | Resultado y procedencia |
|:--|:--|
| Batería inicial | Salida conservada: 159 pruebas, 260 aserciones, 1 omitida. |
| Batería final | Salida conservada: 173 pruebas, 289 aserciones, 1 omitida; no repetida completa por la asesoría. |
| Dos clases nuevas | Reproducidas por la asesoría: 7/18 y 7/11 satisfactorias, con dobles. |
| Configuración | Validación del contenedor repetida por la asesoría tras la sesión: código de retorno 0; no se atribuye al participante. |
| Integración | Procedimientos y salidas previas/posteriores contrastados para tres casos en servicio/repositorio reales y controlador directo. No se reejecutan los que escriben datos. |

Se propone clasificar P02 como episodio controlado con propósito sumativo para valorar M-R1 después del rediseño. No es evaluación de campo ni evidencia causal de mejora frente a P01, porque cambian participante, modalidad, referencia y entorno; tampoco acredita I01–I04 completos, ahorro o evolución posterior. La revisión identifica amenazas de constructo, interna, externa y de conclusión, con controles y límites residuales en la sección 7 del documento de revisión.

**E8 permanece abierta para revisión global de suficiencia:** el dictamen P02 ya está aceptado y no se repetirá su aprobación. Falta contrastar compromisos de evaluación y afirmaciones generales con el conjunto de evidencia, sin eliminar requisitos o indicadores pendientes por el resultado favorable del episodio. El cierre histórico del 4 de noviembre y las tablas inferiores no prevalecen sobre esta revisión ni autorizan traducción final.

## Hallazgo posterior y recomendación aceptada sobre P8 — 6 de noviembre de 2026

En la revisión posterior a P02, el tesista declara que ambos participantes concentraron la documentación al llegar a P8, sin detenerse a registrar notas en cada paso. Según su explicación, esto exigió volver sobre los pasos anteriores para reconstruir decisiones y documentar lo realizado. Es una declaración retrospectiva del tesista: no se atribuye observación directa de P01, cuya modalidad fue autorregistro, ni se infiere ausencia de pruebas previas por ausencia de notas progresivas. El hallazgo no demuestra por sí solo incomprensión del método o incumplimiento de P8.

El tesista también aclara que ambos participantes le transmitieron satisfacción verbalmente. Se registra como comunicación verbal reportada por él durante esta revisión, sin citas textuales, momento preciso ni medición sistemática; no se convierte en un resultado cuantificado de satisfacción o usabilidad. Su expectativa de aplicación en otros sistemas MVC heredados se mantiene como transferencia propuesta, no comprobada por estos episodios.

El tesista acepta mediante «lo considero perfectamente» la recomendación de registrar brevemente las decisiones y evidencias durante cada paso y reservar P8 para consolidar y revisar la trazabilidad. El mecanismo esperado es reducir la reconstrucción retrospectiva y las omisiones; la contrapartida es introducir pequeñas tareas de registro durante la intervención. Se trata de una recomendación posterior a la evaluación, no de una modificación aplicada a M-R1 ni de una mejora con efectividad comprobada. No sustituye mediciones pendientes, no acredita originalidad por sí sola y no cierra E8; su implementación y evaluación quedan pendientes si se decide incorporarla a otra versión.

## Contraste global de requisitos y evidencia — revisión del 6 de noviembre de 2026

Este contraste utiliza los requisitos de `07b_requisitos.md`, el dictamen aceptado de P02 (sección 7 de `revision_aplicacion_p02_2026-11-06.md`) y los resultados históricos de I01–I04 conservados en este archivo. No introduce umbrales nuevos ni transforma aceptación documental en cumplimiento empírico. El respaldo se refiere al alcance examinado, fuertemente asistido por IA; no acredita desempeño autónomo, transferencia o mejora causal.

| Requisito | Evidencia localizada y valoración acotada | Pendiente o límite |
|:--|:--|:--|
| R1. Selección por necesidad y riesgo | P02-P1 registra decisión, frontera y justificación para la tarea. Respaldo en la aplicación asistida. | La tarea fue seleccionada previamente; no demuestra selección independiente ante necesidades diversas ni comparación amplia de riesgos. |
| R2. Delimitación previa | P02-P1/P2 identifica dos consumidores y efectos. Respaldo documental en el episodio. | El orden se sustenta en el registro de sesión, sin commits intermedios que lo acrediten por sí solos. |
| R3. Distinguir observado, requerido e intención | P02-P2/P5 y el contraste previo/posterior respaldan conservación en los escenarios acordados. | No demuestra aplicación completa a una corrección o extensión; no equivale a ratificación general de reglas institucionales. |
| R4. Caracterización antes de mover | P02-P2/P4 documenta caracterización previa y coexistencia. Respaldo acotado. | Secuencia relatada, no reproducida sobre una copia histórica completa; controlador por invocación directa, no HTTP completo. |
| R5. Control y observación | P02-P3/P5: datos/dependencias pertinentes, selección, ausencia, fallos y estado entre llamadas. Respaldo en esos casos y niveles de prueba. | Fallos mediante dobles; no control universal de efectos o persistencia. Una decisión no temporal no valida los indicadores temporales originales. |
| R6. Variación mediante mecanismos existentes | La extracción reutiliza infraestructura existente, pero esto no equivale al escenario de evolución por configuración previsto. | No acreditado el cambio posterior de I04; no marcar satisfecho por evitar infraestructura nueva. |
| R7. Separar costo inicial y posterior | Se conserva la distinción en el método. | Sin medición separada de ambos costos ni episodio de evolución posterior; no acreditado empíricamente. |
| R8. Dependencias transitorias explícitas | P02-P6 y su revisión identifican recarga de tarea, estado de servicio y conversión a entidad o ausencia. Respaldo parcial. | La revisión no acredita inventario exhaustivo y justificación de todas las excepciones del contrato. |
| R9. Evaluar atributos bajo condiciones comparables | P02-P5/P7 aporta escenarios y conservación de comportamiento. Respaldo parcial. | No hay comparación equivalente de esfuerzo ni efectividad de pruebas; las diferencias entre P01/P02 no prueban mejora causal. |
| R10. Versionar decisiones y evidencia | P01 → ajustes aprobados → M-R1 → P02 identifica hallazgos, decisiones y resultados. Respaldo documental. | La recomendación posterior sobre P8 no fue aplicada ni evaluada y no pertenece retrospectivamente a M-R1. |
| R11. Frontera incremental en MVC | P02-P6 muestra selector centralizado y conexión con dos consumidores, manteniendo el monolito. Respaldo parcial. | La extracción no acredita reducción completa del controlador a coordinación ni separación de todas las lecturas, reglas y efectos. |
| R12. Autoridad temporal única en servidor | La centralización de selección de restricciones es evidencia de otra decisión. | No acredita la regla temporal única exigida por R12; la brecha temporal permanece. |
| R13. Satisfacer I01, I02 e I04 | Diagnóstico: I01 con discrepancia; I02 parcial con dobles; I04 no medido por capacidad inexistente. | No se acredita cumplimiento conjunto. C01–C05 de P02 no sustituyen esos indicadores. |
| R14. Medición de esfuerzo activo | I03 conserva un registro descriptivo parcial; P02 declara esfuerzo no medido. | No hay medición completa por fases con espera/automatización separadas ni comparación de ahorro. |

El conjunto respalda una aplicación asistida del método, conservación acotada y una secuencia documentada de evaluación formativa, rediseño y valoración posterior. No demuestra que la instanciación haya satisfecho todas las propiedades comprometidas ni que los cinco principios candidatos estén validados. R6–R7, R9 y R12–R14 conservan vacíos específicos; las reservas de R11 impiden presentar la extracción como transformación completa del subcircuito.

E8 sigue abierta. El siguiente análisis debe relacionar cada principio candidato de E10 con evidencia favorable, contraria o ausente y determinar si aporta conocimiento adicional al de sus antecedentes. No se reabre por este contraste la construcción temporal congelada, no se suprimen requisitos ni se declara suficiencia de maestría por el solo hecho de reconocer limitaciones. Una eventual modificación de alcance deberá ser explícita, justificada y posterior a los resultados, nunca presentada como compromiso inicial.

## Contraste de los cinco principios candidatos — 6 de noviembre de 2026

Se examinan las formulaciones vigentes de `10_contribucion_conclusiones.md` sin sustituirlas ni ratificar su cierre histórico. Los identificadores de esta tabla designan principios, no los pasos homónimos del método. La relación con antecedentes se limita a la comparación ya documentada en E5, secciones 7–9; este contraste no es una nueva búsqueda ni prueba de ausencia de propuestas equivalentes. La aplicación favorable de una práctica no demuestra por sí sola la originalidad o el mecanismo causal de un principio.

| Principio candidato de E10 | Evidencia pertinente | Qué no permite concluir | Dictamen para la revisión de suficiencia |
|:--|:--|:--|:--|
| P1. Selección proporcional del incremento | La explicación del tesista en E5 distingue errata de presentación y decisión distribuida. P02 delimita una decisión y dos consumidores. | La tarea y su alcance ya estaban seleccionados; no se examinó elección entre intervenciones de distinto riesgo ni se midió sobreintervención evitada. E5 reconoce selección proporcional en los antecedentes. | Justificación conceptual y ejemplo de aplicación; no se acredita un criterio original ni su efectividad comparativa. |
| P2. Caracterizar antes de mover | P02 conserva escenarios previos/posteriores y relato de coexistencia; comprobaciones finales respaldan conservación acotada. | El orden no se acredita mediante historial intermedio completo; no hay comparación sin caracterización ni prueba aislada de su efecto protector. E5 registra la caracterización como práctica heredada. | Aplicación asistida respaldada en el alcance documentado; no principio original validado por esos resultados. |
| P3. Autoridad de la decisión en el servidor | El diagnóstico identifica discrepancia temporal; P02 centraliza selección de restricciones en un componente usado por dos consumidores. | La extracción de restricciones no corrige ni unifica la regla temporal entre interfaz y servidor. La evidencia diagnóstica de dispersión no demuestra efectividad de su solución. | Necesidad de diseño fundamentada, con analogía estructural parcial; la prescripción temporal sigue sin evaluación correspondiente. |
| P4. Separar transformación de capacidad nueva | El estudio distingue extracción, corrección y extensión; P02 examina conservación sin reclamar capacidad temporal nueva. | No hubo aplicación evaluada que contrastara ambas intenciones ni medición del efecto de separarlas sobre atribución o errores. E5 reconoce esta distinción en la base reutilizada. | Distinción metodológica aplicada al encuadre y al episodio; falta demostrar conocimiento adicional y respaldo específico del mecanismo. |
| P5. Evaluar por escenarios, no por recuentos | C01–C05 y P7 separan propiedades y niveles de prueba; se conservan casos, resultados, omisiones y límites en vez de inferir éxito por número de pruebas. | No hay escenario de evolución posterior ni comparación equivalente de esfuerzo que demuestre modificabilidad mejorada. La evaluación por escenarios ya figura en E4/E5. | Respaldo a la disciplina de evaluación en el episodio; no prueba de mejora de atributos ni originalidad de la recomendación general. |

Ninguno de estos cinco enunciados cuenta todavía, en esta revisión, con justificación suficiente para declararlo principio original validado. Esto no invalida la utilidad del método ni exige que cada elemento sea nuevo: identifica que el conocimiento adicional debe ubicarse en una adaptación concreta y su evidencia, no en renombrar prácticas conocidas. La explicación histórica de E10 que daba por suficiente formular candidatos con límites no resuelve este pendiente.

Una vía de análisis es precisar la adaptación de los puntos de control: P01 dejó integración sin acreditar; M-R1 separó verificación local e integración; P02 documentó ambas en un alcance fijado. Esta secuencia aporta evidencia de aplicación de una explicitación del método, pero todavía no demuestra que la explicitación causó el resultado o que los antecedentes carecían de ella. Otra observación es el registro diferido en P8; su recomendación de registro progresivo se formuló después de P02 y permanece sin evaluar. Ninguna de las dos vías se adopta aquí como nuevo principio ni como cambio aprobado de la contribución.

**Resultado del contraste:** E8 permanece abierta y E10 requiere revisión posterior del respaldo de su contribución. No basta una mejora de redacción para subsanar evidencia ausente; tampoco se impone como requisito universal una comparación causal si la afirmación puede delimitarse y evaluarse de otra forma. El siguiente paso es que el tesista precise qué conocimiento de adaptación reclama, distinguiendo utilidad observada, mecanismo propuesto y límites de la evidencia, antes de decidir si hace falta evaluación adicional.

## Aclaración del tesista sobre P7 de P02 — 6 de noviembre de 2026

Consultado sobre su expresión «utilizar dobles en lugar de scripts con la DB», el tesista confirma mediante «si» que se refiere únicamente a las pruebas aisladas del servicio y del selector. No niega los procedimientos y salidas de integración con base de datos real conservados en la revisión P02. Por tanto, no existe contradicción resuelta en contra del dictamen aceptado: las pruebas con dobles y las comprobaciones de integración tienen alcances distintos y ambas permanecen registradas.

El tesista explica que P02 disponía del entorno necesario, a diferencia de P01, y que durante P7 no requirió su intervención. Esta declaración se limita a ese paso; no elimina las ayudas operativas ni la asistencia de IA documentadas en el conjunto del episodio. La disponibilidad del entorno es una condición de aplicación, no un efecto demostrado del rediseño. La anotación de conformidad del participante se interpreta junto con los productos y resultados ya revisados, no como evidencia suficiente por sí sola.

La aclaración mantiene el respaldo a la aplicación asistida y a la distinción de niveles de comprobación, pero no aporta evidencia específica de que la separación P7-L/P7-I causara el cumplimiento observado. No se solicita repetir P02, sus comprobaciones ni la aprobación del dictamen. Queda pendiente precisar y justificar el conocimiento adicional de la adaptación; no se cierra E8 por esta aclaración.

## Explicación del tesista sobre ausencia y fallo en P5 — 6 de noviembre de 2026

Durante la revisión, se contrasta la explicación del tesista con C03/C04 de `consigna_participante_restriccion_subpartida.md`: ausencia de restricciones tras consulta satisfactoria y excepción de consulta no son resultados equivalentes. Ante la pregunta sobre capturar una excepción del repositorio y devolver ausencia, el tesista responde que «podria crear la certificacion si no se captura bien el fallo». Su respuesta identifica un riesgo pertinente: continuar por la vía de ausencia sin haber podido determinar si existe una restricción aplicable. Es explicación obtenida en la asesoría después de los episodios, no resultado verbal atribuido a los participantes ni reproducción de un defecto.

El requisito conservador es mantener distinguibles la ausencia válida y el fallo, preservando la propagación prevista por C04; no consiste simplemente en capturar más excepciones. P02 aporta comprobaciones de fallos con dobles y casos de ausencia con los alcances ya registrados; esto no acredita atomicidad ni ausencia universal de escrituras ante cualquier fallo. La satisfacción de esos casos respalda aplicación de la distinción, no efecto causal del rediseño ni originalidad de la práctica.

La explicación concreta el fundamento de RD02/P5: los escenarios y efectos deben depender del significado de los resultados de la decisión, sin imponer rechazo a una ausencia válida ni ocultar fallos como ausencia. Se mantiene como fundamento de la adaptación examinada, no como un nuevo principio aprobado o validado. Una propuesta de unicidad de restricciones requeriría precisar su alcance funcional: el contrato observado admite selección específica y general; no se autoriza modificar datos, esquema o comportamiento como parte de esta aclaración.

## Contraste focalizado de RD02/P5 con la base operativa — 6 de noviembre de 2026

La lectura registrada en `lectura_girjoaba_capiluppi_2026-10-28.md` atribuye al ciclo de Girjoaba y Capiluppi (2024, manuscrito aportado, pp. 5–6) pruebas de comportamiento después de migrar y antes de retirar el original. La preservación y comprobación del comportamiento, por tanto, no son aportes nuevos de M-R1. El 6 de noviembre se reconfirma mediante el DOI la identificación editorial; esto verifica metadatos, no constituye nueva lectura del texto final ni resuelve la correspondencia exacta de versiones.

| Elemento | Resultado del contraste |
|:--|:--|
| Conocimiento reutilizado | Migrar, comprobar comportamiento, retirar y comprobar conexiones/integración, según la lectura primaria ya registrada. |
| Explicitación local de M-R1 | RD02 exige distinguir resultado normal, ausencia y fallo pertinentes a la decisión, en lugar de imponer rechazo como categoría universal. |
| Evidencia producida | P01 motivó el ajuste; P02 documenta aplicación asistida y comprobaciones de ausencia/fallos con sus niveles y límites. La explicación posterior del tesista articula el riesgo de ocultar una excepción como ausencia. |
| Diferencia que no está probada | No se demuestra que el ciclo de origen excluya estas distinciones, que M-R1 sea superior o que RD02 haya causado mejor comprensión o conservación. La ficha de lectura no es una búsqueda exhaustiva de antecedentes equivalentes. |

Se precisa el criterio de suficiencia de los contrastes anteriores: no se exige que cada práctica o cada principio sea inventado por el tesista. La contribución puede residir en conocimiento de adaptación de prácticas existentes, siempre que se explicite qué se aprende, bajo qué condiciones y con qué evaluación. Sin embargo, llamar «adaptación» a una concreción o redactar un principio más específico no acredita por sí solo conocimiento nuevo validado. El candidato que debe examinarse es el diseño de puntos de comprobación según dependencias, resultados y efectos de cada decisión, no la invención de la caracterización o del tratamiento diferenciado de errores.

Como posible evaluación adicional, todavía no acordada, puede considerarse otro incremento con resultados o dependencias diferentes para examinar la adecuación de esos puntos de comprobación. No exige por definición otro sistema ni una comparación causal; tampoco garantiza originalidad o suficiencia ni sustituye los requisitos temporales pendientes. La selección, necesidad, criterios y factibilidad deberán acordarse antes de ejecutar; no se modifica M-R1, SIGPP o el alcance mediante esta propuesta.

### Referencia del contraste focalizado

Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079

**Verificación:** metadatos reconfirmados mediante DOI; contenido según lectura documentada del manuscrito aportado. Correspondencia exacta con la versión editorial final **[por verificar]**.

## Restricción de evaluación adicional comunicada por el tesista

Después de la propuesta de examinar otro incremento, el tesista informa que no es posible contar con otros participantes y que él podría realizarlo, con tiempo limitado. No se ha seleccionado otra decisión ni aprobado protocolo o ejecución. Esta restricción descarta planificar nuevas sesiones con terceros como si fueran recursos disponibles.

Una aplicación adicional por el autor podría ampliar la evidencia sobre otra decisión y sus puntos de comprobación, pero mantendría el sesgo del constructor y no demostraría aplicabilidad independiente o transferencia a otros desarrolladores. No sustituiría P02 ni se exigiría como condición automática de suficiencia. Su conveniencia depende de un objetivo de evidencia específico y un alcance viable; por ahora no se autoriza construcción, nueva funcionalidad ni ampliación del alcance. Se mantiene la prioridad de resolver suficiencia con afirmaciones proporcionadas y de reservar tiempo para análisis y redacción.

## Aplicación adicional del autor sobre importe: preparación aceptada

**Revisión personal confirmada después de la recepción:** el tesista indica que revisó el material señalado y olvidó cambiar el estado; solicita actualización por la asesoría. Registro original y revisión actualizados, sin retrotraer la confirmación. Se resuelve ese pendiente documental y no se repite la consulta. Restan adecuación del ejemplo y dictamen consolidado, no otra ejecución; E8 global permanece abierta.

**Estado posterior, 7 de noviembre de 2026: actividad recibida y revisión preliminar realizada.** El autor informa término y aporta ejemplo explicativo. Se inspeccionan registro P1–P8, prueba y cambio; se reproducen 5 pruebas/25 aserciones, batería 164/285/1 omitida y validación del contenedor con retorno 0. A01–A05 respaldados en el estado final con dobles; caracterización previa/coexistencia sustentadas en registro y prueba temporal retirada, no reejecutadas aquí. Cambio local en métodos privados, sin clase nueva y con cálculo reutilizado desde `create()`. Detalle en `revision_aplicacion_autor_importe_2026-11-07.md`.

La aplicación aporta otra decisión del mismo sistema por el autor, no independencia ni transferencia externa. El suplemento P8 deja registros por paso, sin demostrar reducción de carga; P1 retrospectivo y P3 registrado después de P2. Los escenarios hipotéticos de cambio se definieron después y no se ejecutaron: análisis exploratorio, no cumplimiento prospectivo de I04 o medición de esfuerzo. Pendiente aclarar revisión personal de pruebas/registro y adecuar el ejemplo antes de incorporarlo. E8 permanece abierta; las notas inferiores de preparación no son el estado vigente.

**Preparación comprobada para P1/P2:** P7 acotado aceptado expresamente. La asesoría revisa conexión opcional PostgreSQL en tests, comprueba que no está configurada y ejecuta `make test`: 159 pruebas, 260 aserciones, 1 omitida, sin fallos/errores informados. No código/configuración/datos cambiados ni transformación realizada; la batería general no acredita A01–A05. Guías actualizadas en docs; aplicación del autor aún no iniciada. Próximo paso: delimitación y caracterización por el tesista. No repetir aprobación de criterios/P7; detalles y límites en la preparación.

**Criterios A01–A05 aceptados expresamente:** el tesista adopta cinco casos y rechazo previo a efectos antes de la transformación. Guía y registro creados en docs de SIGPP, sin implementación ni resultados; material M-R1 con suplemento operativo posterior a P02 identificado. No se repite aceptación de escenarios. Falta acordar P7 y preparar/verificar batería inicial; la propuesta de configuración/conexiones y consumidor con dobles no se presenta como persistencia real comprobada. Estado operativo en `preparacion_aplicacion_autor_importe.md`.

**Actualización posterior a la aclaración de otra PC:** se localiza `origin/eval/metodo-mr1-p02` en `0ddd7174`, con documentos de sesión y prueba versionados; no se interpreta la ausencia en master como pérdida ni se exige repetir P02. Se crea `eval/metodo-mr1-importe-autor` desde `7ef29a4f`, limpia, sin pruebas o transformación. Se proponen cinco escenarios (inferior, igual, superior al disponible, cero y negativo) y observación de rechazo antes de efectos; aceptación, alcance de integración e instrumento pendientes. Detalle y límites de preservación en la preparación. Las frases inferiores de ausencia y no creación de rama describen la inspección inicial, no el estado vigente.

El tesista acepta la decisión de importe frente al disponible como tarea adicional y propone rama `eval/`, Docker y `make test` en `/home/mario/dev/sf_projects/sipoa4`. La inspección encuentra master `7ef29a4f` sin cambios locales y contenedor `sigpp-app` activo; la orden Make fue inspeccionada sin ejecutar pruebas. La regla de importe está presente en el servicio, pero no las pruebas históricas de certificación referidas por el índice desactualizado.

No se localizan en esta copia la rama `eval/metodo-mr1-p02` ni los archivos `docs/*p02*`; falta ubicar los originales preservados, sin asumir pérdida ni solicitar repetir P02. Estado detallado y pendientes en `preparacion_aplicacion_autor_importe.md`. No hay nueva rama, protocolo completo, aplicación o resultados. La actividad prevista por el autor ampliaría cobertura de decisiones, no independencia o transferencia; E8 permanece abierta.

## Registro histórico de evaluación y auditoría

Las secciones siguientes se preservan para trazabilidad. Su clasificación de ensayos diagnósticos como sumativos y su cierre del 4 de noviembre fueron observados por la auditoría del 5; no constituyen un nuevo dictamen vigente.

> **Rediseño aprobado y formalizado:** el tesista aprueba los cuatro ajustes derivados de la revisión P01 en P3/P5/P7/P8. M-R1 y la cadena hallazgo → decisión → cambio están documentadas en `metodo_refactorizacion_incremental_mr1.md` y `registro_redisenio_metodo_mr1.md`. Hay evidencia formativa y rediseño del método identificables, pero aún no resultados de una aplicación posterior de M-R1 ni evaluación sumativa concluida. La ratificación P01 y la aprobación del rediseño no validan por sí solas los principios de E10.

> **Ratificación posterior incorporada:** P01 ratifica el registro final; recepción documental cerrada sin nueva aplicación. Se mantiene P7 parcialmente verificado según el alcance técnico, aunque el participante lo reporta como completado con pendientes. Los hallazgos aún deben producir decisiones de rediseño aprobadas y evaluación posterior; la ratificación no cierra E8. Véase la actualización de `revision_aplicacion_p01_2026-11-05.md`.

> **Evidencia posterior a la auditoría de suficiencia:** se recibieron productos de aplicación asistida P01 en la copia sobre master y se reprodujeron 24 pruebas/81 aserciones de certificación, junto con la batería completa 183 pruebas/341 aserciones/1 omitida PostgreSQL. Son resultados de un nuevo episodio formativo con autorregistro, no campo ni sumativa por el solo hecho de ejecutarlos. Quedan pendientes ratificación del resumen final del participante, rediseño documentado del método si se aprueba y evaluación posterior; P7 tiene integración pendiente. Detalle en `revision_aplicacion_p01_2026-11-05.md`. El cierre histórico inferior no sustituye estas condiciones de suficiencia.

**Estado:** en curso. La evaluación distingue dos funciones: demostrar que la instanciación resuelve el problema (utilidad) y demostrar que los principios del método son válidos más allá del caso (contribución). Se declara con honestidad que la evaluación es técnica y analítica; no hubo evaluación de campo. Esta ausencia se registra como amenaza a la validez externa, no se disimula.

## 1. Estrategia de evaluación (marco FEDS)

El marco FEDS cruza propósito (formativo/sumativo) con paradigma (artificial/naturalista). La ubicación de la evidencia de este estudio es:

| Estrategia FEDS | ¿Ocurrió? | Evidencia |
|:--|:--|:--|
| Analítica formativa | Sí | Razonamiento sobre el diseño candidato y la frontera incremental (E7c). |
| Técnica sumativa | Sí | Comprobaciones aisladas de la decisión temporal con datos ficticios y dobles (I01, I02, O06). |
| Campo formativa | No | No hubo uso del artefacto en producción con retroalimentación para rediseño. |
| Campo sumativa | No | No hubo evaluación con usuarios reales en contexto de producción. |

La ausencia de las dos estrategias de campo es la limitación central de esta evaluación. El estándar pleno de maestría la habría exigido; el plazo y el acceso no lo permitieron. Se declara y se acota la contribución en consecuencia.

## 2. Evaluación formativa: ciclo con rediseño

Existe un ciclo formativo real con rediseño documentado. La instanciación parcial (antecedente de marzo de 2025, evaluado formativamente desde octubre de 2026) reveló dos defectos: mezcla de objetos de valor y de transferencia de datos, y ausencia inicial de prueba directa sobre el servicio principal. Esos hallazgos produjeron un rediseño explícito del método: caracterizar antes de mover, prueba directa sobre servicios principales, frontera incremental y autoridad de regla en servidor.

Este ciclo no se reclamó como evaluación de campo: fue aprendizaje sobre un artefacto existente, no uso con destinatarios reales. Pero cumple la condición mínima de maestría de que haya iteración con rediseño, distinta de un proceso lineal de ingeniería.

## 3. Evaluación sumativa: técnica y analítica

### 3.1. Utilidad de la instanciación (resultados por indicador)

| Indicador | Criterio fijado en E6 | Resultado observado | Lectura honesta |
|:--|:--|:--|:--|
| I01 | 100 % de correspondencia de decisiones en el conjunto acordado | Discrepancias: el límite 8/9 no se distingue; O03 no rechaza el día 9 | El sistema no cumple el criterio; la evidencia localiza la brecha |
| I02 | 100 % de rechazos sin certificación, seguimiento, autorización ni adjuntos | O06 de servidor rechaza sin llamar a los cuatro efectos prohibidos | Parcial: un caso comprobado con dobles, no persistencia real |
| I03 | Esfuerzo humano activo, espera y automatización separadas | Registro descriptivo consolidado 26:33.87, por autoinforme | Es descriptivo, no experimental independiente |
| I04 | Cero archivos de producción modificados para la ampliación | No medido: la capacidad extraordinaria no existe | Limitación declarada; modificabilidad solo argumentada |

La lectura honesta es que la evaluación sumativa no demuestra que la instanciación cumpla I01. Demuestra que el problema existe y que la solución no se ha completado: la separación parcial (V1) funciona en lo extraído, pero la decisión temporal sigue distribuida y su corrección no se construyó. Esto es una limitación, no un fracaso a ocultar; la tesis es sobre el método, y el método no se aplicó en su totalidad a esa corrección.

### 3.2. Contribución: argumentación analítica de modificabilidad

La modificabilidad no se midió empíricamente (I04 sin medir). Se argumenta analíticamente: el diseño propone separar la decisión y aplicar su autoridad en servidor, y existe una evidencia estructural relacionada —la comparación de la extracción de la restricción de subpartida, producción +57/−63 en tres archivos— que muestra un cambio localizado. Esto sustenta una afirmación débil de modificabilidad, no una demostración.

## 4. Muestra y roles

La muestra de diseño y la de evaluación no son idénticas: el constructor es el ejecutor principal, pero intervienen un revisor independiente (reduce el sesgo del constructor) y una fuente funcional (ratifica reglas de negocio). Ninguno de ellos constituye una muestra de usuarios en campo; son roles de control, no de evaluación naturalista. El sesgo de confirmación del constructor se mitiga parcialmente y se declara como amenaza interna.

## 5. Amenazas a la validez

| Tipo | Amenaza | Mitigación | Impacto residual |
|:--|:--|:--|:--|
| Constructo | I03 descriptivo por autoinforme; I04 no medido | Definiciones operacionales fijadas en E6 antes de construir | La modificabilidad queda argumentada, no medida |
| Interna | El antecedente de 2025 no fue producido por el método formalizado | Cronología documentada; se distingue antecedente de evaluación | No se puede atribuir causalidad al método sobre ese antecedente |
| Externa | Muestra única (un subcircuito, un sistema), sin campo | Condiciones de contorno y acotación de la contribución | Generalización solo analítica, no estadística |
| Conclusión | Riesgo de sobre-reclamar principios | Contribución limitada a lo que la evidencia soporta | No se reclaman principios validados sin evaluación de campo |

## 6. Gate de E8

El gate exige: al menos un ciclo formativo con rediseño documentado y un ciclo sumativo; muestra de evaluación no idéntica a la de diseño; criterios de éxito declarados antes de la evaluación; y amenazas identificadas con mitigación e impacto residual. Las secciones anteriores proponen ese cumplimiento, con la limitación explícita de que el ciclo sumativo es técnico y analítico, no de campo. Corresponde al tesista validar o corregir.

**Cierre, 4 de noviembre de 2026:** el tesista valida la lectura honesta —la evaluación sumativa localiza la brecha y no acredita cumplimiento total—. El gate de E8 se cumple: hay un ciclo formativo con rediseño documentado y un ciclo sumativo técnico, la muestra de evaluación no es idéntica a la de diseño, los criterios se fijaron antes de la evaluación y las amenazas están identificadas con mitigación e impacto residual.
