# E7e. Construcción y verificación interna

## Registro preliminar de construcción

La intervención inicial en SIGPP/SIPOA4 se realizó como una mejora arquitectónica parcial orientada a separar lógica de negocio que se encontraba concentrada en controladores. La acción técnica principal fue la creación de la carpeta `src/Service`, utilizada para extraer parte de la lógica asociada con procedimientos del subcircuito POA, especialmente la creación de tareas durante la elaboración del POA y la creación de tareas durante la modificación del POA.

Esta versión debe tratarse como un prototipo formativo, no como arquitectura final. En términos de Design Science, su valor no está en demostrar todavía una solución madura, sino en revelar qué decisiones iniciales funcionan, qué inconsistencias aparecen y qué debe formalizarse en el método de refactorización arquitectónica incremental. La separación parcial permitió observar una mejora inicial en separación de responsabilidades y abrió la posibilidad de implementar pruebas unitarias sobre lógica que antes estaba fuertemente acoplada al controlador.

## Evidencia técnica disponible

| Evidencia | Descripción | Estado | Uso metodológico |
|:--|:--|:--|:--|
| Carpeta `src/Service` | Espacio creado para ubicar lógica extraída desde controladores. | Disponible en el código de SIGPP/SIPOA4. | Evidencia de intervención inicial. |
| Extracción parcial de lógica | Separación de lógica en procedimientos vinculados con creación de tareas en elaboración y modificación POA. | Parcial. | Evidencia de aplicabilidad inicial del enfoque. |
| Posibilidad de pruebas unitarias | Algunas piezas de lógica extraída pueden probarse fuera del controlador. | Preliminar. | Verificación técnica inicial de testabilidad. |
| Inconsistencias de diseño | Se mezclaron conceptos de objetos de valor y objetos de transferencia de datos. | Identificadas. | Hallazgo formativo para rediseño. |

## Archivos identificados en la intervención inicial

La evidencia inicial fue contrastada por el tesista con historial y estructura actual de Git. Los archivos identificados permiten sostener que existió una intervención real en el código, aunque todavía parcial y no uniforme.

| Archivo | Tipo de cambio | Evidencia que aporta | Limitación |
|:--|:--|:--|:--|
| `src/Controller/poa/Certificacion/CreateCertificacionController.php` | Modificación del controlador. | Se redujo parte de la lógica de creación de certificaciones y se delegó hacia servicios. | Falta cuantificar reducción de tamaño, complejidad y dependencias directas. |
| `src/Service/Certificacion/CreateCertificacionService.php` | Creación o modificación de servicio. | Concentra reglas de creación de certificación: validación de fecha, tope de certificación, restricciones de subpartida, generación de código, seguimiento y autorización. | No se identificó todavía una prueba unitaria directa para este servicio principal. |
| `src/Service/Certificacion/Dto/CreateCertificacionInput.php` | Creación de objeto de transferencia de datos. | Transporta datos del formulario hacia el servicio de creación de certificación. | Debe revisarse su separación conceptual respecto de objetos de valor. |
| `src/Service/CertificacionAutorizacion/CreateCertificacionAutorizacionService.php` | Creación de servicio específico. | Maneja la creación de autorización de certificación cuando corresponde. | Debe verificarse si su diseño es replicable en otros procedimientos del módulo. |
| `tests/CertificacionAutorizacion/CreateCertificacionAutorizacionTest.php` | Creación de prueba unitaria. | Valida lógica de autorización de certificación fuera del controlador. | Cubre principalmente `CreateCertificacionAutorizacionService`, no el servicio principal de certificación. |

Como evidencia de historial se registran los commits `815ce6c0` ("Dev"), `6e333e27` ("Adición de pruebas unitarias") y `9d4af430` ("Separación a servicios creacion de certificacion"). Estos commits deberán verificarse con el repositorio SIGPP/SIPOA4 antes de ser citados como evidencia final en la tesis.

## Cuantificación preliminar desde Git

La cuantificación inicial del historial Git permite sostener que la intervención no fue meramente declarativa, sino que produjo cambios localizables en archivos del subcircuito de certificación. Los datos disponibles todavía no reemplazan una evaluación sumativa, pero sí son suficientes para documentar una evaluación formativa inicial.

| Commit | Mensaje | Cambio global | Archivos relevantes | Lectura técnica |
|:--|:--|:--|:--|:--|
| `9d4af430` | Separación a servicios creacion de certificacion | 12 archivos modificados, 302 inserciones y 155 eliminaciones. | `CreateCertificacionController.php` (+120/-111), `CreateCertificacionService.php` (+95/-7), `CreateCertificacionInput.php` (+20 aproximado). | Evidencia de reestructuración del flujo de creación de certificación y delegación parcial desde controlador hacia servicio. |
| `6e333e27` | Adición de pruebas unitarias | 16 archivos modificados, 472 inserciones y 87 eliminaciones. | `CreateCertificacionAutorizacionService.php` (+33), `CertificacionAutorizacionDtoInput.php` (+38), `CreateCertificacionAutorizacionTest.php` (+63), `AutorizacionCambioEstadoSeriveTest.php` (+108). | Evidencia de incorporación de pruebas unitarias, concentradas principalmente en autorización de certificación y cambio de estado. |
| `815ce6c0` | Dev | 13 archivos modificados, 428 inserciones y 39 eliminaciones. | `CreateCertificacionController.php` (+28/-2), `CreateCertificacionService.php` (+100/-0), `CreateCertificacionInput.php` (+105). | Evidencia de creación o expansión inicial del servicio de certificación y del objeto de entrada asociado. |

La lectura técnica para la tesis es acotada. En `CreateCertificacionController.php` existe evidencia de refactorización, especialmente en el commit `9d4af430`, donde el volumen de inserciones y eliminaciones sugiere reestructuración del flujo más que simple adición de código. En `CreateCertificacionService.php` se observa concentración de reglas de creación de certificación, incluyendo fecha, tope, restricción de subpartida, generación de código, seguimiento, autorización y archivo adjunto. En `CreateCertificacionAutorizacionService.php` se concentra la regla de creación de autorización cuando la certificación se encuentra en estado de autorización.

La evidencia de pruebas es parcial. `tests/CertificacionAutorizacion/CreateCertificacionAutorizacionTest.php` permite sostener que una parte de la lógica extraída pudo probarse fuera del controlador; no obstante, no se identificó una prueba unitaria directa para `CreateCertificacionService.php`. Por tanto, la conclusión defendible es que la intervención demuestra viabilidad inicial de separación y testabilidad parcial, pero no valida todavía el método completo ni la calidad arquitectónica final.

## Resultado de ejecución de pruebas

La verificación técnica preliminar incluye la ejecución de la batería de pruebas unitarias existente mediante el comando `rtk phpunit`. El resultado reportado fue satisfactorio: `PHPUnit: OK (151 tests, 235 assertions)`.

Este resultado respalda que el sistema conserva una base de pruebas ejecutable y que la intervención no se documenta únicamente desde cambios estructurales en archivos. Sin embargo, su alcance debe formularse con precisión: las pruebas pasaron en conjunto y existe evidencia específica de prueba para autorización de certificación, pero no se identificó todavía una prueba unitaria directa para `CreateCertificacionService.php`. Por ello, el resultado se interpreta como evidencia de testabilidad parcial y verificación formativa, no como validación sumativa del método completo.

## Hallazgos formativos

La intervención inicial confirmó que la extracción hacia servicios puede reducir el acoplamiento directo entre controladores y lógica de negocio, pero también mostró que una extracción ad hoc no produce por sí misma una arquitectura coherente. La mezcla entre objetos de valor y objetos de transferencia de datos evidencia que el sistema necesita reglas explícitas de diseño para distinguir representación de datos, reglas de dominio, coordinación de casos de uso y acceso a persistencia.

El hallazgo más importante es metodológico: la mejora no debe presentarse como una migración terminada hacia una arquitectura madura, sino como evidencia de que el problema existe y de que la solución requiere formalización. Esta lectura evita el error de convertir una refactorización parcial en conclusión final; el trabajo debe usar esta intervención como evaluación formativa y como insumo para rediseñar el método, de acuerdo con la necesidad de documentar decisiones y versiones en Design Science (Wieringa, 2014).

La verificación inicial también muestra una brecha de cobertura: existe prueba unitaria para la autorización de certificación, pero no se identificó todavía una prueba unitaria directa para `CreateCertificacionService`. Esta brecha es útil para la tesis porque permite derivar un requisito de rediseño: cada servicio extraído desde un controlador debe quedar acompañado por pruebas unitarias o de caracterización que cubran sus reglas principales antes de considerarse listo para evaluación sumativa.

## Limitaciones de la versión inicial

- La extracción a `src/Service` no sigue todavía una convención uniforme para todos los procedimientos del subcircuito seleccionado.
- No existe aún una frontera arquitectónica explícita y repetible entre controlador, servicio de aplicación, reglas de negocio, objetos de transferencia de datos, objetos de valor y persistencia.
- La cobertura de pruebas unitarias existe solo como posibilidad o evidencia parcial; falta registrar casos, resultados y alcance.
- La cobertura de pruebas unitarias se concentra en autorización de certificación; no se identificó prueba directa para `CreateCertificacionService.php`.
- La batería de pruebas existente pasó con `rtk phpunit`: 151 pruebas y 235 aserciones en estado OK.
- La intervención todavía no demuestra escalabilidad del patrón hacia todos los objetos, controladores y procedimientos del módulo seleccionado.

## Decisión de rediseño

La siguiente versión del artefacto debe formalizar un método de refactorización incremental que indique: criterios para seleccionar procedimientos, reglas para extraer lógica desde controladores, distinción entre objetos de transferencia de datos y objetos de valor, ubicación de reglas de negocio, estrategia de pruebas unitarias y criterio de suficiencia antes de pasar a evaluación sumativa. Esta decisión mantiene el alcance de maestría: la contribución no será “se creó `src/Service`”, sino principios de diseño validados para convertir una separación parcial en una refactorización incremental coherente y verificable.

La regla de rediseño adoptada no parte de nuevas historias de usuario, sino de refactorizar el comportamiento existente del flujo de certificación. Cuando se trate de lógica heredada difícil de aislar, se usarán pruebas de caracterización previas a la modificación; cuando la lógica ya esté en un servicio, se exigirá prueba unitaria directa sobre sus reglas principales. La arquitectura guía será una arquitectura limpia mínima e incremental, no una migración completa hacia DDD ni arquitectura hexagonal, porque esa complejidad excedería el alcance viable y aumentaría el riesgo de intervención en SIGPP/SIPOA4.

El primer comportamiento elegido para caracterización es la restricción de subpartida. Esta regla se protegerá antes de moverla fuera del controlador, porque decide si la certificación requiere autorización, tipo de contrato o archivo adjunto. La prueba de caracterización debe capturar el comportamiento actual frente a tres escenarios mínimos: restricción activa específica por subpartida, gestión, administración y actividad; restricción activa general para subpartida, gestión y administración sin actividad asociada; y ausencia de restricción. La regla no se define por una subpartida fija, sino por una configuración del Departamento Financiero que puede cambiar en el tiempo.

La salida observable de esta primera prueba será la restricción resuelta, no sus efectos posteriores. Por tanto, la prueba verificará que el comportamiento actual devuelve la restricción específica cuando existe, la restricción general cuando no existe específica, y `null` o equivalente cuando no existe restricción aplicable. La activación de autorización, tipo de contrato o archivo adjunto quedará para pruebas posteriores porque son efectos derivados de la restricción ya resuelta.

El componente de destino para esta extracción será `RestriccionSubPartidaResolver`. Antes de mover la lógica desde `CreateCertificacionController.php`, se deberá crear una prueba de caracterización que fije el comportamiento actual. Después de la extracción, la misma prueba o su equivalente deberá pasar contra el nuevo componente, lo que permitirá documentar el rediseño como una iteración formativa y no como una reescritura informal.

La estrategia elegida precisa ese criterio: la prueba no se escribirá contra el controlador completo, sino directamente contra `RestriccionSubPartidaResolver`. Se acepta esta decisión porque el objetivo es preservar la regla de selección observada en el controlador original sin depender del ciclo HTTP, del formulario ni de Twig. En la tesis, esta evidencia deberá nombrarse con precisión como prueba de caracterización de la regla extraída, no como prueba funcional del controlador.
