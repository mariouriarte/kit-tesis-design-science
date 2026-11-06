# Revisión de suficiencia y pendientes para completar la tesis

**Fecha:** 5 de noviembre de 2026. **Naturaleza:** auditoría documental solicitada por el tesista; no contiene resultados experimentales nuevos ni modifica los compromisos de alcance por decisión unilateral.

## 1. Dictamen

El trabajo cuenta con delimitación, fundamentación, comparación de antecedentes, método formalizado, requisitos, ficha y evidencia técnica parcial. No obstante, los cierres registrados el 4 de noviembre no bastan para acreditar la suficiencia científica: faltan evidencias de aplicación y evaluación del método que sostengan los principios reclamados. La aprobación del tesista sobre una formulación confirma su aceptación, no valida empíricamente su contenido.

Se conservan los cierres como hechos históricos, pero su suficiencia queda observada, especialmente en E7e, E8 y E10. No corresponde declarar el trabajo listo para traducción final sobre la base exclusiva de esas etiquetas. Esta revisión corrige el criterio de suficiencia empleado en el acompañamiento anterior; no atribuye el defecto al tesista.

## 2. Hallazgos y condiciones de resolución

| Prioridad | Hallazgo verificable | Respaldo local | Qué falta para resolverlo |
|:--|:--|:--|:--|
| Crítica | Formalizar el método y comprobar software heredado no demuestra que otro practicante pueda aplicarlo ni que sus adaptaciones sean efectivas. | E7e, secciones 1 y 6; E7f, secciones 8 y 9. | Una aplicación trazable del método formalizado sobre un incremento real y acotado, con productos por paso; distinguir antecedentes retrospectivos de nueva aplicación. No exige reescritura ni construir todas las capacidades pendientes. |
| Crítica | La misma evidencia temporal se clasifica como diagnóstico y como evaluación sumativa. | E7e, sección 5: «no son […] una evaluación sumativa»; E8, secciones 1 y 3: técnica sumativa. | Separar qué se evaluó, sobre qué versión, con qué pregunta y criterios; no cambiar retrospectivamente la finalidad de una prueba. Realizar una evaluación final del método o justificar con evidencia una evaluación existente que realmente lo examine. |
| Crítica | No se acredita evaluación sumativa de campo o experimental del método, conforme al estándar de trabajo de esta asesoría. | E8, secciones 1, 3 y 6; E7f, sección 9. | Protocolo prospectivo adecuado a un método: aplicabilidad y efectividad en una tarea delimitada, unidades y selección justificadas, resultados y amenazas. Un entorno controlado puede ser pertinente; no se exige necesariamente producción. |
| Alta | El rediseño se narra, pero falta vincular con precisión las versiones del método, sus hallazgos y la evaluación posterior. | E8, sección 2; E7e, secciones 1 y 4. | Mostrar versión inicial, pregunta formativa, hallazgo, cambio concreto del método y comprobación posterior. Examinar primero el registro existente; no inventar fechas ni reconstruir una iteración inexistente. |
| Alta | La disponibilidad de un revisor no acredita una revisión realizada. | E8, sección 4, afirma intervención sin identificar informe o resultados en esa sección. | Localizar o recoger una revisión fechada: versión recibida, instrumento, observaciones, independencia, respuesta del constructor y decisiones. En los archivos revisados no se identificó ese respaldo; no se afirma su inexistencia fuera de ellos. |
| Alta | Los principios son candidatos sustentados; no se demuestra todavía su validación ni qué conocimiento adicional produce cada adaptación. | E10, secciones 1 y 5; matriz de coherencia, fila de contribución. | Matriz principio → antecedente → adaptación → mecanismo → aplicación → evidencia favorable/desfavorable → alcance. Distinguir prácticas heredadas de conocimiento generado en el caso. |
| Alta | El objetivo promete mejorar modificabilidad y testabilidad, pero los indicadores no demuestran globalmente esa mejora. | Matriz de coherencia, objetivo; E8, tabla de I01–I04. | Resolver con el tesista la correspondencia entre promesa y evidencia. Mantener resultados negativos; no sustituir metas por otras más cómodas después de observarlos. |
| Media | El documento institucional y su autoevaluación están desactualizados respecto de la formalización reciente. | `entrega_alsie/autoevaluacion_indicadores_avance.md`, corte del 22 de octubre; archivos identificados como avance. | Tras resolver la suficiencia DS, actualizar la traducción y autoevaluar nuevamente. No reutilizar como final el documento provisional. |
| Media | Hay estados editoriales contradictorios y nomenclatura ambigua. | E7b, E7e, E7f, E8–E10 abren con «en curso» y terminan con cierre; P1–P8 son pasos y P1–P5 son principios. | Armonizar estados al dictamen definitivo y distinguir identificadores de pasos y principios sin perder enlaces históricos. |

## 3. Lectura de los indicadores existentes

- **I01:** se conserva el resultado negativo del límite mensual 8/9; no prueba mejora ni cumplimiento del criterio del 100 %.
- **I02:** se conserva la evidencia de O06 con dobles; no acredita todos los rechazos ni persistencia real.
- **I03:** 26:33.87 es un registro descriptivo de esfuerzo con asistencia declarada; no demuestra ahorro frente a una condición comparable.
- **I04:** no medido. La comparación estructural de otra extracción no sustituye ese escenario. No es obligatorio construir una capacidad ajena al alcance para completar este indicador; si se mantiene sin medir, deben examinarse sus consecuencias sobre los requisitos y las afirmaciones.

La falta de resultados favorables no invalida automáticamente una investigación. El vacío crítico es que la evaluación presentada no permite todavía juzgar suficientemente el método propuesto, ni explicar qué principios resisten su aplicación. Declarar ese vacío como limitación no lo convierte en cumplimiento.

## 4. Distinciones que deben corregirse

**Evaluación de campo no equivale exclusivamente a producción.** Como el artefacto central es un método, su uso por desarrolladores en una tarea real puede aportar evidencia naturalista aunque el código se trabaje en una copia segura. Un ensayo experimental controlado también puede ser admisible si examina el método y sus criterios; ejecutar pruebas unitarias existentes no acredita por sí mismo ese diseño.

**Construir una capacidad y medir un cambio posterior no es, por definición, fabricar evidencia.** La frase de E9 que identifica ambas cosas es excesiva. Lo improcedente sería presentarla como capacidad preexistente o línea base histórica, ocultar su costo o diseñar las expectativas después de ver sus resultados; cualquier nueva construcción necesitaría decisión expresa y registro prospectivo.

**Un segundo contexto independiente no se impone como obligación de cierre de maestría.** Puede fortalecer la transferencia, pero no debe convertirse en sobrealcance. La prioridad es una aplicación y evaluación rigurosas en el alcance accesible, con afirmaciones proporcionadas.

## 5. Secuencia recomendada, pendiente de decisión del tesista

1. Seleccionar una única aplicación verificable del método y precisar qué afirmaciones pondrá a prueba. Se recomienda explorar primero un incremento acotado sobre el caso de certificación ya disponible, sin aprobar ahora su implementación.
2. Fijar antes de ejecutar el protocolo formativo y sumativo: participantes, independencia, criterios, comparación cuando proceda, datos, asistencia permitida y productos de trabajo. Reutilizar evidencia anterior solo con su finalidad y cronología reales.
3. Aplicar el método, registrar hallazgos y rediseño, y evaluar la versión resultante. Vincular los resultados, incluidos los negativos, con cada principio y requisito pertinente.
4. Revisar E7e–E10 y la matriz de coherencia; justificar cuáles cierres quedan efectivamente acreditados. E2 y E3 continúan preliminares y requieren armonización final con el alcance que se sostenga.
5. Consolidar el documento DS final en Markdown y, una vez suficiente, realizar la traducción institucional y la revisión de referencias, anexos y presentación. Las conversiones y la comprobación de carga se hacen después y no sustituyen el cierre científico.

El plazo de entrega registrado es el 10 de noviembre de 2026; quedan cinco días calendario desde esta revisión. No se garantiza que una evaluación rigurosa pueda completarse en ese intervalo sin confirmar participantes y alcance. Si no fuera viable, corresponde comunicar al tutor la brecha concreta y acordar su tratamiento, no certificar un cierre sin respaldo.

## 6. Alcance de la auditoría

Se leyeron el estado, la cadena rectora de coherencia, E7b, E7e, E7f, E8, E9, E10 y la autoevaluación institucional provisional; se identificaron los archivos de entrega disponibles y se consultaron los capítulos locales 10 y 13. No se ejecutaron pruebas nuevas, no se inspeccionó de nuevo SIGPP, no se verificó carga institucional y no se realizó una auditoría bibliográfica completa. Las observaciones se sustentan en contradicciones y resultados explícitos de esos archivos, no en una inferencia de inexistencia de todo respaldo externo.

Los capítulos locales contienen formulaciones distintas sobre la exigencia de múltiples contextos; para esta revisión se aplica la calibración explícita de la asesoría: principios evaluados, ciclo formativo con rediseño y ciclo sumativo de campo o experimental, sin imponer dos contextos independientes como requisito de maestría. No se incorporan referencias académicas nuevas no verificadas.
