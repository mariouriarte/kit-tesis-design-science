# Preparación de la aplicación controlada P01

**Fecha:** 5 de noviembre de 2026. **Estado:** materiales y comprobación técnica inicial preparados; sin aplicación del participante ni consentimiento recibido. El tesista solicitó que el compañero pueda realizar la actividad ahora, en esta máquina, sin su intervención, con documento en `docs/` de SIGPP.

## 0. Preparación vigente: base master aceptada

El tesista pregunta si convenía partir de `master` y responde «ok» a cambiar la preparación manteniendo la copia histórica. La ruta de inicio vigente es **`/home/mario/dev/sf_projects/sipoa4-evaluacion-p01-master`**, rama **`eval/metodo-restriccion-p01-master`**, fijada en **`7ef29a4f438e5d2474d39b67f530cb940c922e76`**. El documento que debe abrir el participante es **`docs/evaluacion-metodo-p01.md` de esta nueva copia**. La copia histórica sin sufijo `-master` se conserva como antecedente y no se utilizará para la sesión.

Se comprobó que AGENTS.md, Makefile, los archivos de dependencias y PHPUnit, y las dos clases consumidoras no difieren respecto del padre histórico utilizado inicialmente. La base master incorpora otras correcciones y pruebas de informes CSV; por ello se repitió la batería, sin reutilizar el resultado 151/235 de la otra base.

| Comprobación de la nueva base | Resultado real del preparador |
|:--|:--|
| PHP | 7.4.29 |
| PHPUnit | 9.6.15 |
| Batería completa | 159 pruebas, 260 aserciones, 1 omitida; sin fallos ni errores informados |
| Omisión identificada mediante ejecución con `--verbose` | `App\Tests\Modificacion\ResumenCsv\ResumenRepositoryPostgresTest::test_actual_query_keeps_one_latest_event_and_unmultiplied_totals` |
| Motivo de omisión | Falta conexión aislada `RESUMEN_TEST_PG_DSN` y requisito `psql`; no se habilita PostgreSQL para esta tarea |
| Diferencias finales de código y pruebas respecto del punto de partida | Ninguna en `src`, `tests`, `composer.json`, `composer.lock` ni `phpunit.xml.dist` |

La prueba omitida no se cuenta como satisfactoria ni se oculta. Corresponde a otra función y no se conectará una base de datos para eliminar esa omisión. Si cambia la omisión durante la sesión, se conservará y explicará la diferencia.

El documento operativo se adaptó a las nuevas ruta, rama y referencia; conserva consigna, C01–C05, instrucciones P1–P8 y autorregistro, sin solución histórica. SHA-256 inicial **`0bc94c0f5fa2d3c02f23f05377d168054a958b2f3275ae12a3a95ba60aa47db7`**; objeto Git local de su contenido **`0d74d7df1d877f4fbe08402db3711003ec339c2f`**, sin commit ni publicación. También se verificó la función incluida con `phpunit --version`. El archivo está inicialmente sin seguimiento; el objeto local no constituye archivo permanente y debe conservarse con los resultados antes de cualquier limpieza.

Se mantiene la modalidad solicitada: aplicación con autorregistro, IA documentada y tesista ausente. El participante deberá consentir y completar sus comprobaciones iniciales antes de la tarea. No hay resultados suyos todavía; la preparación no cierra E8. Las secciones siguientes conservan el proceso inicial para trazabilidad y no sustituyen esta ruta de inicio vigente.

## 1. Copia y rama históricas preparadas inicialmente

> **Revisión del punto de partida solicitada por el tesista:** se comprobó después de la preparación que `master` local, en `7ef29a4f438e5d2474d39b67f530cb940c922e76`, tampoco contiene el resolvedor ni la prueba histórica de caracterización en las rutas examinadas. El controlador y servicio de certificación no presentan diferencias respecto de `5313c0e1`, y tampoco difieren `composer.json`, `composer.lock` ni `phpunit.xml.dist`. Por tanto, `master` es una alternativa válida para preparar la misma tarea; no era necesario excluirlo para evitar entregar la solución. Las diferencias entre ambas referencias comprenden ocho archivos de informes/resumen CSV y sus pruebas, ajenos a las dos clases examinadas; no se afirma equivalencia de toda la aplicación. La copia histórica permanece intacta mientras se decide si se cambia la base. Si se elige `master`, habrá que preparar y verificar esa base, actualizar instrucciones, referencias y resultado inicial, y no reutilizar 151/235 como si se hubiera medido allí.

| Elemento | Valor comprobado |
|:--|:--|
| Copia habitual | `/home/mario/dev/sf_projects/sipoa4` |
| Referencia habitual al preparar | `feature/propuesta-tesis`, revisión abreviada `59ffe007`, sin cambios informados por Git |
| Copia de evaluación | `/home/mario/dev/sf_projects/sipoa4-evaluacion-p01` |
| Rama de evaluación | `eval/metodo-restriccion-p01` |
| Punto de partida | `5313c0e150859d86dd9d82b1df21f719d2242076`, anterior a la extracción |
| Documento del participante | `docs/evaluacion-metodo-p01.md`, dentro de la copia de evaluación |

Se creó una copia vinculada de Git, no se cambió de rama la copia habitual. No se modificó código de la tarea, no se trasladó la solución histórica y no se creó ningún commit ni se publicó la rama. El documento está inicialmente sin seguimiento; se conservará su versión inicial antes de recoger las modificaciones del participante.

**Identificación del documento inicial entregable:** SHA-256 `51d2e5413f9058b839d69ebe54766a3b5fa3405441ba7aa2b0642470f5edbfa2`. Se guardó también su contenido como objeto Git local `89ea24eb59abe2c5ffec9049382721424f6c7889`, sin crear commit ni prepararlo en el índice. Permite recuperar el texto inicial mediante `git show` mientras el objeto exista; no constituye archivo permanente ni publicación y debe conservarse con los resultados antes de limpiar la copia o los objetos de Git.

La copia comparte el historial con SIGPP. No es un cegamiento técnico ni impide consultar otras ramas: las instrucciones restringen ese acceso y exigen registrarlo si ocurre. La exposición no se dará por controlada exclusivamente por esa instrucción.

## 2. Verificación técnica del preparador

Se comprobó mediante Git que `composer.json`, `composer.lock` y `phpunit.xml.dist` no difieren entre la referencia inicial y la copia habitual. Se reutilizan dependencias instaladas de esta última mediante montaje de solo lectura; esto no reconstruye completamente el entorno histórico. No se instalaron ni actualizaron dependencias.

La imagen local utilizada es `sha256:fbf938bf6ca2b810ad22ac4094dc5f17f0ddd152fd603a23f77047d198e9793c`. El contenedor es efímero, sin red, con raíz y montajes de código y dependencias de solo lectura, sin capacidades Linux y sin elevación de privilegios. No se inició la aplicación web ni una base de datos; no se intervino el contenedor habitual.

| Comprobación | Resultado |
|:--|:--|
| Intérprete | PHP 7.4.29 |
| Herramienta de pruebas | PHPUnit 9.6.15 |
| Batería inicial | `OK (151 tests, 235 assertions)` |

La función de terminal incluida en el documento se verificó posteriormente con `--version` y la misma batería: nuevamente 151 pruebas/235 aserciones satisfactorias. Son comprobaciones repetidas de preparación, no muestras independientes ni resultados del participante. La comprobación final de diferencias no identificó cambios respecto de `5313c0e1` en `src`, `tests`, `composer.json`, `composer.lock` o `phpunit.xml.dist`; la copia habitual siguió limpia en `59ffe007`.

**Incidencia de preparación:** el primer intento falló antes de arrancar PHP porque no existía el directorio `vendor/` en la copia y Docker no podía crear el punto de montaje bajo la raíz de solo lectura. Se creó un directorio vacío como punto de montaje y se repitió la comprobación satisfactoriamente. No se copió el contenido de las dependencias ni se cambió el código para corregir el fallo.

Estos resultados pertenecen al preparador, no al participante ni al resultado de la tarea. Se le solicita una comprobación inicial propia. El comando habitual `make test` no debe usarse en esta copia porque ejecuta un contenedor de nombre fijo asociado a la copia habitual; el documento proporciona el comando aislado comprobado.

## 3. Material y fidelidad al método

Se preparó un único documento operativo con inicio seguro, consentimiento, contexto, historia de mantenimiento, alcance, C01–C05, tabla de instrucciones generales P1–P8, asistencia permitida, ejecución técnica y formulario de autorregistro. No se incluye el nombre del resolvedor histórico ni las pruebas resueltas. No se entregan E7c/E7f completos.

La tabla P1–P8 reproduce las columnas operativas del diseño vigente, sin la columna de referencias internas ni la arquitectura del caso. Se explicita que los ejemplos temporales de P3 no requieren incorporar fechas y que P7 no autoriza integrar en ramas habituales o conectar servicios reales. Estas son aclaraciones de preparación visibles para el participante, no hallazgos de la sesión ni rediseño derivado de su evaluación. La ausencia de condición de entrada en P8 se expresa verbalmente sin añadir un requisito.

Se conservan las instrucciones generales potencialmente problemáticas para que el participante pueda registrarlas, incluida la exigencia de coexistencia o la no aplicabilidad de un paso. No se predefine el resolvedor como respuesta correcta. No se promete completar los ocho pasos ni obtener una valoración favorable.

## 4. Cambio de modalidad y consecuencias

Por solicitud del tesista, no habrá intervención suya durante la aplicación. El compañero será **practicante externo con autorregistro**, no observador independiente de su propio desempeño. Las dudas y ayudas de IA se recogerán por escrito durante la tarea y el tesista analizará los productos después; no se declarará observación directa de conductas no presenciadas.

Esta modalidad reduce la intervención inmediata del constructor, pero limita la detección de dudas no registradas y depende de la calidad del autorregistro. La ausencia de preguntas no demuestra comprensión. La inspección posterior de productos y la explicación del participante permiten contrastar parcialmente sus afirmaciones; no sustituyen una revisión técnica independiente de su propia implementación.

La categoría «con aclaración del autor» solo se utilizará si realmente recibe tal ayuda; las respuestas de IA se registrarán como IA, no como aclaraciones del autor. No se exige grabación ni se inventará un observador. No se medirá I03 ni ahorro: las horas de inicio y cierre delimitan la sesión, sin equivaler a esfuerzo humano activo.

## 5. Condiciones de inicio y recogida

El participante puede abrir el documento y preparar el inicio. Antes de ejecutar la tarea debe registrar consentimiento voluntario para uso académico anonimizado, exposición previa y comprobaciones iniciales. Si no acepta, no continúa; si detecta un entorno o referencia distintos, registra el bloqueo. No se presume consentimiento por disponibilidad o acceso al equipo.

Al finalizar se recogerán los documentos, cambios y pruebas, junto con errores, ayudas y limitaciones. No se exige un commit ni se autoriza publicar. El material de trabajo deberá conservarse antes de limpiar o reutilizar la copia. La ejecución, el rediseño y el episodio sumativo siguen sin realizarse; la preparación no cierra E8 ni valida principios.
