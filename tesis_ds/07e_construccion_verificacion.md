# E7e. Construcción y verificación interna

> **Actualización al cierre de DS:** este registro distingue el antecedente de 2025 de la construcción/formalización del método y sus aplicaciones posteriores. M-R1 ya tiene evaluación P02 y el episodio de importe dispone de verificación final reproducida; fuentes y niveles en sus revisiones y E8/E9. Las notas inferiores que requieren evaluación posterior describen el momento de formalización y no justifican repetirla. No se convierten las pruebas temporales en sumativa ni se atribuye al método la producción histórica del antecedente; los cambios nuevos de cada episodio tienen su propio registro y asistencia declarada.

> **Construcción posterior del método:** se formaliza M-R1 con cuatro ajustes aprobados tras P01, sin modificar el código ni los registros del participante. Manual en `metodo_refactorizacion_incremental_mr1.md`, comparación y fuentes preservadas en `registro_redisenio_metodo_mr1.md`. La consistencia documental puede verificarse ahora, pero su aplicabilidad y efectividad requieren evaluación posterior. La batería de software P01 no se presenta como prueba de las nuevas instrucciones.

**Estado:** en curso. Este documento consolida el registro de construcción, la verificación técnica y el razonamiento de diseño de la instanciación. Sustituye al borrador del 18 de octubre, corrigiendo tres imprecisiones: la cronología de los commits (marzo de 2025, no de la tesis), el nombre «SIPOA4» (corregido a SIGPP) y la expresión «arquitectura limpia mínima» (corregida a frontera de aplicación incremental).

## 1. Cronología y alcance honesto

La separación parcial hacia `src/Service` es un **antecedente técnico de marzo de 2025**, anterior al encuadre de la tesis (septiembre de 2026). No se presenta como una construcción ejecutada durante el estudio. Lo que la tesis aporta sobre ese antecedente es su **identificación y evaluación formativa**: al encuadrar el problema, se localizó la separación, se reprodujeron sus pruebas y se detectaron sus inconsistencias, lo que motivó el rediseño del método.

El artefacto de la tesis es el método, no el código. La verificación que sigue cubre dos planos: la instanciación parcial heredada, verificada técnicamente, y la coherencia del método formalizado en E7c. No se rehace la construcción; se documenta lo que existe y se declara su grado de verificación.

## 2. Registro de construcción

| Componente | Naturaleza | Responsabilidad | Estado |
|:--|:--|:--|:--|
| `CreateCertificacionService` | Servicio de aplicación | Coordinar validación, creación, persistencia, seguimiento y autorización | Existente, verificado con dobles |
| `CreateCertificacionInput` | Objeto de transferencia de datos | Transportar entrada del formulario al servicio | Existente; mezcla de referencia a formulario detectada |
| `CreateCertificacionAutorizacionService` | Servicio específico | Crear autorización cuando corresponde | Existente, con prueba directa |
| `RestriccionSubPartidaResolver` | Regla focalizada | Resolver la restricción aplicable | Existente; búsqueda específica y alternativa general |
| Archivos de prueba | Verificación | Caracterización y prueba directa | Cinco archivos, sin seguimiento al 18 de octubre |

**Herramientas y entorno:** Symfony 4.4, Doctrine, PHP 7.4.29, PHPUnit 9.6.15, ejecución en contenedor Docker. La referencia de la rama de tesis es `feature/propuesta-tesis`, revisión `7c0bca08`.

**Commits del antecedente (marzo de 2025):** `815ce6c0` («Dev»), `6e333e27` («Adición de pruebas unitarias»), `9d4af430` («Separación a servicios creacion de certificacion»). Se citan como antecedente técnico, no como evidencia de construcción de la tesis.

## 3. Verificación técnica interna

| Comprobación | Comando | Resultado |
|:--|:--|:--|
| Batería completa | `make test` | `OK (188 tests, 540 assertions)`, PHPUnit 9.6.15 |
| Directorio de certificación | `vendor/bin/phpunit tests/Certificacion` | `OK (37 tests, 305 assertions)` |
| Versión de PHP | `php -v` | PHP 7.4.29 |
| Verificación de formato | `git diff --check` | Sin errores |

La prueba directa del servicio principal invoca `create()` con dobles y verifica resultados, validaciones previas y orden de efectos. Esta evidencia corrige la afirmación anterior de ausencia de prueba directa: existe `CreateCertificacionServiceTest.php`, aunque no prueba base de datos real, archivos ni respuesta HTTP. Los cinco archivos de prueba nuevos cubren selección específica/general/ausente de la restricción, propagación de excepciones, sustitución de restricción, delegación y creación bajo condiciones de contrato, archivo y autorización.

## 4. Razonamiento de diseño (design rationale)

La decisión de extraer la restricción de subpartida respondió a un motivo concreto: es una regla de negocio que decide autorización, tipo de contrato y archivo adjunto, y estaba acoplada al controlador. No se extrajo por tamaño de archivo ni por preferencia estética.

**Problema detectado:** la extracción inicial mezcló objetos de valor con objetos de transferencia de datos, y el servicio principal quedó sin prueba directa identificada en un primer momento. Esto reveló que la separación ad hoc no produce por sí misma una arquitectura coherente.

**Solución de rediseño:** caracterizar el comportamiento antes de mover; exigir prueba directa sobre los servicios principales; y fijar un destino de frontera incremental en lugar de una migración total. La autoridad de la regla temporal se fija en el servidor, con la interfaz como representación, para evitar definiciones divergentes.

**Cambio pendiente de distinguir:** la decisión temporal no distingue el límite mensual 8/9 en el punto comprobado, y la consulta de habilitados ocurre después de la creación. Estos hallazgos son del diagnóstico (E6), no defectos que se hayan corregido; la instanciación no los resuelve todavía.

## 5. Verificación de la decisión temporal (enlace con E6)

La instanciación se verificó también sobre la decisión temporal mediante comprobaciones aisladas, registradas en E6: O01–O06 de pantalla, M08/M09 de cierre mensual, O06 de servidor, interacciones del servicio y ensayo bisiesto B01/B02. Estos ensayos caracterizan el comportamiento actual y localizan la brecha; no son una corrección ni una evaluación sumativa. Su detalle, comandos y salidas están en `comprobacion_ordinaria_pantalla_e6.md`, `comprobacion_cierre_mensual_e6.md`, `comprobacion_o06_servidor_e6.md`, `comprobacion_interacciones_fechas_gestion_e6.md` y `bitacora_i03_cierre_bisiesto_e6.md`.

## 6. Suficiencia para la evaluación

El artefacto cumple la condición de E7e en el alcance del producto mínimo viable: la instanciación parcial está construida y verificada técnicamente, el método está formalizado, y los cambios están documentados con su razón. Lo que no se ha construido —la ampliación extraordinaria de I04, la corrección del límite 8/9, la lectura previa de configuración— se declara como capacidad futura, no como resultado verificado. El artefacto queda listo para la evaluación formativa y sumativa sobre la evidencia existente.

## 7. Gate de E7e

El gate exige: artefacto construido y verificado, evidencia de verificación, cambios documentados con su razón, y artefacto listo para la evaluación formativa. Las secciones anteriores proponen ese cumplimiento. Corresponde al tesista validar o corregir, en particular si la cronología del antecedente (2025) y la distinción entre instanciación heredada y verificación de la tesis reflejan con fidelidad lo ocurrido.

**Cierre, 4 de noviembre de 2026:** el tesista valida la cronología —antecedente de marzo de 2025 evaluado formativamente desde octubre de 2026—. El gate de E7e se cumple: la instanciación parcial está construida y verificada, hay evidencia de verificación, los cambios están documentados con su razón y el artefacto queda listo para la evaluación formativa.
