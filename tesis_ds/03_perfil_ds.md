# E3. Perfil de investigación Design Science

**Actualización para presentación del perfil borrador del 31 de octubre de 2026.** Documento de compromisos preliminares, no informe de investigación concluida. E4 y E5 están cerradas al alcance registrado; E6 permanece abierta y E7–E10 pendientes. La actualización armoniza decisiones ya tomadas y evidencia disponible, sin aprobar nuevos requisitos, una integración con contratación o el cierre del diseño metodológico.

## Título provisional

**Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP.**

El tesista aprobó esta formulación el 28 de octubre de 2026. El título declara el artefacto —método—, las actividades de diseño y evaluación, la clase de aplicaciones —MVC heredadas— y el contexto de aplicación —ejecución POA de SIGPP—. «Institucional» caracteriza las restricciones organizacionales del campo de acción, no una variante arquitectónica de MVC. La revisión terminológica no agrega FastAPI como caso ni extiende la evidencia a todas las aplicaciones MVC; los documentos de entregas anteriores conservan su título histórico.

## Planteamiento preliminar del problema

En SIGPP, el subcircuito de ejecución POA comprende tareas vinculadas a operaciones/ACP, presupuesto y certificación. La inspección documentada identifica separación parcial existente, junto con decisiones distribuidas entre controladores, servicios, repositorios, entidades Doctrine, consultas SQL y presentación. La extracción de selección de restricciones permite observar una duplicación concreta y su centralización, mientras la política temporal presenta diferencias entre comportamiento observado y requerido. Todavía falta medir el esfuerzo de cambio y de comprobación; no se afirma que toda modificación exija múltiples capas o que el sistema completo carezca de pruebas o fronteras.

El problema de investigación —que en el formato institucional se registrará como **problema científico**— se plantea como una brecha acotada: los antecedentes ofrecen procedimientos de cambio seguro y ciclos de refactorización, pero la revisión focalizada documentada no aporta evidencia suficiente sobre la adaptación concreta que aquí se propone para seleccionar y verificar incrementos en el campo delimitado. El estudio deberá formalizar y evaluar esa adaptación, no demostrar que arquitectura, refactorización o pruebas son ideas nuevas. E4 y E5 sustentan las decisiones y la necesidad de operacionalizar la propuesta; no prueban inexistencia universal de soluciones, superioridad ni originalidad validada. Este refinamiento se registra después del contraste bibliográfico, no como formulación demostrada desde el encuadre.

## Objeto de estudio

En Design Science, el objeto de estudio es el artefacto propuesto, no SIGPP ni el proceso POA. El objeto de estudio es un **método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas**, cuya aplicación y evaluación se realizarán en SIGPP.

La tipología del artefacto es una **composición**: método + instanciación. El método constituye el componente transferible; la instanciación en SIGPP constituye el vehículo de construcción, demostración y evaluación.

## Campo de acción

El campo de acción comprende subcircuitos funcionales críticos de aplicaciones MVC heredadas en contextos institucionales, con lógica de negocio dispersa, alto acoplamiento al marco de desarrollo y a la persistencia, y necesidad de evolución sin reescritura completa. Son condiciones del contexto y del problema a contrastar, no atributos inherentes a MVC ni a toda aplicación institucional.

En esta tesis, el campo se concreta en el subcircuito de ejecución POA de SIGPP: tareas, operaciones/ACP, presupuesto y certificación. Elaboración POA, validación ministerial y evaluación POA trimestral se consideran contexto y alcance posterior recomendado, no intervención principal.

## Propuesta

Se propone diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos funcionales críticos de aplicaciones MVC heredadas, aplicado en el subcircuito de ejecución POA de SIGPP, con el fin de explicitar fronteras funcionales, separar reglas de negocio de controladores y persistencia, e incorporar pruebas automatizadas que permitan evolucionar el flujo sin reescritura completa.

## Contribución original preliminar

**Base operativa aceptada el 28 de octubre de 2026:** el método se diseñará como una adaptación explícita del ciclo de Girjoaba y Capiluppi (2024), complementada con cambio seguro de Feathers (2004) y razonamiento por atributos y refinamiento de ADD (Bass et al., 2021). No se reclama autoría sobre los pasos heredados ni se presume originalidad por combinarlos. La adaptación y el conocimiento que pueda generar deberán contrastarse y evaluarse dentro del campo definido; no cambia el título ni la tipología método más instanciación.

El tesista precisó que su aplicación debe ser selectiva y proporcional al comportamiento, dependencias y riesgo: no se fuerza reorganización arquitectónica ante una errata de presentación. Cuando una modificación de negocio afecte decisiones dispersas, el método deberá orientar su investigación y protección antes de elegir una intervención focalizada. Un servicio nuevo es una opción de diseño, no una salida obligatoria para todos los cambios; concentrar toda lógica del subcircuito tampoco es el objetivo. La selección y sus efectos deberán documentarse y evaluarse, no darse por correctos por seguir el ciclo.

La contribución original preliminar consiste en formular y evaluar principios de diseño para aplicar refactorización arquitectónica incremental en subcircuitos de aplicaciones MVC heredadas, mostrando cómo traducir principios conocidos de separación de responsabilidades y testabilidad en un método aplicable bajo restricciones reales de continuidad operativa, normativa institucional y datos sensibles. La originalidad y la validación siguen pendientes; el título no las acredita.

Oración candidata de contribución original, en nivel de maestría:

> Esta investigación se propone formular y evaluar principios de diseño para seleccionar, proteger y verificar incrementos de refactorización arquitectónica en subcircuitos de aplicaciones MVC heredadas, mediante un método aplicado en SIGPP bajo restricciones de continuidad operativa.

Esta oración expresa la contribución prevista, no un resultado alcanzado. La formulación anterior, aceptada para el perfil inicial, empleaba «aporta principios de diseño validados» como expectativa; se corrige su tiempo y alcance para no presentar validación pendiente como evidencia existente. El diseño y la evaluación aún deberán determinar qué principios se sostienen, para qué contextos y con qué limitaciones.

## Pregunta de investigación preliminar

¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos de aplicaciones MVC heredadas, sin requerir reescritura completa ni interrupción operativa?

## Subpreguntas preliminares

1. ¿Qué evidencias técnicas muestran la dispersión de lógica, el acoplamiento y la baja testabilidad del subcircuito de ejecución POA en SIGPP?
2. ¿Qué propiedades debe tener un método de refactorización arquitectónica incremental para ser aplicable en subcircuitos de aplicaciones MVC heredadas bajo las restricciones institucionales declaradas?
3. ¿En qué medida la instanciación del método en SIGPP mejora la separación de responsabilidades, la trazabilidad del cambio y la validación automatizada del flujo intervenido?

## Objetivo general preliminar

Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.

## Objetivos específicos preliminares

1. Diagnosticar el estado arquitectónico y de testabilidad del subcircuito de ejecución POA en SIGPP mediante análisis de controladores, servicios, repositorios, entidades, consultas SQL y pruebas existentes.
2. Sistematizar la base de conocimiento sobre arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas legacy MVC.
3. Diseñar el método de refactorización arquitectónica incremental, definiendo pasos, criterios, entradas, salidas y condiciones de aplicación.
4. Instanciar el método en el subcircuito de ejecución POA de SIGPP, manteniendo compatibilidad funcional y usando datos ficticios en entorno controlado.
5. Evaluar la utilidad del método mediante métricas técnicas, revisión independiente y validación institucional acotada.
6. Formular y evaluar principios de diseño a partir de los resultados de aplicación y evaluación del método, explicitando los contextos, mecanismos y límites que la evidencia permita sostener.

El tesista aceptó expresamente el sexto objetivo durante la revisión del perfil borrador del 29 de octubre de 2026. Se incorpora para explicitar la generación de conocimiento ya prevista en la contribución; su aceptación no significa que los principios estén formulados o validados. Los objetivos de aplicación y utilidad se complementan así con un objetivo específico de conocimiento. El procedimiento de análisis y la suficiencia de la evidencia todavía deben precisarse.

## Estrategia metodológica preliminar

El estudio seguirá el enfoque de Design Science, con construcción y evaluación del artefacto. Para nivel de maestría, se planifica al menos un ciclo de evaluación formativa con rediseño documentado y un ciclo sumativo. La evaluación deberá distinguir utilidad práctica del método en SIGPP y contribución de conocimiento mediante principios de diseño transferibles analíticamente a aplicaciones MVC heredadas bajo condiciones semejantes a las del campo de acción.

## Criterios preliminares de evaluación

Las propiedades se operacionalizan en E6 mediante I01, correspondencia de decisiones con resultados esperados; I02, rechazo antes de efectos prohibidos; I03, esfuerzo activo de preparar y comprobar escenarios; e I04, extensión de un cambio posterior representativo. Son instrumentos propuestos, con líneas base y criterios definitivos todavía incompletos, no umbrales aprobados para evaluar retrospectivamente el código. Menos líneas, más pruebas o un nuevo servicio no constituyen por sí solos mejora de modificabilidad o testabilidad. La trazabilidad y la revisión independiente complementarán la evidencia de utilidad y aplicabilidad, sin sustituir mediciones y ciclos de evaluación.

**Acuerdos posteriores a la predefensa:** I01 tiene aceptado el 100 % de correspondencia en el conjunto previamente acordado; I02, el 100 % de rechazos acordados sin crear certificación, seguimiento, autorización o almacenar adjuntos. Se conservan resultados individuales y fallos. No se aplican retrospectivamente como metas previas de las extracciones, ni acreditan conjuntos cerrados, línea base completa o método validado. Los casos, instrumentos y demás criterios siguen por completar en E6; I03 continúa sin línea base humana.

## Evidencia preliminar disponible para presentar

| Evidencia | Qué permite sostener | Qué no permite sostener |
|:--|:--|:--|
| Comparación Git `5313c0e1` → `8dc63307`. | Centralización de dos implementaciones de selección de restricciones en un resolvedor, con dependencia de repositorios conservada en este. | Independencia completa de persistencia, mejor rendimiento o mejora medida del esfuerzo. |
| Ejecución actual en `feature/propuesta-tesis`, `5e0fec3d`: 188 pruebas y 540 aserciones satisfactorias. | Verificación de la batería disponible en ese estado. | Integración completa, cobertura total o validación del método. |
| Trece pruebas y 65 aserciones comunes, satisfactorias en consumidores anteriores y posteriores. | Conservación de selección, propagación de excepciones y limpieza de estado para los casos examinados. | Equivalencia universal o reconstrucción de la aplicación histórica completa: se cargaron dos clases anteriores en el entorno actual con dobles. |
| Cuestionario respondido por el Planificador Nacional, fechado el 29 de octubre y revisado el 30. | Fuente funcional recibida con autorización académica e identificación pública por cargo; concordancias y discrepancias documentadas en E6. | Ratificación íntegra de la síntesis, resolución de todas las excepciones o evaluación independiente del método. |
| Dos comprobaciones locales documentadas de fecha documental y variación horaria. | Registros de avance hasta solicitud de correlativo y de distinta admisibilidad según hora, con límites del instrumento descritos en E6. | Reproducción HTTP, persistencia real, medición de esfuerzo humano o validación del método. |

### Acuerdos del 30 de octubre para la propuesta

La autoridad de fecha y hora operativa será el servidor PHP, en `America/La_Paz`, no el navegador; el mecanismo concreto para controlar el tiempo en pruebas sigue pendiente. Se aceptó una definición única de la decisión extraordinaria en el servidor, reutilizada por sus consumidores. Para I04 se acordó comprobar una ampliación del cierre mediante configuración, sin modificar código: ventana ficticia del 1 al 8 de febrero de 2027, ampliada hasta el 10, con seis casos de frontera y días completos de inicio y cierre. Estos acuerdos fijan parte del plan prospectivo, no una capacidad implementada ni una mejora comparativa demostrada; I03 continúa sin medición humana y E6 permanece abierta.

El procedimiento reproducible y los límites están en `comparacion_extraccion_restriccion_2026-10-29.md`, sección 6. La comparación se seleccionó y ejecutó retrospectivamente; no acredita que las pruebas precedieran a la extracción ni que existiera un ciclo formativo completo con rediseño. La intervención no fue desplegada en producción según declaración del tesista. Las cifras de `master` corresponden a otra evolución del código y no se utilizan como comparación causal directa.

## Compromisos pendientes del perfil borrador

El perfil tiene una base sustantiva para revisión, pero no se declara completo frente a las catorce secciones del capítulo metodológico local. La siguiente tabla distingue información disponible de compromisos que todavía debe resolver el tesista. No se asignan fechas, participantes, umbrales o decisiones de diseño por conveniencia de presentación. La entrega de un borrador no cierra las etapas pendientes.

| Componente | Estado al preparar la presentación | Compromiso pendiente |
|:--|:--|:--|
| Título, objeto, tipología, campo y pregunta. | Formulaciones preliminares documentadas. | Revisar su coherencia al cerrar indicadores y diseño, sin ampliar el alcance por integraciones anunciadas. |
| Fundamentación y antecedentes. | E4 y E5 cerradas como fundamentación y revisión focalizada. | Mantener trazabilidad de decisiones y límites; no presentar adaptación como novedad ya probada. |
| Objetivos de conocimiento. | Sexto objetivo de formulación y evaluación de principios aceptado expresamente por el tesista el 29 de octubre. | Operacionalizar su análisis y suficiencia de evidencia; aceptación del objetivo no equivale a validación de principios. |
| Modelo de proceso de investigación. | Enfoque DS y secuencia formativa–rediseño–sumativa prevista. | Precisar y justificar el modelo de proceso y la estrategia de evaluación; el ciclo técnico adaptado no sustituye el proceso de investigación. |
| Diagnóstico y criterios. | E6 abierta, I01–I04 propuestos y evidencia histórica separada. | Completar línea base, resultados esperados y criterios antes del próximo incremento. |
| Selección de participantes. | Referente funcional identificada y revisor técnico disponible según declaración. | Definir funciones, acceso y separación entre fuentes de diseño y evaluación; no tratarlos como una muestra ya constituida. |
| Cronograma. | Presentación de borrador el 31 de octubre; defensa final de noviembre todavía extraoficial. | Acordar fechas viables con espacio explícito para evaluación formativa, rediseño, sumativa, análisis y escritura. |
| Plan de análisis. | Instrumentos técnicos propuestos y trazabilidad documental. | Definir cómo pasar de resultados y discrepancias a principios con contexto, mecanismo y límites; criterios de suficiencia de evidencia pendientes. |
| Artefacto previsto. | Método adaptado con aplicación preliminar; base operativa y selección proporcional aceptadas. | E7 deberá formalizar alternativas, requisitos, pasos, productos, versiones y suficiencia; la extracción existente no reemplaza la ficha del método. |

La consulta de tareas y certificaciones para contratación permanece como escenario candidato de evolución. Existe una API de lectura con separación parcial; no se ha demostrado que la nueva consulta mida la modificabilidad de las responsabilidades ya intervenidas. No se comprometen para esta presentación una integración completa, provisión de usuarios, migración CI/CD o reconstrucción histórica. La necesidad operativa se conserva en E6 sin desplazar el artefacto ni los indicadores de la tesis.

## Cierre preliminar de E3

Se conserva el cierre preliminar de E3 del perfil inicial; no se convierte en un cierre definitivo por actualizar el documento. E4 y E5 ya aportan fundamentación y contraste, mientras E6 debe completar indicadores y criterios prospectivos antes de una nueva intervención planificada. La evidencia técnica anterior se presenta como preliminar y retrospectiva, no como evaluación integral del método. Los compromisos pendientes anteriores deberán resolverse explícitamente, sin simular un perfil metodológicamente completo.

## Referencias citadas

Se reutilizan las verificaciones registradas en E4 y E5, sin atribuir una búsqueda nueva a esta actualización.

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/ **[verificada en E4]**
- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055 **[verificada en E4]**
- Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079 **[metadatos verificados en E5; contenido consultado en manuscrito aportado, sin equivalencia editorial íntegra certificada]**
