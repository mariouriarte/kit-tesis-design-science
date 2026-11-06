# Revisión de la aplicación controlada P01

**Corte del registro:** sesión declarada del 5 de noviembre de 2026; revisión realizada tras el aviso del tesista de que el participante terminó. **Estado actualizado:** productos recibidos, comprobación técnica final reproducida y ratificación documental del participante incorporada. Recepción del episodio cerrada; rediseño y evaluación posterior pendientes. No se cierra E8.

## 1. Dictamen

Existe una aplicación asistida del método documentada por un practicante externo a su formulación y al antecedente de extracción. Se localizaron cambios en los dos consumidores de certificación, un componente compartido nuevo, tres archivos de pruebas y dos documentos adicionales de registro. Las comprobaciones finales se reprodujeron satisfactoriamente en el alcance aislado, con la omisión inicial de PostgreSQL conservada.

La evidencia respalda factibilidad de esta aplicación con IA y conservación observada en los escenarios comprobados. No acredita aplicación humana autónoma, ahorro, integración completa de Symfony, transferibilidad comprobada, rediseño evaluado ni ciclo sumativo concluido. Los hallazgos son insumos para rediseñar el método y su material; no se presentan como principios ya validados.

## 2. Procedencia, condiciones y atribución

- **Copia:** `/home/mario/dev/sf_projects/sipoa4-evaluacion-p01-master`, rama `eval/metodo-restriccion-p01-master`, `HEAD` en `7ef29a4f438e5d2474d39b67f530cb940c922e76`, sin commits nuevos.
- **Fuentes primarias recibidas:** `docs/evaluacion-metodo-p01.md`, `docs/resultados-metodo-p01.md`, `docs/consultas-ia-p01.md`, código y pruebas de esa copia. Son registros elaborados con asistencia de IA, con explicaciones atribuidas al participante; no equivalen a observación directa ni a una transcripción íntegra de la conversación.
- **Consentimiento:** el formulario registra «Con consentimiento» para uso académico anonimizado. El original también contiene identificación nominal; no se reproducirá automáticamente en anexos públicos. Esa identificación no se interpreta como consentimiento para publicación nominal.
- **Exposición:** el participante declara no conocer la solución histórica; la bitácora declara no haberla consultado. No se auditaron todos los accesos ni se convierte esa declaración en cegamiento técnico.
- **Horario declarado:** apertura a las 21:05, lectura aproximadamente desde las 20:35 y cierre a las 23:16 del 05/11/2026, UTC−04:00. No se calculan esfuerzo humano activo ni ahorro a partir de esos horarios.
- **Autoría técnica declarada:** la IA redactó código de producción y pruebas, propuso alternativas y ayudó a interpretar instrucciones; el participante eligió, autorizó y aportó explicaciones. La ejecución final del revisor no verifica retrospectivamente cada decisión o intervención durante la sesión.

La comparación del formulario recibido con el objeto inicial `0d74d7df1d877f4fbe08402db3711003ec339c2f` muestra cambios en el registro de apertura/cierre, las tablas por paso/criterio y su cierre, no en las instrucciones anteriores. Esto aporta correspondencia documental con el material preparado, sin demostrar por sí solo qué vio el participante en cada momento.

## 3. Intervención recibida y comprobación técnica posterior

El componente `SeleccionarRestriccionSubpartidaService` recibe los repositorios de tarea y restricción. Su operación recarga la tarea por identificador y conserva el orden de consulta específica, alternativa general y retorno de ausencia. El controlador obtiene la restricción mediante ese componente; el servicio de creación reasigna a su propiedad el resultado de la selección, incluso cuando es ausencia. La revisión estática no identifica un cambio funcional intencional en ese algoritmo.

El diff de los archivos de producción ya existentes es de dos archivos, **+9/−72 líneas**. Además hay un archivo de producción nuevo de **54 líneas**; por tanto, +9/−72 no representa todo el código de producción añadido. Los tres archivos de prueba nuevos suman **769 líneas**. Son medidas de extensión, no costo económico, esfuerzo o mantenibilidad demostrada.

Se ejecutaron los comandos de PHPUnit y comprobación de sintaxis usando la misma imagen local y montajes de solo lectura de la preparación, sin red ni servicios institucionales. No se modificó el código ni los registros recibidos para hacer pasar una prueba.

| Comprobación posterior del revisor | Resultado reproducido |
|:--|:--|
| Batería completa con `--do-not-cache-result --no-coverage --verbose` | 183 pruebas, 341 aserciones, 1 omitida; sin fallos ni errores informados |
| `tests/Certificacion`, con `--testdox` y sin caché ni cobertura | 24 pruebas, 81 aserciones, satisfactorias |
| Sintaxis de los dos consumidores y el selector nuevo | Sin errores, PHP 7.4.29 |
| `git diff --check` de cambios seguidos | Sin errores informados |

La omitida continúa siendo `ResumenRepositoryPostgresTest::test_actual_query_keeps_one_latest_event_and_unmultiplied_totals`, por faltar la conexión aislada `RESUMEN_TEST_PG_DSN` y el requisito `psql`. No se cuenta como satisfactoria ni se habilita una base de datos para eliminarla. El aumento de 159 a 183 pruebas es la incorporación de 24 escenarios de la nueva batería, no una medida autosuficiente de mejora.

### Alcance de C01–C05

| Criterio | Respaldo final examinado | Límite |
|:--|:--|:--|
| C01. Específica | Selección y parámetros esperados; controlador, servicio y selector | Dobles; no SQL real |
| C02. General | Alternativa general en ausencia de específica; tres clases de prueba | Dobles; no todas las configuraciones institucionales |
| C03. Ausencia | Resultado nulo o ausencia observada en consumidores | Conjunto de entradas preparado |
| C04. Excepciones | Recarga, consulta específica y general; propagación y efectos observados pertinentes | Excepciones simuladas; no todos los fallos de infraestructura |
| C05. Estado anterior | Creaciones consecutivas del servicio y selecciones consecutivas del selector | No aplica al controlador sin estado de selección; alcance de misma instancia |

Las pruebas del controlador llaman a `new()` con un formulario no enviado y servicios sustituidos; las del servicio llaman a `create()` con repositorios y colaboradores sustituidos. Las pruebas directas del selector comprueban además ausencia de llamadas a `save` en dos repositorios en cuatro escenarios. No se demuestra ausencia universal de escrituras, persistencia real, atomicidad ni atención HTTP real.

El registro informa pruebas previas, fallos iniciales de datos auxiliares, mutaciones, coexistencia de implementaciones y tres ejecuciones aleatorias, dos de ellas con la misma semilla. En esta revisión no se reconstruyeron estados intermedios ni se repitieron las mutaciones; se distinguen esas afirmaciones registradas de la ejecución final reproducida. La existencia de la batería final no prueba por sí sola la cronología de TDD o caracterización previa.

## 4. Lectura por paso del método

| Paso | Evidencia recibida | Lectura de revisión |
|:--|:--|:--|
| P1 | Frontera, consumidores y explicación del participante | Aplicación asistida documentada; la localización inicial ya estaba proporcionada |
| P2 | Pruebas de ambos consumidores y relato de comprobación previa | Productos finales reproducibles; ejecución previa y mutaciones según el registro, no reconstruidas aquí |
| P3 | Alternativas y elección de conservar recarga con tarea como entrada | Elección asistida documentada; no corresponde añadir instante a este caso |
| P4 | Componente nuevo y registro de coexistencia y prueba inicial fallida | Producto existente; coexistencia temporal según registro |
| P5 | Pruebas directas y comprobaciones de efectos limitados | Verificación técnica final reproducida; interpretación de «rechazo» como excepción documentada |
| P6 | Cambios de consumidores y constructores | Retiro de duplicación comprobado estáticamente; conservación final en escenarios examinados |
| P7 | Batería y revisión local, sin integrar a otra rama ni compilar contenedor Symfony | Verificación parcial, no criterio de salida íntegramente acreditado |
| P8 | Bitácora, alternativas, diferencias y límites | Documentación existente; esfuerzo y evolución posterior no medidos, no sustituirlos por recuentos |

«Sin aclaración del autor» significa que no se documenta intervención del tesista durante la tarea. No significa que las instrucciones bastaron sin ayuda: la IA explicó criterios, propuso frontera y alternativas, escribió pruebas y código y precisó respuestas. La conclusión corresponde a **aplicación asistida por IA con autorregistro**, no a uso autónomo de una ficha autoexplicativa.

## 5. Hallazgos formativos y candidatos a rediseño

Estas propuestas todavía no están aprobadas como cambios del método. Se originan en el material recibido y no se atribuyen como solicitudes textuales del participante salvo donde el registro lo haga explícitamente.

| Hallazgo | Evidencia | Propuesta para discutir |
|:--|:--|:--|
| El participante necesitó explicación del significado de C01–C05. | Bitácora de IA, consulta previa | Añadir un ejemplo funcional breve y distinguir criterio técnico de paso del método; no atribuirlo automáticamente a defecto del método |
| La formulación de P3 contiene ejemplos temporales que no corresponden a toda decisión. | Autorregistro P3; el material ya advertía que el instante podía no aplicar | Expresar las entradas como datos y dependencias propios de la decisión, dejando el instante como ejemplo condicionado. No presentarlo como descubrimiento independiente no anticipado |
| «Rechazo» en P5 necesitó interpretación para una consulta sin aceptación/rechazo de dominio. | Autorregistro P5 y explicación de IA | Diferenciar resultados normales, ausencia y fallos, con efectos permitidos/prohibidos para cada caso |
| P7 se marcó completado pese a pendientes de integración. | Formulario, bitácora P7 y ausencia declarada de compilación | Separar comprobación local de integración en entorno objetivo y permitir estado parcial explícito; no reducir la exigencia después para declarar éxito |
| P8 mezcla documentación mínima con medición que no siempre está disponible. | Respuesta del participante y registro de tiempo no medido | Distinguir trazabilidad obligatoria de mediciones condicionadas al estudio; conservar «no medido» donde corresponda, sin convertirlo en cero |

Los problemas para preparar dobles del controlador o la ausencia de una herramienta de terminal no se imputan por defecto al método. La imposibilidad de compilar Symfony en esta sesión es un límite de la verificación y del entorno autorizado, no prueba de un defecto de inyección de dependencias. La opinión favorable sobre la secuencia es evidencia de percepción, no demostración de efectividad general.

## 6. Pendientes de cierre del episodio

1. **Ratificación del participante, resuelta en actualización posterior:** inicialmente la fila «Estado final» decía «Propuesto, a confirmar por el participante» y varios pasos tenían estado propuesto. Tras el aviso «ya lo hizo», se comprobó que el formulario dice «Ratificado por el participante» y que los estados P1–P7 del documento de resultados incorporan ratificación. No se repite la consulta ni la tarea; la cabecera editorial antigua no invalida esa incorporación. La confirmación documental no convierte los límites técnicos en comprobaciones realizadas.
2. **Alcance de P7:** mantenerlo parcialmente verificado mientras no se produzca la evidencia correspondiente. No ampliar ahora el entorno ni modificar la intervención para ocultar ese límite.
3. **Conservación y privacidad:** mantener los originales locales; preparar una copia anonimizada antes de cualquier publicación. El consentimiento para uso anonimizado no autoriza divulgar el nombre que aparece en el formulario. No se ha creado commit ni enviado material remoto en esta revisión.
4. **Rediseño y evaluación posterior:** discutir las propuestas de la sección 5 con el tesista, documentar la versión que apruebe y planificar su evaluación posterior. Esta sesión no sustituye un episodio sumativo ni demuestra automáticamente validez de los principios.

## 7. Identificación de los materiales recibidos

Se guardaron los contenidos recibidos como objetos Git locales, sin preparar el índice ni crear commits. La recuperación mediante `git show` es posible mientras existan esos objetos; no es archivo permanente y deberá consolidarse antes de limpiar copias u objetos. Los documentos nominales no se publican por este registro de identificadores.

| Archivo en la copia de evaluación | Objeto Git del contenido recibido |
|:--|:--|
| `docs/evaluacion-metodo-p01.md` | `f541af6ef66780ed81fda01ae52ac5854fcd199b` |
| `docs/consultas-ia-p01.md` | `bd45be0b40062843f171801fb9b3f8520e750587` |
| `docs/resultados-metodo-p01.md` | `935e26f09ad21333dd71f8a88d6988579d7da35d` |
| `src/Controller/poa/Certificacion/CreateCertificacionController.php` | `c6f5757400b01be2347f366e47e0b921edcea944` |
| `src/Service/Certificacion/CreateCertificacionService.php` | `85289b155ce9e4c0d0817498af8b0d7900c31477` |
| `src/Service/Certificacion/SeleccionarRestriccionSubpartidaService.php` | `8788aa7ed6e533b61836b116cc92c8975a70793c` |
| `tests/Certificacion/CreateCertificacionControllerRestriccionTest.php` | `7a35e6ba2e7fe58ba0c54145d94938ca5c68d833` |
| `tests/Certificacion/CreateCertificacionServiceRestriccionTest.php` | `bff5d3bbddc591dcef903213146a180015f57d59` |
| `tests/Certificacion/SeleccionarRestriccionSubpartidaServiceTest.php` | `d1f3eee9706aecc5c0d95960b0ecb6741c63d54a` |

No se modificaron esos materiales para redactar esta revisión. La reproducción final es evidencia nueva del revisor sobre la misma intervención, no una segunda aplicación independiente del método ni otro participante.

### Actualización: ratificación recibida

Se compararon los documentos actualizados con los objetos iniciales de esta tabla. `docs/evaluacion-metodo-p01.md` cambia la fila final a «Ratificado por el participante»; `docs/resultados-metodo-p01.md` sustituye estados propuestos por ratificados y especifica que el participante mantiene P7 como completado con pendientes. `docs/consultas-ia-p01.md` no cambió. No se atribuye una hora nueva de ratificación no informada.

Los nuevos objetos locales son `bccb197b5789fdf8801a8faf5219669251fab578` para el formulario y `ff4a264d0066458fad2524f853a5751dab2eeb37` para los resultados. Los seis identificadores de código y pruebas coinciden con los de la tabla, por lo que no se repitió la batería: la actualización es documental y se mantiene la evidencia técnica anterior con su fecha y alcance.

La clasificación del participante se conserva literalmente, pero el dictamen técnico sigue siendo **P7 parcialmente verificado**: «completado con pendientes» es su autorreporte, no evidencia de que se compiló el contenedor o se realizó integración. Queda cerrada la recepción y ratificación del episodio, no la integración ni el ciclo formativo completo con rediseño. El próximo compromiso es decidir con el tesista qué cambios del método se realizarán a partir de los hallazgos de la sección 5.
