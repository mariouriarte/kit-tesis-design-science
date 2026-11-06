# E8. Evaluación

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
