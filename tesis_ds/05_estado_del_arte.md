# E5. Estado del arte sobre métodos y artefactos de refactorización

> **Estado vigente: E5 cerrada el 28 de octubre de 2026 como revisión comparativa focalizada y delimitación de la adaptación.** La justificación propia del tesista y sus límites se registran en la sección 9. Las notas de apertura y los pendientes fechados anteriores conservan la cronología. No se declara búsqueda exhaustiva, originalidad ya demostrada, superioridad del método ni resultados de evaluación; corresponde iniciar E6 para obtener línea base y criterios prospectivos.

**Estado:** iniciado el 28 de octubre de 2026, después del cierre documentado de E4, y ampliado mediante búsqueda ejecutada y comparación C01–C08. El registro `comparacion_antecedentes_e5_2026-10-28.md` añade dos artículos recientes de texto completo accesible, una técnica de práctica y un antecedente industrial próximo con resumen primario pero PDF bloqueado. **No se declara insuficiencia de las soluciones, novedad demostrada ni cierre de E5.** No se probaron herramientas ni modificó SIGPP.

**Actualización posterior:** el tesista aportó el texto completo de Girjoaba y Capiluppi; el bloqueo de acceso al contenido está resuelto. Su manuscrito presenta datos editoriales provisionales, por lo que se distingue de la referencia final verificada. Extracción y crítica en `lectura_girjoaba_capiluppi_2026-10-28.md`; las notas sobre 403 describen el intento inicial, no el estado vigente.

## 1. Objeto de la comparación

El artefacto propuesto es un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas, aplicado en ejecución POA de SIGPP. Esta revisión compara **métodos y artefactos que ayudan a decidir y verificar la transformación**, no marcos web como si fueran soluciones rivales ni manuales administrativos como si fueran métodos de arquitectura. El objetivo no es encontrar una arquitectura «limpia» universal, sino establecer qué conocimiento ya existe, qué cubre y qué adaptación necesita el caso. La reutilización de prácticas conocidas no se convierte por sí misma en contribución original.

**Pregunta de revisión:** ¿qué procedimientos, métodos o herramientas existentes permiten seleccionar, ejecutar y verificar incrementos arquitectónicos en aplicaciones heredadas, y qué evidencia ofrecen para mejorar modificabilidad y testabilidad sin reescritura completa? Como subpregunta de contraste se examina cómo tratan reglas repartidas entre presentación, configuración y coordinación con efectos. No se presupone que los antecedentes carezcan de ese tratamiento: se debe localizar evidencia y distinguir ausencia de cobertura, falta de evaluación y falta de acceso al texto. Este protocolo es focalizado, no una revisión sistemática exhaustiva.

## 2. Protocolo de búsqueda y selección

### Alcance previsto

Se priorizará el intervalo **28 de octubre de 2021–28 de octubre de 2026**, incorporando obras fundacionales y métodos anteriores cuando constituyan comparadores necesarios. Las tres lecturas recientes de E4 corresponden a la búsqueda del 26 de octubre y conservarán ese corte; no se alteran sus fechas retroactivamente. La unidad de comparación es el método o artefacto, distinguiendo sus versiones y publicaciones para no contarlas como soluciones independientes. Las fuentes inaccesibles permanecen como pendientes de contenido, no como prueba de insuficiencia.

| Elemento | Regla propuesta para la revisión |
|:--|:--|
| Descubrimiento. | Consultar Crossref y rastrear bibliografía de las fuentes pertinentes; utilizar OpenAlex para localizar versiones accesibles. Registrar fecha, consulta, filtros y resultados examinados. |
| Evidencia sustantiva. | Usar texto primario editorial o manuscrito de autor identificado; diferenciar acceso al resumen, acceso al texto y lectura focalizada. |
| Inclusión. | Método, procedimiento, técnica o herramienta con pasos o mecanismo explícito de transformación/verificación y relación con aplicaciones existentes, modificabilidad o testabilidad. Incluir resultados desfavorables y límites que contradigan la propuesta. |
| Exclusión. | Recomendaciones sin procedimiento o evidencia pertinente; propuestas dedicadas exclusivamente a reescritura total sin trayectoria incremental aplicable; trabajos sobre otros objetivos sin conexión con la decisión estudiada. No excluir por usar DDD, puertos/adaptadores o microservicios si describen una intervención incremental comparable. |
| Artefactos accesibles. | Cuando se identifique una herramienta pertinente, verificar documentación y disponibilidad; distinguir descripción publicada de uso o reproducción efectiva. No exigir un programa de software si el comparador es un método. |
| Extracción. | Registrar objetivo, unidad de intervención, pasos/entradas/salidas, supuestos, preservación funcional, verificaciones, contexto de evaluación, resultados, límites y recursos para reproducir. |
| Comparación. | Aplicar las dimensiones de la sección 3 a todos los antecedentes, declarando qué es evidencia y qué es inferencia del estudio. No convertir «no localizado en los pasajes leídos» en «el método no lo contempla». |

### Cadenas base y adaptaciones registradas

```text
("legacy" OR "existing software") AND
("incremental refactoring" OR "architectural refactoring") AND
("testability" OR "modifiability" OR "behavior preservation")

("framework" OR "MVC") AND
("refactoring method" OR "incremental architecture") AND
("business logic" OR "service layer")
```

Las expresiones anteriores se conservan como cadenas base: no se ejecutaron literalmente con esa sintaxis booleana. El registro de comparación del 28 de octubre detalla cuatro adaptaciones por relevancia de título en Crossref, tres para revistas y una para actas, con filtros, cantidades y resultados examinados. La búsqueda de E4 no se rebautiza como búsqueda sistemática de E5 ni se acredita cobertura exhaustiva. La selección final de comparadores responde a la clase de problema, no únicamente a los documentos disponibles.

## 3. Dimensiones de comparación fijadas para la revisión

| ID | Dimensión | Qué debe extraerse y por qué importa |
|:--|:--|:--|
| C01 | Selección y delimitación del incremento. | Cómo identifica una necesidad de cambio y su unidad de intervención; evita elegir solo por tamaño o carpeta. |
| C02 | Conservación y cambio funcional. | Cómo distingue preservación de comportamiento, correcciones y capacidades nuevas; permite atribuir resultados. |
| C03 | Decisiones, contexto y dependencias. | Cómo separa reglas, lectura de datos, transporte y efectos; cómo justifica dependencias que conserva. |
| C04 | Protección y conexión. | Qué pruebas, análisis o revisiones exige y cómo comprueba consumidores, no solo componentes aislados. |
| C05 | Aplicabilidad y restricciones. | Qué tecnología, acceso, competencias, datos y costos requiere; qué presupone del sistema existente. |
| C06 | Modificabilidad y testabilidad. | Cómo define y mide ambas; qué parte es métrica estructural, esfuerzo, efectividad, percepción o efecto observado. |
| C07 | Iteración y reproducibilidad. | Qué versiones, decisiones, hallazgos y rediseños documenta; qué necesitaría otro investigador para aplicarlo. |
| C08 | Evidencia y condiciones de transferencia. | Contexto, muestra, independencia de evaluación y amenazas; evita trasladar hallazgos de Java a PHP o de clase a subcircuito sin justificación. |

Estas son dimensiones de revisión de antecedentes, no métricas ni umbrales de éxito de SIGPP. La operacionalización prospectiva corresponde a E6 y los requisitos del artefacto a E7b. No se seleccionará un comparador desfavorable para garantizar superioridad. Si los antecedentes ya resuelven adecuadamente la necesidad, deberá revisarse la contribución reclamada, no inventar una carencia.

## 4. Comparación inicial: antecedentes ya consultados

| Antecedente y tipología | Cobertura respaldada en las lecturas | Relación con la propuesta | Comprobación pendiente |
|:--|:--|:--|:--|
| Procedimiento de cambio en código heredado de Feathers (2004): procedimiento práctico. | Identificación de cambio y puntos de prueba, ruptura de dependencias, caracterización y comprobación de conexión; pp. 18–20, 186–190, 194–195 y 249–251. | Comparador directo del cambio seguro. Sus pasos ya cubren parte del método pretendido: no son novedad por aplicarlos en SIGPP. | Comparar C01–C08 y localizar qué adaptaciones requiere realmente la combinación presentación/configuración/efectos. No se ha demostrado insuficiencia del procedimiento. |
| ADD de Bass et al. (2021): método de diseño arquitectónico. | Diseño por atributos de calidad, refinamiento de elementos existentes, iteraciones, decisiones y análisis; secs. 3.3 y 20.1–20.2. | Comparador del razonamiento y refinamiento arquitectónico; no se lo trata como reescritura total ni rival idéntico de un procedimiento de caracterización. | Precisar cómo se complementaría con protección de comportamiento y evidencia del incremento. No se declara que ADD sea incapaz de abordar el caso. |
| Propuesta de Zakeri-Nasrabadi y Parsa (2022): modelo de testabilidad y aplicación de herramientas de transformación. | Medición de esfuerzo/efectividad bajo condiciones explícitas y refactorización automatizada de 42 clases Java; manuscrito versión 2, secs. 3.1, 3.3.1, 4.5 y 5. | Comparador **parcial** de medición/transformación para testabilidad, no un método equivalente de refactorización del flujo MVC. Evidencia técnica contextual útil sin transferir predictor o porcentajes a PHP. | Examinar C04–C08 y compatibilidad real de artefactos; no se ejecutaron herramientas ni se reprodujo el estudio. |
| Fischer et al. (2025): patrones y proceso de refactorización arquitectónica verificados en modelos. | SysMLv2 → teorías de Isabelle → obligaciones y pruebas; transformaciones con componentes, canales e invariantes; demostración de equivalencia de un modelo de comunicación cifrada. | Comparador de preservación y pasos arquitectónicos, no prueba de comportamiento del código PHP. | Estimar formalización/correspondencia con implementación y costo; no adoptar ausencia de pruebas de integración fuera de sus supuestos. |
| Orosz y Kozsik (2026): LADY y generación de código C#. | Reespecificación de herramienta industrial; pruebas de sistema, revisión de arquitectos propietarios y métricas CK; secs. 3.1, 4 y 5. | Mecanismo alternativo de transformación con condiciones tecnológicas y cambio de firmas propios. | No confundir revisión de propietarios con independencia. Refactorizar unidades con componentes externos es trabajo futuro del artículo; adaptación a SIGPP no realizada. |
| Fowler (2014): técnica de ramificación mediante abstracción. | Abstracción, migración de clientes, coexistencia de implementaciones y sustitución gradual, con pruebas y continuidad de construcción. | Comparador directo de transición gradual; introduce una idea ya conocida, no novedad propia. | Examinar necesidad/costo del mecanismo en el incremento y sus consumidores; no imponer reemplazo de ORM o coexistencia de reglas contradictorias. |
| Girjoaba y Capiluppi (2024): ciclo iterativo de refactorización industrial; **contenido recibido del tesista**. | Siete pasos con investigación de usos, migración antes de retiro y comprobaciones de comportamiento/dependencias/integración; seis interfaces C++ de un autor, investigación-acción. | Antecedente directo de formalización incremental y repetible; aporta puntos de comparación de conexión y separación de cambios. | Comparar adaptación concreta a SIGPP; no inferir causalidad de muestra pequeña y aprendizaje. El adjunto tiene plantilla/DOI provisionales: correspondencia exacta con versión editorial por verificar, no falta de contenido. |

La tabla reúne siete antecedentes de propósitos y niveles de abstracción distintos, no siete soluciones intercambiables. Noei et al. (2025) y AlOmar et al. (2021) se usan como evidencia de límites de atribución y métricas, no como métodos prescriptivos automáticamente comparables. La revisión de Bagheri-Galle et al. (2025) permanece con contenido pendiente y no se le adjudican conclusiones. Todos los antecedentes conservan versiones y estados de acceso registrados.

## 5. Preguntas de suficiencia todavía abiertas

La dimensión candidata del método es seleccionar y verificar incrementos en un subcircuito institucional donde una decisión atraviesa interfaz, configuración y coordinación con efectos. Falta establecer si esa combinación requiere adaptación no resuelta por los antecedentes o solo aplicación competente de procedimientos ya conocidos. La diferencia de lenguaje, de institución o de nombre de los pasos no basta para sostener originalidad. El resultado de esta comparación podría obligar a precisar o reducir la contribución.

**Condición de cierre de E5:** poder explicar con evidencia documentada qué cubren las soluciones pertinentes, por qué resultan insuficientes o qué adaptación evaluable necesitan en la clase de contextos delimitada y qué aportaría el método. Ya existe búsqueda, comparación y contenido del ciclo industrial próximo, pero falta precisar y contrastar la adaptación concreta. No se mantiene la falta de acceso como pendiente ni se convierte la versión provisional en una brecha científica. E5 permanece abierta y no autoriza implementar el incremento o definir metas retrospectivas.

## 6. Resultado de la primera búsqueda ejecutada

Se examinaron 21 registros en cuatro consultas, sin afirmar que correspondan a 21 soluciones únicas. Se accedió a los textos publicados de Fischer et al. (2025) y Orosz y Kozsik (2026), y a la nota primaria de Fowler (2014); la lectura fue focalizada y no se ejecutaron artefactos. El resumen de Girjoaba y Capiluppi (2024) se verificó en el portal institucional de Groningen, pero el PDF vinculado respondió 403. Las consultas, accesos, fichas, límites y comparación completa están en `comparacion_antecedentes_e5_2026-10-28.md`.

Los hallazgos muestran que ya existen mecanismos de transición gradual, protección del comportamiento y ciclos repetibles. No se reclama ninguno de esos elementos por primera vez, ni se adjudican a la propuesta resultados ajenos. La contribución candidata deberá precisar una adaptación y producir evidencia sobre su aplicación, en lugar de renombrar una combinación conocida. La nueva literatura no reabre el cierre de fundamentación de E4, aunque deberá informar las decisiones que se adopten después.

## 7. Contraste del ciclo con el incremento de SIGPP

**Resultado del 28 de octubre de 2026:** el ciclo de Girjoaba y Capiluppi cubre una parte sustancial de la intervención pretendida. No se ha demostrado que haga falta inventar una secuencia nueva o que el ciclo sea inaplicable a SIGPP. La comparación siguiente distingue contenido heredado, concreción necesaria para el caso y evidencia todavía faltante. Concretar una fase no prueba, por sí mismo, novedad o insuficiencia del método de origen.

### 7.1 Correspondencia por fases

La columna SIGPP se apoya en el escenario ya delimitado y en la inspección estática del 26 de octubre, no en una revisión de código nueva. En el antecedente se consideran los pasos del manuscrito aportado, pp. 5–6. Las correspondencias son razonamiento de aplicación del estudio, no decisiones ya aprobadas de E7. No se proponen ramas nuevas, eliminación de entidades o sustitución de Doctrine por trasladar el ciclo.

| Fase del antecedente | Qué se puede reutilizar | Qué requiere concretarse en SIGPP | Límite de la comparación |
|:--|:--|:--|:--|
| Investigar interfaz. | Localizar usos, dependencias, funcionalidad y ubicación de destino; discutir la solución. | Delimitar una decisión temporal repartida entre presentación, parámetros y creación; distinguir comportamiento observado y requerido. | La unidad local no es una interfaz obsoleta que deba desaparecer. Esto requiere mapear la fase, no demuestra que el ciclo carezca de capacidad para hacerlo. |
| Migrar funcionalidad sin retirar originales. | Separar migración y eliminación para identificar el origen de errores. | Extraer solo la decisión seleccionada y conectar consumidores sin alterar inadvertidamente saldo, restricciones y demás efectos. No confundir esa extracción con añadir la extraordinaria. | No imponer ejecución duplicada de guardados ni coexistencia de reglas contradictorias; una condición no se migra ejecutando dos veces sus efectos. |
| Probar comportamiento. | Comprobar el contrato después de mover la funcionalidad y antes de eliminar lo anterior. | Probar decisiones con contexto controlado y conservar caracterización; aplicar aceptación distinta cuando cambie el comportamiento esperado. | La separación entre caracterización y capacidad nueva se fundamenta también en Feathers (2004) y Fowler (2018); no se reclama como idea original. |
| Retirar archivos y limpiar dependencias. | Eliminar la vía anterior solo cuando se haya comprobado la conexión con la nueva. | Retirar duplicación o conexiones sustituidas en el alcance elegido, no controladores, entidades o repositorios completos por preferencia arquitectónica. | Puede no existir un archivo entero para eliminar. El retiro pertinente depende del incremento y no exige copiar la estructura C++. |
| Probar dependencias. | Verificar las conexiones que quedaron después de la retirada. | Comprobar uso de la decisión desde creación y coherencia de consumidores; conservar semántica de parámetros y gestión pertinente. | Una prueba aislada no demuestra aplicación antes del guardado; no se afirma fallo HTTP reproducido. |
| Integrar cambios. | Mantener una versión identificable y reconstruible del incremento. | Registrar diferencias, razón del cambio e intención estructural o funcional, usando el flujo de versiones pertinente al proyecto. | No se adopta una política específica de ramas ni se ejecutan operaciones Git por este contraste. |
| Probar integración. | Comprobar el funcionamiento conjunto, no solo piezas separadas. | Observar rechazo antes de efectos y comportamiento conservado en el entorno controlado definido; la interfaz no sustituye al servidor. | Pruebas con dobles, petición HTTP y persistencia real prueban propiedades distintas. Su selección y suficiencia deben justificarse, no asumirse por analogía con ASML. |

### 7.2 Diferencias del caso y de la evidencia, no carencias universales

| Diferencia contrastada | Evidencia de partida | Consecuencia candidata | Afirmación que todavía no corresponde |
|:--|:--|:--|:--|
| Unidad de intervención. | El caso ASML retira interfaces obsoletas conservando funcionalidad interna; SIGPP selecciona una decisión dentro de un flujo que sigue en operación. | Especificar cómo se identifica la frontera funcional y qué consumidores pertenecen al incremento. | «El ciclo solo funciona con C++» o «no sirve para decisiones en controladores». |
| Protección disponible. | El manuscrito describe pruebas existentes que se adaptan; en SIGPP hay pruebas directas del servicio, pero la cobertura del recorrido completo no está acreditada. | Explicitar qué se caracteriza, qué requiere preparación y qué conexión se comprueba antes de retirar la vía anterior. | «SIGPP no tiene pruebas» o «las pruebas anteriores bastan para demostrar toda la regla temporal». |
| Intención del cambio. | El ciclo declara ausencia de funcionalidad nueva; la habilitación extraordinaria acordada cambia condiciones de aceptación respecto del antecedente inspeccionado. | Mantener trazabilidad separada de extracción y extensión/corrección, sin necesidad de inventar otra fase universal. | «Agregar restricciones o habilitaciones conserva automáticamente todo el comportamiento anterior». |
| Resultado a examinar. | El caso ASML mide esfuerzo/fallos durante la refactorización; el tesista espera además localizar y extender una regla después de la intervención. | Evaluar la modificabilidad mediante un cambio posterior especificado, distinguiéndola del costo de reorganizar inicialmente. | «Menor tiempo de refactorización demuestra menor costo de todos los cambios posteriores». |
| Evidencia y sesgos. | Seis interfaces de un ejecutor y revisión interna en ASML; el constructor de SIGPP también conoce el sistema. | Declarar aprendizaje, orden, complejidad y revisión independiente en la futura evaluación, con alcance viable. | «Cambiar de tipo de tarea elimina el aprendizaje» o «una revisión institucional equivale a aplicación independiente». |

El contraste muestra necesidades de explicitación y de evaluación local, pero no demuestra que los antecedentes sean incapaces de resolverlas. Feathers ya trata caracterización y conexiones; ADD orienta selección por atributos y refinamiento; el ciclo aporta migración, retirada y comprobaciones intermedias. La aportación candidata no es sumar sus nombres, sino formular y evaluar reglas de adaptación para una clase de subcircuitos bajo condiciones declaradas. La diferencia PHP/C++ o CPS/ASML no basta para reclamar conocimiento nuevo.

### 7.3 Base operativa aceptada por el tesista

El 28 de octubre de 2026, tras la recomendación explícita, el tesista respondió «acepto y continuemos». Se adopta **el ciclo de limpieza como base operativa explícita**, complementado con el cambio seguro de Feathers y el razonamiento por atributos de ADD, para diseñar una adaptación acotada del método. La aceptación no implica copiar literalmente cada fase o instrumento ni presentar como propios los pasos publicados. El título aprobado no cambia y la contribución prevista sigue siendo principios de diseño sustentados por evaluación, no la mera aplicación del ciclo a SIGPP.

| Orientación | Beneficio | Costo o riesgo |
|:--|:--|:--|
| Aplicar el ciclo existente sin adaptación específica. | Menor esfuerzo de diseño; permite comprobar aplicabilidad y aprovechar su estructura. | Puede ser suficiente como trabajo de ingeniería; por sí sola no acredita principios de diseño nuevos ni la contribución de maestría. No se declara que necesariamente fracase. |
| Diseñar y evaluar una adaptación explícita. | Hace trazables unidad funcional, comportamiento protegido, conexiones y examen del cambio posterior. | Requiere justificar cada adaptación y someter su utilidad y conocimiento derivado a evaluación; todavía no se garantiza originalidad ni superioridad. |

**Decisión resuelta:** la base operativa está aceptada y no debe preguntarse nuevamente. **Pendiente:** precisar y contrastar las adaptaciones necesarias; su necesidad, formulación y posible aportación se distinguen en la sección 8. La aprobación de la base no cierra E5 por sí sola ni aprueba clases, contratos o una implementación. No hubo modificación de SIGPP ni nueva evaluación por esta comparación documental.

## 8. Adaptaciones candidatas y prueba concreta de necesidad

**Corte:** 28 de octubre de 2026, después de la aceptación de la base operativa. No se añade otra secuencia universal al ciclo ni se adoptan todavía contratos o requisitos detallados de E7. Las adaptaciones se formulan como concreciones que deben justificarse, probarse y distinguirse del contenido heredado. La aprobación del ciclo no se interpreta como aprobación automática de cada producto propuesto a continuación.

### 8.1 De una interfaz obsoleta a una decisión de un subcircuito

| ID | Adaptación candidata | Antecedente que se reutiliza | Producto propuesto y necesidad en el caso | Estado de originalidad |
|:--|:--|:--|:--|:--|
| A01 | Delimitar el incremento por una decisión funcional y sus consumidores, no por un archivo aislado. | Investigación de usos/dependencias del ciclo; identificación de cambio/puntos de prueba de Feathers (2004); escenarios de Bass et al. (2021). | Ficha que identifique decisión, entradas, consumidores y efectos alcanzados. En SIGPP la condición temporal atraviesa presentación, parámetros y creación, sin una interfaz obsoleta única que retirar. | Adaptación del punto de entrada, no prueba de que el ciclo no sirva fuera de C++. El criterio genérico de separación ya tiene antecedentes. |
| A02 | Distinguir comportamiento observado por punto de decisión, regla requerida e intención del cambio. | Caracterización de Feathers (2004), preservación del ciclo y distinción refactorización/capacidad nueva de Fowler (2018). | Matriz observado/requerido/preservar–corregir–extender para no caracterizar un punto del flujo como si representara todo el contrato. La inspección local ya mostró decisiones de fecha no equivalentes. | Producto candidato de explicitación y trazabilidad; no se afirma que diferenciar comportamiento e intención sea una idea nueva ni que los autores sean incapaces de hacerlo. |
| A03 | Explicitar qué se comprueba en cada punto de control y qué efectos quedan prohibidos ante rechazo. | Pruebas de comportamiento/dependencias/integración del ciclo y comprobación de consumidores en Feathers (2004). | Traza regla → decisión → consumidor → punto de comprobación → efectos observados. La autoridad del servidor acordada debe comprobarse al crear, no inferirse del botón ni de una prueba aislada. | Concreción de comprobaciones, no fase nueva. Los contratos y niveles de prueba precisos siguen pendientes de E6/E7. |
| A04 | Distinguir costo de transformar y facilidad de evolucionar después de la transformación. | Medición contextual del ciclo; escenarios de modificabilidad y costos de Bass et al. (2021); cautelas empíricas de E4. | Especificación prospectiva de un cambio posterior y observación de localización, trabajo, dependencias y protección de comportamiento. El caso ASML estudia el proceso de refactorizar; la expectativa del tesista incluye modificar/extender después. | Aporte candidato de evaluación y reglas de adaptación, no ahorro demostrado ni novedad del concepto de modificabilidad. Escenario, instrumentos y umbrales se definirán antes de construir. |

Estos productos no reemplazan los principios de diseño como contribución prevista de maestría: organizan decisiones y evidencia de donde podrán derivarse, revisarse y evaluarse esos principios. Tampoco convertirlos en formularios asegura reproducibilidad o utilidad. La cuestión de E5 es justificar qué debe explicitar el método para el problema seleccionado y qué se toma de los antecedentes. La prueba de utilidad y los límites de transferencia se obtendrán después, no se anticipan por aprobar la adaptación.

### 8.2 Ejemplo documental de A02, sin ejecución del sistema

Se utiliza un día de referencia **ficticio y controlado: 15 de junio de 2026**, tarea de gestión 2026. La tabla compara exclusivamente las funciones inspeccionadas el 26 de octubre: `fechaEstaEnGestion()` y el predicado de hoy/cierre mensual del JavaScript; no una petición completa, formulario real o despliegue. Los resultados de las columnas técnicas son deducciones de esas comprobaciones bajo el supuesto indicado, **no pruebas ejecutadas**. La regla requerida procede de HU-FEC-01 declarada por el tesista; no se añade una regla institucional nueva ni se presume respaldo funcional externo ya obtenido.

| Fecha solicitada | Comprobación anual local del servicio | Predicado de fecha del JavaScript | Regla requerida declarada | Intención que debe registrarse |
|:--|:--|:--|:--|:--|
| 15/06/2026 | Superaría el rango anual. | Corresponde a hoy. | Admitir respecto de fecha. | Preservar ese resultado en el alcance de fecha, sin dispensar otros controles. |
| 31/05/2026 | Superaría el rango anual. | Corresponde al cierre del mes anterior. | Admitir respecto de fecha. | Preservar ese resultado. |
| 14/06/2026 | Superaría el rango anual. | No corresponde a hoy ni al cierre anterior. | Rechazar respecto de fecha. | Caracterizar la diferencia y registrar la futura corrección como cambio funcional; no ocultarla como extracción conservadora. |

El tercer caso muestra por qué no basta describir «comportamiento existente» sin indicar dónde se observa. Extraer la comprobación anual preservando sus resultados puede ser una transformación conservadora, pero no implementa por sí sola HU-FEC-01. Sustituirla por la política requerida introduce rechazos que ese método local antes no producía, aunque sean intencionales. A02 propone que esa distinción quede explícita antes del cambio y no se reconstruya mirando resultados favorables.

La misma lógica se aplica a la extraordinaria ya acordada: introducir habilitación de otra gestión no se confunde con mover una condición. No se repiten preguntas sobre ventana, días o gestión porque están definidos. La tabla no demuestra que el servidor completo acepte peticiones indebidas ni que el JavaScript se ejecute en todos los caminos; falta la comprobación integrada. Esa limitación debe conservarse en diagnóstico y evaluación.

### 8.3 Qué permite sostener la comparación y qué falta para E5

| Afirmación | Estado al cierre de este contraste |
|:--|:--|
| Hay un antecedente operativo explícito y pertinente. | Respaldada por el manuscrito del ciclo y aceptada por el tesista. |
| Copiar sus siete fases garantiza resolver el caso y generar conocimiento de maestría. | No demostrada; requiere concretar alcance, comportamiento, comprobaciones y evaluación. |
| El caso necesita distinguir resultados por punto de decisión e intención del cambio. | Justificación documental concreta mediante la diferencia local de fecha; no prueba todavía que A02 mejore el método. |
| A01–A04 son principios originales y validados. | No corresponde afirmarlo. Son propuestas de adaptación/evidencia con antecedentes reconocidos. |
| El artículo es insuficiente porque usa C++, o porque no menciona POA. | Rechazada como argumento: esas diferencias no demuestran carencia. |
| La adaptación aporta algo más que la combinación nominal de fuentes. | Hipótesis por defender y evaluar: debe explicarse qué explicitación necesaria agrega y qué conocimiento transferible podría generar bajo condiciones acotadas. |

El pendiente de E5 ya no es elegir una base ni conseguir el artículo. Se requiere que el tesista pueda explicar la diferencia defendible entre aplicar el ciclo y formalizar esta adaptación, apoyándose en el caso y no en el lenguaje o la institución; si no identifica una necesidad adicional, deberá reducirse o revisarse lo reclamado. No se exige demostrar mejora empírica antes de construir, pero tampoco se declara nueva una técnica conocida. E5 permanece abierta; no se inicia aún E6 ni se implementa SIGPP por estas propuestas.

## 9. Justificación del tesista y cierre de la comparación

El 28 de octubre de 2026 el tesista preguntó si «método» ya designa la propuesta de refactorización arquitectónica incremental. Se precisa que sí: es **nuestro artefacto propuesto**, diseñado como adaptación explícita del ciclo de Girjoaba y Capiluppi y apoyado en Feathers y ADD, no el artículo original tomado como creación propia ni una obligación de reorganizar cada cambio. La tipología sigue siendo método más instanciación y la contribución prevista son principios respaldados por evaluación. No cambia el título ni se sustituye la intervención del subcircuito por una migración total.

### 9.1 Explicación propia y alcance de lo acordado

El tesista justifica examinar primero si el cambio puede hacerse de forma segura y rechaza «refactorizar todo porque el método me lo diga». Contrasta una corrección ortográfica de una etiqueta con modificar la regla temporal que encuentra distribuida entre JavaScript, controlador y servicios. Para el segundo caso propone encapsular la responsabilidad y aplicar el ciclo, con las reglas de negocio en el servidor. Esa explicación identifica una necesidad de selección proporcional y de caracterización previa, no una diferencia basada únicamente en el lenguaje o la institución.

| Criterio explicado | Decisión que se registra | Límite que se conserva |
|:--|:--|:--|
| Evaluar seguridad y alcance antes de cambiar. | La actuación arquitectónica debe justificarse por comportamiento, dependencias y riesgo del cambio, no por ejecutar todas las fases de forma mecánica. | «Cambio simple» no es garantía de inocuidad: debe comprobarse su alcance real. |
| Una errata de presentación no justifica reorganizar el subcircuito. | Si el cambio se limita efectivamente a texto visible y no afecta reglas o contratos, no se fuerza una extracción arquitectónica. | Sí corresponde la verificación pertinente al cambio; no se adopta trabajar sin comprobar. |
| Una regla distribuida exige examinar sus decisiones y conexiones. | Investigar qué se observa y qué se requiere antes de decidir encapsulación, reutilización o extensión focalizada. | Tener código en varias capas no basta por sí solo: puede haber responsabilidades legítimamente distintas. La discrepancia temporal documentada aporta una razón concreta para examinar el caso. |
| Encapsular la regla temporal y hacerla cumplir en servidor. | La responsabilidad seleccionada debe tener autoridad verificable en creación; presentación coherente, sin sustituir comprobación de servidor. | «Nuevo servicio» es una opción planteada por el tesista, no una clase obligatoria. El diseño de E7 decidirá si extraer, reutilizar o ampliar un componente; saldo y permisos no se concentran automáticamente allí. |

No se atribuye al artículo una prescripción de trasladar lógica a un servidor web: del antecedente se reutiliza el ciclo de transformación y sus comprobaciones. La aplicación al flujo MVC de SIGPP es adaptación del estudio. El propio ciclo diferencia interfaces que no necesitan todas sus fases; la selección proporcional no se reclama como idea nueva. La aportación candidata está en explicitar cómo seleccionar, proteger y verificar la intervención bajo las condiciones del subcircuito y qué evidencia genera esa adaptación.

### 9.2 Insuficiencia de la aplicación mecánica y alcance de la aportación

El contraste documental mostró que las fases publicadas ya cubren investigar, migrar, retirar y probar. Aplicarlas mecánicamente no determina por sí solo si una edición de presentación justifica cambio arquitectónico, qué observación se preserva cuando las capas difieren, qué corrección se introduce o dónde se hace cumplir una regla antes de efectos. La explicación del tesista, junto con el ejemplo de A02, justifica **operacionalizar** esas decisiones para el caso, sin afirmar incapacidad universal del ciclo o de Feathers/ADD. Se mantiene la separación entre conocimiento heredado, adaptación propuesta y evidencia que falta producir.

El aporte que se someterá a evaluación es una adaptación explícita con selección proporcional del incremento, distinción observado/requerido/intención, comprobación de conexiones y efectos y examen de una modificación posterior. No se afirma que cada elemento sea novedoso ni que una combinación nominal constituya contribución suficiente. Los principios, su utilidad y las condiciones de transferencia deberán sustentarse mediante aplicación, evaluación formativa con rediseño y evaluación sumativa. Si la evidencia no sostiene la adaptación o sus principios, se deberá reducir la contribución reclamada.

### 9.3 Condiciones revisadas y cierre

| Condición de E5 | Evidencia documentada | Juicio y límite |
|:--|:--|:--|
| Soluciones y cobertura existentes identificadas. | Siete antecedentes de distinto alcance, fuentes/versiones registradas, búsqueda focalizada y comparación C01–C08. | Suficiente para la revisión focalizada actual, no cobertura exhaustiva de toda la literatura. |
| Necesidad de adaptación justificada sin inventar carencias. | Correspondencia del ciclo con SIGPP, contraste de intención/observaciones por capa y razonamiento del tesista sobre riesgo y proporcionalidad. | Justifica concretar la aplicación y su evaluación, no declarar que los métodos originales sean erróneos o inaplicables. |
| Aportación candidata acotada y diferenciada de lo heredado. | A01–A04 y selección proporcional; título, objeto y campo se conservan. | La originalidad y validez de los principios no se anticipan a su evaluación ni se sustentan solo en PHP/C++ o CPS/ASML. |
| Explicación propia del tesista. | Ejemplos de etiqueta y regla temporal distribuida; prioridad de evaluación de seguridad y autoridad de servidor. | Se satisface el pendiente conceptual de E5; no es aprobación de contratos o clases concretas. |

Se declara **E5 cerrada al nivel de esta revisión comparativa**, manteniendo explícitos el alcance focalizado y las condiciones anteriores. El paso siguiente es E6: fijar versión y escenario de diagnóstico, obtener línea base y acordar criterios antes del próximo cambio planificado. La afirmación «solo así estaremos seguros» se limita metodológicamente: encapsular reduce ciertos riesgos, pero no garantiza corrección; hacen falta comprobaciones de comportamiento, conexión y efectos. No se modificó código, ejecutó una petición o obtuvo resultados de evaluación propia mediante este cierre documental.

## Referencias

- AlOmar, E. A., Wang, T., Raut, V., Mkaouer, M. W., Newman, C., & Ouni, A. (2021). *Refactoring for reuse: An empirical study* [Prepublicación, versión 1]. arXiv. https://doi.org/10.48550/arXiv.2111.07002
- Bagheri-Galle, F., Parsa, S., & Zakeri, M. (2025). A systematic literature review on transformation for testability techniques in software systems. *Information and Software Technology, 185*, Article 107788. https://doi.org/10.1016/j.infsof.2025.107788 **[metadatos verificados; contenido por verificar, no usado para atribuir resultados]**
- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/
- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055
- Fischer, L., Kausch, H., Rumpe, B., Stachon, M., Stüber, S., & Wollenhaupt, L. (2025). Methodical and formally verified model-driven architecture refactoring. *Journal of Object Technology, 24*(2), 2:1–2:14. https://doi.org/10.5381/jot.2025.24.2.a13 **[texto editorial y metadatos contrastados; lectura focalizada, sin ejecución formal]**
- Fowler, M. (2014, 7 de enero). *Branch by abstraction*. https://martinfowler.com/bliki/BranchByAbstraction.html **[página primaria verificada; técnica de práctica, no estudio controlado]**
- Fowler, M. (2018). *Refactoring: Improving the design of existing code* (2nd ed.). Addison-Wesley Professional. https://martinfowler.com/books/refactoring.html **[edición y pasajes ya contrastados en E4; no nueva lectura íntegra]**
- Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079 **[metadatos verificados; contenido recibido del tesista en manuscrito de doce páginas con datos editoriales provisionales. Correspondencia exacta de versiones por verificar; no se usa el DOI provisional del adjunto]**
- Noei, S., Li, H., & Zou, Y. (2025). An empirical study on release-wise refactoring patterns. *Proceedings of the ACM on Software Engineering, 2*(FSE), Article FSE019. https://doi.org/10.1145/3715734
- Orosz, B. D., & Kozsik, T. (2026). Case study: Refactoring with design and architectural patterns. *Annales Mathematicae et Informaticae, 63*, 107–121. https://doi.org/10.33039/ami.2026.07.003 **[texto publicado, metadatos y sumario editorial verificados; lectura focalizada, sin ejecución de LADY]**
- Zakeri-Nasrabadi, M., & Parsa, S. (2022). *An ensemble meta-estimator to predict source code testability* [Prepublicación, versión 2]. arXiv. https://doi.org/10.48550/arXiv.2208.09614

**Verificación:** antecedentes iniciales con pasajes ya contrastados en E4 y nuevas fuentes primarias focalizadas de E5, distinguidas en el registro de comparación. No se afirma lectura lineal íntegra, reproducción empírica o evaluación propia de un artefacto ajeno.
