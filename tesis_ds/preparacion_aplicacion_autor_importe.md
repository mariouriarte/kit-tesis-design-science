# Preparación de aplicación adicional por el autor: validación del importe

## Acuerdo y propósito

El tesista acepta examinar la validación del importe de certificación frente al disponible como aplicación adicional acotada del método. Informa que no dispone de otros participantes y que él puede realizarla, con tiempo limitado. Autoriza utilizar `/home/mario/dev/sf_projects/sipoa4`, una rama con prefijo `eval/`, Docker y `make test`. La autorización no equivale a protocolo completo ni a resultados obtenidos.

Se busca ampliar evidencia sobre puntos de comprobación de una decisión distinta de la selección de restricciones. La aplicación del autor no prueba independencia, transferencia a otros desarrolladores o sistemas, ahorro ni superioridad. No sustituye los indicadores temporales pendientes ni garantiza suficiencia de maestría.

## Inspección preparatoria

| Elemento | Resultado comprobado |
|:--|:--|
| Repositorio | La ruta indicada es la raíz Git del proyecto. |
| Referencia actual | `master`, `7ef29a4f`; un commit por delante de `origin/master`; estado local sin cambios informados por Git. |
| Regla candidata | `CreateCertificacionService::topeCertificacion()`: obtiene disponible desde la tarea y calcula cantidad por precio; rechaza total no positivo y exceso sobre disponible. Se invoca después de validar fecha y antes de consultar restricciones y crear la certificación. |
| Límite semántico | El mensaje de total no positivo dice «menor a 1», pero el predicado es `<= 0`. No reinterpretar el umbral como uno ni corregir mensaje, decimales o reglas monetarias dentro de una transformación conservadora sin decisión separada. |
| Docker | Contenedores activos `sigpp-app`, `sigpp-web`, `sigpp-docs` y `sigpp-postgres`. Aplicación en `/appdata/www` con montaje de la carpeta indicada. |
| Orden de pruebas | `make -n test` muestra `USERID=1000 docker exec --user 1000 sigpp-app vendor/bin/phpunit`. Es simulación de la orden, no ejecución satisfactoria de pruebas. |
| Configuración de PHPUnit | `phpunit.xml.dist` usa `vendor/autoload.php` y no fija entorno de pruebas en el bloque activo. No se infiere aislamiento de datos por usar PHPUnit. |
| Índice de código | CodeGraph informa fuente desactualizada respecto del disco; se lee el servicio actual. El índice remite a `tests/Certificacion/CreateCertificacionServiceTest.php`, inexistente en esta copia actual; no se cuentan sus pruebas históricas como disponibles. |
| P02 | La rama local `eval/metodo-mr1-p02` no se encuentra y no aparecen archivos `docs/*p02*` en esta copia. Esto no prueba pérdida global: falta localizar los originales conservados. La revisión P02 en el repositorio de tesis permanece disponible. |

## Actualización: otra PC y evidencia P02 localizada

El tesista aclara que trabaja en otra PC y que acaba de actualizar desde `origin`. La comprobación posterior localiza `origin/eval/metodo-mr1-p02` en `0ddd71740f4a09cdd0a832e87f407a61ac914a0c`. Su árbol contiene las tres guías/registros `docs/evaluacion-metodo-p02.md`, `docs/observacion-metodo-p02.md`, `docs/comprobaciones-p7i-p02.md` y la prueba `tests/Certificacion/CreateCertificacionServiceRestriccionTest.php`. Los commits localizados incluyen registro de sesión y materiales de evaluación. No se afirma inspección exhaustiva de todos los originales ni de los archivos no versionados de la otra PC; la ausencia inicial en master no demuestra pérdida.

Se crea la rama `eval/metodo-mr1-importe-autor` desde el master local `7ef29a4f`, con estado limpio. No se mezcla la solución P02 en el punto de partida ni se cambia su rama remota. No se ejecuta otro `pull`, no hay commit o publicación de la nueva rama y no se modifican código, configuración o datos. La referencia P02 sigue accesible para consulta sin repetir su actividad.

## Escenarios aceptados antes de transformar

El tesista responde «aceptado» al conjunto A01–A05 y a la condición de rechazo previo a efectos. La aceptación es anterior a la transformación de esta actividad, no retrospectiva sobre la implementación inicial. Se conserva el conjunto sin agregar medición de esfuerzo o criterios de integración por inferencia.

Se propone utilizar disponible ficticio de 100 y variar únicamente el total calculado, con fecha válida y las demás condiciones pertinentes fijadas. Los valores describen comportamiento observado en el predicado actual, no aprobación funcional institucional nueva. El conjunto mínimo deberá examinarse antes y después de la transformación mediante los consumidores pertinentes; no se impone una extracción o clase concreta.

| Caso propuesto | Total | Expectativa de la validación de importe |
|:--|--:|:--|
| A01 | 50 | Permite continuar: positivo e inferior al disponible. |
| A02 | 100 | Permite continuar: igualdad con el disponible. |
| A03 | 101 | Rechaza por exceso. |
| A04 | 0 | Rechaza por total no positivo. |
| A05 | -1 | Rechaza por total no positivo. |

En A03–A05 se propone comprobar que el rechazo precede a las llamadas de guardado de certificación, seguimiento, autorización y carga de adjuntos, distinguiendo dobles de efectos reales. En A01–A02 la expectativa es que esta validación no impida continuar; no se presupone que cualquier entrada restante permita crear una certificación. Si se compara a través de `create()`, las condiciones restantes deben prepararse de forma explícita y ficticia.

No se reclama equivalencia universal con cinco casos ni se define una medición de ahorro. El alcance de integración y sus autorizaciones siguen pendientes. Se crean en la rama preparada `docs/aplicacion-metodo-importe-autor.md` y `docs/registro-metodo-importe-autor.md`, sin solución implementada o resultados simulados. Identifican M-R1 con suplemento operativo de registro progresivo posterior a P02, sin atribuirlo a la versión recibida por P02. El registro declara la actividad no iniciada.

Para P7 se propone validar configuración del contenedor y conexiones del incremento, pruebas del consumidor con dobles y batería `make test`, sin escrituras reales, HTTP completo o concurrencia. La propuesta no equivale a integración con persistencia real ni está todavía aceptada. Su suficiencia se revisará frente al diseño elegido; no se supondrá probada por compilar configuración.

## P7 aceptado y batería inicial comprobada

El tesista responde «acepto» al alcance de configuración/conexiones del incremento, pruebas del consumidor con dobles y `make test`, sin escrituras reales en base de datos, HTTP completo o concurrencia. No se exige otra aceptación del mismo alcance. El material operativo identifica el suplemento de registro progresivo posterior a P02; no cambia retrospectivamente aquella versión.

Antes de ejecutar, la asesoría revisa mecanismos de conexión en tests y la prueba `ResumenRepositoryPostgresTest`: requiere `RESUMEN_TEST_PG_DSN` y se omite si falta. Se comprueba que no está configurada en el contenedor, sin imprimir credenciales. La búsqueda no identifica otros mecanismos directos de conexión/arranque de núcleo en las pruebas, pero no constituye auditoría exhaustiva o aislamiento de red.

La asesoría ejecuta `make test` en la rama preparada: **159 pruebas, 260 aserciones, 1 omitida**, sin fallos o errores informados; PHP 7.4.29 y PHPUnit 9.6.15. La omisión no es éxito ni evidencia de persistencia real. Git conserva referencia `7ef29a4f438e5d2474d39b67f530cb940c922e76` y ninguna diferencia preparada o sin preparar en `src`, `tests`, `Makefile` o `phpunit.xml.dist`; solo las dos guías nuevas sin commit. Resultado registrado en docs, sin atribuirlo al tesista ni a los cinco escenarios aún no ejecutados.

La preparación permite al tesista comenzar por P1, registrar su delimitación y preparar la caracterización P2 antes de transformar. No se ha ejecutado la tarea por él, elegido una clase nueva ni acreditado A01–A05. P7 debe justificarse frente al diseño que elija; si este requiere comprobaciones adicionales, se acuerdan antes de ejecutarlas. No se declara aislamiento de datos por usar rama/Docker ni se configura conexión real para la prueba omitida.

## Pendientes iniciales y resolución

1. Evidencia P02 localizada en la referencia remota indicada; no repetir la actividad. La disponibilidad de archivos adicionales no versionados en la otra PC no se certifica por inspeccionar el árbol remoto.
2. Rama creada desde `7ef29a4f`: `eval/metodo-mr1-importe-autor`.
3. Fijar escenarios y expectativas antes de transformar, incluida admisión en el límite y rechazo antes de efectos. Separar conservación de cualquier corrección; no imponer clase nueva o extracción antes de que el tesista delimite y justifique el incremento.
4. Acordar alcance local e integración, datos ficticios y límites de ejecución; una rama no aísla la base. No autorizar escrituras por el solo uso de Docker o `make test`.
5. Registrar las decisiones durante los pasos y consolidar en P8. Si se incorpora la recomendación posterior a P02, identificar el suplemento y su fecha antes de iniciar; no atribuirlo a la versión M-R1 evaluada por P02.

Se ha creado y seleccionado la nueva rama y ejecutado la batería inicial en las condiciones anteriores; no se ha modificado código funcional, configuración o datos ni iniciado la transformación. La preparación no demuestra que la regla requiera una extracción. Delimitación, caracterización de A01–A05, intervención, verificación y análisis de resultados son trabajo pendiente del autor.
