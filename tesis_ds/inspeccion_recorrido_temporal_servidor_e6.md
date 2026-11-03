# Inspección del recorrido temporal del servidor — E6

## Alcance y referencia

El 3 de noviembre de 2026 se inspeccionó el recorrido de creación de certificaciones para localizar los controles temporales pertinentes a O01–O06. Git confirmó la revisión `7c0bca084b05c462137fd62c24e6b025bb09a12c` de SIGPP y no informó cambios locales antes de la lectura. Esta actividad es análisis estático, no ejecución de casos, petición HTTP o medición de esfuerzo humano. No se modificó SIGPP ni se ejecutó nuevamente O06.

## Recorrido observado

| Punto del recorrido | Evidencia local en la revisión indicada | Alcance de la conclusión |
|:--|:--|:--|
| Inicialización de fecha | `src/Controller/poa/Certificacion/CreateCertificacionController.php`, líneas 88–97: fecha inicial mediante `new DateTime()`, creación del formulario y recepción de la solicitud. | Existe uso de reloj PHP para inicializar la fecha; no equivale a comparar la fecha documental recibida con el día operativo. |
| Configuración del campo | `src/Form/poa/EmitirCertificacionType.php`, líneas 32–42: `disabled` depende de `!$this->verificarDia()` y el atributo `onchange` llama a JavaScript. | El formulario contiene un candidato a control temporal en PHP; el atributo de pantalla no es una validación temporal del servicio. |
| Candidato a límite mensual | Mismo formulario, líneas 196–210: consulta el día actual, retorna `true` si encuentra coincidencia entre 1 y 8 y también retorna `true` al terminar el bucle. | Para cualquier ejecución normal de esa función, el resultado es `true`, también fuera de 1–8. Esta función no deshabilita el campo por superar el día 8. Deducción del código, no ensayo con reloj controlado. |
| Invocación del servicio | Controlador, líneas 99–147: tras `isSubmitted()` e `isValid()`, construye la entrada y llama a `create()` en la línea 137. | En el bloque inspeccionado no hay comparación explícita entre fecha documental y día operativo antes de invocar el servicio. No se declara ausencia de validadores externos, escuchas o controles globales no examinados. |
| Validación temporal del servicio | `src/Service/Certificacion/CreateCertificacionService.php`, líneas 48–52 y 94–109: comprueba pertenencia de fecha al año de la tarea antes de saldo y restricciones. | Ese punto distingue O06 por gestión, pero no representa el día del intento necesario para O02/O03 o las relaciones de O04/O05 con «hoy». No se rotularán llamadas iguales como distintos relojes controlados. |
| Consulta de habilitados | Controlador, líneas 150–151: `findArrayDeHabilitados($gestion)` está después del bloque de envío y creación; su resultado se entrega a la vista. | La consulta visible no constituye una condición previa a la llamada a `create()` en este método. No demuestra por sí sola aceptación HTTP indebida o ausencia de controles externos. |
| Servicio de parámetros | `src/Service/ParametroSistemaService.php`, líneas 38–93 y 104–141: carga colecciones al construirse y consulta parámetros activos. | Este mecanismo existe, pero el constructor y el bloque de creación del controlador inspeccionado no lo invocan explícitamente. No se confunde la existencia de parámetros con su aplicación efectiva en ese recorrido. |

## Implicación para el diagnóstico

La revisión identifica un punto PHP concreto que parecía limitar la edición al día 8, pero cuyo resultado booleano no distingue días. Esto complementa la discrepancia ya ejecutada en JavaScript para O03, sin convertir dos observaciones de código distinto en dos ejecuciones independientes del mismo caso. La extracción de una función o su traslado a otro componente no corregiría por sí sola ese comportamiento. Cualquier futura corrección del resultado deberá distinguirse de una refactorización que conserve comportamiento.

No corresponde calcular un porcentaje de I01 de servidor a partir de esta lectura ni declarar I02 incumplido: no se observaron escrituras o interacciones para O03–O05 en esta actividad. Tampoco se afirma que una solicitud real eluda todos los controles de la aplicación. La inspección acota dónde falta localizar o instrumentar una decisión efectiva, y evita fabricar una línea base añadiendo previamente la solución.

## Pendiente inmediato

Antes de una prueba HTTP deben examinarse las restricciones de validación de la entidad, la configuración de validación y los controles globales pertinentes a la ruta. Solo después podrá fijarse un instrumento que distinga rechazo temporal, sustitución de fecha y paso hacia efectos, conservando datos ficticios y aislamiento. No se exige desplegar ni modificar producción para hacerlo. La comprobación aislada de O06 conserva su validez y no necesita repetirse para cubrir esta inspección.

E6 permanece abierta: I03 humano, I04 y la línea base completa siguen pendientes. Este registro es evidencia diagnóstica del caso de aplicación, no formalización o evaluación del método de refactorización.
