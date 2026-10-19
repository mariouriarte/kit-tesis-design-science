# Certificación: reglas de fecha y trazabilidad

## Fuente y alcance

Especificación aportada por el tesista en la sesión del 18 de octubre de 2026. Se registra como conocimiento institucional declarado, pendiente de respaldo documental o confirmación del responsable funcional; no se atribuye a una norma publicada ni se presenta como requisito nuevo. Las reglas describen el comportamiento esperado, no acreditan su cumplimiento uniforme en SIGPP. El tesista confirmó `America/La_Paz` como zona horaria institucional para determinar hoy y los cambios de día, mes, trimestre y año. También confirmó que `fecha` representa exclusivamente el día del documento y calificó la inclusión de hora como error de implementación; la hora no tiene significado institucional en ese campo.

## Condiciones comunes

Para crear una certificación, el usuario debe tener permiso en la unidad correspondiente, la operación debe estar habilitada para la gestión seleccionada mediante período normal o ampliación vigente y debe existir saldo suficiente. La fecha del documento debe pertenecer a la gestión de la tarea. Estas condiciones deben verificarse en el servidor, con independencia de las restricciones de la pantalla. La conformidad con la regla de fechas, por sí sola, no habilita la operación.

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

Durante enero, febrero y marzo se permite registrar pendientes de una tarea cuya gestión sea el año inmediatamente anterior al año de operación. Se admiten exclusivamente el 29 o el 31 de diciembre de esa gestión anterior; desde el 1 de abril se rechaza este escenario. La habilitación vigente y las demás condiciones comunes siguen siendo obligatorias. No se convierte automáticamente otra fecha al 31 de diciembre.

| Operación | Gestión de tarea | Fecha solicitada | Resultado respecto de la fecha |
|:--|:--|:--|:--|
| 10/02/2026 | 2025 | 31/12/2025 | Aceptar. |
| 10/02/2026 | 2025 | 29/12/2025 | Aceptar. |
| 10/02/2026 | 2025 | 30/12/2025 | Rechazar. |
| 10/02/2026 | 2025 | 31/12/2024 | Rechazar. |
| 10/02/2026 | 2025 | 10/02/2026 | Rechazar: gestión incompatible. |
| 01/04/2026 | 2025 | 31/12/2025 | Rechazar: excepción finalizada. |

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

Antes de implementarlo, el diseño debe especificar entradas por día calendario, fecha de operación controlable en `America/La_Paz` y una salida de aceptación o rechazo con motivo. Los criterios prospectivos son los casos de ambas historias, equivalencia frente a distintas horas del mismo día, límites de mes/año/trimestre y rechazo previo a efectos. La integración debe preservar el día elegido y no ajustar auditoría ni convertir silenciosamente otra fecha al cierre anual. No se propone cambiar columnas, modernizar bibliotecas ni reorganizar todo JavaScript en ese incremento.

Estos criterios se registran antes del cambio, pero la intervención sigue condicionada a la fundamentación y requisitos de las etapas pendientes. El caso debe contribuir al método con una regla de selección de responsabilidades y evidencia de su aplicación, no presentarse como una corrección aislada suficiente para validar la tesis. El diagnóstico actual es estático; la reproducción controlada de la brecha y la verificación del punto de integración aún están pendientes.

Se propone una política comprobable con tres entradas explícitas: fecha solicitada, gestión de la tarea y fecha de operación determinada por el servidor. Su responsabilidad sería aceptar o rechazar la fecha, sin leer formularios, DOM, repositorios ni modificar auditoría. La operación de creación la invocaría antes de los efectos, conservando separados permisos, habilitación y saldo. Es un diseño candidato, no una clase aprobada ni implementada.

Antes de implementar deben precisarse:

1. Verificar que la implementación utilice `America/La_Paz`, zona horaria institucional confirmada por el tesista para hoy y los cambios de día, mes, trimestre y año. Esta decisión no implica modificar la zona de almacenamiento ni los campos de auditoría.
2. Aplicar la semántica confirmada de fecha calendario: ninguna hora de un mismo día debe cambiar su admisibilidad. Decidir por separado la transición del formulario y del almacenamiento actual `datetime`, tras revisar consumidores y datos; no se acordó migración, conversión masiva ni normalización histórica.
3. Respaldo o confirmación funcional de HU-FEC-01 y HU-FEC-02, en particular la excepción de 29 y 31 de diciembre.
4. Casos de frontera y criterios de aceptación fijados antes del cambio: enero, 31 de marzo/1 de abril, febrero bisiesto, gestión incompatible y rechazo sin efectos.

Como criterio prospectivo de la corrección, entradas heredadas del mismo día con horas distintas deben recibir la misma decisión respecto de la fecha; por ejemplo, el 31 de diciembre no puede rechazarse únicamente por tener segundos posteriores a las 23:59:00. Esta equivalencia no concede validez al día: debe seguir cumpliendo HU-FEC-01 o HU-FEC-02. La aceptación no modifica `createdAt` ni `updatedAt` para reproducir la fecha del documento. Estos criterios están documentados antes de implementar la corrección y todavía no se han ejecutado como pruebas.

El contrato técnico de referencia sigue siendo el borrador `docs/development/architecture-contract.md` del proyecto, pendiente de adopción. Este registro aporta un escenario concreto para justificar la separación de una regla de fechas, pero no cierra E4–E6, no valida el método y no autoriza una refactorización global.
