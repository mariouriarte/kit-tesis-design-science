# Registro de rediseño del método: P01 → M-R1

**Decisión:** el tesista responde «aprobado» a los cuatro ajustes de P3, P5, P7 y P8 después de recibir y ratificar la aplicación P01. **Estado:** rediseño formalizado; evaluación posterior pendiente. La aprobación no precedió a P01 y no se presenta como tal.

> **Actualización de estado posterior a la formalización:** P02 ya aplicó M-R1 y su dictamen está aceptado en `revision_aplicacion_p02_2026-11-06.md`, sección 7. E8, E9 y E10 están cerradas en sus alcances aceptados; E10 recoge los principios y conclusiones adoptados. Las formulaciones «pendiente» de este registro describen la situación al rediseñar y las preguntas fijadas entonces, no una ausencia actual de evaluación. No se reescribe RD01–RD04 como si sus resultados posteriores se hubieran conocido al decidirlos.

**Fecha de formalización:** 6 de noviembre de 2026, comprobada con el reloj del entorno en America/La_Paz. La sesión P01 conserva su fecha declarada del 5 de noviembre; no se atribuye el rediseño a esa sesión ni se inventa una hora de aprobación.

## 1. Versiones y preservación

Se denomina **M-P01** a las instrucciones generales que recibió el participante y **M-R1** a la versión rediseñada después de esa aplicación. Son identificadores documentales del método; no sustituyen las denominaciones V1–V3 del plan histórico de construcción ni implican tres aplicaciones realizadas. El texto operativo de M-R1 está en `metodo_refactorizacion_incremental_mr1.md`.

| Elemento preservado | Referencia |
|:--|:--|
| Diseño anterior a este rediseño | `tesis_ds/07c_diseno_artefacto.md` en el commit del kit `ed42c24421eb651c6d1c4033ac23ccb0737a8ab3`; objeto del archivo `026ed589b7880188739c7383ba61ecad45f8442c` |
| Ficha anterior | Objeto `3fd1d362d5620ac4ceea632d1b879b278b25b16b`, también sin diferencias respecto de ese commit antes de editar |
| Requisitos anteriores | Objeto `b22ddcaad8f678288cd57033ea1a458b936b1042`, también sin diferencias respecto de ese commit antes de editar |
| Material inicial M-P01 entregable sobre master | Objeto `0d74d7df1d877f4fbe08402db3711003ec339c2f`; SHA-256 y preparación en `preparacion_sesion_p01_2026-11-05.md` |
| Material P01 ratificado | Objetos del formulario y resultados en la actualización de `revision_aplicacion_p01_2026-11-05.md` |

Los objetos locales sin commit no son archivo permanente. El commit existente permite recuperar los tres documentos originales del kit; los materiales nuevos y la evidencia deben conservarse antes de limpiar copias u objetos. No se modificó la copia de trabajo del participante para formalizar M-R1.

## 2. Pregunta de diseño y evidencia de entrada

La pregunta de rediseño es: **¿cómo deben formularse las instrucciones para que el método no presuponga decisiones temporales o rechazos de dominio y para distinguir verificación local, integración y mediciones sin inducir cumplimiento aparente?** La entrada es la aplicación asistida P01, sus productos y la revisión técnica posterior, no una nueva búsqueda de resultados favorables. La evidencia procede de autorregistro con IA y comprobaciones finales reproducidas; no es observación directa.

Las pruebas finales de P01 aportan conservación observada del comportamiento, pero no prueban que M-R1 sea más comprensible. En especial, el material de P01 ya advertía que el instante podía no aplicar: se trata de incorporar esa condición al método general, no de atribuirle al participante un descubrimiento no anticipado. Tampoco la falta de compilación de Symfony demuestra un defecto de la implementación.

## 3. Cadena hallazgo → decisión → cambio → comprobación pendiente

| ID | Evidencia y límite | Formulación anterior | Decisión aprobada y formulación M-R1 | Qué falta comprobar |
|:--|:--|:--|:--|:--|
| RD01 | P3: selección sin dependencia temporal; advertencia ya presente en la consigna | Salida: entradas explícitas «gestión, instante» | Inventariar datos y dependencias pertinentes; instante condicionado a una decisión temporal | Si el practicante identifica entradas reales sin agregar tiempo innecesario ni requerir una aclaración adicional del autor |
| RD02 | P5: «rechazo» se interpretó como excepción con ayuda de IA | Prueba de comportamiento y ausencia de efectos prohibidos «ante rechazo» | Distinguir resultados normales, ausencia y fallos, con efectos permitidos/prohibidos pertinentes | Si clasifica resultados y efectos sin inventar rechazo ni ocultar errores como ausencia |
| RD03 | P7 se ratifica como completado con pendientes, sin compilación del contenedor | Un único criterio: integración verificada sin regresión observada | Separar P7-L y P7-I, conservando criterio integral y estado parcial cuando falta una parte | Si distingue lo local de lo integrado y respalda sus estados con evidencia; no aceptar una omisión como cumplimiento |
| RD04 | P8: documentación producida, esfuerzo/evolución no medidos y carga de medición percibida | Registro de costo y versión, sin distinción operativa suficiente | Trazabilidad obligatoria; mediciones con protocolo cuando se requieran, ausencias explícitas y conclusiones limitadas | Si documenta decisiones y versión sin inventar datos; si mantiene medidas necesarias para las afirmaciones que pretenda sostener |

Las observaciones pendientes no son resultados de M-R1 ni un protocolo sumativo aprobado. Sus unidades, tarea, muestra y reglas de decisión deberán fijarse antes de ejecutar ese episodio. No se aprobaron en este turno puntuaciones, porcentajes de éxito o una tarea nueva.

## 4. Qué cambia y qué se conserva

Se actualizan P3, P5, P7 y P8 del diseño y su correspondencia en la ficha. La métrica de R5 se armoniza para que las entradas temporales solo se exijan cuando correspondan; el registro de P8 explicita que no medir una propiedad limita la afirmación que dependa de ella. Esta armonización rige la versión nueva, no reevalúa retrospectivamente P01.

Se conservan P1, P2, P4 y P6, la tipología método más instanciación, la selección proporcional, la intención conservadora de la tarea P01 y sus criterios C01–C05. No se cambia el estado de medición de I01–I04, no se reabre I04 ni se completa integración productiva. Los principios de E10 no se declaran validados por este rediseño documental.

La necesidad de explicar C01–C05 queda como hallazgo adicional sobre el material de la tarea; no se incorpora un quinto cambio sustantivo al método bajo esta aprobación de cuatro ajustes. La eventual mejora del material de evaluación deberá identificarse separadamente.

## 5. Estado del ciclo y siguiente compromiso

Quedan documentadas la versión aplicada, la evidencia formativa, la ratificación y la versión rediseñada que esos hallazgos motivaron. Esto hace trazable el rediseño real del método, pero no acredita todavía que los cambios funcionen ni sustituye la evaluación sumativa exigida. Se requiere un episodio posterior sobre M-R1 con protocolo prospectivo.

Repetir sin más la misma tarea con el mismo participante introduciría aprendizaje; usar esa repetición requeriría declararlo y limitar la interpretación. Tampoco basta que el tesista relea el texto y lo considere más claro. La próxima decisión debe delimitar una evaluación de M-R1 factible, con alcance y evidencia proporcionados, sin reclamar dos contextos independientes como obligación añadida de maestría.
