# Borrador de propuesta para presentación — 31 de octubre de 2026

**Tesista:** Mario Arturo Uriarte Marin  
**Programa:** Maestría en Ingeniería de Software  
**Tutor:** Luis Roberto Pérez Rios, Ph.D.  
**Carácter del documento:** síntesis para exposición y revisión; no informe de investigación concluida.

## 1. Título y planteamiento central

**Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP.**

La propuesta no consiste en reescribir SIGPP ni en migrarlo íntegramente a otra arquitectura. Se diseñará y evaluará un método para seleccionar, proteger y verificar incrementos de refactorización en un subcircuito funcional existente. SIGPP proporciona el contexto de aplicación; los principios de diseño que puedan sostenerse mediante la evaluación constituirán la contribución de conocimiento. El trabajo se presenta como propuesta en desarrollo, con evidencia técnica preliminar y decisiones metodológicas todavía pendientes.

## 2. Problema práctico y alcance

SIGPP articula tareas, operaciones/ACP, presupuesto y certificación dentro de la ejecución POA. La inspección documentada identifica separación parcial de responsabilidades, junto con decisiones distribuidas entre controladores, servicios, persistencia y presentación. La selección de restricciones de subpartida permitió localizar una duplicación concreta; las comprobaciones temporales documentadas también muestran diferencias entre lo observado y lo requerido. No se afirma ausencia total de arquitectura o pruebas, ni se dispone aún de una medición del costo humano de modificar el flujo.

| Delimitación | Compromiso actual |
|:--|:--|
| Intervención principal | Subcircuito de ejecución POA; certificación como incremento técnico acotado. |
| Contexto disponible | SIGPP, con acceso técnico declarado por su desarrollador principal y datos ficticios para comprobaciones locales. |
| Restricciones | Continuidad operativa, datos sensibles y compatibilidad con el entorno existente. |
| Fuera de la intervención principal | Reescritura completa, migración integral a DDD o arquitectura hexagonal, elaboración y evaluación trimestral del POA e integración completa con contratación. |

## 3. Brecha y pregunta

El **problema de investigación —que en el formato institucional se registrará como problema científico—** es determinar qué adaptación y evidencia requieren los procedimientos existentes para seleccionar y verificar incrementos en la clase delimitada de aplicaciones. La revisión focalizada aporta antecedentes de cambio seguro, diseño arquitectónico y ciclos de refactorización, pero no demuestra todavía la validez de la adaptación propuesta. No se reclama que separar responsabilidades, usar pruebas o trabajar incrementalmente sea novedoso. La investigación deberá mostrar qué decisiones del método se sostienen con la aplicación y la evaluación, y cuáles deben corregirse.

**Pregunta principal:** ¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos de aplicaciones MVC heredadas, sin requerir reescritura completa ni interrupción operativa?

## 4. Objeto, objetivo y contribución prevista

En la resignificación propia de Design Science, el **objeto de estudio es el método propuesto**, no SIGPP ni el proceso POA. La tipología declarada es una composición de método más instanciación; el método deberá formalizarse y aplicarse, mientras el incremento de SIGPP aportará evidencia de su uso. El objetivo general es diseñarlo y evaluarlo para mejorar modificabilidad, testabilidad y trazabilidad de cambios sin reescritura completa. Construir una mejora funcional no bastará para cumplir el objetivo de conocimiento.

> La investigación se propone formular y evaluar principios de diseño para seleccionar, proteger y verificar incrementos de refactorización arquitectónica en subcircuitos de aplicaciones MVC heredadas, mediante un método aplicado en SIGPP bajo restricciones de continuidad operativa.

Los objetivos específicos cubren diagnóstico, fundamentación, diseño del método, aplicación, evaluación de utilidad y formulación/evaluación de principios. Sus formulaciones completas se conservan en `03_perfil_ds.md`. La contribución prevista es de nivel de maestría y de transferencia analítica acotada, no una teoría universal. No se presentan principios como validados antes de obtener la evidencia correspondiente.

## 5. Propuesta y fundamento

La base operativa aceptada es una adaptación explícita del ciclo de Girjoaba y Capiluppi (2024), complementada con el cambio seguro de Feathers (2004) y el razonamiento por atributos de calidad de Bass et al. (2021). Estos antecedentes orientan protección del comportamiento, selección de incrementos y evaluación contextual, sin convertirse en una contribución propia por combinarlos. La selección será proporcional: una errata de presentación no exige reorganizar la arquitectura, mientras una regla distribuida justifica investigar dependencias, comportamiento y riesgo. El detalle de pasos, alternativas, productos de trabajo y versiones todavía corresponde a la formalización pendiente del método.

Para el incremento temporal se acordó que la decisión extraordinaria tenga una única definición en el servidor, reutilizada por los consumidores pertinentes y sin duplicación de la regla en controladores o plantillas. La autoridad de fecha y hora operativa será el servidor PHP, en `America/La_Paz`, no el navegador. Esto no obliga a crear una clase por cada control ni demuestra que el diseño ya esté implementado. Se distinguirá extracción conservadora de incorporación de comportamientos nuevos, para no confundir refactorización con corrección funcional.

## 6. Evidencia disponible y límites

| Evidencia documentada | Afirmación defendible | Límite principal |
|:--|:--|:--|
| Comparación `5313c0e1` → `8dc63307`. | Dos consumidores delegan la selección de restricciones en un resolvedor. | Centralización no equivale a reducción global de acoplamiento o esfuerzo. |
| Instrumento común: 13 pruebas y 65 aserciones satisfactorias por estado comparado. | Conservación del comportamiento examinado en consumidores anteriores y posteriores. | Comprobación retrospectiva en entorno actual con clases históricas y dobles; no reconstrucción histórica completa o equivalencia universal. |
| Batería registrada en `5e0fec3d`: 188 pruebas y 540 aserciones satisfactorias. | Verificación técnica de ese estado. | No describirla como resultado de la revisión actual `7c0bca08`, que incorpora pruebas posteriores. |
| Cuestionario respondido por el Planificador Nacional. | Fuente funcional recibida, con autorización académica e identificación pública por cargo. | Persisten discrepancias y falta ratificación íntegra de la síntesis; no es evaluación del método. |
| Comprobación de fecha documental: 1 prueba, 1 aserción, 1 fallo registrado. | El instrumento documenta avance hasta solicitar correlativo antes del rechazo requerido. | Sin reloj controlado, HTTP o persistencia real; discrepancia de gestión en un auxiliar declarada en E6. |
| Comprobación horaria: 3 pruebas, 5 aserciones, 1 fallo registrado. | Para el mismo día, distintas horas producen distinta admisibilidad en el servicio examinado. | Evidencia local documentada, no reproducción nueva ni diagnóstico integral de producción. |

Los procedimientos y restricciones se conservan en `comparacion_extraccion_restriccion_2026-10-29.md` y `06_diagnostico.md`. La revisión local más reciente sitúa SIGPP en `feature/propuesta-tesis`, `7c0bca08`; no se ejecutó una nueva batería para preparar esta síntesis. Las duraciones asistidas registradas no son minutos humanos activos: I03 continúa sin línea base. La evidencia permite justificar continuar la investigación, no declarar mejora demostrada o método validado.

## 7. Evaluación prevista

Se mantiene el compromiso de al menos un ciclo formativo con hallazgos y rediseño documentados, seguido de un ciclo sumativo. La evaluación distinguirá utilidad del artefacto, aplicabilidad del método y respaldo de los principios de diseño. Existe disponibilidad declarada de un revisor técnico independiente y una fuente funcional consultada, pero sus papeles y la selección final aún deben precisarse. La extracción histórica no se presentará por sí sola como cumplimiento de un ciclo formativo completo.

| Indicador | Qué se observará | Estado |
|:--|:--|:--|
| I01. Correspondencia de decisiones | Resultados frente a expectativas funcionales explícitas. | Evidencia parcial; conjunto funcional completo y criterios pendientes. |
| I02. Rechazo antes de efectos | Ausencia de interacciones o efectos prohibidos cuando corresponde rechazar. | Instrumentos locales parciales; integración y suficiencia pendientes. |
| I03. Esfuerzo de comprobación | Minutos humanos activos de preparación, escritura/ajuste y análisis, separados de espera y automatización. | Procedimiento aceptado; sin línea base humana. |
| I04. Extensión del cambio posterior | Componentes existentes modificados y nuevos, separando producción, pruebas y configuración. | Escenario de ampliación por configuración aceptado; sin ejecución. |

Para I04 se acordó una ventana ficticia del 1 al 8 de febrero de 2027 y su ampliación al día 10, con inicio y cierre por días completos. Los seis casos contrastan antes del inicio, inicio, final del cierre original, comienzo de la ampliación, final del nuevo cierre y comienzo del día siguiente. Se espera ampliar la ventana sin modificar código, registrando el cambio de datos y las pruebas por separado. Esto comprueba flexibilidad de configuración, no incorporación de reglas nuevas ni mejora causal frente a una implementación anterior inexistente; los casos no equivalen a una apertura institucional autorizada.

## 8. Trabajo pendiente y cierre de exposición

E4 y E5 están cerradas como fundamentación y revisión focalizada; E6 permanece abierta y E7–E10 pendientes. Antes del nuevo incremento deben completarse los criterios, la línea base pertinente y el instrumento reproducible; después corresponde formalizar alternativas, requisitos, diseño y versiones del método. La construcción deberá reservar espacio para evaluación formativa, rediseño, evaluación sumativa y análisis de principios. El cronograma fechado, el modelo concreto de proceso DS, los papeles de evaluación y los criterios de suficiencia siguen por acordar; no se inventan para hacer parecer completo el borrador.

**Cierre sugerido:** «Presento una propuesta de método, no una migración arquitectónica terminada. Cuento con un contexto accesible, antecedentes contrastados y evidencia técnica preliminar que delimita la intervención. El compromiso pendiente es formalizar y evaluar el método, documentar el rediseño y determinar qué principios pueden sostenerse con la evidencia, sin atribuir al caso una generalidad que no tiene».

## Referencias citadas

Se reutilizan las verificaciones documentadas en E4 y E5; no se realizó una búsqueda bibliográfica nueva para esta síntesis.

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/ **[verificada en E4]**
- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055 **[verificada en E4]**
- Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079 **[metadatos verificados en E5; contenido consultado en manuscrito aportado, sin equivalencia editorial íntegra certificada]**
