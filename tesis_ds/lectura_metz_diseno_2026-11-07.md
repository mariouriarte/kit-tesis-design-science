# Lectura focalizada de Metz: decisiones de diseño y alcance de la evidencia

## 1. Ejemplar y verificación

El tesista aporta «PDF 1», con 281 páginas, texto extraído e imágenes de páginas, de la segunda edición de *Practical object-oriented design: An agile primer using Ruby*, de Sandi Metz. La portada y la página de título confirman autora, título y edición; la página legal, página 7 del PDF, indica copyright 2019 de Pearson e ISBN 978-0-13-445647-8. La ficha editorial primaria ya consultada confirma Addison-Wesley Professional y distingue publicación comercial de agosto de 2018 de copyright 2019. Se conserva Metz (2019) como identificación del ejemplar aportado, sin confundir esas fechas.

La lectura se concentra en las páginas impresas 29–32, correspondientes a páginas 52–55 del PDF, capítulo 2, sección 2.3.2. Se cotejan también las cautelas de páginas impresas 9–10 y 13 sobre métricas y calidad, y el cierre del ejemplo en página 33. No se afirma revisión exhaustiva de los nueve capítulos. El ejemplar aportado permite resolver la literalidad antes pendiente en esta asesoría, sin solicitar nuevamente el libro.

## 2. Pasajes cotejados y límites de interpretación

Los fragmentos siguientes son citas breves del original; las interpretaciones son síntesis propias. La selección no pretende convertir las recomendaciones del libro en mediciones del caso SIGPP. Se respetan las páginas impresas y no se utilizan las páginas del archivo como localizador bibliográfico.

| Localizador APA 7 | Fragmento cotejado | Interpretación y límite |
|:--|:--|:--|
| Metz (2019, p. 29) | “Methods, like classes, should have a single responsibility.” | Apoya separar responsabilidades a nivel de método, no solo de clase. No prescribe una cantidad universal de métodos ni acredita una mejora medida del caso. |
| Metz (2019, p. 30) | “The refactoring introduces an additional message send” | En ese momento del ejemplo se prioriza código modificable y se permite posponer optimización si hiciera falta. No afirma que cualquier cantidad de llamadas sea gratuita o que no deba considerarse rendimiento en otros contextos. |
| Metz (2019, p. 30) | “it merely reorganizes code that is currently in use” | La reorganización del ejemplo trabaja sobre comportamiento existente; su reutilización es un beneficio del diseño mostrado. No demuestra que toda división imaginable evite sobrediseño. |
| Metz (2019, pp. 31–32) | “Expose previously hidden qualities”; “Avoid the need for comments”; “Encourage reuse”; “Are easy to move to another class” | Los dos primeros beneficios aparecen en p. 31 y los dos últimos en p. 32. No se añade «simplificar pruebas» como cita textual de esta enumeración. |
| Metz (2019, p. 32) | “Small methods lower the barriers to improving your design.” | Fundamenta la intención de facilitar reorganizaciones posteriores; no mide costo o esfuerzo en SIGPP. |
| Metz (2019, p. 32) | “Don’t decide; preserve your ability to make a decision later.” | Debe leerse junto con la alternativa de crear una clase `Wheel` si las circunstancias lo permiten. El ejemplo aísla responsabilidad sin comprometer una clase independiente; no prohíbe extraer clases ni prescribe específicamente métodos privados PHP. |

Las citas más largas aportadas por el tesista se corresponden con los pasajes examinados en esas páginas, incluidas las omisiones indicadas. Para una cita final debe transcribirse solo el fragmento necesario y señalar las omisiones sin unir frases como si fueran continuas. Si se traduce, se identifica la traducción propia y se mantiene el localizador. No es necesario reproducir todas las citas en el cuerpo de la tesis o en una diapositiva.

## 3. Contraste con la intervención de importe

La intervención de SIGPP divide operaciones de `topeCertificacion()` y centraliza el cálculo del total para reutilizarlo desde `create()`. Esta decisión es consistente con responsabilidad acotada y reutilización del comportamiento existente en Metz (2019, pp. 29–32). La decisión del autor de no extraer una clase puede fundamentarse como compromiso de diseño contextual, no como obligación deducida del libro. La analogía no acredita por sí sola que la solución sea óptima o que todo el servicio tenga responsabilidad única.

| Nivel de afirmación | Qué corresponde sostener |
|:--|:--|
| Fundamento de diseño | La separación de operaciones y la reutilización se alinean con criterios de responsabilidad única y reorganización incremental de Metz. |
| Resultado estructural observado | Un cálculo implementado en dos lugares pasa a uno; métodos activos 14 → 18; llamadas internas contadas textualmente 16 → 21, con reservas por comentarios. |
| Conservación comprobada | Cinco escenarios A01–A05 con prueba final reproducida y controles de interacciones mediante dobles; no equivalencia universal. |
| Análisis posterior de cambios hipotéticos | Se cuentan lugares potenciales de edición; no se ejecutan esos cambios ni se mide su esfuerzo. |
| Beneficio esperado | Facilitar comprensión, reutilización o cambios posteriores como justificación de diseño, no mejora empírica de mantenibilidad demostrada en este estudio. |

La cautela no contradice el libro: Metz (2019, pp. 9–10) distingue métricas de indicadores directos de calidad y advierte que buenos valores no garantizan que el siguiente cambio sea fácil o barato. También reconoce que aplicar principios o patrones correctamente no garantiza por sí solo una aplicación fácil de cambiar (Metz, 2019, p. 13). Por ello, reemplazar «mejor mantenibilidad» por «mejor diseño» sin decir bajo qué criterios dejaría una afirmación demasiado amplia. Se debe declarar la mejora estructural concreta y la justificación teórica, conservando la ausencia de una medición de cambio real.

## 4. Redacción propuesta para tesis y exposición

La intervención separó operaciones y centralizó el cálculo del total, manteniendo el comportamiento en los cinco escenarios examinados. Esta organización es consistente con los criterios de responsabilidad única y reutilización descritos por Metz (2019, pp. 29–32). Su selección tiene, por tanto, una justificación de diseño explícita; no demuestra una reducción del costo de cambio o una mejora empírica de mantenibilidad, porque los cambios posteriores no se ejecutaron ni se cronometraron.

Para una lámina puede utilizarse la síntesis: **«Separación de operaciones y cálculo reutilizado, fundamentados en Metz; conservación comprobada en cinco casos; mantenibilidad no medida»**. Los recuentos estructurales son apoyo descriptivo, no el titular de una mejora global del sistema. El ejemplo académico derivado puede incluir esta justificación sin reproducir el libro o sustituir la evidencia del episodio.

## 5. Cronología y alcance metodológico

La incorporación y el cotejo del ejemplar en esta asesoría ocurren después de la aplicación de importe. El registro de aquella aplicación ya invocaba Metz, pero no se utiliza esta recepción para afirmar que la lectura precedió a la extracción o para introducir criterios de éxito retrospectivos. Es fundamentación complementaria de una decisión documentada, no una evaluación adicional de mantenibilidad ni validación de PA1–PA3 por autoridad bibliográfica. Posteriormente se adoptó la contribución acotada y se cerró E10; ese dictamen y el control final, no este cotejo por sí solo, habilitan la traducción documental.

## Referencia

Metz, S. (2019). *Practical object-oriented design: An agile primer using Ruby* (2nd ed.). Addison-Wesley Professional. https://www.informit.com/store/practical-object-oriented-design-an-agile-primer-using-9780134456478

**Estado:** metadatos editoriales verificados y ejemplar primario aportado cotejado en los localizadores descritos. No se copia el PDF ni se declara que el archivo binario haya sido almacenado en este repositorio.
