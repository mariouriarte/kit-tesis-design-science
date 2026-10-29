# Revisión del título y de la clase de aplicaciones

## Resultado aprobado

**Actualización:** 28 de octubre de 2026, fecha de aprobación y de contraste de la documentación 3.x. El nombre del archivo conserva la fecha de apertura de la revisión.

El tesista cuestionó «MVC institucional» porque puede interpretarse como una arquitectura específica y aclaró el foco en un método incremental para subcircuitos con responsabilidades mezcladas. Después aceptó expresamente el título propuesto: «el titulo que sugieres es lo mas cercano a lo que pienso, y esta perfecto». Se adopta la formulación de la sección 3 y se armonizan estado, delimitación, perfil, introducción del marco teórico y cadena de coherencia. MVC continúa caracterizando las aplicaciones; el contexto institucional no se convierte en patrón arquitectónico y FastAPI no se agrega como caso. Las entregas anteriores conservan su título histórico; no se cierra una etapa ni se valida el método por esta aprobación.

## 1. Distinciones necesarias

| Expresión o afirmación | Tratamiento |
|:--|:--|
| «MVC institucional». | No se introdujo ni sustentó una variante arquitectónica con ese nombre. «Institucional» describe el contexto organizacional; la formulación previa confunde ese contexto con el patrón. Se propone desambiguar. |
| «Arquitectura sucia». | Expresión informal del tesista, no diagnóstico operacional. Describir concentración o dispersión de reglas, duplicación, acoplamiento y responsabilidades mezcladas con evidencia específica. |
| «No hay cohesión» y «el código es rígido». | Tratar como percepción o diagnóstico candidato; precisar unidades, cambios representativos e indicadores antes de afirmar ausencia o mejora cuantificada. |
| «Los libros de los marcos enseñan a poner lógica en controladores». | No se acepta como generalización causal sin corpus y análisis. La documentación oficial Symfony 4.x explícitamente recomienda controladores sin lógica de negocio. Los libros concretos mencionados por el tesista no fueron identificados ni examinados en esta revisión. |
| FastAPI como ejemplo. | Su documentación consultada presenta operaciones de ruta, APIRouter y dependencias, pero no basta para clasificar cualquier aplicación FastAPI como MVC ni demostrar que el marco cause mezcla de responsabilidades. No se amplía la evaluación por esa mención. |

## 2. Contraste documental

Symfony (s. f.-d, apartado «Controllers») explica que los controladores deben contener código de enlace, sin lógica de negocio; el apartado sobre ParamConverters admite determinadas consultas desde controladores. Por tanto, no puede inferirse que cualquier consulta constituye mala arquitectura, ni que Symfony prescribe concentrar allí las reglas del dominio. Context7 devolvió ejemplos de una rama posterior, por lo que se verificó directamente la documentación **4.x**, correspondiente al contexto de SIGPP. Esta fuente contradice la generalización sobre la recomendación oficial, sin desmentir que el tesista haya aprendido mediante ejemplos simplificados.

FastAPI (s. f.) muestra agrupación de operaciones en APIRouter, módulos y dependencias, con ejemplos breves que incluyen condiciones en las funciones de ruta. Eso acredita contenido didáctico, no una prescripción universal para estructurar toda la lógica de una aplicación compleja. Tampoco establece una relación causal entre seguir un tutorial y desarrollar los problemas observados en SIGPP. La procedencia formativa del estilo de programación se conserva como explicación del tesista, no como resultado empírico de la investigación.

## 3. Título aprobado sin ampliar el alcance actual

> Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP.

El artefacto es el método; MVC caracteriza las aplicaciones y no los subcircuitos como si fueran arquitecturas autónomas. El contexto institucional se desarrolla en la delimitación y la aplicación POA permanece explícita. «Diseño y evaluación» es coherente con la construcción del método y su aplicación ya previstas; no acredita resultados ni convierte el trabajo en una comparación puramente descriptiva. La contribución de maestría sigue siendo conocimiento transferible expresado como principios de diseño evaluados, no una reorganización local del código.

La aprobación mantiene **MVC como límite de la clase de aplicaciones**; no adopta la alternativa más amplia por la mención de FastAPI. El título no elimina las restricciones institucionales del campo de acción ni permite generalizar a todas las aplicaciones MVC. Se conserva tipología método más instanciación y contribución prevista en principios de diseño, con originalidad y validación pendientes. Esta decisión es de formulación y alcance, no autoriza una nueva migración tecnológica.

## 4. Contexto histórico precisado por el tesista y contraste de Symfony 3.x

El tesista declara que SIGPP se desarrolló con Symfony 4 y que su aprendizaje se apoyó en un libro de Symfony 3, porque no disponía entonces de un libro oficial correspondiente a la versión utilizada. Se registra su experiencia sin volver a preguntarle por la versión. No se cuenta todavía con título, edición o pasajes del ejemplar concreto ni fecha precisa de lectura; por tanto, no se acredita que no existiera otra publicación oficial en ese momento. La documentación histórica consultada a continuación no se presenta como el libro que leyó.

Symfony (s. f.-b), en las buenas prácticas de controladores 3.x, recomienda controladores delgados y separación explícita de lógica de negocio, a la vez que acepta acoplar controladores al marco y muestra consultas Doctrine desde una acción. Symfony (s. f.-c), en el tutorial de persistencia 3.x, enseña creación de entidades, asignaciones, `persist()` y `flush()` dentro de una acción, pero también explica organización de consultas en repositorios. Existe una tensión real entre el ejemplo breve de integración y la estructura necesaria al crecer un flujo; documentarla no demuestra que el marco prescriba acumular reglas de negocio en controladores. Tampoco prueba que ese material sea la causa exclusiva de la evolución de SIGPP.

El tutorial describe la entidad como una clase PHP y permite metadatos de mapeo mediante anotaciones, YAML o XML (Symfony, s. f.-c). Integración con persistencia y dependencias concretas pueden generar costos de cambio o prueba, pero usar un ORM o mapear entidades no acredita por sí solo que todas las reglas de negocio deban depender del ORM. El método deberá identificar qué dependencias conviene aislar y cuáles se conservan justificadamente durante la transición. No se adopta reemplazo de Doctrine ni duplicación completa de entidades como consecuencia de esta discusión.

Symfony (s. f.-a) documenta `MicroKernelTrait` en la rama 3.x, con una aplicación mínima que devuelve JSON y la posibilidad de elegir componentes y estructura. Esa fuente impide presentar el uso mínimo o sin plantillas como una posibilidad exclusivamente reciente. Context7 volvió a recuperar ejemplos de documentación actual, por lo que el contraste histórico se realizó directamente en las páginas oficiales **3.x**; no se atribuyen a esa versión ejemplos actuales. Estas páginas archivadas consultadas hoy tampoco acreditan el texto exacto disponible en la fecha de aprendizaje del tesista sin cotejar una revisión fechada.

## Referencias verificadas

- FastAPI. (s. f.). *Bigger applications—Multiple files*. https://fastapi.tiangolo.com/tutorial/bigger-applications/ **[verificada: página oficial y apartados APIRouter y dependencias consultados el 26 de octubre de 2026; no estudio causal de enseñanza ni imposición de MVC]**
- Symfony. (s. f.-a). *Building your own framework with the MicroKernelTrait* (documentación 3.x). https://symfony.com/doc/3.x/configuration/micro_kernel_trait.html **[verificada: página oficial archivada, aplicación mínima JSON y selección de estructura/componentes; consultada el 28 de octubre de 2026]**
- Symfony. (s. f.-b). *Controllers* (documentación 3.x, buenas prácticas). https://symfony.com/doc/3.x/best_practices/controllers.html **[verificada: página oficial archivada, separación de lógica de negocio, consultas en acciones y acoplamiento de controladores; consultada el 28 de octubre de 2026]**
- Symfony. (s. f.-c). *Databases and the Doctrine ORM* (documentación 3.x). https://symfony.com/doc/3.x/doctrine.html **[verificada: página oficial archivada, entidades, metadatos de mapeo, persistencia en controladores y repositorios; consultada el 28 de octubre de 2026]**
- Symfony. (s. f.-d). *The Symfony framework best practices* (documentación 4.x). https://symfony.com/doc/4.x/best_practices.html **[verificada: página oficial de la versión, apartados Controllers, Business Logic y ParamConverters consultados el 26 de octubre de 2026]**
