# Actualización bibliográfica reciente: ampliación posterior al corpus original

**Estado:** propuesta de trabajo. No modifica `IFI_ALSIE.md`, `tesis_ds/`, el diagnóstico, los criterios, los resultados, la evaluación ni las conclusiones empíricas.

> **Verificación posterior (8 de noviembre de 2026):** los nueve DOI se contrastaron en Crossref o arXiv. Se confirmaron Özkan (2023), Fazzini (2022), Abgaz (2023), Gomes (2022), Nogueira (2024), Horikawa (2026), Cordeiro (2026) y Gheyi (2026) como publicadas; Reich y Maalej (2023) como prepublicación de arXiv. **Dos cifras se corrigieron al incorporar:** Cordeiro et al. se citan por su versión publicada (cinco modelos; GPT-4o y DeepSeek-v3 superan el 90 % en pass@5), no por el preprint de StarCoder2; Gheyi et al. se citan por la publicada (GPT-OSS 80,5 % y GPT-5.4 93,8 %), no por el preprint. Gomes et al. (2022), que esta búsqueda había dejado sin verificar, se confirmó y se incorporó como fuente brasileña directamente sobre suites de regresión para *Extract Method*.
**Fecha de la búsqueda:** 8 de noviembre de 2026.
**Ventana de publicación aplicada:** 7 de noviembre de 2021 a 7 de noviembre de 2026, verificada contra la fecha de publicación o de aceptación en línea y no contra la fecha de carga a un repositorio.
**Procedencia:** esta lectura es una **ampliación bibliográfica posterior al cierre del corpus original**. No se atribuye al tesista ninguna lectura de estas fuentes. Su examen personal sigue siendo necesario antes de la defensa, como ya se declaró para el complemento meso/micro.

## 0. Resultado en una línea

Se verificaron ocho fuentes recientes, pertinentes y no duplicadas, todas con lectura sustantiva (texto completo o secciones primarias, indicadas en cada ficha). **Ninguna de las ocho estudia la refactorización conservadora de una aplicación PHP/Symfony con pruebas de caracterización.** Cada una fundamenta o discute una afirmación concreta del IFI, y sus límites de transferencia figuran en la ficha. Con ellas, la proporción pasa de 11/29 a 19/37 (51,4 %) **contando por año calendario**. El §6 explica una salvedad sobre Bass et al. (2021) que podría dejar el resultado en 18/37 (48,6 %).

## 1. Estrategia y consultas efectivamente realizadas

### 1.1 Principios aplicados

- Se buscó sobre cinco ejes: (a) refactorización y pruebas (preservación del comportamiento, regresión, caracterización); (b) testabilidad y modificabilidad; (c) dependencias, responsabilidades y erosión arquitectónica; (d) modernización incremental con evidencia y límites; (e) refactorización asistida por IA validada con pruebas. El eje (e) se incluyó porque el IFI declara asistencia de IA en las aplicaciones (§2.1 y capítulo IV).
- No se limitó la búsqueda a PHP, Symfony o Bolivia. La prioridad secundaria latinoamericana no condicionó la aceptación de fuentes internacionales.
- Una fuente solo conocida por título o resumen quedó como candidata y no se contó.

### 1.2 Rutas y consultas (resumen fiel)

**Búsqueda web general (16 consultas, inglés y español).** Cubrieron: pruebas de caracterización y refactorización; refactorización arquitectónica incremental con pruebas de regresión; patrón estrangulador y modernización incremental; refactorización, testabilidad y modificabilidad; preservación del comportamiento y adecuación de suites; refactorización arquitectónica en aplicaciones web MVC/PHP; refactorización asistida por modelos de lenguaje con pruebas; coevolución de pruebas y código; patrones de refactorización por testabilidad; olores arquitectónicos y esfuerzo; migración de monolitos con pruebas; pruebas diferenciales y golden master; ruptura de pruebas tras refactorizar; monolito modular y arquitectura en capas; refactorización en América Latina; dobles de prueba y testabilidad; impacto en mantenibilidad y modificabilidad; acoplamiento y propagación del cambio; revisión sistemática en español; extensiones de revista de «¿Rompe la refactorización las pruebas?».

**Descubrimiento por interfaces académicas (dos rondas).**
- Ronda general: 21 consultas ejecutadas contra OpenAlex y Crossref con filtro de fechas (comportamiento y pruebas; modernización; deuda técnica arquitectónica; golden master; PHP/Symfony/Laravel; modularidad; ruptura de pruebas; refactorización por LLM; erosión; microservicios con entrevistas; monolito modular; inyección de dependencias; capas/MVC, esta última con cero resultados).
- Ronda latinoamericana: unas 18 consultas en OpenAlex con filtros de país (Brasil, Argentina, Chile, Colombia, México, Ecuador, Perú, Bolivia, Uruguay, otros) en inglés, español y portugués, sobre refactorización, modernización, pruebas de regresión, erosión, migración y PHP.
- Verificación: consultas a Crossref/doi.org por DOI, lectura de texto completo en versiones abiertas legítimas y localización de páginas en SOL-SBC, arXiv, repositorios institucionales.

### 1.3 Rutas bloqueadas o agotadas (declaradas, no ocultas)

- DBLP (denegado por protección anti-robot) y Semantic Scholar (límite de tasa): no aportaron.
- ACM Digital Library (403), IEEE Xplore (418 en PDF), Springer (cookie obligatoria para sus PDF): no se eludieron. Se usaron copias abiertas legítimas (CC BY, repositorios institucionales, arXiv).
- No se localizó ningún estudio empírico revisado por pares sobre refactorización de aplicaciones **PHP/Symfony** en la ventana. El único hallazgo sustantivo sobre PHP (Rio y Brito e Abreu, 2023) es observacional, de olores de código, y excluye aplicaciones basadas en marcos de trabajo.
- Las consultas de «golden master / approval testing» solo devolvieron material de práctica, patentes y herramientas.
- No se localizó evidencia revisada por pares específica sobre estrangulador o abstracción por ramificación.
- Las consultas en español y portugués devolvieron sobre todo tesis de grado y revistas de bajo nivel; no se usaron como fuentes científicas.
- SciELO, Redalyc y CLEI no se consultaron de forma directa; la cobertura de OpenAlex en SciELO es parcial. Queda como ruta no agotada.

## 2. Selección final (orden alfabético, APA 7)

Abgaz, Y., McCarren, A., Elger, P., Solan, D., Lapuz, N., Bivol, M., Jackson, G., Yilmaz, M., Buckley, J., & Clarke, P. (2023). Decomposition of monolith applications into microservices architectures: A systematic review. *IEEE Transactions on Software Engineering, 49*(8), 4213–4242. https://doi.org/10.1109/TSE.2023.3287297

Cordeiro, J., Noei, S., & Zou, Y. (2026). An empirical study on the code refactoring capability of large language models. *ACM Transactions on Software Engineering and Methodology*, Article 3801158. https://doi.org/10.1145/3801158

Fazzini, M., Choi, C., Copia, J. M., Lee, G., Kakehi, Y., Gorla, A., & Orso, A. (2022). Use of test doubles in Android testing: An in-depth investigation. En *Proceedings of the 44th International Conference on Software Engineering (ICSE '22)* (pp. 2266–2278). ACM. https://doi.org/10.1145/3510003.3510175

Gheyi, R., Melo, R., Oliveira, J., Ribeiro, M., & Fonseca, B. (2026). Foundation models as oracles for refactoring correctness detection. *Empirical Software Engineering, 32*(1), Article 32. https://doi.org/10.1007/s10664-026-10951-y

Horikawa, K., Li, H., Kashiwa, Y., Adams, B., Iida, H., & Hassan, A. E. (2026). Agentic refactoring: An empirical study of AI coding agents. *ACM Transactions on Software Engineering and Methodology*, Article 3859242. https://doi.org/10.1145/3859242

Nogueira, V. L., Felizardo, F. S., Amaral, A. M. M. M., Assunção, W. K. G., & Colanzi, T. E. (2024). Insights on microservice architecture through the eyes of industry practitioners. En *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 765–777). IEEE. https://doi.org/10.1109/ICSME58944.2024.00080

Özkan, O., Babur, Ö., & van den Brand, M. (2023). Refactoring with domain-driven design in an industrial context: An action research report. *Empirical Software Engineering, 28*(4), Article 94. https://doi.org/10.1007/s10664-023-10310-1

Reich, P., & Maalej, W. (2023). *Testability refactoring in pull requests: Patterns and trends* [Prepublicación]. arXiv. https://doi.org/10.48550/arXiv.2303.14253

### 2.1 Reservas de versión y de metadatos (obligatorias al incorporar)

| Fuente | Versión leída | Reserva |
|:--|:--|:--|
| Abgaz et al. (2023) | Versión de registro, CC BY 4.0 (repositorio DORAS) | Ninguna sobre versión. Fechas: recibido 15/02/2023, aceptado 11/06/2023, publicado 23/06/2023. |
| Cordeiro et al. (2026) | **Prepublicación arXiv v1** (4/11/2024), con marcadores de plantilla ACM | Las cifras se citan «según el preprint v1» hasta cotejarlas con la versión de la revista. Crossref confirma DOI, número de artículo y fecha en línea (10/03/2026); no hay volumen, número ni páginas. |
| Fazzini et al. (2022) | PDF de autor con pie de derechos de ACM, aparentemente versión final | Estado de acceso abierto de la licencia ACM no comprobado. DOI, páginas y fecha confirmados con Crossref. |
| Gheyi et al. (2026) | **Prepublicación arXiv v3** (13/08/2026), CC BY 4.0 | Las cifras pueden diferir de la versión de la revista. Crossref confirma publicación en línea el 24/08/2026; el fascículo 32(1) corresponde al volumen impreso de 2027. Se cita el año de publicación en línea. |
| Horikawa et al. (2026) | **Manuscrito aceptado en arXiv v2**, con el DOI de la revista en su formato de cita | Publicación en línea anticipada (21/10/2026), sin volumen ni páginas definitivos. No se afirma identidad con el PDF del editor. |
| Nogueira et al. (2024) | **arXiv v1** (19/08/2024), no la versión de registro | El texto de ICSME podría diferir. Páginas y DOI tomados de Crossref. |
| Özkan et al. (2023) | Copia abierta del PDF del editor (Springer Open Access) vía repositorio institucional | La versión de arXiv 2310.01905 es **otro artículo** (su revisión sistemática de DDD); no debe citarse como este. |
| Reich y Maalej (2023) | **arXiv v1**, único disponible | Se confirmó presentación en ICSE 2023 (18/05/2023). **No se confirmaron DOI ni páginas de la versión final**; por eso se cita como prepublicación. Un DOI de IEEE que aparece en la página de la sesión corresponde a otra ponencia. |

## 3. Fichas por fuente

### 3.1 Abgaz et al. (2023)

- **Verificación:** 10 autores; *IEEE Transactions on Software Engineering*, 49(8), pp. 4213–4242, agosto de 2023; tipo «artículo de revisión» (*Survey Paper*). DOI confirmado con Crossref. Acceso abierto legítimo (CC BY 4.0).
- **Lectura realizada:** resumen; secciones I–III (incluida la estrategia de búsqueda); IV-D (fase de evaluación); V (brechas); VI (amenazas); inicio de VII. No se leyeron IV-A a IV-C ni el cierre de VII.
- **Problema:** cartografiar cómo se descomponen aplicaciones monolíticas en microservicios.
- **Método:** revisión sistemática con *snowballing*; búsqueda del 28/10/2021 sobre trabajos revisados por pares de 2015–2021. 5.022 resultados, 968 tras eliminar duplicados, 126 tras título, 92 tras resumen, 33 tras texto completo y 35 tras *snowballing*. Cuatro preguntas de investigación y un marco de seis fases (M2MDF).
- **Resultados:** el 88 % de los estudios evalúa su producto, el 71 % con métricas y el 17 % de forma manual; predominan acoplamiento y cohesión. Experimentos 60 % y estudios de caso 22,8 %. El 68,6 % usa Java. Solo el 10 % emplea más de cuatro aplicaciones. Brechas nombradas: sin métricas ni conjuntos de datos estándar, el análisis dinámico no garantiza cobertura, escasa evidencia sobre despliegue y poco soporte de herramientas.
- **Limitaciones declaradas:** selección por consenso sin medida de acuerdo entre revisores, primer autor hizo el cribado inicial solo, ventana 2015–2021, solo fuentes revisadas por pares, fronteras de fase discutibles, la tecnología da soluciones parciales.
- **Pertinencia para el IFI:** respalda que la evaluación de métodos de modernización es fragmentada, métrica-céntrica y sin líneas base comunes, y que ninguno de los enfoques revisados demuestra preservación de comportamiento. **Límites de transferencia:** trata identificación de microservicios, no refactorización incremental dentro de un único desplegable MVC; su búsqueda termina en 2021.

### 3.2 Cordeiro, Noei y Zou (2026)

- **Verificación:** tres autores; *ACM Transactions on Software Engineering and Methodology*, número de artículo 3801158; en línea y emitido el 10/03/2026. DOI confirmado con Crossref. Es un autor distinto del Cordeiro de SAST 2022.
- **Lectura realizada:** resumen; secciones 1 y 2 (diseño, 2.1–2.2.4); sección 3 (3.1.1–3.1.3 y tablas pass@k, el resto por lectura rápida); sección 4 (amenazas). No se leyó íntegra la conclusión. **Versión leída: preprint v1, no la de la revista.**
- **Problema:** determinar si un modelo de lenguaje puede refactorizar mejor que los desarrolladores y para qué tipos de refactorización y de olores.
- **Método:** un solo modelo (StarCoder2-15B-Instruct); 30 proyectos Java de Apache elegidos de 195 tras excluir los presentes en el entrenamiento; línea base de commits de refactorización de desarrolladores (detectados con RefactoringMiner); muestra de 5.194 commits (39.309 archivos). La preservación del comportamiento se evaluó con pruebas unitarias generadas por EvoSuite sobre el código previo (de 381 pruebas muestreadas manualmente, 348, el 91,3 %, resultaron válidas). Variantes de instrucción: sin ejemplo, un ejemplo y cadena de pensamiento.
- **Resultados (según el preprint v1):** el modelo pasó las pruebas en el 28,36 % de los casos al primer intento (pass@1) y en el 57,15 % con cinco intentos (pass@5), frente al 100 % por construcción de las refactorizaciones de desarrolladores. En refactorizaciones generadas automáticamente, los olores se redujeron un 20,1 % más que con las de los desarrolladores. Los desarrolladores superaron al modelo en olores de diseño complejos (modularización rota, encapsulación deficiente, abstracción multifacética). Los autores recomiendan pruebas exhaustivas al usar modelos de lenguaje.
- **Limitaciones declaradas:** alucinaciones, alcance de un solo commit, posible fuga de datos de entrenamiento, una sola versión del modelo, solo proyectos Apache en Java, las métricas no capturan legibilidad ni rendimiento, y los oráculos de prueba son generados, no los originales.
- **Pertinencia para el IFI:** contraste empírico con tratar como conservada una refactorización asistida por modelos solo porque reduce olores o parece correcta. **Límites de transferencia:** modelo pequeño abierto, no agentes actuales; EvoSuite produce oráculos débiles; proyectos Java de Apache, no aplicaciones web MVC.

### 3.3 Fazzini et al. (2022)

- **Verificación:** siete autores en el orden citado (confirmado en el PDF y en Crossref); *Proceedings of the 44th ICSE*, Pittsburgh, 21–29/05/2022, pp. 2266–2278; fecha de impresión 21/05/2022. DOI confirmado.
- **Lectura realizada:** resumen, introducción, antecedentes (2), metodología (3), resultados RQ1–RQ4 (4, parcial), implicaciones (5), amenazas (6) y conclusión. No se leyó con detalle RQ5.
- **Problema:** cómo crean y usan los desarrolladores dobles de prueba en aplicaciones Android.
- **Método:** RQ1 sobre 1.006 aplicaciones con pruebas públicas; RQ2–RQ5 con análisis manual de 2.365 dobles de Mockito/Mockito-Kotlin que sustituyen 784 clases en las 10 aplicaciones con más dobles. Dos codificadores, con acuerdo declarado «considerablemente alto».
- **Resultados:** Mockito o Mockito-Kotlin está en el 33,5 % de las aplicaciones. El 90 % de las clases sustituidas son externas o acopladas a dependencias externas. Por tipo de clase: lógica de dominio 67,5 %, interfaz gráfica 10,7 %, red 8,7 %, base de datos 8,5 %, configuración 4,6 %. Por tipo de doble: dummies 39,9 %, stubs 32,9 %, mocks 26 %, spies 1,2 %. Los dobles pueden introducir olores de prueba y errores (RQ5).
- **Limitaciones declaradas:** RQ2–RQ5 son un estudio de casos de 10 aplicaciones; posibles errores de herramienta y desacuerdo entre codificadores.
- **Pertinencia para el IFI:** fundamenta que los dobles sirven sobre todo para aislar dependencias externas (justifica el aislamiento en las pruebas de consumidor) y, a la vez, que no son neutros: su uso exige declarar qué acreditan. **Límites de transferencia:** Android, Java/Kotlin, acoplamiento a interfaz móvil; no estudia refactorización ni preservación.

### 3.4 Gheyi et al. (2026)

- **Verificación:** cinco autores (UFCG y UFAL, Brasil). *Empirical Software Engineering*, 32(1), Artículo 32; publicado en línea el 24/08/2026. DOI confirmado con Crossref.
- **Lectura realizada:** resumen; sección 3 (3.1–3.8); sección 4 (inicio de RQ1); sección 5 (discusión: 5.2 temperatura, 5.3 verdaderos positivos, 5.7 costos, 5.12 amenazas); el resto por encabezados. **Versión leída: arXiv v3 (13/08/2026), no la del editor.**
- **Problema:** determinar si modelos de lenguaje pueden detectar errores de motores de refactorización de IDE (errores de compilación y cambios de comportamiento) en Java.
- **Método:** 226 errores reales de los repositorios de IntelliJ, Eclipse y NetBeans (47 tipos de refactorización; 185 errores de compilación y 41 cambios de comportamiento), ampliación del conjunto de Wang et al.; sin ejemplos; GPT-OSS-20B y GPT-5.4 con cinco ejecuciones, otros modelos con una; pruebas metamórficas con seis operadores. La noción de preservación proviene de SafeRefactor (equivalencia basada en pruebas).
- **Resultados (según el preprint v3):** precisión global de GPT-OSS-20B entre 0,757 y 0,805 (media 0,784); GPT-5.4, 93,8 % en la primera ejecución. En cambios de comportamiento, 0,854–0,927 (GPT-OSS). Con 50 refactorizaciones que sí preservan comportamiento, el 86 % (GPT-OSS) y el 96 % (GPT-5.4) fueron reconocidas como correctas. La precisión en cambios de comportamiento cae con decodificación determinista. En una comprobación de factibilidad con proyectos grandes, 18 de 44 casos quedaron «desconocidos».
- **Limitaciones declaradas:** el conjunto solo contiene casos defectuosos (la precisión equivale a la exhaustividad y no se caracteriza la tasa de falsos positivos), solo 41 casos de cambio de comportamiento, verdad de referencia reconstruida, sensibilidad al aviso y a la decodificación, fuga de datos no descartada, versión del modelo congelada. Los autores aclaran que el estudio **no establece verificación de equivalencia de comportamiento ni garantías de corrección para uso productivo**.
- **Pertinencia para el IFI:** antecedente iberoamericano reciente que muestra que incluso las herramientas de refactorización automática introducen cambios de comportamiento, y que un modelo de lenguaje solo puede complementar, no sustituir, la comprobación con pruebas. **Límites de transferencia:** Java, errores de motores de IDE en programas pequeños; no aplicaciones heredadas ni refactorización arquitectónica dirigida por personas.

### 3.5 Horikawa et al. (2026)

- **Verificación:** seis autores; *ACM TOSEM*, número de artículo 3859242; en línea y emitido el 21/10/2026, sin volumen ni páginas definitivos. DOI confirmado con Crossref.
- **Lectura realizada:** resumen; 1 Introducción; 2 Trabajos relacionados; 4 Recolección de datos (4.1, 4.2.1, 4.2.2, 4.2.5); 5 Resultados (5.1 y 5.2, lectura rápida); 6 Implicaciones; 7 Amenazas; 8 Conclusión. No se leyeron la sección 3 ni los resultados completos de 5.3 y 5.4. **Versión leída: manuscrito aceptado en arXiv v2 (26/10/2026), con el DOI de la revista en su formato de cita; no se afirma identidad con el PDF del editor.**
- **Problema:** cuán ampliamente refactorizan los agentes de codificación con IA, cómo se compara con la refactorización humana y qué efecto tiene en la calidad.
- **Método:** conjunto AIDev, solo commits Java: 14.998 commits de 12.256 solicitudes de integración en 1.613 repositorios; 51.412 instancias de refactorización; 3.907 commits con intención explícita de refactorizar (32.611 instancias). Detección con RefactoringMiner, métricas con DesigniteJava y clasificación de propósito con un modelo de lenguaje (validada con 79 pares de etiquetas, kappa 0,83 entre humanos y 0,77 contra el modelo). **No se evaluó la preservación del comportamiento: no hubo ejecución de pruebas.**
- **Resultados:** el 26,1 % de los commits apunta explícitamente a refactorizar; el 36,6 % de las instancias ocurre en commits que no mencionan refactorización. Las refactorizaciones de bajo nivel son el 27,6 % en agentes frente al 24,4 % en humanos. Motivos declarados: mantenibilidad 52,5 %, legibilidad 28,1 %. Mejoras de métricas pequeñas pero significativas, sobre todo en cambios de nivel medio. El 86,9 % de las solicitudes de agentes fue integrado.
- **Limitaciones declaradas:** error de las herramientas de detección, detección de intención por palabras clave, ambigüedad del «commit agéntico» por la intervención humana, métricas de clase que pueden redistribuir la complejidad, solo proyectos públicos de adopción temprana y solo Java.
- **Pertinencia para el IFI:** sus propias implicaciones afirman que la mezcla de refactorización con otros cambios «dificulta verificar» la preservación y recomiendan aislar los commits de limpieza y que el agente informe las pruebas ejecutadas. Respalda la separación entre refactorización, corrección y nueva funcionalidad del §3.1 y la prudencia ante la asistencia de IA. **Límites de transferencia:** solo Java de código abierto, sin foco en MVC ni en sistemas heredados, sin evidencia de corrección.

### 3.6 Nogueira et al. (2024)

- **Verificación:** cinco autores; ICSME 2024, pp. 765–777; fecha de Crossref 06/10/2024; prepublicación en arXiv el 19/08/2024. DOI confirmado. Los autores tienen filiaciones brasileñas y el 77,4 % de la muestra es de Brasil.
- **Lectura realizada:** texto completo del arXiv v1 (secciones I a VII y el inicio de las referencias). **No es la versión de registro.**
- **Problema:** por qué y cómo migran los profesionales sistemas heredados hacia microservicios.
- **Método:** encuesta de métodos mixtos con 53 profesionales (35 de un estudio previo y 18 nuevos); 29 preguntas (20 cerradas, 9 abiertas); reclutamiento por redes sociales y contactos (muestreo por conveniencia); síntesis temática de las respuestas abiertas; estudio piloto con desarrolladores con experiencia.
- **Resultados:** migración gradual 50,9 %; descomposición por capacidad de negocio 52,8 %; comprender el sistema heredado 71,7 %; pruebas unitarias 83 % e integración 79 %; monitoreo automatizado 83 %. Las respuestas mencionan periodos de coexistencia y validación.
- **Limitaciones declaradas:** muestra concentrada en Brasil, muestreo por conveniencia, posible influencia de las preguntas cerradas, datos autoinformados; las dos preguntas sobre comprensión del sistema heredado tuvieron solo 18 respuestas.
- **Pertinencia para el IFI:** antecedente meso (muestra mayoritariamente brasileña) que documenta que las pruebas unitarias y de integración son la verificación habitual durante la migración y que la migración gradual con coexistencia es frecuente. **Límites de transferencia:** microservicios y no refactorización de un MVC; no menciona pruebas de caracterización ni mide preservación del comportamiento; todo es autoinforme.

### 3.7 Özkan, Babur y van den Brand (2023)

- **Verificación:** tres autores; *Empirical Software Engineering*, 28(4), Artículo 94 (36 pp.); aceptado el 27/02/2023, en línea el 15/06/2023. DOI confirmado con Crossref. Artículo de investigación completo (investigación-acción), acceso abierto.
- **Lectura realizada:** texto completo en la copia abierta del PDF del editor: resumen y secciones 1 a 11 (introducción, antecedentes, diseño de la investigación, sistema existente, problemas, sistema refactorizado con la sección 6.9 de pruebas, resultados, lecciones aprendidas, amenazas, trabajos relacionados y conclusiones).
- **Problema:** mejorar la mantenibilidad de un sistema industrial existente mediante una refactorización guiada por diseño dirigido por el dominio (DDD), y recoger los efectos y desafíos percibidos.
- **Método:** un solo producto de una empresa (gestor de dominio operativo para conducción autónoma; interfaz AngularJS, servidor Java/Spring con servicios REST y PostgreSQL; arquitectura por capas controlador-servicio-repositorio con dominio anémico); equipo de 13 personas. Dos minigrupos focales de 60 minutos con 7 ingenieros para identificar problemas; un ciclo de acción sobre una rebanada acotada de extremo a extremo (2 controladores, 4 servicios, 1 repositorio, 9 objetos de datos) aislada con una capa anticorrupción; evaluación con entrevistas semiestructuradas escritas de 90 minutos (9 preguntas alineadas con ISO 25010: modularidad, reutilización, analizabilidad, modificabilidad, testabilidad), cuestionario mTAM y clasificación de tarjetas.
- **Resultados:** percepciones mayoritariamente positivas; mTAM utilidad percibida 85, facilidad percibida 83, global 84. Las pruebas unitarias, de integración y de caja negra se reelaboraron y se añadieron (sección 6.9), pero el artículo **no informa mediciones de preservación del comportamiento, regresión ni defectos**.
- **Limitaciones declaradas:** grupo pequeño de participantes, un equipo y una base de código, sin pretensión de generalización, mantenibilidad percibida y no medida, la refactorización no fue una decisión de negocio, el trabajo continuo de nuevas funciones se aisló, y se redactaron materiales por propiedad intelectual.
- **Pertinencia para el IFI:** es el antecedente más cercano al método encontrado: refactorización incremental acotada a una rebanada funcional de un sistema por capas, protegida mediante una capa de aislamiento, con evaluación por escenarios de calidad. Permite discutir que la mejora percibida de analizabilidad, modificabilidad y testabilidad no es mejora medida. **Límites de transferencia:** Java/Spring con servicios REST (no MVC con vistas renderizadas en servidor), empresa grande y una sola rebanada.

### 3.8 Reich y Maalej (2023)

- **Verificación:** dos autores (Universität Hamburg); ICSE 2023, pista técnica, Melbourne, presentación del 18/05/2023. DOI de arXiv confirmado (10.48550/arXiv.2303.14253); **no se confirmaron DOI ni páginas de la versión final**.
- **Lectura realizada:** texto completo del arXiv v1 (único disponible, 24/03/2023): resumen, introducción, discusión (VI.A y VI.B) y parte de los trabajos relacionados. No se leyó con detalle el catálogo de patrones (sección IV) ni la sección V.
- **Problema:** cómo refactorizan los desarrolladores el código de producción para hacerlo probable mediante pruebas unitarias.
- **Método:** 346.841 solicitudes de integración Java de 621 proyectos de GitHub. Paso 1: comparar refactorizaciones atómicas en solicitudes que cambian conjuntamente pruebas y producción con las que no. Paso 2: análisis manual de 200 solicitudes que mencionan «testability» o «refactor + test». Paso 3: análisis manual de otras 524 solicitudes con pares de prueba (muestreo mixto aleatorio y dirigido).
- **Resultados:** las solicitudes con pares de prueba contienen significativamente más refactorizaciones atómicas. Se identificaron diez patrones compuestos de refactorización por testabilidad. Alrededor del 25 % de las solicitudes con pares de prueba analizadas contiene al menos uno; los autores advierten que la frecuencia general es probablemente menor, y la muestra aleatoria sugiere cerca del 13 %. Los más frecuentes: extraer un método para sobrescribirlo o invocarlo, ampliar el acceso a un método para invocarlo y extraer una clase para invocarla. La mayoría rompe dependencias, en coincidencia con las técnicas de Feathers.
- **Limitaciones declaradas:** solo proyectos de código abierto Java/JVM; muestreo por máscaras de palabras clave, por lo que las frecuencias no se generalizan; un etiquetador principal, con alrededor del 60 % de las solicitudes doblemente etiquetadas y kappa de Cohen cercano a 0,70; posibles errores en los guiones de análisis; se esperan falsos negativos.
- **Pertinencia para el IFI:** aporta evidencia empírica reciente de que crear puntos de prueba mediante extracción, ampliación de visibilidad y ruptura de dependencias es una práctica frecuente y ligada a cambios conjuntos de pruebas, lo que concuerda con los pasos 3.1 que ya se apoyan en Feathers. **Límites de transferencia:** Java de código abierto y datos a nivel de solicitud; no dice nada sobre preservación de comportamiento ni pruebas de caracterización; las frecuencias no se trasladan a PHP.

## 4. Apartado exacto del IFI donde encajaría cada fuente

| Fuente | Apartado del IFI | Función |
|:--|:--|:--|
| Reich y Maalej (2023) | §3.1, tras el párrafo de Feathers sobre conexión con el consumidor (pp. 194–195) | Contraste empírico reciente de los puntos de prueba y de la ruptura de dependencias |
| Fazzini et al. (2022) | §3.3, antes de la definición propia de capacidad de prueba | Fundamento y límites de los dobles de prueba en las aplicaciones de consumidor |
| Cordeiro et al. (2026); Gheyi et al. (2026); Horikawa et al. (2026) | §3.3, párrafo nuevo tras Noei et al. (2025) | Refactorización asistida y verificación independiente (el IFI declara asistencia de IA en §2.1, en el capítulo IV y en las limitaciones) |
| Özkan et al. (2023) | §3.4 (antecedente macro): fila 8 de la Tabla 5 y un párrafo previo a la síntesis | Comparador más cercano: refactorización acotada con capa de aislamiento y evidencia percibida |
| Nogueira et al. (2024); Abgaz et al. (2023) | §3.4: nuevo párrafo «Síntesis del contraste reciente» y ampliación de la «Síntesis del complemento» | Práctica declarada de migración gradual y pruebas (meso) y límites de evidencia de la modernización |
| Todas | §8 (Referencias) y Anexo C (mapa) | Alta de referencias y registro de procedencia posterior |

Nota: §1.7 (métodos) no requiere cambio; solo cabría un enlace de «ver §3.3–§3.4» si se desea citar la ampliación como parte del análisis bibliográfico.

## 5. Párrafos propuestos de integración (APA 7, contrastados con lo ya desarrollado)

Los párrafos usan el mismo registro del IFI. No modifican las conclusiones empíricas.

### 5.1 §3.1 (tras el párrafo de Feathers sobre conexión con el consumidor)

> La práctica de crear puntos de prueba mediante separaciones mínimas tiene respaldo empírico reciente, aunque con alcance distinto del de este estudio. Reich y Maalej (2023) analizaron 346.841 solicitudes de integración Java de 621 proyectos y describieron diez patrones compuestos de refactorización orientados a la testabilidad; entre los más frecuentes figuran extraer un método para sobrescribirlo o invocarlo, ampliar el acceso a un método para invocarlo y extraer una clase para invocarla. Los autores observaron que la mayoría de esos patrones rompe dependencias, lo cual coincide con las técnicas de ruptura que Feathers (2004) describe para introducir pruebas en código heredado. La coincidencia fortalece el supuesto de que separar para observar es una operación conocida y no una invención de este trabajo. No lo extiende, sin embargo, a la preservación del comportamiento: el estudio de Reich y Maalej es observacional, se limita a Java de código abierto y a solicitudes de integración, estima una frecuencia de alrededor del 25 % en la muestra analizada manualmente (cerca del 13 % en la aleatoria) y no evalúa si las pruebas asociadas conservaron el comportamiento. Por ello, la selección de qué separar y qué comprobar sigue dependiendo de la decisión funcional, de sus consumidores y de sus efectos, como se establece en este capítulo.

### 5.2 §3.3 (antes de «La definición propia asumida…»)

> Los dobles de prueba permiten aislar dependencias, pero no son neutros respecto de lo que acreditan. Fazzini et al. (2022) examinaron 1.006 aplicaciones Android y analizaron manualmente 2.365 dobles de Mockito y Mockito-Kotlin que sustituían 784 clases en diez aplicaciones; hallaron que el 90 % de las clases sustituidas eran externas o estaban acopladas a dependencias externas y que los dobles pueden introducir olores de prueba y errores. La evidencia es de Android y de diez aplicaciones, por lo que no se traslada como frecuencia a PHP. Su utilidad aquí es conceptual: refuerza la distinción ya establecida en este estudio entre una prueba de interacción con dobles y una comprobación con persistencia real. El doble delimita la conexión que se observa; no sustituye la comprobación del recurso que reemplaza.

### 5.3 §3.3 (párrafo nuevo tras Noei et al., 2025)

> La asistencia de modelos de lenguaje al refactorizar exige sumar una consideración que el IFI ya incorpora como límite de las aplicaciones (§2.1): el resultado aparentemente correcto no equivale a conservación comprobada. Cordeiro et al. (2026), en el preprint consultado, hicieron refactorizar a un modelo abierto 30 proyectos Java de Apache y evaluaron la preservación con pruebas generadas sobre el código anterior; el modelo las superó en el 28,36 % de los casos al primer intento y en el 57,15 % con cinco intentos, aunque redujo olores en mayor medida que las refactorizaciones de desarrolladores, y los autores recomiendan pruebas exhaustivas. Horikawa et al. (2026), sobre 51.412 instancias de refactorización de agentes de codificación en solicitudes Java, informan que más de un tercio ocurre en commits que no declaran refactorización, y señalan que esa mezcla dificulta verificar la preservación del comportamiento; el estudio no ejecutó pruebas. Gheyi et al. (2026), con 226 errores reales de motores de refactorización de IDE, muestran que incluso las herramientas deterministas provocan cambios de comportamiento y que los modelos de lenguaje pueden detectarlos solo de forma parcial, sin ofrecer garantías de equivalencia. Las tres investigaciones son de Java de código abierto, usan modelos o agentes distintos de los empleados en SIGPP y no estudian aplicaciones MVC heredadas. Su aporte a esta tesis es de límites de evidencia: confirman que la asistencia de IA obliga a mantener la comprobación independiente y la separación de refactorización, corrección y nueva funcionalidad, y no autorizan a atribuir a SIGPP ni la eficacia ni la fiabilidad que reportan.

### 5.4 §3.4 (antes de «Síntesis del complemento y posición crítica», como antecedente macro adicional)

> **Antecedente macro adicional: refactorización guiada por diseño dirigido por el dominio en una empresa.** Özkan et al. (2023) informan una investigación-acción en una empresa industrial sobre un sistema por capas (controlador, servicio y repositorio) con dominio anémico. Refactorizaron una rebanada acotada de extremo a extremo —dos controladores, cuatro servicios, un repositorio y nueve objetos de datos— aislada con una capa anticorrupción, y la evaluaron mediante entrevistas semiestructuradas alineadas con ISO 25010 y un cuestionario de aceptación; las percepciones fueron mayoritariamente positivas (puntaje global de 84). Esta estructura se asemeja a la delimitación por decisión y a la protección de consumidores que propone esta tesis. La diferencia es de evidencia y de fondo: los autores reelaboraron pruebas, pero no informan mediciones de preservación del comportamiento, de regresión ni de defectos, y declaran que la mantenibilidad fue percibida y no medida, con un equipo, una base de código y sin pretensión de generalización. El método de esta investigación comparte con aquel estudio el alcance acotado y la separación mediante una frontera, pero distingue de forma explícita lo observado de lo esperado, y no extrae del estudio de Özkan et al. una mejora medida de modificabilidad que éste no produjo.

### 5.5 §3.4 (síntesis de contraste reciente, tras el antecedente nacional)

> **Contraste reciente de la práctica y de la evidencia de modernización.** El nivel meso se amplía con una encuesta de Nogueira et al. (2024) a 53 profesionales, con 77,4 % de participantes en Brasil, sobre migración de sistemas heredados hacia microservicios; el 50,9 % declara migrar de forma gradual, y las pruebas unitarias (83 %) y de integración (79 %) figuran como la verificación habitual, junto con un monitoreo automatizado del 83 %. Se trata de un muestreo por conveniencia y de datos autoinformados, que no menciona pruebas de caracterización ni mide la conservación del comportamiento. Complementa este cuadro la revisión sistemática de Abgaz et al. (2023), que reunió 35 estudios de descomposición de monolitos publicados hasta 2021: la mayoría evalúa su producto, el 71 % con métricas de acoplamiento y cohesión, predominan aplicaciones Java, solo el 10 % usa más de cuatro aplicaciones y los autores señalan la ausencia de métricas y conjuntos de datos estándar. Ambos estudios se ocupan de microservicios y no de refactorización dentro de un monolito MVC, por lo que no sirven de comparador directo de M-R1. Permiten, en cambio, situar la limitación de esta tesis: la evidencia de modernización es en general métrica o autoinformada y rara vez muestra preservación del comportamiento, de modo que la exigencia de este estudio de declarar el nivel de evidencia de cada propiedad no es un exceso de cautela sino una carencia frecuente del campo.

### 5.6 §3.4, nota para la Tabla 5 (fila propuesta)

| Antecedente | Cobertura, mecanismo y evidencia | Posición y límite de transferencia |
|:--|:--|:--|
| Özkan et al. (2023) | Refactorización guiada por DDD de una rebanada de extremo a extremo con capa anticorrupción; investigación-acción en una empresa; entrevistas ISO 25010 y mTAM. | Comparador cercano por alcance y aislamiento. Mantenibilidad percibida, sin medición de preservación; Java/Spring con servicios REST y una sola rebanada. |

## 6. Recuento bibliográfico proyectado (sin duplicar estudios)

| Concepto | Valor |
|:--|--:|
| Referencias actuales del IFI | 29 |
| Fuentes nuevas propuestas (ninguna duplica una entrada actual; Reich y Maalej, Cordeiro et al. y Gheyi et al. no tienen otra publicación o prepublicación ya incluida) | 8 |
| Total proyectado | 37 |
| Recientes actuales (conteo del IFI) | 11 |
| Recientes proyectadas | 19 |
| Proporción proyectada de recientes | 51,4 % (19/37) |

**Salvedad que debe resolver el tesista o el asesor:** el conteo de 11 recientes del IFI parece hacerse por año calendario (2021–2026). La edición de Bass et al. (2021) cuenta como reciente en ese criterio, pero no verifiqué su fecha exacta de publicación. Si la ventana se aplica por fecha completa (7/11/2021 a 7/11/2026) y esa edición apareció antes del 7/11/2021, la proporción sería 18/37 (48,6 %), es decir, no superaría la mitad. Debe fijarse el criterio de conteo antes de afirmar «predominio». Con otra fuente verificada de la lista de reserva (§7.2) se superaría la mitad incluso bajo el criterio estricto, pero sumar fuentes solo para cumplir el umbral contradice el propósito de esta búsqueda.

Dos precisiones adicionales sobre el recuento:

1. **Naturaleza de las ocho fuentes.** Siete son artículos de revista o de congreso arbitrado con DOI confirmado; Reich y Maalej se cita como prepublicación porque no se confirmó el DOI de su versión final. Cuatro de las ocho (Cordeiro, Gheyi, Horikawa y Nogueira) se leyeron en manuscrito o prepublicación y no en la versión del editor. REF-2 pide fuentes científicas; todas lo son, a diferencia de las fuentes de práctica ya declaradas en el §8.
2. **Las reservas de versión del §2.1 deben pasar a la nota «Reservas bibliográficas» del §8** si se incorporan, como ya se hace con Abbasi, AlOmar y Zakeri-Nasrabadi.

## 7. Candidatas descartadas, en reserva o no verificadas

### 7.1 Descartadas

| Candidata | Motivo |
|:--|:--|
| Sun et al. (2022), *Computers* (inyección de dependencias y mantenibilidad) | Mide mantenibilidad solo con métricas de acoplamiento; muestra pequeña y desigual; la prueba estadística del subconjunto tiene p = 1,0; el acoplamiento aumenta con la inyección, lo que contradice el resumen. |
| DePalma et al. (2024), *Expert Systems with Applications* (refactorización con ChatGPT) | La preservación del comportamiento la juzgó el propio ChatGPT, sin ejecutar pruebas (cifra del 97,2 % circular). Lectura parcial. |
| «Kamble y Kulkarni (2024)» | Atribución errónea de mi búsqueda inicial. El artículo localizado (IJSI, DOI 10.4018/ijsi.339884) es de Kuo et al.; solo se leyó su resumen. No se cita. |
| Hayashi, Minami y Saeki (2017); Rachatasumrit y Kim (2012) y similares | Fuera de la ventana. |
| Kashiwa et al. (ICSME 2021); Pianini y Neri (ICSME 2021) | Aparecen como publicaciones de 2021 anteriores al 7/11/2021 por la fecha del congreso; no se verificó el registro exacto. Pertinentes pero fuera de ventana por criterio. |
| Li, Liang y Avgeriou (2023, *IST*); Sas y Avgeriou (2023, *TSE*) | Leídas en preprint; pertinencia baja para la tesis: no estudian pruebas ni refactorización como intervención. Li et al. usan comentarios de revisión como indicio de erosión; Sas y Avgeriou validan el índice con opiniones, no con esfuerzo real. Pueden servir de contexto si se amplía el apartado de erosión. |
| Teixeira et al. (SBES 2024, METEOR) | Leída. Refactoriza **código de pruebas**, no código de producción; es una herramienta con demostración sobre dos escenarios. Útil solo para la idea de que la refactorización de pruebas necesita su propia verificación. |
| Sartorio y Rossi (CIbSE 2026) | Leída. Antecedente argentino, pero la validación es una demostración con un caso de Odoo (Python) sin pruebas ni preservación; clasificada como «artículo de póster» en el repositorio. |

### 7.2 En reserva (válidas con salvedades; no cuentan en la selección)

| Candidata | Lectura | Motivo para no seleccionarla ahora |
|:--|:--|:--|
| Martins et al. (2025, *EMSE*, refactorización de código de pruebas) | Manuscrito de autor, secciones 1–7 | Trata de código de pruebas; su conclusión de efectividad descansa en 20 refactorizaciones; versión no final. |
| Faustino et al. (preprint arXiv 2201.07226, ene. 2022; versión de revista: *Performance Evaluation*, 2024) | Preprint, migración y rendimiento | El DOI de la versión publicada no pudo cotejarse; un solo caso; no usa pruebas de preservación. Muestra que la modularización escalonada tiene costo medible. |
| Wang et al. (2026, *TOSEM*) | Preprint arXiv v1 (título distinto) | Cifras del preprint pueden diferir; evidencia por analogía con motores de IDE; ya aparece indirectamente vía Gheyi et al. |
| Aversano et al. (2023, ENASE) | Hasta la sección 4.1 | Correlacional; contexto de motivación; sin evidencia de preservación ni de pruebas. |
| Rio y Brito e Abreu (2023, *JSS*) | Solo el preprint v1 (estudio menor) | Único estudio sustantivo sobre PHP, pero observacional, excluye aplicaciones con marco y no se leyó la versión de la revista; sus cifras no pueden citarse como las del artículo. |
| Villaça et al. (ERES 2024) | Texto completo | Antecedente brasileño de estrategias previas a la migración a microservicios; sin evidencia de preservación ni de PHP. |

### 7.3 Identificadas, no verificadas (no cuentan)

Conocidas solo por registro o resumen: Gomes, Cordeiro y Alves (SAST 2022; resumen: suites manuales detectaron el 61,9 % de fallos inyectados en Extraer Método, Randoop el 46,7 % y EvoSuite el 55,8 %; DOI 10.1145/3559744.3559745; es un antecedente latinoamericano pertinente que merece lectura de texto completo); Nagy y Abdalkareem (MSR 2022, texto inaccesible); Fonseca et al. (SBQS 2024, informe de experiencia de Eldorado, solo resumen); Pandini et al. (2026), Pomian et al. (2024), Gao et al. (2025), Wright (2023), Verhaeghe et al. (2022), Almeida et al. (2022), Veronez et al. (2024), Medeiros et al. (2023); y el artículo de práctica de Komura (2026, Zenodo) sobre pruebas de caracterización, que no está revisado por pares.

## 8. Cierre

- Se obtuvieron ocho fuentes válidas y verificadas, con las reservas del §2.1. No se rellenó el número con referencias inventadas o irrelevantes, y se declaran como no resueltas las rutas bloqueadas del §1.3.
- No se modificó `IFI_ALSIE.md` ni `tesis_ds/`.
- **Decisión pendiente del tesista:** si se incorporan las ocho, sin las ocho o un subconjunto, y con qué criterio contar «recientes» (por año o por fecha completa). Si se incorporan, el paso siguiente sería actualizar el §8 y el Anexo C, redactar las reservas de versión y recalcular REF-2 en la autoevaluación sin alterar el resto de los criterios.
