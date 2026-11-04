# I04. Protocolo de ampliación de ventana extraordinaria

## Estado y compromiso previo

El 4 de noviembre de 2026 el tesista acepta separar la comprobación directa de la decisión temporal de la comprobación de lectura efectiva de configuración por el consumidor. Acepta el criterio de cero archivos de código de producción modificados para ampliar el cierre, con configuración, pruebas y costo inicial separados. Esta aceptación no autoriza construcción o cambios en SIGPP ni acredita ejecución. Es un protocolo de observación previsto; la selección de los puntos ejecutables y del mecanismo de control temporal sigue pendiente.

## Escenario y alcance

Se conserva el conjunto X01–X06 aceptado en `matriz_escenarios_temporales_e6.md`: ventana ficticia del 1 al 8 de febrero de 2027, ampliada hasta el 10 de febrero de 2027, en `America/La_Paz`. Inicio incluido desde las 00:00 y corte exclusivo a las 00:00 del día posterior al cierre. Se mantiene la misma gestión destinataria, inicio, estado y demás condiciones; solo se modifica el cierre. La apertura ordinaria se mantiene cerrada para evitar que oculte el resultado extraordinario. El ejercicio observa habilitación temporal, no autorización integral de creación ni admisibilidad de cualquier fecha documental.

La confirmación funcional por WhatsApp no permite trasladar esta ventana a cualquier mes: en abril ya no se admite registrar certificaciones de tareas de la gestión pasada. Los ejemplos de febrero siguen dentro del período pertinente. Los seis instantes no evalúan por sí solos la frontera marzo–abril o el calendario del último día hábil.

## Nivel A. Decisión temporal directa

El instrumento suministrará cada instante acordado a la decisión real bajo evaluación y conservará entrada, ventana, gestión destinataria, resultado esperado, resultado observado y error, si corresponde. No se sustituirá la decisión por un colaborador que devuelva respuestas prefijadas. En funcionamiento normal el instante provendrá del servidor PHP; el control del tiempo es una condición del ensayo y no una entrada autorizada al usuario.

| Caso | Instante ficticio | Cierre original 08/02 | Cierre ampliado 10/02 |
|:--|:--|:--|:--|
| X01 | 31/01/2027 23:59:59 | No habilitado | No habilitado |
| X02 | 01/02/2027 00:00:00 | Habilitado | Habilitado |
| X03 | 08/02/2027 23:59:59 | Habilitado | Habilitado |
| X04 | 09/02/2027 00:00:00 | No habilitado | Habilitado |
| X05 | 10/02/2027 23:59:59 | No habilitado | Habilitado |
| X06 | 11/02/2027 00:00:00 | No habilitado | No habilitado |

Las doce observaciones previstas no equivalen a doce casos independientes de uso institucional. La tabla fija expectativas, no resultados. La comprobación directa no demuestra lectura de datos persistidos o conexión con el consumidor.

## Nivel B. Lectura efectiva por el consumidor

**Alcance aceptado posteriormente:** el 4 de noviembre de 2026 el tesista responde «aceptamos» a observar la habilitación antes de permitir la creación, con lectura efectiva del cierre configurado; no basta su representación en pantalla. El recorrido de referencia es `CreateCertificacionController::new()` hacia `CreateCertificacionService::create()`. Esto selecciona la frontera observable, no impone que la regla resida en el controlador ni autoriza añadir código. En `7c0bca08`, la consulta de habilitados observada ocurre después del bloque de creación; no se la presenta como una barrera previa ya existente. El punto de decisión futuro y el control temporal de su acceso a configuración se concretarán sin fabricar una línea base de capacidad inexistente.

1. Identificar consumidor real, fuente de configuración y punto de decisión antes de ejecutar; conservar versión del código y diferencias locales.
2. Preparar configuración ficticia en un entorno aislado, sin credenciales o datos productivos. Registrar el valor almacenado y el leído con cierre original.
3. Observar el consumidor en el instante X04: debe resultar no habilitado con cierre 08/02.
4. Modificar únicamente el cierre a 10/02 mediante el mecanismo pertinente, conservando inicio, gestión, estado y restantes condiciones.
5. Recargar la configuración y el estado del consumidor, sin reutilizar inadvertidamente una colección anterior; registrar valor leído y decisión para el mismo X04. Debe resultar habilitado.
6. Observar X06 con la configuración ampliada: debe resultar no habilitado, descartando una apertura ilimitada.
7. Conservar instrucciones, comando, salida, diferencias y limpieza del entorno. Informar todos los fallos sin reparar la solución dentro del mismo registro de resultados.

El nivel B requiere lectura real de la configuración de prueba: un repositorio sustituido que devuelva manualmente el cierre nuevo no demuestra persistencia y recarga. El transporte HTTP y la persistencia real de certificaciones no quedan incluidos automáticamente; el informe declarará el recorrido efectivamente observado. No se obliga a crear certificaciones para comprobar únicamente habilitación.

## Recuento del cambio posterior

La referencia anterior será la versión que ya contenga la capacidad extraordinaria inicial verificada, no una versión que carezca de ella. La referencia posterior diferirá por la ampliación de cierre y los ajustes auxiliares explícitos del ensayo. Registrar por separado archivos de producción modificados y nuevos, componentes/responsabilidades afectados, archivos de prueba modificados y nuevos, y cambios de datos de configuración. No equiparar archivos y componentes ni contar solo líneas favorables.

El criterio aceptado para ampliar el cierre es **cero archivos de código de producción modificados o añadidos**. Las pruebas y la configuración no se presumen sin cambios: sus intervenciones se registran. Cumplir este criterio no demuestra por sí solo menor esfuerzo, superioridad respecto de una implementación anterior o validez del método. El costo de incorporar inicialmente la capacidad se documentará en otro tramo.

## Barreras y pendientes de instrumentación

**Referencia recuperada y recorrido precisado:** nueva comprobación confirma `feature/propuesta-tesis`/`7c0bca08` limpia. El controlador de creación invoca `create()` antes de consultar directamente `findArrayDeHabilitados()`, método con reloj de base de datos; no usa `ParametroSistemaService` en ese recorrido visible. Se recomienda seleccionar como consumidor de observación la habilitación previa a creación, no limitar la evidencia a una colección general o menú. Selección y mecanismo temporal todavía pendientes; sin ejecución o construcción. Detalle y localizadores en `continuidad_i04_rama_sigpp_2026-11-04.md`. La nota de bloqueo siguiente conserva el estado anterior, ya resuelto.

**Comprobación posterior de continuidad, 4 de noviembre:** la copia SIGPP está en `hotfix/bsip-163-tarea-calculo`, revisión `c20fba5440d25be91ae42f9a45fd9c5f16bb12b4`, sin cambios locales informados, no en la referencia de tesis `7c0bca08`. La lectura actual de `ParametroSistemaService` confirma carga al construir y consulta posterior de colección estática en esta copia. No se usará como reconfirmación de la rama de tesis ni se cambiará de rama sin acordarlo. Registro en `continuidad_i04_rama_sigpp_2026-11-04.md`; selección del consumidor detenida hasta recuperar la referencia pertinente.

La lectura del repositorio `ParametroSistemaRepository.php` durante esta sesión muestra métodos que filtran con `new DateTime('now')` y otros con `CURRENT_TIMESTAMP()`. Es inspección estática, no ejecución o comprobación de versión Git. Controlar el instante solo en la decisión no controla esos filtros; antes de ejecutar el nivel B debe identificarse el recorrido usado y cómo observarlo con el mismo instante, sin modificar relojes del equipo o producción.

En la referencia diagnóstica previa no se acreditó un punto extraordinario completo: se registrará esa limitación, no seis rechazos inventados o una línea base de cero aciertos. Faltan seleccionar el consumidor concreto, resolver el control temporal del recorrido de configuración y especificar entorno y comandos reproducibles. Estos pendientes impiden denominar al protocolo instrumento ejecutable listo. E6 permanece abierta y no se ejecutan pruebas por aprobar este documento.
