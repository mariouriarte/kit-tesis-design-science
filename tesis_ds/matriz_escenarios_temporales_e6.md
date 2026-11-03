# Matriz de escenarios temporales y observables — E6

**Estado:** conjunto ordinario **O01–O06 aceptado por el tesista**, quien responde «aceptamos». Los criterios I01 e I02 del 100 % también están aceptados. Esto no acredita ejecución completa, observables resueltos o cierre de E6. La ventana y los seis casos I04 ya aceptados se conservan aparte y no se someten a una nueva elección. No se agregan reglas o funcionalidades por aceptar esta matriz.

## 1. Separación de propiedades y alcance

- **I01:** correspondencia entre decisión temporal requerida y resultado del punto de comprobación elegido.
- **I02:** rechazo sin crear certificación, seguimiento, autorización ni almacenar adjuntos, en los casos que requieran rechazo.
- **I03:** esfuerzo humano activo de preparación y comprobación; no se obtiene de la ejecución automatizada o de esta documentación.
- **I04:** cambio posterior por ampliación de cierre configurado; no equivale a comparar costo inicial de construir esa capacidad.

Una decisión correcta de pantalla no demuestra permiso integral de creación ni rechazo sin efectos de servidor. Los resultados se informarán por caso y por punto observado, sin sumar verificaciones de capas diferentes como si fueran casos independientes de eficacia. Todos los casos del conjunto aprobado deberán comprobarse para declarar cumplimiento; ejecutar únicamente un subconjunto favorable no satisface el criterio del 100 %. La cobertura de ejecución se informará descriptivamente, sin crear un indicador de mejora adicional.

## 2. Conjunto ordinario aceptado

Supuestos comunes: tarea de gestión **2026**, apertura ordinaria vigente y pertinentes permisos, elegibilidad y saldo válidos. Se usarán datos ficticios y un contexto temporal controlado en el instrumento que lo permita; los supuestos no se presentarán como controles comprobados si no se observaron. El día documental se compara por calendario en `America/La_Paz`; no se cambian fechas de auditoría. El cambio de día no se simula mediante etiquetas sobre dos llamadas idénticas al servicio actual.

| ID | Día del intento | Fecha documental | Decisión requerida | I02 |
|:--|:--|:--|:--|:--|
| O01 | 08/06/2026 | 08/06/2026 | Admitir respecto de fecha: mismo día. | No corresponde a rechazo. |
| O02 | 08/06/2026 | 31/05/2026 | Admitir respecto de fecha: cierre mensual en día 8 incluido. | No corresponde a rechazo. |
| O03 | 09/06/2026 | 31/05/2026 | Rechazar: fuera del plazo mensual ordinario. | Sí. |
| O04 | 15/06/2026 | 14/06/2026 | Rechazar: día anterior distinto del cierre admitido. | Sí. |
| O05 | 15/06/2026 | 16/06/2026 | Rechazar: fecha futura. | Sí. |
| O06 | 10/01/2026 | 31/12/2025 | Rechazar: fecha de otra gestión para tarea 2026, sin extraordinaria. | Sí. |

O01/O04/O05/O06 se apoyan en las reglas y casos funcionales existentes; O02 incorpora la inclusión del día 8 aclarada por el tesista y O03 el límite ordinario resultante. Las entradas no son una muestra estadística de uso ni cubren todos los calendarios. La selección reúne decisión admisible, frontera y rechazos distintos sin intervenir saldo o permisos como reglas nuevas. La aprobación de los criterios porcentuales no sustituye la aceptación de este conjunto y la definición del instrumento.

## 3. Evidencia disponible: no confundir antecedente con ejecución del conjunto

**Interacciones auxiliares del servicio, 3 de noviembre:** `comprobacion_interacciones_fechas_gestion_e6.md`: tres fechas de gestión 2026 pasan la validación anual y llegan a una llamada de guardado de certificación y seguimiento cada una, con colaboradores sustituidos; 3 pruebas/36 aserciones satisfactorias. No hay día operativo controlado, persistencia real o ejecución de la ruta. S31/S14/S16 no se cuentan como O03–O05 completos ni como porcentaje global I01/I02; cero autorización/archivo corresponde solo a la rama sin restricción. Git `7c0bca08` permanece limpio y no se obtiene esfuerzo humano I03.

**Comprobación adicional del formulario, 3 de noviembre:** `comprobacion_formulario_temporal_e6.md` ejecuta Form y Validator reales, con anotaciones y sin iniciar la aplicación: cuatro fechas válidas conservadas y formularios válidos; fecha mal formada rechazada y fecha vacía provoca excepción de mapeo, conservada como discrepancia del control técnico. No controla día del intento ni ejecuta servicio, HTTP o persistencia. F01–F04 no se suman como O01–O05 completos ni producen un porcentaje nuevo de I01/I02. La imagen local utilizada difiere de la histórica de O06 y se identifica en el registro; SIGPP permanece en `7c0bca08` limpio.

| Caso o antecedente | Evidencia existente | Qué sigue faltando |
|:--|:--|:--|
| O01–O05, pantalla | En `comprobacion_ordinaria_pantalla_e6.md`, cuatro resultados concordantes y discrepancia O03, con contexto temporal controlado en fragmento aislado. | Comprobación del consumidor pertinente en servidor y conexión; no se validaron autorización o persistencia. |
| O02 y O03, antecedente | Primer instrumento M08/M09: campo conservado sin avisos en ambos días, con discrepancia al día 9. | No sumar su repetición en la ampliación como observaciones independientes. |
| O04, antecedente PHP | Registro local previo de solicitud de correlativo con fecha 14/06/2026 y tarea de entrada 2026. | En ese punto, día del intento controlado, datos auxiliares coherentes y recorrido pertinente; el registro previo conserva límites. |
| O06, servicio PHP | `comprobacion_o06_servidor_e6.md`: excepción de fecha esperada y cero llamadas a los cuatro colaboradores de efectos; 1 prueba, 8 aserciones satisfactorias. | Interacciones con dobles, no escrituras reales; día 10/01 contextual, no reloj controlado del servicio. No completa I02 para O03–O06. |
| Control 30/05 del instrumento mensual | Aviso y vaciado correctos en la comprobación aislada. | Se conserva como control técnico original; no se incorpora retrospectivamente para mejorar el porcentaje del conjunto ordinario. |

La nueva agrupación no convierte los ensayos anteriores en un protocolo definido antes de esas ejecuciones. Los registros mantienen sus condiciones y fecha. Para una comparación posterior se deberá fijar versión, condiciones y qué observaciones son equivalentes antes de construir o medir. No se reconstruye una línea base completa a partir de estos fragmentos heterogéneos.

## 4. Observables de rechazo para I02

Para O03–O06 se registrarán decisión y motivo, y se comprobarán por separado los cuatro efectos ya incluidos en el criterio aceptado. El diseño del instrumento deberá activar y observar el consumidor real pertinente, sin sustituir la decisión temporal evaluada por un doble que siempre rechace. No basta una excepción originada por saldo inválido u otro error ajeno al escenario temporal. Los datos de entrada, la tarea recargada y la gestión deberán ser coherentes; no se heredará silenciosamente la discrepancia 2025/2026 del auxiliar anterior.

| Efecto prohibido | Observable de interacciones disponible en pruebas aisladas | Comprobación de efectos reales aún por definir |
|:--|:--|:--|
| Crear certificación | Ausencia de llamada a `EmitirCertificacionRepository::save()`. | Estado antes/después de la persistencia aislada, si ese nivel se selecciona. |
| Crear seguimiento | Ausencia de llamada a `SeguimientoCertificacionRepository::save()`. | Ausencia de registros relacionados en el alcance de integración acordado. |
| Crear autorización | Ausencia de llamada a `CreateCertificacionAutorizacionService::create()`. | Ausencia de autorización persistida en ese mismo alcance. |
| Almacenar adjunto | Ausencia de llamada a `UploadFileService::upload()`. | Ausencia de archivo u objeto creado en almacenamiento de prueba. |

Las ausencias de llamadas con dobles respaldan únicamente el alcance aislado. No se declararán equivalentes a ausencia de escrituras reales sin un ensayo de integración. La solicitud de correlativo puede registrarse como interacción auxiliar —como ocurrió en el diagnóstico previo—, pero no se presume que esa llamada tenga por sí sola un efecto persistente ni se redefine I02 a partir de ella. Una respuesta de error después de cualquiera de los cuatro efectos prohibidos no cumple el criterio.

## 5. Punto de comprobación y barreras del instrumento

El servicio PHP actual en `7c0bca08` comprueba rango anual y no recibe ni consulta el día del intento. Las pruebas de O02/O03 necesitan distinguir contextos temporales que ese punto no representa; no se ejecutarán dos llamadas idénticas presentándolas como los días 8 y 9. La función JavaScript original permitió observar una discrepancia local, pero no reemplaza la autoridad PHP acordada. La ausencia del punto de decisión adecuado se registra como limitación, no como seis resultados fallidos prefabricados.

Antes de ejecutar el conjunto completo faltan seleccionar el consumidor y la forma de control y observación pertinentes a cada propiedad. Preparar datos o instrumentos no autoriza añadir la solución a producción para fabricar la línea base. En la capacidad futura deberá comprobarse tanto la decisión como su uso efectivo por consumidores. Esta matriz no aprueba un mecanismo de reloj, clase, contrato o alternativa de E7.

## 6. I04 permanece separado: seis casos ya aceptados

Ventana ficticia original del **01 al 08/02/2027**, ampliada al **10/02/2027**; misma gestión destinataria y demás condiciones. Inicio a las 00:00 incluido y corte exclusivo a las 00:00 del día posterior al cierre, en `America/La_Paz`. Los ejemplos con segundos no limitan la definición del intervalo ni excluyen fracciones del día. Su aceptación no constituye una apertura institucional real ni una ejecución.

| ID | Instante ficticio | Cierre original 08/02 | Cierre ampliado 10/02 |
|:--|:--|:--|:--|
| X01 | 31/01/2027 23:59:59 | No habilitado | No habilitado |
| X02 | 01/02/2027 00:00:00 | Habilitado | Habilitado |
| X03 | 08/02/2027 23:59:59 | Habilitado | Habilitado |
| X04 | 09/02/2027 00:00:00 | No habilitado | Habilitado |
| X05 | 10/02/2027 23:59:59 | No habilitado | Habilitado |
| X06 | 11/02/2027 00:00:00 | No habilitado | No habilitado |

Los identificadores X01–X06 facilitan trazabilidad de la tabla original, sin crear casos o cambiar resultados. La capacidad extraordinaria y lectura efectiva de configuración todavía requieren instrumento y construcción autorizados en su etapa. No se miden modificabilidad o esfuerzo comparativos frente a una implementación anterior inexistente. El resultado estructural esperado de ampliación sin modificar código conserva separado el cambio de configuración y el costo inicial de incorporar la capacidad.

Al contrastar esta tabla se corrigió una errata del documento consolidado DSR: X05 aparecía habilitado en la ventana original que cerraba el día 8. La fuente aceptada de E6 ya decía «No habilitado». Se corrigió el Markdown y se dejó nota editorial; no se cambiaron criterios por resultados. El PDF previamente cargado no se actualiza por esa corrección y debe revisarse si se prepara una nueva versión.

## 7. Exclusiones y pendientes explícitos

- El calendario real de días hábiles y la ratificación completa de excepciones anuales siguen pendientes; no se rellenan con una autorización hipotética de agosto o días fijos 29/31.
- Las tres horas del 31/12 ya comprobadas permanecen como diagnóstico específico, no se mezclan con O01–O06 o X01–X06 para aumentar un porcentaje.
- La selección del conjunto ordinario no promete refactorización de todos los controles de certificación ni una nueva integración.
- I03 sigue sin línea base humana. La preparación de esta matriz y el ensayo automatizado anterior son asistencia declarada, no minutos activos del tesista.

## 8. Procedencia y decisiones resueltas

Fuentes: `06_diagnostico.md`, `reglas_fecha_certificacion.md`, `cuestionario_planificacion_certificacion.md` y `comprobacion_cierre_mensual_e6.md`. Los resultados de referencia se reutilizan con sus límites; la organización inicial de la matriz no efectuó nuevas ejecuciones. Los criterios I01/I02, O01–O06 y X01–X06 están aceptados y no debe repetirse su aceptación. Faltan completar puntos de comprobación, instrumentos y línea base; aceptar un conjunto no equivale a cumplirlo.

La ampliación aislada de pantalla para O01–O05 se documenta separadamente en `comprobacion_ordinaria_pantalla_e6.md`. O06 depende de la gestión de la tarea, que el fragmento seleccionado no recibe, y no se fuerza dentro de ese instrumento para completar artificialmente seis casos. Los cuatro efectos de I02 tampoco se comprueban mediante avisos y campos de pantalla.

O06 se comprobó posteriormente en el servicio real con dobles, mediante contenedor efímero sin red y montaje de solo lectura. Su registro preserva un primer fallo del reporte y la repetición con datos y expectativas iguales después de corregir solo el informe. No se suman esas dos ejecuciones ni los puntos de pantalla y PHP como casos homogéneos de un único porcentaje.
