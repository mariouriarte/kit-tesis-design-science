# E5: búsqueda ejecutada y comparación de antecedentes próximos

> **Actualización posterior del 28 de octubre:** el tesista aportó el manuscrito completo de Girjoaba y Capiluppi. Contenido y figuras analizados en `lectura_girjoaba_capiluppi_2026-10-28.md`; la limitación a resumen y el 403 descritos en el corte de búsqueda siguiente son históricos. No volver a solicitar el texto como faltante; distinguir sus datos editoriales provisionales de la referencia final verificada.

**Resultado:** se amplió la comparación con dos artículos recientes de texto completo accesible y lectura focalizada, una técnica de migración gradual publicada por un practicante y un antecedente industrial particularmente próximo cuyo resumen fue verificado, pero cuyo PDF respondió 403. La evidencia impide reclamar como novedad la mera extracción, la transformación incremental o la existencia de ciclos repetibles. **E5 permanece abierta:** no se ha demostrado qué adaptación específica necesita el método frente a todos los antecedentes pertinentes.

## 1. Registro de búsqueda del 28 de octubre de 2026

La búsqueda se inició a las 22:10, hora local UTC−04. Se adaptaron las cadenas base del protocolo a consultas de relevancia por título de Crossref; no se ejecutó su expresión booleana literalmente ni se afirma una recuperación exhaustiva. Se añadió una consulta de actas para no limitar la selección a revistas. OpenAlex se utilizó para localizar textos; los resultados sustantivos proceden de fuentes primarias accesibles, no del orden de relevancia del buscador.

| Consulta | Parámetros ejecutados en Crossref `/works` | Registros examinados por metadatos |
|:--|:--|:--|
| Q1 | `query.title=incremental architectural refactoring legacy testability`; fechas `2021-10-28` a `2026-10-28`; tipo `journal-article`; `rows=6`. | 6; se priorizó el caso de Orosz y Kozsik. |
| Q2 | `query.title=architecture refactoring method behavior preservation`; mismas fechas/tipo; `rows=6`. | 6; se priorizó Fischer et al.; el trabajo sobre práctica arquitectónica con DOI `10.1109/TSE.2025.3636150` quedó a nivel de metadatos/resumen de agregador, sin usarlo para atribuir resultados primarios. |
| Q3 | `query.title=MVC framework refactoring method business logic service layer`; mismas fechas/tipo; `rows=5`. | 5; baja precisión, con resultados de otros dominios. No recuperar un método directo en estos cinco registros no demuestra su inexistencia. |
| Q4 | `query.title=incremental refactoring legacy systems methodology framework`; mismas fechas; tipo `proceedings-article`; `rows=4`. | 4; se identificó el trabajo industrial de Girjoaba y Capiluppi. |

Se examinaron **21 registros de consulta**, no se declara que sean 21 soluciones únicas o evaluadas. Los resultados no priorizados permanecen fuera de la comparación sustantiva por ahora; no se presentan como descartes basados en lectura completa. La técnica *Branch by Abstraction* —ramificación mediante abstracción, que permite coexistencia y sustitución gradual de implementaciones— se incorporó como antecedente anterior necesario, a partir de su página primaria conocida, no como resultado reciente de Crossref.

Para conservar la trazabilidad aunque cambie el orden del buscador, se registran los identificadores recuperados. Este inventario no atribuye calidad, revisión por pares o pertinencia final a cada registro.

| Consulta | DOI recuperados en el orden observado |
|:--|:--|
| Q1 | `10.31695/ijasre.2026.8.2`; `10.33039/ami.2026.07.003`; `10.1016/j.is.2026.102743`; `10.1016/j.procs.2026.08.325`; `10.1016/j.jss.2021.111049`; `10.63282/3050-9246.ijetcsit-v3i1p111`. |
| Q2 | `10.17513/snt.39101`; `10.4018/ijsi.339884`; `10.24076/infosjournal.2024v7i01.1579`; `10.5381/jot.2025.24.2.a13`; `10.1109/TSE.2025.3648996`; `10.1109/TSE.2025.3636150`. |
| Q3 | `10.53514/jco.v4i2.550`; `10.1080/23311975.2024.2320996`; `10.18502/ijse.v3i2.20832`; `10.51179/tika.v6i03.849`; `10.1017/S1471068423000200`. |
| Q4 | `10.5593/sgem2021/2.1/s07.11`; `10.1145/3789418.3789437`; `10.1109/ICSME58944.2024.00079`; `10.1109/ICOCT64433.2025.11118372`. |

### Acceso, versiones e incidencias

| Fuente | Acceso y verificación alcanzados | Límite |
|:--|:--|:--|
| Fischer et al. (2025). | PDF editorial `https://www.jot.fm/issues/issue_2025_02/a13.pdf`; portada, secs. 3–7 y página oficial `https://www.jot.fm/contents/issue_2025_02/a13.html`. Autores, revista, volumen 24(2), DOI y pp. **2:1–2:14** contrastados. | Lectura focalizada; no ejecución de Isabelle ni reproducción de demostraciones. La primera ruta intentada, `article13.html`, no contenía el artículo; la ruta válida es `a13.html`. |
| Orosz y Kozsik (2026). | PDF publicado del repositorio institucional `https://publikacio.uni-eszterhazy.hu/9298/1/107_121.pdf`; portada, secs. 3.1, 4 y 5; tabla 1. Crossref y sumario editorial confirman volumen 63 y pp. 107–121; PDF indica publicación en línea el 17 de julio de 2026. | No se ejecutó LADY ni se verificó el código de la aplicación industrial. No se declara lectura de la especificación formal del lenguaje, que el propio artículo deja fuera de su alcance. |
| Fowler (2014). | Página primaria *Branch by Abstraction*, fechada el 7 de enero de 2014, secuencia y notas de aplicación leídas. | Técnica de práctica, no ensayo controlado; los casos enlazados no se cuentan como reproducciones ni se atribuyen sus resultados sin leerlos. |
| Girjoaba y Capiluppi (2024). | Metadatos y **resumen primario** en Groningen: `https://research.rug.nl/en/publications/f297cd32-0cfd-4608-9944-dafc963d0f33`; actas ICSME, pp. 753–764 y DOI contrastados. | PDF enlazado por el repositorio devolvió HTTP 403 mediante descarga y consulta directa. No se deducen de ese resumen los pasos completos, valores de esfuerzo o diseño de evaluación. |

Los PDF y extracciones se mantuvieron en `/tmp/opencode/`; los entregables son estas síntesis Markdown, no copias completas de los artículos. Acceso abierto indicado por un agregador no equivale a texto recuperado. La imposibilidad de recuperar el PDF de Groningen no es una carencia del método descrito. No se eludieron controles de acceso.

## 2. Fichas de extracción de los antecedentes añadidos

### 2.1 Patrones arquitectónicos verificados mediante modelos

Fischer et al. (2025, secs. 3–6) trabajan con arquitecturas de componentes y conectores descritas en SysMLv2 y traducidas a teorías de Isabelle. Su procedimiento cambia el modelo, genera obligaciones de prueba y verifica la transformación; formaliza adición/eliminación de componentes y canales, refactorización bajo invariantes y agrupación/desagrupación de subarquitecturas. El caso introduce un canal cifrado mediante pasos intermedios y demuestra equivalencia bajo las condiciones especificadas. Esto es un antecedente explícito de transformación arquitectónica gradual con protección de comportamiento, no una ausencia que nuestra tesis pueda reclamar.

La evidencia es formal sobre el modelo y su semántica, no una evaluación del esfuerzo de modificar una aplicación PHP existente. El artículo reconoce que buena parte de las pruebas del caso son manuales, que encontrar invariantes resulta difícil y que representar todos los sistemas intermedios aumenta el esfuerzo de modelado (sec. 7). Para aplicarlo a SIGPP habría que establecer una correspondencia entre implementación, modelos, condiciones y garantías, cuyo costo no se ha estimado. No se adopta su afirmación de evitar pruebas adicionales de integración fuera de esos supuestos formales ni se exige introducir SysMLv2/Isabelle como parte de la propuesta.

### 2.2 Reespecificación y generación de patrones en una herramienta industrial

Orosz y Kozsik (2026, secs. 3.1 y 4) utilizan LADY, un lenguaje para expresar decisiones y patrones, y un transpilador que genera C#. El caso reespecifica una herramienta industrial de escritorio para reorganizar espacios de nombres de proyectos; gran parte de la especificación se reescribe mediante reglas formales y se conservan fragmentos C# para operaciones particulares. La evaluación descrita aplica pruebas de sistema para funcionalidades, revisión de los arquitectos propietarios del código y métricas de Chidamber y Kemerer. Se informa reducción de WMC, CBO y RFC; no corresponde resumirlo como mejora demostrada de todas las métricas o de todos los atributos.

Los autores explican que cambios de firmas invalidan pruebas unitarias previas; por eso su protección se realiza a nivel de sistema (sec. 4.3). LCOM no está disponible para el código original y la revisión de propietarios no acredita por sí sola independencia del evaluador. La posibilidad de refactorizar unidades pequeñas manteniendo componentes externos se presenta como trabajo futuro (sec. 5), no como capacidad ya demostrada. Esta solución muestra otro mecanismo de transformación, pero su aplicación directa a SIGPP exigiría adaptación de lenguaje, generación y preservación que no está realizada; no se declara superioridad del método propuesto por esa diferencia.

### 2.3 Coexistencia y migración por abstracción

Fowler (2014) propone introducir una abstracción entre clientes y un proveedor existente, migrar gradualmente los clientes, construir otra implementación y sustituirla por partes mientras el sistema continúa construyéndose y funcionando. La página incluye mejora de pruebas sobre la abstracción y comparación en entornos de prueba, además de variantes y eventual retirada del proveedor y la abstracción. Este antecedente cubre precisamente la transición gradual con dependencias existentes. No puede reclamarse que introducir una frontera reutilizable durante la operación sea nuevo por sí mismo.

La página describe una técnica con ejemplos de práctica y no presenta medición controlada de modificabilidad o testabilidad. Tampoco especifica allí una plantilla única para seleccionar cualquier incremento de certificación ni demuestra que el mecanismo concreto sea adecuado para SIGPP. No se impone coexistencia de dos reglas contradictorias de producción, una nueva interfaz por clase o reemplazo de Doctrine. La técnica queda como alternativa que debe analizarse, no como patrón adoptado automáticamente.

### 2.4 Ciclos industriales de refactorización: antecedente próximo con lectura pendiente

Girjoaba y Capiluppi (2024), en su resumen primario, describen refactorización de interfaces obsoletas de ASML mediante investigación-acción y revisión repetida de planificación, actuación, observación y reflexión. Informan que el proceso se estabilizó en un ciclo de limpieza repetible y que disminuyeron tiempo y fallos por interfaz durante su evolución. Es un antecedente particularmente próximo a la intención de formalizar una práctica incremental y producir un procedimiento para otros desarrolladores. Su existencia basta para descartar novedad basada únicamente en «proponer ciclos iterativos y repetibles», pero no para concluir equivalencia con nuestro método o insuficiencia del suyo.

Falta el texto completo para extraer sus pasos, productos, criterios, control del esfuerzo, papel de los participantes y amenazas a la validez. La ficha institucional distingue la conferencia de octubre y publicación de diciembre de 2024; se conserva el año 2024 sin usar la fecha del evento como si resolviera toda la cronología editorial. **Esta falta es de acceso/lectura de evidencia, no una brecha científica**. El PDF requerido está identificado por el repositorio en `https://research.rug.nl/files/1260821528/Refactoring_Legacy_Code_Using_Cleaning_Up_Cycles_An_Experience_Report.pdf`.

## 3. Comparación bajo C01–C08

Se reutilizan además pasajes ya consultados de Feathers (2004) y Bass et al. (2021). La propuesta de Zakeri-Nasrabadi y Parsa (2022) permanece como comparador parcial de medición/transformación para testabilidad, no como un procedimiento equivalente del flujo MVC. Las celdas describen cobertura en el material leído; «pendiente» no se interpreta como ausencia de la propiedad en la solución. No se asignan puntuaciones de superioridad sin evidencia.

| Dimensión | Cobertura documentada en antecedentes | Qué debe contrastarse para SIGPP |
|:--|:--|:--|
| C01. Selección del incremento. | Feathers identifica cambio y puntos de prueba; ADD usa objetivos/atributos; Fischer parte de un objetivo y transformaciones formalizadas; LADY selecciona una herramienta con requisitos incumplidos. El ciclo ASML se orienta a interfaces obsoletas según su resumen. | Justificar la unidad de intervención por cambio y riesgo sin confundir un ejemplo temporal con regla universal de selección; extraer el criterio completo del ciclo ASML. |
| C02. Conservación/cambio funcional. | Feathers caracteriza comportamiento; Fischer demuestra equivalencia bajo condiciones; LADY usa pruebas de sistema; la técnica de Fowler conserva funcionamiento durante sustitución gradual. | Distinguir extracción conservadora y ampliación extraordinaria; definir qué comportamiento se protege y cómo, sin afirmar equivalencia formal por tener pruebas verdes. |
| C03. Contexto y dependencias. | ADD redistribuye responsabilidades; la técnica por abstracción cambia conexiones de clientes; Fischer transforma componentes/canales e invariantes; LADY fuerza patrones mediante generación. | Examinar fronteras entre reglas, parámetros y efectos, más costo de la adaptación; no asumir que ningún antecedente cubre la separación por no emplear vocabulario POA. |
| C04. Protección y conexión. | Feathers exige atender conexión y consumidor; Fowler describe pruebas en la abstracción; Fischer aporta obligaciones formales; LADY conserva pruebas de sistema ante cambio de firmas. | Determinar el nivel de prueba apropiado y conexión con `create()`, sin imponer que todas las pruebas unitarias antiguas deban permanecer idénticas ni prescindir de integración por analogía con pruebas de modelos. |
| C05. Aplicabilidad. | ADD y Feathers son procedimientos generales; Fowler describe sustitución de proveedores; Fischer requiere modelado/prueba formal; LADY emplea generación C#; el texto completo ASML sigue inaccesible. | Estimar competencias, esfuerzo y dependencias que realmente exige cada opción; no descartar automáticamente principios por lenguaje ni adoptar sus herramientas sin validación. |
| C06. Atributos y medidas. | ADD estructura escenarios; LADY compara ciertas métricas y describe requisitos no funcionales; la propuesta de testabilidad leída en E4 usa presupuesto/efectividad/esfuerzo; ASML declara mejora de tiempo/fallos solo contrastada en resumen. | Comparar el mismo tipo de cambio y condiciones; no importar porcentajes ni afirmar cohesión mejorada cuando no hay línea base comparable. |
| C07. Iteración y reproducción. | ADD registra iteraciones; Feathers proporciona una secuencia; la técnica de Fowler migra clientes por partes; Fischer presenta modelos intermedios y pruebas; ASML declara un ciclo repetible. | Extraer productos y criterios concretos de cada iteración y distinguir réplica de aplicación propia. La refactorización por componentes externos de LADY es futura, no resultado. |
| C08. Evaluación/transferencia. | Fischer demuestra un modelo; LADY informa un caso industrial con revisión de propietarios; la técnica de Fowler es una nota de práctica; ASML informa un caso industrial cuyo cuerpo no se leyó. | No tratar garantías de modelo, pruebas de sistema, revisión interna y estudio industrial como evidencia intercambiable. Identificar condiciones para transferencia analítica y evaluación independiente. |

## 4. Consecuencia para la contribución candidata

La revisión ya muestra soluciones para cambio seguro, decisiones guiadas por atributos, sustitución gradual, verificación de transformaciones y ciclos repetibles. Por ello, no sería defendible afirmar que la propuesta aporta cualquiera de esas ideas por primera vez. Los comparadores tampoco son alternativas idénticas que se puedan ordenar simplemente por cantidad de características. Debe distinguirse reutilización del conocimiento existente de la adaptación que el estudio pretende examinar.

La dimensión candidata sigue siendo seleccionar y verificar un incremento del subcircuito cuando una decisión atraviesa interfaz, configuración y coordinación con efectos, dentro de las restricciones de la aplicación de referencia. No se ha demostrado aún que los métodos existentes sean insuficientes para esa dimensión. El caso ASML requiere lectura prioritaria por su proximidad; la revisión podría reducir o modificar lo que se reclama como original. No se reformula la brecha para que coincida inevitablemente con lo que ya se construyó.

**Balance de E5:** búsqueda ejecutada y comparación ampliada; se añade evidencia que limita la novedad genérica, no una declaración de superioridad del método. Permanecen pendientes lectura del antecedente industrial próximo y contraste de una adaptación concreta frente a la cobertura ya existente. No se modificó SIGPP, ejecutó una herramienta de refactorización ni obtuvo evidencia de evaluación propia. E4 permanece cerrada; E6 y construcción siguen pendientes.

## Referencias

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/
- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055
- Fischer, L., Kausch, H., Rumpe, B., Stachon, M., Stüber, S., & Wollenhaupt, L. (2025). Methodical and formally verified model-driven architecture refactoring. *Journal of Object Technology, 24*(2), 2:1–2:14. https://doi.org/10.5381/jot.2025.24.2.a13 **[verificada: metadatos, página editorial y PDF publicado, lectura focalizada; no reproducción formal]**
- Fowler, M. (2014, 7 de enero). *Branch by abstraction*. https://martinfowler.com/bliki/BranchByAbstraction.html **[verificada: página primaria y técnica; antecedente anterior al intervalo reciente, no estudio controlado]**
- Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079 **[verificada: metadatos y resumen primario institucional; PDF localizado pero acceso 403, contenido completo por verificar]**
- Orosz, B. D., & Kozsik, T. (2026). Case study: Refactoring with design and architectural patterns. *Annales Mathematicae et Informaticae, 63*, 107–121. https://doi.org/10.33039/ami.2026.07.003 **[verificada: PDF publicado, metadatos y sumario editorial; lectura focalizada, no ejecución de LADY]**
- Zakeri-Nasrabadi, M., & Parsa, S. (2022). *An ensemble meta-estimator to predict source code testability* [Prepublicación, versión 2]. arXiv. https://doi.org/10.48550/arXiv.2208.09614 **[lectura focalizada y versiones ya contrastadas en E4, sin nueva reproducción]**
