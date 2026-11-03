# Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP

**Trabajo original bajo el enfoque de investigación en Design Science — consolidación de avance para predefensa**

**Tesista:** Mario Arturo Uriarte Marin.

**Programa:** Maestría en Ingeniería de Software.

**Tutor:** Luis Roberto Pérez Rios, Ph.D.

**Fecha de consolidación:** 31 de octubre de 2026.

**Corte de decisiones y evidencia de investigación:** registros disponibles hasta el 30 de octubre de 2026.

**Inicio del encuadre:** 27 de septiembre de 2026.

## Condición y procedencia del documento

Este documento consolida el trabajo original de investigación en Design Science —DSR, por su denominación en inglés— disponible en `tesis_ds/`. Se prepara para la entrega de predefensa solicitada por el tutor el 31 de octubre, antes de la presentación. No es el IFI en estructura ALSIE, una traducción institucional final o una investigación concluida. Su consolidación reúne compromisos, fundamentos y evidencia existentes; no incorpora decisiones científicas, experimentos, mediciones ni autorizaciones nuevas.

El estado rector mantiene E0 y E1 cerradas; E2 y E3 cerradas preliminarmente para el perfil; E4 cerrada como fundamentación y E5 como revisión focalizada; E6 abierta; E7–E10 pendientes. La existencia de notas preliminares de requisitos, diseño y verificación no acredita el cierre de esas etapas. Se priorizan las precisiones posteriores cuando los borradores iniciales conservan afirmaciones superadas, sin atribuir a una fecha anterior conocimiento adquirido después. El anexo A identifica las fuentes de la consolidación y los criterios utilizados para resolver esos desfases.

## Resumen

Se propone diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas, aplicado a la ejecución de la planificación operativa anual de SIGPP, en la Caja Petrolera de Salud. El problema práctico comprende decisiones distribuidas y duplicación localizada que dificultan delimitar cambios verificables, sin que se haya cuantificado todavía su costo institucional. La contribución prevista son principios de diseño sobre selección, protección y verificación de incrementos, no la reorganización del código por sí misma. La fundamentación relaciona cambio seguro, escenarios de calidad y testabilidad; la revisión focalizada reconoce procedimientos existentes y adopta como base operativa una adaptación explícita del ciclo de Girjoaba y Capiluppi (2024), sin presentarla como aporte ya validado.

Una comparación retrospectiva de selección de restricciones registró trece pruebas y 65 aserciones satisfactorias por estado, utilizando clases históricas y dobles en el entorno actual. Se recibió una fuente funcional autorizada y se documentaron discrepancias temporales mediante comprobaciones locales, sin reproducir el recorrido HTTP o persistencia real. El diagnóstico conserva cuatro indicadores propuestos, con criterios incompletos y sin línea base humana de esfuerzo. La formalización completa del método, su aplicación documentada, la evaluación con rediseño y la evaluación final permanecen pendientes. La evidencia disponible permite delimitar la intervención y sus límites, pero no demuestra reducción de esfuerzo, mejora arquitectónica global, principios validados ni transferencia universal.

## 1. Contexto y motivación

SIGPP, Sistema Integral de Gestión POA Presupuesto, articula elaboración, validación y ejecución de la planificación operativa anual —POA—, presupuesto y certificación en la Caja Petrolera de Salud —CPS—. En el subcircuito seleccionado se relacionan tareas, operaciones y acciones de corto plazo —ACP— con recursos y certificaciones. El Departamento Nacional de Gestión y Planificación se identifica como área dueña del sistema según el contexto declarado por el tesista. La continuidad de uso y la sensibilidad de los datos condicionan la intervención; no se presentan como resultados demostrados de la propuesta.

El tesista es creador y desarrollador principal de SIGPP y declaró acceso técnico suficiente para construir y evaluar con datos ficticios en un entorno local. La aplicación examinada utiliza PHP 7.4, Symfony 4.4, Doctrine, formularios y plantillas Twig; una ejecución registrada informó PHP 7.4.29 y PHPUnit 9.6.15. Ese acceso facilita reconocer reglas implícitas e historial, pero introduce sesgo de constructor. La disponibilidad declarada de otro desarrollador conocedor del sistema aporta una posibilidad de revisión, no una evaluación independiente ya realizada.

Los documentos de dominio sitúan el contexto sin demostrar propiedades arquitectónicas. El RE-SPO de la CPS, aprobado mediante R.H.D. 003/19 de 11 de marzo de 2019, respalda relaciones de operaciones, tareas y modificaciones; el reglamento presupuestario y las directrices de gestión aportan restricciones distintas (Caja Petrolera de Salud, 2007, 2019, 2026). Las directrices contemplan tareas con o sin presupuesto, por lo que no toda tarea se trata automáticamente como una asignación monetaria. El manual aportado como quinto borrador no se convierte en norma vigente por su disponibilidad, y esos documentos no acreditan por sí mismos las excepciones de fecha específicas de certificación.

## 2. Problema de diseño y delimitación

### 2.1. Situación práctica

La inspección documentada muestra separación parcial de responsabilidades y decisiones distribuidas entre controladores, servicios, repositorios, entidades persistentes, consultas y presentación. En selección de restricciones se identificaron dos implementaciones equivalentes dentro de los consumidores comparados; posteriormente ambas delegan en un resolvedor. En fechas, las comprobaciones inspeccionadas tienen alcances diferentes entre presentación y servicio. Estas observaciones justifican estudiar una frontera funcional explícita, pero no permiten afirmar que SIGPP carezca de arquitectura, que toda dependencia sea defectuosa o que todo cambio exija modificar varias capas.

La consecuencia práctica esperada es dificultad para localizar, modificar y comprobar decisiones sin alterar efectos relacionados. No se dispone de medición del costo institucional, tasa de incidentes, cobertura porcentual o esfuerzo humano comparativo. La intervención no se justifica por el número de clases ni por preferencia por una arquitectura nominal. El problema exige mantener separadas la evidencia estructural, la discrepancia funcional y las expectativas de mejora.

| Componente | Delimitación documentada |
|:--|:--|
| Contexto | Ejecución POA de SIGPP en la CPS; aplicación MVC heredada con continuidad operativa y datos sensibles. |
| Problema | Decisiones distribuidas, duplicación localizada y comprobaciones de distinto alcance; frontera del incremento aún parcial. |
| Solución conceptual | Método para seleccionar, proteger y verificar transformaciones arquitectónicas incrementales, aplicado en certificación. |
| Criterios de éxito | Propiedades preliminares de comportamiento, rechazo antes de efectos, esfuerzo y cambio posterior; operacionalización y suficiencia aún incompletas. |

### 2.2. Alcance y exclusiones

El alcance principal comprende ejecución POA: tareas vinculadas a operaciones y ACP, presupuesto y certificación. Certificación constituye el incremento técnico acotado de referencia, no una demostración de intervención completa en todos los módulos. Elaboración, validación ministerial y evaluación trimestral se mantienen como contexto y posible trabajo posterior. La consulta desde contratación y la evolución de CI/CD son necesidades contextuales registradas, no objetivos adicionales automáticamente incorporados.

No se promete reescritura, migración completa a DDD, arquitectura hexagonal o microservicios, sustitución de Doctrine ni actualización mayor de Symfony. Tampoco se incluyen auditoría general de seguridad, integración financiera completa, reconstrucción histórica de saldos o normalización masiva de datos. Los controles de saldo y permisos se conservan como condiciones del flujo, sin convertirlos en reestructuración obligatoria. Estos límites protegen la atribución de resultados y la viabilidad del trabajo, no demuestran que el incremento ya sea suficiente.

## 3. Problema de investigación —institucionalmente, problema científico—, objeto y contribución prevista

### 3.1. Brecha y pregunta

El **problema de investigación —que en el formato institucional se registrará como problema científico—** no se formula como ausencia general de técnicas de refactorización. Feathers (2004), Bass et al. (2021) y Girjoaba y Capiluppi (2024) ya aportan procedimientos de cambio, razonamiento arquitectónico y ciclos verificables. La brecha candidata se concentra en precisar y evaluar una adaptación para seleccionar y verificar incrementos en subcircuitos MVC con decisiones distribuidas y restricciones institucionales. La revisión focalizada justifica operacionalizar esa adaptación; no demuestra inexistencia universal de soluciones ni originalidad validada.

La formulación se refinó después del contraste bibliográfico y se registra como tal. Diferencias de lenguaje —PHP frente a C++—, institución o nombre del procedimiento no constituyen por sí solas conocimiento nuevo. La investigación deberá distinguir qué toma de los antecedentes, qué adapta y qué evidencia permite sostener esas decisiones. Si la aplicación no genera conocimiento adicional defendible, deberá reducirse la contribución reclamada.

**Pregunta principal:** ¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos de aplicaciones MVC heredadas, sin requerir reescritura completa ni interrupción operativa?

Las subpreguntas preliminares examinan la evidencia de dispersión y capacidad de prueba, las propiedades necesarias para que el método sea aplicable y la utilidad de su aplicación acotada. No se responde la pregunta principal solamente describiendo el código o recogiendo percepciones. Requiere formalizar, aplicar y evaluar el método y analizar el conocimiento que pueda derivarse. La continuidad operativa incluida en la pregunta necesita evidencia propia y no queda probada por éxito unitario.

### 3.2. Objeto de estudio y campo de acción

En la resignificación de Design Science adoptada en este trabajo, el **objeto de estudio es el artefacto propuesto**: el método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas. La tipología declarada es una composición de **método más instanciación**; el método constituye el componente transferible y su aplicación en SIGPP el vehículo de evidencia. Construir el método implica formalizar y aplicar, no únicamente desarrollar software. SIGPP y el proceso administrativo POA pertenecen al contexto, no sustituyen al objeto.

El campo comprende subcircuitos funcionales críticos de aplicaciones MVC heredadas en contextos institucionales, con lógica distribuida, dependencia del marco y persistencia y necesidad de evolución sin reescritura completa. En el caso concreto se delimita a ejecución POA y certificación. La transferencia pretendida es analítica hacia contextos con semejanzas justificadas, no estadística a toda institución o sistema heredado. «Institucional» describe restricciones del contexto, no una variante arquitectónica de MVC.

### 3.3. Objetivo general y objetivos específicos

**Objetivo general:** diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.

1. Diagnosticar el estado arquitectónico y de testabilidad del subcircuito de ejecución POA en SIGPP mediante análisis de controladores, servicios, repositorios, entidades, consultas SQL y pruebas existentes.
2. Sistematizar la base de conocimiento sobre arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas heredados MVC.
3. Diseñar el método de refactorización arquitectónica incremental, definiendo pasos, criterios, entradas, salidas y condiciones de aplicación.
4. Instanciar el método en el subcircuito de ejecución POA de SIGPP, manteniendo compatibilidad funcional y usando datos ficticios en entorno controlado.
5. Evaluar la utilidad del método mediante métricas técnicas, revisión independiente y validación institucional acotada.
6. Formular y evaluar principios de diseño a partir de los resultados de aplicación y evaluación del método, explicitando los contextos, mecanismos y límites que la evidencia permita sostener.

El sexto objetivo fue aceptado expresamente el 29 de octubre y hace explícito el compromiso de conocimiento. Su incorporación no añade un resultado ya obtenido ni acredita principios formulados o validados. El análisis y los criterios de suficiencia necesarios para cumplirlo permanecen pendientes. Esta consolidación conserva los seis objetivos, sin reformularlos para ajustarlos a cuatro capítulos institucionales.

### 3.4. Enunciado de contribución prevista

> Esta investigación se propone formular y evaluar principios de diseño para seleccionar, proteger y verificar incrementos de refactorización arquitectónica en subcircuitos de aplicaciones MVC heredadas, mediante un método aplicado en SIGPP bajo restricciones de continuidad operativa.

El enunciado describe una aspiración de nivel de maestría, no una conclusión. La mejora del sistema puede aportar utilidad local, pero no reemplaza principios utilizables por otro investigador sin reproducir exactamente las mismas clases. El nivel de abstracción pretendido y la presentación de conocimiento deben permanecer proporcionados a la evidencia (Gregor & Hevner, 2013). No se reclama una teoría de diseño general ni condiciones universales de eficacia.

## 4. Enfoque metodológico y estado de ejecución

El enfoque es Design Science, con construcción y evaluación de un artefacto y distinción entre utilidad y conocimiento (Hevner et al., 2004; Peffers et al., 2007; Wieringa, 2014). Se mantiene el compromiso de un ciclo formativo con rediseño documentado y un ciclo sumativo. FEDS sirve como referencia para distinguir propósito formativo y sumativo y entorno artificial o naturalista (Venable et al., 2016). El mínimo particular de ciclos corresponde al estándar de esta asesoría, no se atribuye como exigencia universal del artículo FEDS.

No está definitivamente seleccionado y justificado el modelo concreto de proceso de investigación ni cerrada la secuencia de estrategias de evaluación. El ciclo técnico de Girjoaba y Capiluppi no sustituye por sí mismo un proceso de investigación. Las inspecciones, comparaciones y pruebas parciales tampoco se rebautizan como experimento controlado o evaluación sumativa. La formalización deberá distinguir actividades ya realizadas, evaluación prevista y decisiones todavía abiertas.

| Componente | Situación al corte |
|:--|:--|
| Contexto y selección | SIGPP elegido intencionalmente por acceso y pertinencia; unidades y selección de evaluación por precisar. |
| Fundamentación y comparación | E4/E5 cerradas al alcance documentado el 28 de octubre. |
| Diagnóstico | E6 abierta; indicadores propuestos y evidencia parcial, sin criterios completos. |
| Diseño y construcción del método | Existen borradores y antecedentes técnicos; E7a–E7f pendientes. |
| Evaluación y contribución | E8–E10 pendientes; no hay método completo validado. |

La evaluación deberá separar practicantes que aportan al diseño de participantes que juzgan la propuesta y controlar el sesgo del constructor. La fuente funcional confirma o cuestiona expectativas de negocio; no representa automáticamente una evaluación independiente del método. La disponibilidad de un revisor tampoco constituye muestra constituida o revisión realizada. No se justifican inferencias estadísticas por contar casos parametrizados de una prueba como observaciones independientes.

## 5. Base de conocimiento que orienta el diseño

### 5.1. Cambio seguro y preservación del comportamiento

Feathers (2004, pp. 14–20) aborda la dificultad de introducir pruebas cuando las dependencias impiden aislar código. Esto justifica identificar puntos de cambio y comprobación y aceptar separaciones mínimas conservadoras cuando resultan necesarias para probar. No autoriza una extracción masiva sin protección ni exige cobertura completa antes de cualquier movimiento. La decisión relevante es documentar qué comportamiento se protege y cuál riesgo residual permanece.

La caracterización registra comportamiento real, no intención institucional; además debe comprobarse la conexión del componente extraído con sus consumidores (Feathers, 2004, pp. 186–190, 194–195). Una prueba aislada puede pasar aunque el servicio no aplique la decisión. En SIGPP, proteger la selección de restricciones no demuestra cumplimiento de la política de fechas ni ausencia de efectos ante rechazo. Esta distinción modifica el diseño del instrumento y la amplitud de las conclusiones.

Fowler (2018, pp. 45–47) permite distinguir refactorización de incorporación o corrección funcional. Extraer el rango anual conservando resultados puede ser estructural; agregar una habilitación extraordinaria o rechazos faltantes modifica aceptaciones. Ambas actividades pueden alternarse en incrementos pequeños, pero necesitan trazabilidad separada. La existencia de pruebas no acredita la secuencia de TDD, que exige prueba previa, implementación y refactorización (Fowler, 2023).

### 5.2. Responsabilidades, escenarios y testabilidad

Bass et al. (2021, secs. 3.3 y 8.2) vinculan las decisiones arquitectónicas con escenarios y motivos de cambio, no con cantidad de carpetas. La modificabilidad requiere definir qué cambio se pide y cómo se observa su costo. El costo de preparar un mecanismo de variación y el de utilizarlo después no son intercambiables. Por ello, medir solamente una configuración administrativa futura no acreditaría ahorro neto de la transformación inicial.

La testabilidad requiere controlar entradas y observar resultados y efectos (Bass et al., 2021, secs. 12.1–12.2). En reglas temporales eso obliga a distinguir día documental, instante del intento, datos de habilitación y consumidor. La autoridad operativa del servidor no resuelve automáticamente el control del tiempo en pruebas. Tampoco una prueba con dobles verifica base de datos, transacciones o archivos reales.

Stafford (2003) fundamenta la capa de servicios como frontera de operaciones y coordinación. Su aplicación no convierte todo acceso del controlador en defecto ni exige independencia completa del marco. La propuesta considera conservar Symfony, Doctrine y entidades durante una transición acotada, con excepciones explícitas. La preparación de pantalla se separaría solamente si una necesidad documentada lo justifica, no para completar un diagrama de clases.

### 5.3. Evidencia reciente y límites de inferencia

E4 incorporó tres trabajos únicos recientes con texto accesible y lectura focalizada, no lectura íntegra atribuida al tesista. AlOmar et al. (2021) ayudan a distinguir intención de reutilización y transformación de una mejora demostrada. Zakeri-Nasrabadi y Parsa (2022) relacionan esfuerzo y efectividad bajo condiciones explícitas, pero su evidencia Java y generación automatizada no constituyen un instrumento validado para PHP. Noei et al. (2025) advierten diferencias entre métricas locales y problemas arquitectónicos, lo que impide inferir calidad global por reducir dependencias en un consumidor.

Se consultaron dos de esos trabajos como manuscritos de autor y uno como artículo publicado. Las versiones editoriales posteriores contrastadas solamente en metadatos no se presentan como textos finales leídos. El conteo de tres no incluye por duplicado prepublicación y versión editorial ni transforma un resumen en lectura completa. Estas cautelas afectan qué se medirá y qué no podrá afirmarse del incremento.

### 5.4. Trazabilidad de decisiones D01–D09

El mapa de E4 relaciona nueve decisiones con fuentes, localizadores y estado. Su fundamentación no convierte recomendaciones concretas en contratos aprobados ni principios validados. La tabla siguiente integra sus consecuencias vigentes; D01–D09 se conservan como identificadores documentales. Las decisiones institucionales de fechas se apoyan en declaraciones y documentos del dominio, no se atribuyen a autores de arquitectura.

| ID | Orientación fundamentada | Estado o límite |
|:--|:--|:--|
| D01 | Seleccionar por necesidad de cambio y riesgo, no por limpieza de carpetas; Feathers y Bass et al. | Alcance incremental aceptado; formalización detallada pendiente. |
| D02 | Separar por motivos de cambio y conexiones; Bass et al. y Feathers. | Objetivo de separación, no reparto completo aprobado. |
| D03 | Caracterizar y comprobar consumidores; Feathers. | Protección acordada; conexión integral pendiente. |
| D04 | Controlar contexto y observar resultados y efectos; Bass et al. y Feathers. | Semántica documental y rechazo acordados; instrumento temporal pendiente. |
| D05 | Reutilizar variación existente y separar costos; Bass et al. | Reutilización administrativa aceptada; capacidad extraordinaria no acreditada. |
| D06 | Separar extracción conservadora y cambio funcional; Fowler y Feathers. | Distinción registrada; no implica implementación prospectiva completa. |
| D07 | Revisar consumidores y dependencias desplazadas; Bass et al. y Noei et al. | Sin migración total; no inferir mejora global de reducción local. |
| D08 | Evaluar escenarios, esfuerzo y efectividad; Bass et al., AlOmar et al. y Zakeri-Nasrabadi y Parsa. | Indicadores y criterios completos pendientes. |
| D09 | Versionar decisiones, hallazgos y rediseño; Bass et al. y Venable et al. | Ciclos previstos, no acreditados por el mapa. |

La prueba de eliminación de E4 es concreta: sin Feathers se pierde el fundamento de caracterización y conexión; sin Fowler, la distinción estructural y funcional; sin Bass et al., escenarios, costos y control/observación. Sin los estudios recientes reaparece la inferencia indebida de mejora desde recuentos, y sin la distinción formativa/sumativa puede confundirse revisión interna con juicio final. La explicación propia del tesista vinculó separación con localizar, modificar o extender y probar una regla. Ese cierre conceptual permitió cerrar fundamentación el 28 de octubre, no validación del método.

## 6. Estado del arte y adaptación propuesta

### 6.1. Alcance de la revisión

La pregunta de revisión examina procedimientos, métodos o herramientas para seleccionar, ejecutar y verificar incrementos en aplicaciones existentes y su evidencia de modificabilidad y testabilidad. Se priorizó el intervalo 28 de octubre de 2021–28 de octubre de 2026, con antecedentes fundacionales necesarios. El registro de búsqueda documenta cuatro consultas adaptadas por relevancia en Crossref y 21 registros examinados; no son 21 soluciones únicas. Las cadenas booleanas conservadas en E5 son propuestas base, no consultas literalmente ejecutadas con esa sintaxis.

La extracción se organizó en ocho dimensiones: delimitación del incremento; conservación y cambio funcional; decisiones y dependencias; protección y conexión; aplicabilidad; modificabilidad y testabilidad; iteración y reproducibilidad; evidencia y transferencia. La revisión es focalizada y compara antecedentes de propósitos distintos. No se ejecutaron sus herramientas ni se reprodujeron sus evaluaciones. Falta de acceso o ausencia en un pasaje leído no se convierte en prueba de que un método carezca de una capacidad.

| Antecedente | Cobertura considerada | Relación y límite |
|:--|:--|:--|
| Feathers (2004) | Cambio seguro, ruptura de dependencias, caracterización y conexión. | Comparador directo; prácticas ya existentes, no novedad local. |
| ADD, Bass et al. (2021) | Diseño por atributos, refinamiento e iteración. | Complementa razonamiento arquitectónico; no equivale a reescritura total. |
| Zakeri-Nasrabadi y Parsa (2022) | Medición y transformación para testabilidad en clases Java. | Comparador parcial; predictor y resultados no se trasladan a PHP. |
| Fischer et al. (2025) | Refactorización de modelos SysMLv2 y comprobaciones con Isabelle. | Preservación formal en modelos, no prueba del código de SIGPP. |
| Orosz y Kozsik (2026) | LADY, generación C# y comprobaciones en un caso industrial. | Supuestos y transformación distintos; revisión de propietarios no equivale automáticamente a independencia. |
| Fowler (2014) | Ramificación mediante abstracción y transición gradual. | Técnica conocida de coexistencia y migración; no obliga a sustituir el ORM. |
| Girjoaba y Capiluppi (2024) | Ciclo industrial de investigación, migración, retirada e integración con comprobaciones. | Base operativa aceptada; límites de caso y aprendizaje preservados. |

El manuscrito del ciclo fue aportado después de un intento de acceso bloqueado. Contiene una plantilla y DOI provisionales, mientras los metadatos finales IEEE están verificados en el registro bibliográfico. Se utiliza el contenido leído y se conserva pendiente la equivalencia editorial íntegra, no la disponibilidad temática. La selección de esta base no demuestra superioridad de la adaptación.

### 6.2. Ciclo heredado y decisiones de adaptación

El 28 de octubre el tesista aceptó el ciclo de Girjoaba y Capiluppi (2024) como base operativa, complementado con Feathers y ADD. En el manuscrito se describen investigación de la interfaz, migración sin retirada inicial, prueba de comportamiento, retirada y ajuste de dependencias, prueba de dependencias, integración y prueba de integración. El caso involucra seis interfaces C++ de un ejecutor y reconoce límites de aprendizaje y transferencia. Sus tiempos y resultados estadísticos no se convierten en metas ni efectos causales demostrados para SIGPP.

En SIGPP la unidad candidata no es necesariamente una interfaz obsoleta que desaparece, sino una decisión dentro de un flujo que sigue operando. La correspondencia requiere concretar qué se observa, qué se preserva y qué conexión se comprueba. Copiar mecánicamente siete fases no fija esas decisiones, pero tampoco demuestra que el ciclo original sea incapaz de tratarlas. Las adaptaciones siguientes son candidatas para formalización y evaluación, no principios originales ya validados.

| ID | Adaptación candidata | Producto previsto |
|:--|:--|:--|
| A01 | Delimitar por decisión funcional y consumidores. | Identificar entradas, consumidores y efectos del incremento. |
| A02 | Distinguir observado, requerido e intención. | Registrar qué se preserva, corrige o extiende y en qué punto se observa. |
| A03 | Precisar comprobaciones y efectos prohibidos. | Vincular regla, consumidor, punto de control y efectos observados. |
| A04 | Separar costo inicial y evolución posterior. | Especificar un cambio representativo y observar trabajo, conexiones y resultado. |

La selección proporcional fue defendida por el tesista al contrastar una errata de presentación con una regla distribuida. Una errata confirmada como texto no fuerza extracción arquitectónica; una decisión de negocio requiere investigar comportamiento, dependencias y riesgo antes de elegir intervención. «Nuevo servicio» es una opción, no una salida obligatoria ni motivo para reunir saldo, permisos y fechas indiscriminadamente. Esa explicación permitió cerrar E5 como revisión focalizada, sin anticipar la contribución empírica.

## 7. Diagnóstico del caso y evidencia disponible

### 7.1. Cronología y referencias técnicas

La extracción inicial hacia servicios contiene antecedentes de marzo de 2025, anteriores al encuadre de septiembre de 2026. Los commits `815ce6c0` y `9d4af430` no se presentan como construcción realizada durante la investigación. La extracción posterior de selección de restricciones está registrada en `8dc63307`, con `5313c0e1` como padre; documentación y pruebas posteriores aparecen en otras revisiones. La referencia más reciente consignada en el estado es `feature/propuesta-tesis`, `7c0bca08`, sin nueva batería acreditada para preparar esta consolidación.

Las ramas actuales no difieren solamente por la intervención de tesis: `master` contiene correcciones productivas adicionales. Por ello se seleccionó retrospectivamente el padre y el commit de extracción para una comparación acotada, no las ramas completas como experimento controlado. El nombre de una rama o «v2.0» no identifica por sí solo una versión reproducible. La equivalencia con producción se mantiene como declaración del tesista cuando no se inspeccionó el despliegue.

Los recuentos iniciales de once archivos y aproximadamente 4177 líneas constituyen contexto histórico, no diagnóstico actual de todas las propiedades. Instanciaciones directas, SQL o métodos privados no equivalen automáticamente a defectos. Asimismo, la afirmación inicial de ausencia de prueba directa de `CreateCertificacionService` fue superada por la revisión del 18 de octubre. No se utiliza ese vacío antiguo como justificación vigente de un requisito ya satisfecho parcialmente.

### 7.2. Selección de restricciones: cambio y comprobación retrospectiva

La selección busca una restricción activa por subpartida, gestión, administración y actividad; en ausencia de específica, busca una general y, si no existe, retorna ausencia. No está asociada a una subpartida fija. El controlador y el servicio pasaron de implementar la secuencia a delegarla en `RestriccionSubPartidaResolver`. El resolvedor conserva dos repositorios; por ello no es una política pura independiente de persistencia.

La comparación de producción registra controlador +6/−31, servicio +5/−32 y resolvedor nuevo +46/−0: 57 líneas añadidas y 63 eliminadas, con cinco archivos de prueba o auxiliar añadidos. La reducción neta de seis líneas no mide modificabilidad. Los consumidores reducen localmente colaboradores de siete a seis, pero el resolvedor incorpora los repositorios desplazados. Estos datos describen estructura y extensión del cambio, no reducción global de acoplamiento.

El 29 de octubre se documentó un instrumento común de trece casos: selecciones específica/general/ausente en dos consumidores, propagaciones de excepciones y limpieza de estado previo del servicio. Las dos clases consumidoras históricas se recuperaron de Git y cargaron en memoria antes de PHPUnit, utilizando el entorno y los dobles actuales. Se verificó correspondencia de cuatro archivos del contenedor con `HEAD` mediante SHA-256. No se reconstruyeron dependencias, configuración o datos de toda la aplicación histórica.

| Estado examinado | Resultado registrado | Alcance |
|:--|:--|:--|
| Consumidores `5313c0e1`, cargados en entorno actual | 13 pruebas, 65 aserciones; OK. | Expectativas del instrumento retrospectivo. |
| Consumidores posteriores, selección correspondiente a `8dc63307` | 13 pruebas, 65 aserciones; OK. | Mismo conjunto, no equivalencia universal. |

Los tiempos registrados en una ejecución por estado, 0,104 y 0,109 segundos, no se comparan como rendimiento: incluyen preparación distinta y no constituyen ensayo repetido. La reflexión sobre métodos privados y propiedad del servicio es protección transitoria, no prueba pública de extremo a extremo. La evidencia sostiene conservación de los casos examinados y centralización local. No acredita TDD previo, esfuerzo menor, integración real o método completo validado.

### 7.3. Baterías registradas y límites

| Fecha y referencia | Resultado documentado | Interpretación |
|:--|:--|:--|
| 13/10, registro preliminar | 151 pruebas, 235 aserciones; satisfactorias. | Antecedente; no reconstrucción actual del estado. |
| 18/10, batería y certificación | 188/540 general; 37/305 en certificación, satisfactorias. | Subconjunto incluido en general; no sumar ni tratar como cobertura. |
| 29/10, rama de tesis `5e0fec3d` | 188 pruebas, 540 aserciones; OK, sin omisiones informadas. | Nueva ejecución registrada, no identidad automática con batería del 18. |
| 29/10, referencia distinta de `master` | 159 pruebas, 260 aserciones y una omitida. | Evolución diferente; no comparación causal con tesis. |

La prueba directa de creación invoca `create()` y comprueba resultados, validaciones e interacciones con dobles. No verifica transacciones reales, archivos o contrato HTTP completo. La secuencia prueba–implementación–refactorización no se deduce del estado final ni de un commit que contiene conjuntamente código y pruebas. La consolidación reutiliza estos registros sin volver a ejecutar SIGPP.

### 7.4. Fuente funcional y discrepancias conservadas

Se recibió un cuestionario del Planificador Nacional, fechado el 29 de octubre y revisado el 30, con autorización académica acotada e identificación pública únicamente por cargo. No se incorporan aquí el nombre de la participante ni datos de certificaciones productivas. La identificación por cargo no garantiza anonimato frente a referencias o historial anteriores. Esta consulta aporta expectativas funcionales, no prueba de cumplimiento del software ni evaluación del método.

| Grupo de respuestas | Concordancia o diferencia | Estado de interpretación |
|:--|:--|:--|
| Mismo día, día anterior y futuro | Admisión del mismo día y rechazo de anterior/futuro en ejemplos. | Concordancias acotadas, no norma universal inferida. |
| Cierre mensual | Rechazo de 31/05 al registrar 15/06 y referencia al día 8; admisión de 29/02/2028 al registrar 01/03. | Límite mensual requiere precisión; no mantener cierre anterior sin plazo como regla plenamente ratificada. |
| Gestión incompatible | Rechazo de fechas o tareas de otras gestiones en los casos consultados. | Correspondencia parcial con el alcance declarado. |
| Casos extraordinarios de agosto | Rechazo de 29/12 y admisión condicional de 30/12 y 31/12 bajo algo hipotético. | No reconciliar por mayoría ni asumir una apertura autorizada; aclaraciones posteriores precisan último día hábil. |
| Ventana vencida o de otra gestión | Rechazo declarado. | Respalda vigencia y correspondencia; no ratifica todas las combinaciones de controles. |

El tesista aclaró posteriormente, tras consulta funcional, que corresponde el **último día hábil de la gestión anterior**, excluyendo fines de semana, feriados y otros días no laborables aplicables. La jefatura comunica el plazo, habitualmente hasta el 8 de febrero, con extraordinarias dentro del trimestre; el trimestre se precisó como práctica habitual y ausencia de precedente posterior. No existe prohibición normativa ni permiso universal para agosto acreditados. La fuente de calendario y la síntesis completa requieren ratificación; se preservan las respuestas originales sin corregirlas para que coincidan.

La fecha documental y el instante de registro son conceptos distintos. `fecha` expresa el día del documento; `createdAt` y `updatedAt` son auditoría y no deben alterarse para simular emisión. La zona institucional declarada es `America/La_Paz`, y el servidor PHP es la autoridad operativa acordada, no el navegador. Estos acuerdos no autorizan migración de columnas o normalización histórica y no demuestran una capacidad ya implementada.

### 7.5. Comprobaciones locales de fecha y hora

El registro de fecha documental del 30 de octubre informa una prueba, una aserción y un fallo. Con tarea de entrada 2026 y fecha 14/06/2026, el instrumento observó solicitud de correlativo antes del rechazo requerido. La captura amplia de una excepción y la búsqueda del texto «fecha» en el mensaje no constituyen una excepción funcional de fecha validada. El auxiliar recarga una tarea de gestión 2025 y no se controla el reloj; el 15/06/2026 es contexto hipotético, no entrada efectiva del servicio.

El alcance defendible es el avance local hasta solicitar correlativo. No se afirma que se guardaron certificaciones, autorizaciones, seguimientos o archivos, que se completó la creación o que hubo petición HTTP reproducida. La prueba examina comportamiento requerido, no caracteriza conservadoramente una regla correcta por el hecho de existir. Las limitaciones deben resolverse antes de ampliar la conclusión o reutilizar el instrumento como integración.

La comprobación horaria informa tres pruebas, cinco aserciones y un fallo. Para el día 31/12/2026, las entradas 00:00 y 12:00 retornan una certificación en el alcance local, mientras 23:59:30 produce `Fecha en gestión incorrecta`. La diferencia concuerda con el límite anual construido a las 23:59 identificado por inspección. No hay navegador, persistencia real o apertura comprobada, y la relación de dos entradas concordantes sobre tres no es tasa del uso institucional.

El registro externo relacionó ese fallo con I03; E6 corrige la atribución porque I03 mide esfuerzo humano, no admisibilidad horaria. Las comprobaciones funcionales se relacionan con I01 y no completan el conjunto de decisiones. Los registros fueron inspeccionados, sin reproducción nueva para este documento. No se reparó código ni se presentó el fallo como evaluación de una mejora.

## 8. Indicadores y criterios prospectivos

Los indicadores derivan de comportamiento y conexión, control/observación y escenarios de cambio (Feathers, 2004; Bass et al., 2021). Su selección no convierte resultados históricos en metas previas. La tabla integra definiciones ya propuestas y acuerdos posteriores, conservando incompletos los valores que no se midieron o aprobaron. No se asignan ceros para simular ausencia de capacidades no implementadas.

| Indicador | Definición y fuente propuesta | Estado y criterio pendiente |
|:--|:--|:--|
| I01. Correspondencia de decisiones | Casos con decisión esperada / casos ejecutados del conjunto definido; conservar resultado por caso. | Evidencia local parcial; conjunto funcional completo y ratificación pendientes. No es tasa de uso institucional. |
| I02. Rechazo antes de efectos | Casos inválidos rechazados sin efectos prohibidos / casos ejecutados que requieren rechazo. | Faltan observables y suficiencia de integración. Un doble que siempre rechaza no prueba la política real. |
| I03. Esfuerzo de comprobación | Minutos humanos activos en preparación, escritura/ajuste y análisis; bitácora con intervalos, pausas y asistencia. | Procedimiento aceptado; sin línea base humana, meta o comparación causal. |
| I04. Extensión de cambio posterior | Componentes existentes modificados y nuevos; separar producción, pruebas y configuración. | Escenario de ampliación aceptado; no ejecutado. Costo inicial se registra aparte y no se presume mejora comparativa. |

### 8.1. Registro de esfuerzo: qué no constituye línea base

El primer registro asistido informa 178 segundos, equivalentes a 2,9667 minutos, y declara tiempo humano no medido. La ventana automática de herramientas tampoco equivale al tiempo interno de PHPUnit. El segundo informa 16 segundos de actividad del agente y un intervalo rotulado como revisión de la persona, pero vuelve a declarar esfuerzo humano no medido. No se transforman intervalos de reloj, espera o actividad de IA en minutos activos del tesista.

El tesista aceptó conservar esas duraciones como auxiliares y mantener I03 pendiente. No se exige trabajar sin IA o ejecutar manualmente: se exige declarar reparto de tareas y separar intervención humana, espera y automatización. Tampoco corresponde repetir el caso aprendido para simular una primera preparación independiente. Una medición futura necesita escenario, condiciones comparables y registro prospectivo antes de ejecutarse.

### 8.2. I04: ampliación de una ventana extraordinaria

El escenario aceptado el 30 de octubre amplía, mediante configuración existente, el cierre de una ventana ficticia del 1–8 de febrero de 2027 al 10 de febrero. Se mantienen inicio, gestión destinataria y otras condiciones; la intención es comprobar flexibilidad de configuración, no incorporación de reglas nuevas. El inicio incluye desde las 00:00 de su día y el cierre todo su día, con corte exclusivo al comenzar el siguiente en `America/La_Paz`. Es una especificación prospectiva, no apertura institucional autorizada ni comportamiento actual verificado.

| Instante ficticio | Ventana hasta 08/02 | Ventana hasta 10/02 |
|:--|:--|:--|
| 31/01/2027 23:59:59 | No habilitado | No habilitado |
| 01/02/2027 00:00:00 | Habilitado | Habilitado |
| 08/02/2027 23:59:59 | Habilitado | Habilitado |
| 09/02/2027 00:00:00 | No habilitado | Habilitado |
| 10/02/2027 23:59:59 | No habilitado | Habilitado |
| 11/02/2027 00:00:00 | No habilitado | No habilitado |

La tabla contiene resultados esperados aceptados, **no resultados ejecutados**. Las decisiones conciernen exclusivamente a la ventana y no dispensan fecha documental válida, permisos, saldo u otros controles. Se espera ampliar sin componentes de código de producción nuevos o modificados; el cambio de configuración y las pruebas se registran aparte. Ese recuento no demuestra ahorro neto o novedad, porque el mecanismo de períodos ya existe y la capacidad extraordinaria inicial debe construirse y costearse por separado.

**Corrección editorial posterior a la entrega:** la celda original del 10/02/2027 a las 23:59:59 para la ventana que cerraba el 08/02 decía «Habilitado» por error de consolidación. Se corrige a «No habilitado», conforme a la tabla aceptada y conservada en E6. No se modifica el criterio ni se presenta como rediseño derivado de resultados. Esta corrección del Markdown no actualiza automáticamente el PDF ya cargado en Drive.

La inspección registrada identifica colección de parámetros cargada al construir el servicio, relojes PHP internos y consultas con reloj de base de datos. Invocar solamente `create()` no ejecuta una habilitación extraordinaria todavía inexistente ni controla los seis instantes. Falta un instrumento reproducible que distinga decisión temporal y lectura efectiva de configuración actualizada. Una entrada explícita de instante o proveedor de reloj son propuestas, no mecanismo aprobado; no se cambia producción para fabricar la línea base.

## 9. Estado del diseño y aplicación del artefacto

La propuesta sigue siendo un método adaptado más su aplicación técnica. La fundamentación y base operativa no sustituyen pasos, roles, entradas, salidas, precondiciones, versiones y criterios de suficiencia de un método reproducible. Los borradores de requisitos y diseño conservan formulaciones anteriores, incluida «arquitectura limpia mínima», que la revisión posterior precisó como MVC con frontera de aplicación incremental candidata. Esta consolidación no aprueba ese destino arquitectónico ni cierra E7 por incorporar sus antecedentes.

### 9.1. Alternativas arquitectónicas documentadas

| Alternativa candidata | Beneficio | Costo o límite |
|:--|:--|:--|
| Extracciones puntuales sin contrato | Menor cambio inmediato, reutiliza lo existente. | Puede trasladar concentración a servicios sin fronteras claras. |
| MVC con frontera incremental | Compatibilidad con servicios y repositorios actuales; reglas locales verificables. | Conserva dependencias concretas y exige excepciones explícitas; recomendada para discusión, no elección completa aprobada. |
| Núcleo con puertos y adaptadores | Mayor independencia tecnológica potencial. | Más contratos, conversiones y evaluación; migración completa no justificada con la evidencia disponible. |

Las tres alternativas provienen de la revisión técnica del 18 de octubre. No se presenta una matriz formal de selección ponderada ni una autorización de implementación que no existen. El conocimiento que fundamenta la capa de servicios no prescribe automáticamente todos los componentes de SIGPP. La decisión debe responder al escenario y sus restricciones, no a preferencia por carpetas.

### 9.2. Responsabilidades candidatas y acuerdos actuales

| Responsabilidad | Papel candidato y límite |
|:--|:--|
| Controlador | HTTP, formulario y respuesta; no sustituirlo por un coordinador de todas las reglas y escrituras. |
| Preparación opcional | Contexto de pantalla si se justifica; no guarda ni concede autorización definitiva. |
| Servicio de aplicación | Coordina creación, validaciones y efectos; no procesa HTTP o Twig. |
| Regla focalizada | Decide una condición pertinente al cambio; una regla calculable no necesita infraestructura por definición de su contrato. |
| Resolvedor existente | Selecciona específica/general/ausente mediante repositorios; no decide todos los efectos de restricción. |
| Persistencia y archivos | Consultas y mecanismos de efectos; comportamiento integral pendiente de comprobación. |
| DTO y vista | Transporte explícito y representación, sin convertir la vista en autoridad de negocio. |

Para la decisión extraordinaria se aceptó una definición única en el servidor, reutilizada por consumidores pertinentes y sin duplicar la regla en controladores o plantillas. No se exige una clase por control ni se prohíbe ayuda visual de validación. El servidor PHP es autoridad temporal operativa, pero falta decidir su control reproducible en pruebas. Son acuerdos del diseño previsto, no evidencia de implementación.

La extracción de restricciones ofrece una aplicación técnica parcial, pero no acredita que otro practicante pueda seguir el método completo. La ficha reproducible, el plan de versiones, la pregunta de diseño por versión y la suficiencia para evaluación siguen pendientes. No se certifica una arquitectura final, independencia total de Symfony/Doctrine, atomicidad o continuidad por el resultado de dobles. El código existente es insumo de aprendizaje y diagnóstico, no la contribución de conocimiento por sí mismo.

## 10. Evaluación prevista y estado de sus condiciones

La evaluación deberá demostrar utilidad contextual y aportar evidencia para los principios, distinguiendo ambas funciones. Para el método se requiere examinar aplicabilidad, productos generados y obstáculos, no solamente pruebas unitarias de su aplicación. Para reglas y consumidores se necesitan observaciones del contrato pertinente, separando pruebas con dobles de integración real. Una demostración de que el código puede ejecutarse no equivale a comparación sistemática contra criterios previos.

Se mantiene al menos una evaluación formativa que produzca hallazgos y rediseño documentado y una evaluación sumativa posterior. No se acredita ese ciclo completo mediante las extracciones antiguas o el estado final de pruebas. Faltan selección de participantes, instrumentos definitivos, condiciones comparables y suficiencia de evidencia. La valoración funcional recibida se conserva como diagnóstico, no como juicio independiente de utilidad del método.

Los requisitos y resultados esperados del siguiente incremento deberán quedar fijados antes de construir y evaluar. Las comparaciones retrospectivas seguirán identificadas como retrospectivas; no se presentarán como criterios definidos antes de la intervención. El análisis de resultados hacia principios con contexto, mecanismo y límites también está por precisar. No existe cronograma detallado aprobado con tiempos de rediseño que permita asegurar la conclusión dentro de las fechas anunciadas.

## 11. Cadena de coherencia y límites de la solución

La cadena problema–objeto–campo–objetivo–pregunta–artefacto–evaluación–criterios–evidencia–contribución se conserva sin completar eslabones con resultados supuestos. La evidencia de selección se relaciona con centralización y comportamiento examinado, no automáticamente con toda la política temporal. Las comprobaciones de fecha justifican el diagnóstico local, no éxito de una solución aún no implementada. La tabla explicita las correspondencias posibles al corte.

| Eslabón | Correspondencia vigente |
|:--|:--|
| Problema práctico | Separación parcial, duplicación localizada y decisiones temporales de distinto alcance. |
| Objeto y campo | Método más instanciación; subcircuitos MVC heredados bajo restricciones institucionales. |
| Objetivo y pregunta | Diseñar/evaluar método y determinar principios para mejorar cambio y prueba sin reescritura. |
| Artefacto | Adaptación explícita con A01–A04 y selección proporcional; formalización incompleta. |
| Evaluación y criterios | Formativa–rediseño–sumativa previstas; I01–I04 y condiciones incompletas. |
| Evidencia | Comparación retrospectiva, baterías fechadas, fuente funcional y fallos locales; sin validación integral. |
| Contribución | Principios previstos, no formulación validada ni mejora global demostrada. |

## 12. Amenazas a la validez

Las amenazas se identifican para limitar afirmaciones y orientar la evaluación pendiente, no para declararlas resueltas. El constructor conoce el caso y puede compartir supuestos con los dobles y expectativas de prueba. La comparación común reduce diferencias del instrumento en un alcance, pero no elimina sesgo ni reproduce el entorno histórico completo. Las mitigaciones previstas requieren ejecución y documentación posterior.

| Dimensión | Amenaza y efecto residual |
|:--|:--|
| Constructo | Recuentos, cantidad de pruebas o centralización pueden confundirse con modificabilidad y testabilidad. I01–I04 requieren completar operaciones y contexto; aún no miden toda la utilidad del método. |
| Interna | Correcciones productivas, aprendizaje, cambios simultáneos y comparación retrospectiva dificultan atribuir efectos. Seleccionar el incremento acotado no vuelve experimental la comparación. |
| Externa | Un caso institucional y tecnología específica limitan transferencia. Se pretende análisis de semejanzas y límites, no representatividad estadística. |
| Conclusión | Pocos escenarios y una ejecución por estado no justifican significación, eficacia universal o comparación de rendimiento. No se aplican pruebas estadísticas a tiempos de carga ni se infiere cobertura de aserciones. |

La ratificación funcional pendiente introduce incertidumbre sobre algunos resultados esperados y calendario. Los instrumentos temporales comparten limitaciones de dobles y control del tiempo que impiden extrapolar a producción. La revisión independiente y los ciclos comprometidos son mitigaciones por realizar, no garantías. Las discrepancias y ensayos fallidos se conservan para evitar selección favorable de resultados.

## 13. Conclusiones del avance y trabajo pendiente

El avance delimita un problema práctico con duplicación observada, separación parcial y diferencias locales de validación; no cuantifica todavía costo institucional o mejora de esfuerzo. La fundamentación conecta decisiones con cambio seguro, escenarios de calidad y límites empíricos, y la revisión focalizada permitió adoptar una base operativa explícita sin reclamar sus pasos como propios. Esos productos justifican formalizar y evaluar la adaptación, no declarar superioridad. El cierre de E4 y E5 no equivale a método construido o conocimiento validado.

La extracción de selección y su comparación retrospectiva muestran centralización y conservación de las expectativas examinadas en el entorno declarado. La consulta funcional y las comprobaciones temporales ampliaron el diagnóstico y precisaron límites, pero no completan I01–I04 ni integración. Los tiempos asistidos no constituyen línea base humana. La evidencia no sostiene todavía reducción de esfuerzo, mantenibilidad global, hipótesis contrastada o principios validados.

Permanece pendiente completar diagnóstico y criterios, formalizar alternativas y método, documentar aplicación y versiones, ejecutar evaluación con rediseño y evaluación final y derivar principios proporcionados a la evidencia. Esta consolidación no ejecuta esas actividades ni modifica el alcance para cumplir un plazo de presentación. La entrega del trabajo original DSR en PDF se hará como conversión externa de este avance Markdown y no como sustitución por el IFI ALSIE. El requisito docente de documento final y la condición provisional actual continúan siendo distintos.

## 14. Referencias

Se reutilizan las verificaciones y lecturas registradas en E4/E5 y en `referencias.md`; no se realizó búsqueda bibliográfica nueva para consolidar. «Verificada» identifica el alcance consignado, no lectura completa de toda obra ni comprobación jurídica externa. Las fuentes metodológicas mantienen la verificación del libro base sin atribuir nuevas lecturas primarias. La consulta funcional se describe por cargo y registro local; no se expone identificación personal.

AlOmar, E. A., Wang, T., Raut, V., Mkaouer, M. W., Newman, C., & Ouni, A. (2021). *Refactoring for reuse: An empirical study* [Prepublicación, versión 1]. arXiv. https://doi.org/10.48550/arXiv.2111.07002

**Verificada:** manuscrito y lectura focalizada; versión editorial final no comparada íntegramente.

Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/

**Verificada:** catálogo y pasajes primarios focalizados; publicación 2021 y copyright 2022 diferenciados.

Caja Petrolera de Salud. (2007). *Reglamento específico del Sistema de Presupuesto de la C.P.S.*

**Verificada localmente:** expediente aportado con R.D. 023/06 fechada 25 de enero de 2007; número y fecha conservados. Vigencia actual y modificaciones **[por verificar]**.

Caja Petrolera de Salud. (2019). *Reglamento específico del Sistema de Programación de Operaciones de la CPS* (Versión 1).

**Verificada localmente:** reglamento y R.H.D. 003/19 de 11 de marzo de 2019; vigencia íntegra actual y modificaciones **[por verificar]**.

Caja Petrolera de Salud. (2026). *Directrices para la formulación del Plan Operativo Anual y anteproyecto de presupuesto institucional gestión 2027*.

**Verificada localmente:** ejemplar aportado y pasajes contrastados; autenticidad y vigencia externas **[por verificar]**.

Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055

**Verificada:** publicación y pasajes primarios; primera impresión 2004, copyright 2005; sin lectura íntegra atribuida.

Fischer, L., Kausch, H., Rumpe, B., Stachon, M., Stüber, S., & Wollenhaupt, L. (2025). Methodical and formally verified model-driven architecture refactoring. *Journal of Object Technology, 24*(2), 2:1–2:14. https://doi.org/10.5381/jot.2025.24.2.a13

**Verificada:** texto editorial y metadatos; lectura focalizada, sin ejecución formal de la propuesta.

Fowler, M. (2014, 7 de enero). *Branch by abstraction*. https://martinfowler.com/bliki/BranchByAbstraction.html

**Verificada:** nota primaria de práctica, no estudio controlado.

Fowler, M. (2018). *Refactoring: Improving the design of existing code* (2nd ed.). Addison-Wesley Professional. https://martinfowler.com/books/refactoring.html

**Verificada:** publicación y pasajes del ejemplar local; copyright 2019 diferenciado de publicación.

Fowler, M. (2023, 11 de diciembre). *Test driven development*. https://martinfowler.com/bliki/TestDrivenDevelopment.html

**Verificada:** página primaria y revisión utilizada; no estudio empírico.

Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079

**Verificada:** metadatos finales y contenido del manuscrito aportado; equivalencia editorial íntegra **[por verificar]**. No se utiliza el DOI provisional del adjunto.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. *MIS Quarterly, 37*(2), 337–355. https://doi.org/10.25300/MISQ/2013/37.2.01

**Verificada en el libro base:** sin nueva lectura primaria acreditada en la consolidación.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105. https://doi.org/10.2307/25148625

**Verificada en el libro base:** sin nueva lectura primaria acreditada.

Noei, S., Li, H., & Zou, Y. (2025). An empirical study on release-wise refactoring patterns. *Proceedings of the ACM on Software Engineering, 2*(FSE), Article FSE019. https://doi.org/10.1145/3715734

**Verificada:** PDF publicado y lectura focalizada; se conservan autores y artículo del PDF frente a discrepancias catalográficas.

Orosz, B. D., & Kozsik, T. (2026). Case study: Refactoring with design and architectural patterns. *Annales Mathematicae et Informaticae, 63*, 107–121. https://doi.org/10.33039/ami.2026.07.003

**Verificada:** PDF publicado y metadatos; sin reproducción del artefacto.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302

**Verificada en el libro base:** referencia no implica adopción definitiva de DSRM.

Stafford, R. (2003, 5 de marzo). *Service layer*. Martin Fowler. https://martinfowler.com/eaaCatalog/serviceLayer.html

**Verificada:** página primaria; Stafford es el autor, no se atribuye la obra a Fowler por su alojamiento.

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36

**Verificada en el libro base:** aplicación conceptual; no lectura primaria nueva ni mínimo universal de maestría atribuido al artículo.

Wieringa, R. J. (2014). *Design science methodology for information systems and software engineering*. Springer. https://doi.org/10.1007/978-3-662-43839-8

**Verificada en el libro base:** proceso concreto del estudio aún por justificar.

Zakeri-Nasrabadi, M., & Parsa, S. (2022). *An ensemble meta-estimator to predict source code testability* [Prepublicación, versión 2]. arXiv. https://doi.org/10.48550/arXiv.2208.09614

**Verificada:** versión 2 y lectura focalizada; no se presume identidad íntegra con la versión editorial posterior ni validación del predictor en PHP.

## Anexo A. Procedencia y reglas de consolidación

Este documento organiza el avance en una lectura continua; no concatena indiscriminadamente borradores ni convierte historial en estado actual. Las fuentes originales permanecen en el repositorio con sus fechas y contradicciones históricas explícitas. Las referencias siguientes permiten revisar el respaldo de cada sección sin abrir el IFI ALSIE como fuente del trabajo DSR. No se adjuntan documentos personales o datos productivos.

| Fuente en `tesis_ds/` | Contenido utilizado |
|:--|:--|
| `00_estado.md` | Etapas vigentes, decisiones aceptadas y límites. |
| `02_delimitacion.md` y `03_perfil_ds.md` | Alcance, objeto, campo, pregunta, seis objetivos y contribución prevista; se prioriza el perfil actualizado. |
| `04_marco_teorico.md` y `mapa_fundamentacion_e4_2026-10-28.md` | Fundamentos, nueve decisiones y cierre E4; no se reproduce como actual la antigua ausencia de prueba directa. |
| `05_estado_del_arte.md` | Revisión focalizada, siete antecedentes, ciclo aceptado, A01–A04 y cierre E5. |
| `referencias.md` | Referencias APA 7, versiones y alcance de verificación. |
| `06_diagnostico.md` | I01–I04, aclaraciones funcionales, pruebas locales y distinción de esfuerzo humano. |
| `comparacion_extraccion_restriccion_2026-10-29.md`, sección 6 | Instrumento común, carga histórica, trece casos y límites retrospectivos. |
| `07e_construccion_verificacion.md`, actualización del 18/10 | Prueba directa existente, baterías y cronología de antecedentes de 2025. |
| `arquitectura_candidata_certificacion_2026-10-18.md` | Alternativas, preparación opcional y responsabilidades candidatas, no diseño aprobado. |
| `07b_requisitos.md` y `07c_diseno_artefacto.md` | Antecedentes preliminares; no se adoptan como vigentes sus afirmaciones superadas de ausencia de prueba o arquitectura cerrada. |
| `matriz_coherencia.md` | Cadena de coherencia; referencias históricas a intervención formativa se limitan por los registros posteriores. |

Las reglas de fecha se actualizan por la aclaración de último día hábil, sin reproducir 29/31 fijos como contrato vigente. El cuestionario se sintetiza por cargo, sin alterar el original ni inferir ratificación completa. Los resultados retrospectivos siguen siendo retrospectivos y las baterías conservan fecha, rama y alcance. La mera preparación de este documento no produce un cierre E6–E10.

## Anexo B. Material técnico identificable y reproducibilidad parcial

Los archivos técnicos se encuentran en el repositorio separado SIGPP y no se incorporan como código completo en este documento. Los nombres permiten localizar unidades de evidencia, pero no constituyen por sí solos un paquete reproducible. Se conservan los identificadores de comparación y se reconoce que entorno, dependencias y datos requieren instrucciones completas antes de afirmar reproducción independiente. No se da acceso implícito a producción mediante la publicación de este texto.

| Material | Papel en la evidencia |
|:--|:--|
| `RestriccionSubPartidaResolver.php` | Selección específica, general y ausencia con repositorios. |
| `RestrictionSelectionFixture.php` | Datos ficticios y dobles compartidos del instrumento. |
| `RestrictionSelectionCharacterizationTest.php` | Trece casos del instrumento retrospectivo común. |
| `RestriccionSubPartidaResolverTest.php` | Comprobación directa del resolvedor. |
| `ConsumerResolverDelegationTest.php` | Delegación desde consumidores. |
| `CreateCertificacionServiceTest.php` | Creación con dobles y comprobaciones temporales locales posteriores. |
| `docs/development/fecha-documental-tesis-evidencia.md` | Registro del primer fallo y tiempos asistidos no humanos. |
| `docs/development/fecha-hora-i03-evidencia.md` | Registro horario; atribución a I03 corregida en el diagnóstico. |

La ficha de comparación conserva el procedimiento de carga histórica y comprobación de correspondencia de archivos. La revisión funcional, los datos ficticios completos, las versiones del método y la verificación de integración no están íntegramente reunidos en una ficha reproducible. Esa limitación impide declarar E7f cerrada. Este anexo identifica lo existente sin prometer un artefacto completo que aún no fue formalizado.

## Anexo C. Estado de los compromisos al entregar

| Compromiso | Situación |
|:--|:--|
| Evidencia contextual distinta de literatura | Existe inspección, historial, pruebas y fuente funcional recibida; ratificación e indicadores completos pendientes. |
| Criterios previos al siguiente cambio | Acuerdos parciales, incluido escenario I04; no protocolo completo cerrado. |
| Formalización del método | Base y adaptaciones candidatas, sin ficha completa ni suficiencia aprobada. |
| Evaluación formativa con rediseño | Comprometida; antecedentes no acreditan por sí solos un ciclo completo. |
| Evaluación sumativa | Pendiente. |
| Contribución de conocimiento | Prevista; principios y condiciones respaldadas pendientes. |
| Presentación institucional | Documento ALSIE separado y provisional; este trabajo original no lo sustituye. |

**Cierre de la consolidación:** avance original DSR reunido en Markdown, con evidencia y pendientes explícitos. No se generó PDF, no se cargó a Google Drive ni se realizó investigación adicional por esta consolidación.
