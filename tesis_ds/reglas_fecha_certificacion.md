# Certificación: reglas de fecha y trazabilidad

## Fuente y alcance

> **Revisión funcional del 20 de octubre de 2026:** el tesista confirmó una habilitación extraordinaria configurable para una gestión anterior concreta, que podrá abrirse en cualquier momento del año actual. Esto sustituye la restricción fija de enero–marzo en el diseño propuesto, sin ampliar las fechas del documento: siguen siendo únicamente 29 o 31 de diciembre del año inmediatamente anterior. También confirmó que la habilitación extraordinaria basta como habilitación temporal, aunque la apertura global esté cerrada. No dispensa permisos, saldo ni validación documental. La revisión se registra después del diagnóstico y antes de su implementación; no se presenta como condición que el código ya cumpliera ni como criterio histórico de éxito.

Especificación aportada por el tesista en la sesión del 18 de octubre de 2026. Se registra como conocimiento institucional declarado, pendiente de respaldo documental o confirmación del responsable funcional; no se atribuye a una norma publicada ni se presenta como requisito nuevo. Las reglas describen el comportamiento esperado, no acreditan su cumplimiento uniforme en SIGPP. El tesista confirmó `America/La_Paz` como zona horaria institucional para determinar hoy y los cambios de día, mes, trimestre y año. También confirmó que `fecha` representa exclusivamente el día del documento y calificó la inclusión de hora como error de implementación; la hora no tiene significado institucional en ese campo.

## Condiciones comunes

### Aclaración de vocabulario: tarea, operación y día de registro

El tesista aclaró que la temporalidad pertinente corresponde a la tarea y que la entidad `Operacion` agrupa tareas. La inspección confirma `Tarea.periodoInicio`, `periodoFin`, `tareaProgramacion` y `Tarea::getGestion()` a través de `parametroSistemas`; `Operacion::getTareas()` expone la colección de tareas. Estos elementos no prueban por sí solos cómo los trimestres restringen la fecha de certificación; esa condición requiere aclaración funcional.

En esta nota, la expresión anterior «fecha de operación» y la columna «Operación» de los ejemplos significan **día en que se intenta registrar la certificación**, determinado por el servidor en `America/La_Paz`; no se refieren a una fecha de la entidad `Operacion` ni a su auditoría. En adelante se usará **día de registro de referencia** para ese dato de evaluación, distinto de `createdAt` persistido y de la programación temporal de la tarea. Las reglas de hoy y vigencia de la ventana extraordinaria requieren ese día de referencia; eliminarlo no sería simplemente corregir un nombre.

### Programación referencial y modificaciones POA

El tesista aclaró que los períodos de planificación y montos programados son referenciales para la ejecución y que la evaluación monitorea su avance. No se añade, por ello, una condición de rechazo por encontrarse fuera del trimestre programado de la tarea; se mantienen la pertenencia a su gestión y las reglas institucionales específicas de certificación ya declaradas. Esta aclaración distingue un instrumento de planificación y seguimiento de una restricción autoritativa para emitir el documento. Es conocimiento del contexto aportado por el tesista, no una comprobación normativa independiente.

También declaró que las tareas pueden perder recursos o desaparecer como consecuencia de modificaciones POA. La programación histórica no demuestra, por tanto, disponibilidad actual ni permiso de ejecución. La comprobación de saldo pertenece a la coordinación de creación y debe basarse en la situación pertinente al momento de certificar, no en montos planificados usados como si fueran saldos. Falta precisar qué significa técnicamente «desaparecer» —estado, sustitución, anulación u otro mecanismo— y qué consecuencias tiene para la elegibilidad; no se presupone un borrado físico ni se introduce una prohibición nueva sin aclaración. Tampoco se afirma que el código actual controle concurrencia o vigencia de forma suficiente.

Para crear una certificación, el usuario debe tener permiso en la unidad correspondiente, debe existir la habilitación temporal pertinente al escenario y debe existir saldo suficiente. En el escenario ordinario se utiliza la apertura global aplicable; en el extraordinario, una habilitación vigente para la gestión anterior concreta basta sin exigir apertura global. La fecha del documento debe pertenecer a la gestión de la tarea y cumplir los días admisibles del escenario. Estas condiciones deben verificarse en el servidor, con independencia de las restricciones de la pantalla. La conformidad con la regla de fechas, por sí sola, no habilita la operación.

## HU-FEC-01. Gestión actual

Para una tarea de la gestión del año de operación, se permiten la fecha de hoy y el último día del mes anterior, siempre que esta última pertenezca a la gestión de la tarea. Se rechazan otras fechas, incluidas las futuras y los días anteriores distintos del cierre mensual permitido. En enero, el 31 de diciembre anterior queda fuera de esta historia y se evalúa conforme a HU-FEC-02. Se conserva la fecha válida seleccionada.

| Operación | Gestión de tarea | Fecha solicitada | Resultado respecto de la fecha |
|:--|:--|:--|:--|
| 15/06/2026 | 2026 | 15/06/2026 | Aceptar. |
| 15/06/2026 | 2026 | 31/05/2026 | Aceptar. |
| 15/06/2026 | 2026 | 14/06/2026 | Rechazar. |
| 15/06/2026 | 2026 | 30/05/2026 | Rechazar. |
| 15/06/2026 | 2026 | 16/06/2026 | Rechazar. |

## HU-FEC-02. Gestión anterior

La formulación inicial limitaba el registro a enero, febrero y marzo. En la revisión confirmada por el tesista, se permite registrar pendientes de una tarea de la gestión inmediatamente anterior cuando exista una habilitación extraordinaria vigente para esa gestión; esa ventana podrá situarse en cualquier momento del año actual. Se admiten exclusivamente el 29 o el 31 de diciembre de la gestión anterior y se conserva la fecha válida seleccionada, sin convertir otras fechas al cierre anual. Estar en el año actual no habilita por sí solo el registro: debe cumplirse la ventana configurada y las demás condiciones aplicables. La apertura global puede estar cerrada: la extraordinaria vigente satisface el requisito temporal de este escenario.

| Operación | Gestión de tarea | Fecha solicitada | Resultado respecto de la fecha |
|:--|:--|:--|:--|
| 10/02/2026 | 2025 | 31/12/2025 | Aceptar respecto de fecha, condicionado a habilitación extraordinaria vigente y demás controles. |
| 10/02/2026 | 2025 | 29/12/2025 | Aceptar respecto de fecha, condicionado a habilitación extraordinaria vigente y demás controles. |
| 10/02/2026 | 2025 | 30/12/2025 | Rechazar. |
| 10/02/2026 | 2025 | 31/12/2024 | Rechazar. |
| 10/02/2026 | 2025 | 10/02/2026 | Rechazar: gestión incompatible. |
| 01/04/2026 | 2025 | 31/12/2025 | No rechazar solo por ser abril; depende de habilitación extraordinaria vigente y demás controles. |
| 20/08/2026 | 2025 | 29/12/2025 | Admisible con habilitación extraordinaria vigente para 2025 y demás controles. |
| 20/08/2026 | 2024 | 31/12/2024 | Rechazar: no es la gestión inmediatamente anterior. |

Las filas de aceptación son criterios prospectivos, no pruebas ejecutadas. Cuando no exista una habilitación extraordinaria vigente para la gestión pertinente, se rechazará ese registro, aunque la apertura global esté activa. El administrador establecerá inicio/fin mediante el mecanismo existente; la extensión conservará su semántica y deberá caracterizarla, sin rediseñar esos límites.

### Combinación de habilitaciones en el escenario extraordinario

La tabla supone tarea del año inmediatamente anterior y documento del 29 o 31 de diciembre de ese año; permisos, saldo y demás controles se verifican por separado. «Permitir» significa satisfacer únicamente la condición temporal de habilitación, no una autorización incondicional de creación. La habilitación extraordinaria debe corresponder a la gestión y estar vigente en el día de registro de referencia.

| Apertura global | Extraordinaria pertinente vigente | Decisión de habilitación |
|:--|:--|:--|
| Cerrada | Sí | Permitir por extraordinaria. |
| Abierta | Sí | Permitir por extraordinaria. |
| Abierta | No | Rechazar el escenario extraordinario. |
| Cerrada | No | Rechazar el escenario extraordinario. |

El razonamiento no se implementa como un `global OR extraordinaria` indistinto para cualquier certificación: primero se identifica el escenario y se verifica la habilitación correspondiente. Una excepción para la gestión anterior no habilita por sí sola la gestión actual ni una gestión histórica arbitraria. La regla es prospectiva y aún no se ha ejecutado como prueba.

## Rechazo y efectos

Un rechazo de fecha debe informar la condición incumplida y producirse antes de crear la certificación, seguimiento, autorización o almacenar adjuntos. Las pruebas deben controlar la fecha de operación para que los resultados no dependan del día de ejecución. No se puede simular la emisión alterando los campos de auditoría. Los controles de acceso, habilitación y saldo requieren verificación propia y no se trasladan a la política de fechas por el solo hecho de ser condiciones comunes.

## Significado de los campos

| Campo | Significado declarado | Evidencia estática contrastada |
|:--|:--|:--|
| `fecha` | Fecha institucional seleccionada por el usuario dentro de las reglas. | `Certificacion::setFecha()` asigna el valor; `Resources/config/doctrine/Certificacion.orm.xml`, línea 22, declara `datetime`. |
| `createdAt` | Momento real de creación, no fecha del documento. No debería cambiar por edición normal posterior. | Mapeo `datetime` con `gedmo:timestampable on="create"`, líneas 105–107. |
| `updatedAt` | Momento de última actualización; no historial completo ni garantía de actualización por cambios en entidades relacionadas. | Mapeo `datetime` con `gedmo:timestampable on="update"`, líneas 108–110. |

Se verificó la configuración del mapeo, no una persistencia real ni la activación efectiva de los mecanismos de auditoría en todos los caminos. La validación debe actuar sobre el día de `fecha`, manteniendo separados los valores de auditoría, que sí representan momentos temporales. La nota del tesista establece que consultar o imprimir no es una modificación; comprobar esa propiedad exige observar los caminos correspondientes. La discrepancia entre el significado de fecha calendario y el mapeo `datetime` está identificada, pero no autoriza todavía migrar datos históricos ni modificar su hora o zona horaria de almacenamiento.

## Contraste con la implementación inspeccionada

`CreateCertificacionService::verrificarFecha()` únicamente delega en `fechaEstaEnGestion()`, que compara la fecha con el inicio y fin de la gestión de la tarea. Este método no recibe la fecha de operación ni comprueba hoy, cierre del mes anterior o la excepción de primer trimestre. Por tanto, esta validación local es insuficiente para las reglas declaradas; todavía falta revisar otras posibles barreras del servidor antes de afirmar un defecto explotable del recorrido completo. No se ejecutó en esta sesión una petición HTTP ni una prueba que reproduzca el incumplimiento.

El límite superior actual se construye como `31 de diciembre 23:59`, incompatible con tratar todas las horas de un mismo día como irrelevantes para su admisibilidad. Conforme a la aclaración del tesista, la validación futura debe comparar fechas calendario y no depender de minutos o segundos. La regla institucional documentada no debe sustituir retroactivamente las pruebas que caracterizan el comportamiento existente: primero se separa estructura conservando comportamiento y luego se corrige el incumplimiento con pruebas de aceptación distintas. Aunque la necesidad institucional sea antigua, exigir condiciones que el código no aplicaba constituye un cambio funcional observable.

## Diseño candidato y decisiones abiertas

### Alternativa planteada: reutilizar parámetros del sistema

El tesista propuso aprovechar el mecanismo existente de parámetros que abre y cierra posibilidades de uso del sistema. Se inspeccionaron `ParametroSistemaService`, `ParametroSistema`, `AmpliacionParametroSistema` y `CertificacionParametroFactory`: existen gestión, estado, fechas de inicio/fin y ampliaciones; el servicio consulta períodos normales y ampliaciones, y la fábrica de certificación carga el parámetro `CERTIFICACIÓN`. Esto acredita un mecanismo existente que debe considerarse antes de introducir otra configuración. No acredita que el recorrido de creación lo haga cumplir ni demuestra que configure los días admisibles del documento.

Quedan diferenciadas dos decisiones: habilitación del registro en el día de referencia y admisibilidad del día seleccionado como fecha del documento. Los métodos inspeccionados muestran carga y consulta de habilitación; no mostraron una lista configurable de días documentales como 29, 30 o 31 de diciembre. El tesista aclaró después que `ParametroSistema` abre certificaciones globalmente y que el registro para la gestión anterior está fijado en código y debería parametrizarse. Esta es una necesidad de cambio declarada, no una capacidad existente ni una extensión aprobada del modelo de parámetros.

El tesista confirmó que la ventana extraordinaria se configura para una gestión concreta y puede abrirse en cualquier momento del año actual para certificar el 29 o el 31 de diciembre del año inmediatamente anterior. Por ello, HU-FEC-02 se revisó explícitamente; la condición fija de primer trimestre permanece como antecedente del JavaScript inspeccionado, no como restricción del diseño nuevo. La extraordinaria vigente es suficiente como habilitación temporal y no requiere apertura global. Inicio/fin se configurarán mediante la administración existente y se conservará su semántica; la excepción no dispensa permisos o saldo. Los días documentales 29/31 no se consideran configurables ni se autoriza cualquier gestión histórica.

Si la política documental se configura, una propuesta candidata es mantener separados la lectura del parámetro, su interpretación y la coordinación de creación. La configuración puede evitar cambios de código para ciertos ajustes, pero no elimina la lógica que valida la configuración y decide aceptación o rechazo. El alcance y complejidad de esa variación deben compararse con la alternativa de una regla explícita, sin introducir un motor genérico de reglas por anticipación. La apertura de una ventana de registro no se interpreta automáticamente como permiso para cualquier fecha del documento.

### Punto de extensión verificado de las fábricas

El tesista señaló que el mecanismo es extensible mediante fábricas. La inspección confirma que `ParametroSistema` es la entidad, `AbstractFactoryMethodParametro` define la base de las fábricas, `CertificacionParametroFactory` selecciona `CERTIFICACIÓN` y `ParametroSistemaService` construye una lista explícita de fábricas y reúne sus resultados. Por tanto, existe un punto de extensión reutilizable, pero no un descubrimiento automático de cualquier nueva variante: agregar otra fábrica exigiría considerar también su incorporación al servicio. Esta constatación favorece estudiar una extensión acotada del mecanismo existente, sin dar por adoptada una clase nueva ni otra infraestructura.

La carga obtiene la gestión mediante `GestionService::getGestion()` y consulta parámetros por esa gestión. La revisión del 20 de octubre confirma que `getGestion()` devuelve la gestión seleccionada desde la URL `/poa/...` o `/presupuesto/...`, con valor alternativo de la gestión actual; `getGestionActual()` devuelve la marcada como actual en la base de datos. Ninguna debe confundirse automáticamente con el año del reloj institucional. Para la excepción se debe identificar la gestión de la tarea y contrastar selección, año del día de registro y parámetro pertinente; la URL por sí sola no acredita correspondencia con la tarea. La reutilización sigue pendiente de comprobarse con global cerrada/extraordinaria vigente y gestión objetivo distinta del año actual.

### Resultado del seguimiento de consumidores y siguiente decisión

En `config/packages/twig.yaml`, `parametros_sistema` expone `ParametroSistemaService` a Twig. `templates/poa/emitir_certificacion/mostrar_emitir_certificaciones.html.twig`, líneas 15–29, muestra el botón de creación si el usuario tiene el permiso de certificación, la apertura `CERTIFICACIÓN` está activa y existe saldo. Este es un control de presentación: no acredita por sí mismo rechazo de una petición directa. La futura extraordinaria suficiente no puede integrarse solo en ese botón ni quedar bloqueada allí por exigir apertura global; presentación y creación necesitan decisiones coherentes con el escenario.

La recomendación técnica candidata es reutilizar entidad, períodos y punto de extensión de fábricas existentes para cargar una habilitación extraordinaria distinguible de la ordinaria; comprobar su vigencia y la fecha documental sin depender de Twig; y hacer cumplir la decisión antes de efectos en la creación. No se fija todavía un nombre de parámetro, una clase nueva ni un cambio de esquema. Es necesario comprobar que la variante seleccionada conserva aperturas ordinarias y que la habilitación de una gestión no se reutiliza para otra. Se plantea como diseño para justificar, no como E7 ya aprobada ni como implementación realizada.

El tesista acotó el mecanismo administrativo: un operador con permisos de administración selecciona la gestión anterior —por ejemplo, 2025— y crea un parámetro nuevo de certificación extraordinaria mediante la administración existente. No se rediseñarán formulario, permisos o semántica de períodos como parte de esta propuesta; se reutilizará su comportamiento vigente, que debe caracterizarse al probar la extensión. La fecha documental sigue siendo un día sin significado institucional de hora; las fechas de apertura/cierre del parámetro son datos diferentes. No se requiere otra pregunta funcional sobre granularidad para continuar el análisis de esta extensión.

### Alcance administrativo acordado y puntos mínimos de extensión

La captura aportada por el tesista muestra administración de parámetros por gestión, tipo, fechas y estado. La inspección de `src/Form/admin/ParametroSistemaType.php` confirma selección de gestión, lista cerrada de tipos y campos de inicio/fin `DateTimeType`. La capacidad actual de escoger gestión y períodos permite reutilizar ese flujo, pero el tipo extraordinario todavía no aparece en la lista inspeccionada. Por tanto, no bastará escribir libremente otro nombre: deberá reconocerse una nueva opción y su variante en la carga existente.

El alcance técnico candidato queda limitado a incorporar el tipo extraordinario al formulario, proporcionar su fábrica siguiendo la extensión existente e incorporarla a la lista del servicio, y utilizar la habilitación pertinente en la decisión de creación y su representación visual. Se conserva el parámetro ordinario `CERTIFICACIÓN` y se evita modificar el mecanismo general de períodos o ampliaciones sin necesidad comprobada. «CertificacionExtraordinaria» es la denominación conceptual sugerida por el tesista; el identificador exacto y el nombre visible quedan como detalle técnico pendiente, no como una nueva decisión funcional bloqueante. No se propone una entidad o pantalla nuevas ni una migración de datos por este alcance.

Los criterios prospectivos mínimos son: seleccionar parámetro de la gestión de la tarea; admitir el escenario anterior con extraordinaria pertinente vigente aunque global esté cerrada; rechazar cuando no esté vigente o corresponda a otra gestión; conservar los días documentales 29/31 de diciembre y los demás controles; mantener el comportamiento ordinario; y comprobar coherencia entre interfaz y guardado. La representación y la lista de cambios son propuestas para el diseño, no una declaración de implementación autorizada o realizada. Se separará la parametrización funcional de las extracciones estructurales y se conservarán sus pruebas diferenciadas.

**Punto de partida Git actualizado:** el repositorio de aplicación tiene `HEAD` en `1294047effc21a97b86758eeedc99f1703b6d8ca`; el resolvedor y sus pruebas figuran en `8dc63307` y el contrato en `1294047e`, ambos del 18 de octubre de 2026. Por tanto, ya no están sin seguimiento como en la inspección inicial. No se ejecutaron esos commits en esta revisión ni se acreditó su envío remoto; siguen pendientes los registros intermedios que demuestren la secuencia previa declarada de caracterización/TDD.

### Diagnóstico estático del recorrido de creación

Se amplió la inspección a `CreateCertificacionController`, `EmitirCertificacionType`, `CreateCertificacionService`, `config/packages/security.yaml`, `config/services.yaml`, `ParametroSistemaRepository` y `PermisoUnidadProduccionUsario`. Se siguió el recorrido normal del controlador hacia el formulario y el servicio; no se ejecutaron peticiones HTTP ni se intentó eludir permisos. Los hallazgos describen el código inspeccionado, no una auditoría exhaustiva de configuración desplegada, extensiones, otros recorridos o base de datos.

| Condición | Evidencia del recorrido inspeccionado | Resultado y límite |
|:--|:--|:--|
| Acceso general | `security.yaml` exige `ROLE_POA` para rutas `/poa/`. | Hay barrera general; no equivale a permiso de certificar una unidad concreta. |
| Permiso de certificación por unidad | Existe `PermisoUnidadProduccionUsario::verificaPermisosCertificacion()`, pero no se observó su invocación en el controlador ni el servicio de creación. | No se acredita el control específico en este recorrido. Su existencia en otra clase no demuestra aplicación al guardar. |
| Habilitación normal o ampliación | El controlador obtiene `findArrayDeHabilitados()` después del bloque de creación, para datos de vista. Ese método consulta períodos normales y está marcado obsoleto. | Esa consulta no protege el guardado previo; no se observó comprobación de ampliación en el controlador o servicio inspeccionados. Otros mecanismos requieren contraste. |
| Saldo e importe | `CreateCertificacionService::topeCertificacion()` exige total positivo y no superior al disponible obtenido de la tarea. | Validación local identificada. No se demuestra protección frente a concurrencia ni actualización atómica del saldo. |
| Día institucional | `fechaEstaEnGestion()` comprueba solo rango anual; el formulario usa `DateTimeType` y no implementa las dos historias de fechas. | Brecha local respecto de las reglas declaradas; no se ha reproducido una aceptación inválida por HTTP. |
| Orden de efectos | `create()` invoca validación de fecha antes de crear la entidad, generar código, almacenar adjunto, persistir o registrar derivados. | Hay un punto temprano para validar la fecha. La nueva política y el rechazo sin efectos requieren pruebas propias. |

La evidencia no permite afirmar que todos los controles estén únicamente en JavaScript. Sí permite distinguir un control positivo de saldo, un control anual incompleto y controles específicos de permisos/habilitación no acreditados en el recorrido inspeccionado. Los posibles hallazgos de acceso y habilitación deben registrarse para revisión, sin ampliar automáticamente la primera intervención ni corregirlos como efectos secundarios. El primer candidato sigue siendo la regla de fechas porque ya cuenta con comportamiento esperado explícito.

### Siguiente incremento candidato: regla de fechas

Antes de implementarlo, el diseño debe especificar entradas por día calendario, día de registro de referencia controlable en `America/La_Paz`, datos de habilitación pertinentes y una salida de aceptación o rechazo con motivo. Los criterios prospectivos son los casos de ambas historias revisadas, equivalencia frente a distintas horas del mismo día, límites de mes/año, apertura/cierre de la ventana configurada y rechazo previo a efectos. La integración debe preservar el día elegido y no ajustar auditoría ni convertir silenciosamente otra fecha al cierre anual. No se propone cambiar columnas, modernizar bibliotecas ni reorganizar todo JavaScript en ese incremento.

Estos criterios se registran antes del cambio, pero la intervención sigue condicionada a la fundamentación y requisitos de las etapas pendientes. El caso debe contribuir al método con una regla de selección de responsabilidades y evidencia de su aplicación, no presentarse como una corrección aislada suficiente para validar la tesis. El diagnóstico actual es estático; la reproducción controlada de la brecha y la verificación del punto de integración aún están pendientes.

Se propone distinguir la admisibilidad del día documental —fecha solicitada, gestión de la tarea y día de registro de referencia— de la habilitación extraordinaria configurada. La decisión total de permitir el registro no puede obtenerse solo de aquellas tres entradas: debe combinarse con la vigencia de la ventana para la gestión correspondiente. Si la comprobación se integra en un único componente, deberá recibir explícitamente los datos pertinentes de la habilitación, sin leer formularios, DOM o repositorios dentro de la decisión; su lectura es otra responsabilidad. Los períodos referenciales de planificación no se añaden como restricciones. El reparto final entre política y coordinación es candidato, no una clase aprobada ni implementada.

Antes de implementar deben precisarse:

1. Verificar que la implementación utilice `America/La_Paz`, zona horaria institucional confirmada por el tesista para hoy y los cambios de día, mes, trimestre y año. Esta decisión no implica modificar la zona de almacenamiento ni los campos de auditoría.
2. Aplicar la semántica confirmada de fecha calendario: ninguna hora de un mismo día debe cambiar su admisibilidad. Decidir por separado la transición del formulario y del almacenamiento actual `datetime`, tras revisar consumidores y datos; no se acordó migración, conversión masiva ni normalización histórica.
3. Respaldo o confirmación funcional de HU-FEC-01 y HU-FEC-02, en particular la excepción de 29 y 31 de diciembre.
4. Casos de frontera y criterios de aceptación fijados antes del cambio: enero, febrero bisiesto, inicio/fin de la ventana configurada, gestión incompatible y rechazo sin efectos. Marzo/abril deja de ser frontera fija: debe poder aceptarse registro extraordinario después de marzo si la ventana pertinente está vigente.

Como criterio prospectivo de la corrección, entradas heredadas del mismo día con horas distintas deben recibir la misma decisión respecto de la fecha; por ejemplo, el 31 de diciembre no puede rechazarse únicamente por tener segundos posteriores a las 23:59:00. Esta equivalencia no concede validez al día: debe seguir cumpliendo HU-FEC-01 o HU-FEC-02. La aceptación no modifica `createdAt` ni `updatedAt` para reproducir la fecha del documento. Estos criterios están documentados antes de implementar la corrección y todavía no se han ejecutado como pruebas.

El contrato técnico de referencia sigue siendo el borrador `docs/development/architecture-contract.md` del proyecto, pendiente de adopción. Este registro aporta un escenario concreto para justificar la separación de una regla de fechas, pero no cierra E4–E6, no valida el método y no autoriza una refactorización global.
