# E4: fuentes locales y lectura focalizada de Feathers y Fowler

## Resultado y alcance de la revisión

**Fecha:** 21 de octubre de 2026. Se inventariaron nombres de archivos PDF/PDF en `/home/mario/Documents/libros/Software Engineering/` y sus subdirectorios. Se revisó el texto de *Working effectively with legacy code* aportado por el tesista y se extrajeron las páginas iniciales y las páginas impresas 45–47 del ejemplar local de *Refactoring*, segunda edición. No se leyó íntegramente toda la biblioteca ni se copiaron los libros al repositorio. Los archivos bibliográficos siguen fuera del trabajo versionado; el entregable de análisis es este Markdown.

Los PDF no son obligatorios como formato de referencia: lo necesario es acceso verificable al contenido que se utiliza. Pueden servir también ejemplares impresos o versiones editoriales en otro formato. Un título de archivo acredita localización, no año, edición, autoría ni lectura del contenido. Las fuentes fundacionales aportan sustento, pero no reemplazan el examen reciente necesario para contrastar el problema de investigación —que institucionalmente se registrará como problema científico—.

## Selección prioritaria de la biblioteca

Rutas relativas a `/home/mario/Documents/libros/Software Engineering/`:

| Archivo localizado | Prioridad y propósito | Verificación alcanzada |
|:--|:--|:--|
| `Object Oriented Programing/Working effectively with legacy code (Feathers, Michael C).pdf` | Principal: cambio seguro, dependencias, caracterización y responsabilidades. | Archivo localizado; contenido analizado desde el texto/figuras que aportó el tesista. No se afirma comparación binaria con el adjunto ni lectura lineal íntegra. |
| `Object Oriented Programing/Refactoring Improving the Design of Existing Code (Martin Fowler, Kent Beck).pdf` | Principal: transformación estructural frente a cambio funcional. | Portada, página legal, índice y pp. 45–47 contrastados directamente en el archivo; segunda edición, ISBN 978-0-13-475759-9. |
| `Object Oriented Programing/Practical object-oriented design an agile primer using Ruby.pdf` | Complementaria: dependencias y responsabilidades si las fuentes principales no cubren una decisión. | Solo archivo localizado; edición/contenido por verificar. |
| `arquitectura/Addison.Wesley.Implementation.Patterns.Nov.2007.pdf` | Complementaria: decisiones de implementación acotadas. | Solo archivo localizado; datos editoriales/contenido por verificar. |
| `Software_Requirements_3rd_Edition.pdf` y `Software_Requirements_3rd_ES.pdf` | Complementaria: especificación y trazabilidad, no eje de la arquitectura. | Archivos localizados; autoría, edición del ejemplar español y contenido por verificar. |
| `python/Architecture Patterns with Python (Harry Percival, Bob Gregory).pdf` | Posible contraste de límites y pruebas; no implica adoptar su arquitectura en SIGPP. | Solo archivo localizado; no se atribuyen resultados o recomendaciones. |
| Archivos de DDD, microservicios, desarrollo web, DevOps, sistemas operativos y editores. | No prioritarios para esta decisión: evitar ampliar el marco por disponibilidad de libros. | Inventario por nombre, sin evaluación de contenido. |

No se localizó por nombre *Software architecture in practice*, de Bass, Clements y Kazman, ni el libro metodológico de Wieringa en la ruta solicitada. Esto no acredita ausencia en otras unidades o archivos con nombres distintos. La siguiente fuente prioritaria a solicitar es la edición de Bass et al. (2021) ya registrada en el marco, para leer escenarios de modificabilidad/testabilidad y documentación de decisiones, no solo su índice editorial.

## Lectura directa de Feathers: decisiones que respalda

La portada identifica a Michael C. Feathers y a Prentice Hall Professional Technical Reference; la página legal consigna copyright 2005 y primera impresión en septiembre de 2004. Se conserva el año bibliográfico 2004 ya contrastado con la publicación editorial y se precisa el sello Prentice Hall PTR del ejemplar. Esa diferencia no se resuelve escogiendo automáticamente el año del copyright. La paginación impresa es el localizador de citas; el número de página del PDF incluye preliminares.

| Pasaje comprobado en el material aportado | Síntesis propia | Consecuencia candidata para el método |
|:--|:--|:--|
| Cap. 2, pp. 14–20; secuencia en p. 18. | Las dependencias pueden impedir poner pruebas; una separación conservadora inicial puede ser necesaria para obtener protección antes de cambios mayores. | No exigir pruebas unitarias completas antes de cualquier separación mínima. Identificar cambio, punto de prueba y riesgo residual antes de intervenir. |
| Cap. 3, pp. 21–28. | Separación permite ejecutar la pieza; observación permite detectar sus efectos. Un doble comprueba ciertas interacciones sin verificar el recurso real. | Documentar qué acredita cada prueba del servicio y qué requiere integración con persistencia/archivos. |
| Cap. 4, pp. 30–36 y 40–44. | Un punto de sustitución permite variar comportamiento en pruebas sin editar el punto de uso; debe existir un lugar donde se seleccione la alternativa. | Localizar cómo controlar repositorios, contexto o tiempo, sin convertir toda clase en una interfaz ni confundir configuración funcional con sustitución de pruebas. |
| Cap. 10, pp. 138–141. | Primero considerar prueba mediante interfaz pública; acceder por reflexión puede ayudar transitoriamente, pero no debe ocultar responsabilidades mezcladas. | Las caracterizaciones privadas existentes no se convierten en un requisito permanente de la arquitectura. Priorizar contrato público del servicio y del componente que se decida extraer. |
| Cap. 13, pp. 186–190 y 194–195. | La caracterización documenta comportamiento real, no el deseado; una extracción necesita verificar también su conexión con los consumidores. | Separar pruebas del comportamiento anterior de las de aceptación extraordinaria. Mantener casos de consumidor y punto de integración, no solo pruebas aisladas de la regla. |
| Cap. 20, pp. 249–251 y 265–268. | Las responsabilidades pueden identificarse por métodos, relaciones y decisiones susceptibles de cambiar; la separación se realiza según necesidad y riesgo, no como descomposición total inmediata. | El nuevo tipo de parámetro reutiliza un mecanismo real; no exige rehacer pantallas, permisos ni todos los servicios del subcircuito. |

Estas síntesis se basan en los pasajes comprobados del texto primario proporcionado (Feathers, 2004), no solo en el índice. Su aplicación a parámetros, fechas y Twig es razonamiento de este estudio, no un caso de SIGPP tratado por el autor. El material respalda una intervención incremental, pero no demuestra por sí solo utilidad, productividad o transferibilidad de la propuesta. Las mediciones y evaluación del método permanecen pendientes.

## Lectura directa de Fowler: separación de cambios

La portada local declara segunda edición, autor Martin Fowler y contribuciones de Kent Beck; el nombre del archivo no convierte automáticamente a Beck en coautor de la referencia. La página legal indica copyright 2019 y el ISBN 978-0-13-475759-9; se mantiene 2018 como año de publicación ya contrastado en la página del autor. En este ejemplar, las pp. impresas 45–47 corresponden a las páginas físicas 67–69 del PDF. Se verificó esa correspondencia mediante extracción selectiva, no mediante una suposición de desplazamiento para todas las páginas.

En «Defining Refactoring», Fowler (2018, pp. 45–46) diferencia transformaciones que preservan comportamiento observable de una reorganización genérica. En «The Two Hats», distingue añadir capacidades de refactorizar y explica que ambas actividades pueden alternarse en pasos cortos manteniendo clara su intención (pp. 46–47). Para el piloto, centralizar una regla sin alterar resultados es estructural; admitir registro extraordinario fuera del primer trimestre y mediante un nuevo tipo configurable incorpora una capacidad distinta. No se requiere separar artificialmente todo en dos proyectos, pero sí conservar pruebas y evidencia que permitan distinguir qué se preserva y qué cambia.

## Tensión de originalidad que debe resolverse

Feathers (2004, pp. 18–20) ya propone una secuencia para localizar cambios, identificar pruebas, romper dependencias, escribir pruebas y transformar el código. Por tanto, reproducir esos pasos con etiquetas locales no bastaría para demostrar una contribución original de maestría. Esta lectura debilita cualquier afirmación previa de inexistencia de un método incremental genérico, aunque todavía no resuelve si hay una brecha específica en la clase de contextos propuesta. La adaptación a SIGPP puede ser necesaria para la ingeniería sin constituir por sí sola conocimiento novedoso.

La pregunta pendiente es qué compromisos del método propuesto no quedan suficientemente resueltos por esos antecedentes y cómo se evaluarán: selección de intervención en un subcircuito institucional, reutilización de mecanismos de configuración, coherencia entre presentación y comprobación autoritativa, y trazabilidad entre extracción y ampliación funcional. Son dimensiones candidatas de contraste, no contribuciones ya originales o validadas. No se reformula la brecha a posteriori para garantizar novedad; debe contrastarse con literatura y artefactos existentes. El acceso a los libros permite ahora ese examen con mayor precisión, sin cerrar E4 automáticamente.

## Lectura del tesista para continuar

Primero lea Feathers (2004), pp. 18–20 y 186–190; después, pp. 249–251 y Fowler (2018), pp. 45–47. El producto de esa lectura debe ser una explicación propia de qué parte del cambio extraordinario conserva comportamiento, qué parte lo modifica y dónde se observará la conexión con el servicio que guarda. No se necesita leer ambos libros de principio a fin antes de responderlo. El asesor ya contrastó los pasajes indicados; eso no acredita que el tesista los haya leído o defendido.

## Referencias

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/ **[fuente institucional e índice editorial verificados previamente; ejemplar local no localizado por nombre; capítulos completos pendientes]**
- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055 **[publicación editorial y pasajes del ejemplar aportado contrastados; primera impresión 2004, copyright 2005]**
- Fowler, M. (2018). *Refactoring: Improving the design of existing code* (2nd ed.). Addison-Wesley Professional. https://martinfowler.com/books/refactoring.html **[publicación en página del autor y edición/pp. 45–47 en PDF local contrastadas; copyright 2019]**
