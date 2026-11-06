# Evaluación posterior de M-R1: acuerdos de preparación

**Fecha de apertura:** 6 de noviembre de 2026. **Estado vigente:** P02 realizó la aplicación y el tesista aceptó su dictamen acotado; véase `revision_aplicacion_p02_2026-11-06.md`, sección 7. Este archivo conserva los acuerdos y estados sucesivos de preparación, incluidos pendientes después resueltos o condiciones modificadas durante la actividad. No debe utilizarse para afirmar que la sesión sigue sin iniciarse ni para cerrar E8 globalmente.

## Registro histórico de preparación operativa

**Materiales operativos creados, 6 de noviembre de 2026:** por solicitud del tesista se crean en `docs/` de SIGPP `evaluacion-metodo-p02.md`, `observacion-metodo-p02.md` y `comprobaciones-p7i-p02.md`. La guía contiene contexto sin solución histórica y material operativo P1–P8 de M-R1; el registro diferencia ayudas, productos y dictamen; la guía técnica contiene comandos generales y define los casos y recorridos que deben concretarse. Los documentos no contienen consentimiento recibido ni resultados simulados. La sintaxis del bloque PHP de comprobación de conexión se revisa con PHP 7.4.29 mediante `php -l`, sin ejecutar ese bloque ni acceder a la base. Se comprueba disponibilidad de las clases de comandos de inspección/validación en las dependencias instaladas, no su ejecución funcional.

La guía P7-I no implementa las pruebas específicas ni la refactorización del participante. Antes de transformar deben materializarse conjunto ficticio, recuperación y observables de ambos consumidores y registrarse línea inicial. Esta preparación documental no permite declarar listo el episodio ni P7-I satisfecho. Los tres archivos quedan nuevos y sin commit en `eval/metodo-mr1-p02`; no se modificó código funcional o datos ni se inició la aplicación.

El 6 de noviembre de 2026, el tesista autoriza expresamente usar la base de datos ya configurada para la actividad y crear la rama en la copia habitual de SIGPP. Indica que los datos institucionales podrán ocultarse en el informe y que se requieren las métricas. Esta decisión sustituye, para este episodio, la propuesta anterior de exigir otra base o anonimización completa; no acredita anonimización de los originales, conexión efectiva comprobada ni actividad realizada.

Se crea `/home/mario/dev/sf_projects/sipoa4`, rama `eval/metodo-mr1-p02`, desde `master` en `8256bb8cfcd72730572fbe7750765d0941490861`. Git informa la nueva rama sin cambios locales tras su creación. Es separación por rama en la carpeta habitual, no una copia ni una base aisladas; ese límite se declarará. No se inició el episodio ni se alteró código o datos, y no se creó respaldo ni se ejecutaron pruebas.

Las métricas y los resultados técnicos se conservarán sin alterarlos para favorecer conclusiones. La ocultación de información institucional se aplicará a las copias destinadas al informe y a evidencia pública, no se describirá retrospectivamente la base original como ficticia. No se enviarán registros institucionales ni credenciales a asistentes de IA. El conjunto ficticio identificable acordado para las comprobaciones sigue previsto dentro de la base configurada; su preparación, alcance de escrituras y recuperación deberán quedar definidos antes de ejecutarlo.

La exigencia de comprobar el destino efectivo de la conexión y de registrar los comandos, condiciones y resultados se mantiene: la autorización de uso no prueba que la aplicación se conecte al destino esperado. La propuesta de respaldo completo no se ejecutará por el solo permiso de crear la rama. Siguen pendientes materiales del participante, instrumentos ejecutables, mecanismos de recuperación del ensayo y plan de análisis; la aplicación continúa bloqueada hasta completar el protocolo.

## Decisión y justificación

El tesista acepta que el compañero con experiencia en SIPOA3 aplique M-R1 sobre la misma tarea de selección de restricciones de subpartida utilizada en P01, en una copia inicial aislada de SIGPP, sin la solución ni los resultados de P01. La aceptación corresponde a la propuesta explícita de utilizar esa tarea para evaluar la versión rediseñada. No se exige replicar la estructura, los nombres ni la implementación histórica: el participante debe justificar la intervención mínima y comprobar la conservación del comportamiento.

Mantener la tarea permite examinar las instrucciones rediseñadas sobre un caso conocido, sin añadir funcionalidad ni reescribir SIGPP. Otro participante reduce la repetición individual de la tarea, pero introduce diferencias de experiencia y familiaridad contextual. Por ello no se atribuirán causalmente las diferencias respecto de P01 al rediseño ni se presentará este episodio como transferencia a otro sistema.

## Participante previsto

El tesista declara que el compañero conoce PHP, Symfony y PHPUnit, no ha visto el código, las pruebas o los resultados de P01 y está disponible antes del 10 de noviembre. Solo le había comunicado que está realizando la tesis y consultado su posible colaboración. Estos datos son declaraciones del tesista, no comprobaciones independientes ni consentimiento documentado del participante.

Antes de comenzar se registrarán consentimiento, exposición previa efectiva, materiales recibidos y familiarización con el contexto. No se solicitará que estudie anticipadamente la solución de P01. La experiencia en SIPOA3 no convierte a SIPOA3 en un segundo contexto de aplicación: la tarea aceptada se ejecutará sobre SIGPP.

## Artefacto y evidencia que se examinarán

La versión a aplicar es `metodo_refactorizacion_incremental_mr1.md`, aprobada después de P01. Sus cuatro ajustes se documentan en `registro_redisenio_metodo_mr1.md`. El nuevo episodio debe conservar evidencia del seguimiento del método, las decisiones, los productos y las ayudas, además del resultado técnico; repetir únicamente la batería de pruebas no evalúa M-R1.

Los materiales originales, registros y código de P01 se conservarán intactos. Su protocolo en `protocolo_aplicacion_controlada_metodo.md` es antecedente, no autorización automática de este episodio. No se utilizarán resultados históricos como resultados del nuevo participante ni se reconstruirán tiempos de esfuerzo inexistentes.

## Condiciones pendientes antes del inicio

**Alcance P7-I aceptado, 6 de noviembre de 2026:** el tesista acepta comprobar configuración e inyección de dependencias, selección mediante repositorio y persistencia reales con datos ficticios identificables y conexión de ambos consumidores con la decisión refactorizada. Acepta fijar conservación y recuperación del estado inicial antes de cambiar datos, sin información institucional en consultas a IA o evidencia. No exige recorrer todo el proceso de certificación. Esta aceptación fija el alcance; no acredita ejecución ni autoriza aún sustituir sin medidas de protección la copia aislada por la carpeta habitual.

**Aclaración de datos del tesista, 6 de noviembre de 2026:** declara que la base local es de desarrollo y que los datos institucionales no tendrían que salir en la prueba. Se registra como expectativa de uso local, no como evidencia de anonimización ni comprobación de ausencia de datos reales. No se inspeccionaron registros de la base. Para concretar P7-I se propone un conjunto ficticio identificable y exclusivo para la actividad, sin publicar datos institucionales ni introducirlos en consultas a IA, capturas o registros de evidencia. La selección de registros, preservación de datos ajenos al ensayo y recuperación del estado inicial deberán fijarse antes de modificar la base. No hay modificaciones autorizadas por este registro documental.

**Ruta corregida y verificación inicial, 6 de noviembre de 2026:** el tesista confirma `/home/mario/dev/sf_projects/sipoa4`. Git muestra `master` en `8256bb8cfcd72730572fbe7750765d0941490861`, sin cambios locales informados, una referencia distinta de la base histórica de P01. El servicio de creación examinado conserva selección directa mediante el repositorio; el listado de `src/Service/Certificacion` no contiene el selector extraído. Esta inspección es acotada, no certificación exhaustiva de ausencia de toda solución o material revelador.

Docker informa activos los contenedores de aplicación, servidor web y PostgreSQL. La inspección de montajes confirma que aplicación y servidor web usan esta carpeta y que PostgreSQL conserva datos en el volumen `sipoa4_sigpp-pgsql-data`. Por tanto, una rama en esa carpeta compartiría el entorno y los datos locales habituales: no proporciona por sí sola el aislamiento de datos acordado. No se verificó aún el destino efectivo de la conexión de Symfony, la naturaleza ficticia o anonimizada de los datos ni un recorrido de integración.

Existe `AGENTS.md` versionado con instrucciones generales de herramientas y estilo; no equivale por sí mismo a memoria de P01, pero impide afirmar ausencia de todo material para agentes. No se auditó la memoria externa de los asistentes ni los archivos ignorados. Se requiere sesión nueva del asistente y control de materiales si se usa IA. No se cambiaron ramas, código, contenedores ni datos y no se ejecutaron pruebas.

**Entorno propuesto por el tesista, 6 de noviembre de 2026:** utilizar una rama dentro de la copia habitual indicada como `/home/mario/dev/sf_projects/sipoa`, con base de datos local y contenedor Docker. Declara que `master` no contiene las soluciones ni memoria de agentes de IA, que la base está actualizada y que permite cambiar datos en desarrollo local. Estas condiciones aún no se verificaron; no acreditan aislamiento, ausencia de exposición o integración ejecutada. La lectura de la ruta indicada devuelve «File not found» y sugiere, entre otras, `/home/mario/dev/sf_projects/sipoa4`. Se requiere aclarar la ruta antes de inspeccionar o preparar el entorno. No se cambiaron ramas, contenedores ni datos; no se sustituye aún la copia aislada acordada por esta propuesta.

Las dimensiones y reglas de dictamen de la sección siguiente están aceptadas. Falta concretar las comprobaciones de integración exigibles y sus observables, la familiarización, la referencia y el entorno iniciales y el plan de análisis. La política ya aceptada de documentación e IA con uso registrado se conserva como antecedente; el material operativo deberá explicitarla, sin presentar trabajo asistido como desempeño autónomo. No hay copia nueva preparada ni ejecución autorizada por esta aceptación.

Los criterios se fijarán antes de aplicar M-R1, sin atribuirles anterioridad a la construcción o a P01. El episodio no mide automáticamente I01–I04 ni demuestra ahorro, modificabilidad posterior o suficiencia de la contribución. E8 permanece abierta.

## Modalidad de observación aceptada

El 6 de noviembre de 2026, el tesista acepta estar presente como observador mientras el participante realiza la actividad en la máquina prestada, sobre una copia aislada. La justificación es recoger dificultades, consultas y ayudas durante la aplicación, sin depender exclusivamente del recuerdo posterior. Esta modalidad difiere del autorregistro de P01; cualquier comparación deberá declarar esa diferencia y no atribuir los cambios observados únicamente a M-R1.

Antes de comenzar, el tesista explicará el contexto y el entorno sin mostrar la solución ni sugerir la estructura del código. Durante la tarea anotará paso, dificultad, consulta, ayuda y consecuencia; no anticipará errores, dictará decisiones ni tomará el teclado para resolver. Podrá atender problemas operativos y proporcionar aclaraciones solicitadas del método, dejando registro de su contenido y efecto. No se ocultarán las intervenciones ni se mantendrá al participante bloqueado para aparentar autonomía.

Al terminar, el participante explicará sus decisiones y revisará el resumen de observaciones; se conservarán sus correcciones y las discrepancias con el dictamen del revisor. Documentación e IA siguen permitidas con registro de uso. La presencia del autor introduce riesgo de orientación y de respuestas favorables por su presencia: se declarará aplicación por un practicante externo observada por el autor, no observación independiente ni desempeño autónomo sin asistencia. No se ha acordado grabación obligatoria.

## Dimensiones y reglas de dictamen aceptadas

El 6 de noviembre de 2026, antes de la aplicación posterior, el tesista acepta las siguientes dimensiones y reglas como base del dictamen. Son criterios del nuevo episodio; no se presentan como definidos antes de construir el método o de realizar P01. Las comprobaciones concretas de integración siguen pendientes y deberán fijarse antes de comenzar.

| Dimensión | Evidencia exigida | Trazabilidad a requisitos existentes |
|:--|:--|:--|
| Aplicación del método | Cada paso tiene producto verificable y explicación del participante, o no aplicación justificada. Se distingue realización sin aclaraciones de realización con ayuda. | R1–R4, R8 y R10; condiciones de salida P1–P8 de M-R1. |
| Ajustes P3 y P5 | Identificación de dependencias pertinentes y comprobación de resultados normales, ausencia y fallos aplicables, sin inventar condiciones para completar el formulario. | R5; ajustes de M-R1 en P3 y P5. |
| Verificación P7 | Registro separado de comprobación local e integración. Solo se declara cumplimiento integral cuando ambas cuentan con la evidencia previamente exigida. | R8 y R10; condición de salida de P7 y distinción P7-L/P7-I de M-R1. |
| Trazabilidad P8 | Conservación de decisiones, cambios, ayudas y limitaciones; declaración «no medido» cuando corresponda, sin afirmar ahorro no medido. | R10; P8 de M-R1. No sustituye las mediciones exigidas por R7, R9 o R14. |

La conservación técnica seguirá examinándose mediante C01–C05: selección específica, alternativa general, ausencia, propagación de excepciones y limpieza del estado anterior, en los consumidores donde correspondan. Estos criterios no sustituyen la evaluación del método. Si las pruebas son satisfactorias, pero el tesista resolvió las decisiones centrales, no se concluirá que el participante pudo aplicar el método sin esa intervención.

Reconocer y documentar una integración pendiente satisface la exigencia de registro de esa limitación, pero no demuestra integración completada. Los resultados se presentarán por dimensión y con sus ayudas y límites; esta aceptación no establece puntuación agregada ni permite compensar una verificación faltante con más pruebas locales. Tampoco elimina requisitos o indicadores previos pendientes ni acredita por sí sola suficiencia científica de la tesis.

## Preparación técnica de P7-I: alcance aceptado y observables por concretar

La inspección estática de `master` local identifica dos consumidores: `CreateCertificacionController::new()` obtiene la restricción para preparar el formulario; `CreateCertificacionService::create()` la obtiene antes de construir la certificación y determinar efectos posteriores. Ambos contienen selección específica seguida de alternativa general mediante `RestriccionSubPartidaRepository`. La tarea no obliga a una estructura o nombre de componente, pero las comprobaciones deberán alcanzar ambos consumidores, no únicamente el destino de la extracción.

| Comprobación aceptada | Evidencia exigida dentro de ese alcance | Límite del dictamen |
|:--|:--|:--|
| Configuración | Construcción del contenedor Symfony y resolución de las dependencias de los componentes intervenidos; comandos, entorno y resultados conservados. | Un proceso de Docker activo o sintaxis correcta no sustituye esta comprobación. |
| Persistencia y selección | Casos específico, general y ausente sobre datos ficticios identificables, mediante el repositorio real; entradas, resultado esperado y observado conservados. | No sustituir el repositorio por un doble y declarar comprobado SQL real. Se preserva C01–C05 con sus niveles de prueba pertinentes, sin forzar excepciones reales destructivas. |
| Consumidores | Evidencia de que controlador y servicio usan la decisión refactorizada en los recorridos pertinentes, con condiciones y observables definidos antes de la aplicación. | Inspección del código o prueba exclusiva del componente extraído no acreditan por sí solas estos recorridos. No se exige demostrar todo el proceso de certificación. |

El repositorio real filtra por subpartida, gestión, administración, actividad y estado activo; la alternativa general exige actividad nula. El conjunto ficticio deberá distinguir esos escenarios sin depender de coincidencias accidentales con registros institucionales. No se han seleccionado identificadores ni preparado datos, y no se han diseñado todavía los mecanismos ejecutables de prueba para ambos consumidores.

Se detecta una condición de preparación relevante en `phpunit.xml.dist`: la configuración activa usa `vendor/autoload.php`, sin fijar `APP_ENV=test`; las instrucciones que sí lo hacen están comentadas. `config/packages/doctrine.yaml` obtiene la conexión de `DATABASE_URL`. Por ello, ejecutar PHPUnit sin una configuración específica comprobada no garantiza una base separada ni el entorno de pruebas. No se leyó ni publicó el valor secreto de conexión, no se comprobó su destino efectivo ni se ejecutaron pruebas.

Antes de preparar una rama en la carpeta habitual se requiere fijar la referencia, conservar los materiales de P01 fuera del material inicial del participante y comprobar el destino local de conexión sin revelar credenciales. También deberá establecerse un respaldo local recuperable o una alternativa equivalente de aislamiento, delimitar qué datos se crearán y cómo se recuperará el estado inicial. El respaldo operativo no será evidencia pública de tesis ni contendrá material para asistentes de IA.
