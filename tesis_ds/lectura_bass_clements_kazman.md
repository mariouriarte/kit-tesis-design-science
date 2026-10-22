# E4: lectura focalizada de Bass, Clements y Kazman

## Fuente y alcance comprobado

Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/

**Estado: verificada.** El tesista adjuntó el PDF de 687 páginas y su texto extraído. Portada y página legal identifican autores, cuarta edición, ISBN 978-0-13-688609-9 y copyright 2022. El catálogo del Software Engineering Institute confirma ese mismo ISBN y publicación el 3 de agosto de 2021; por ello se conserva 2021 en la referencia, distinguiéndolo del copyright. No se afirma que el tesista haya leído el libro por haberlo adjuntado ni que el asesor haya realizado una lectura lineal íntegra.

El archivo contiene una conversión de texto redistribuido: sus páginas físicas no coinciden con la paginación editorial. Para evitar localizadores falsos, las paráfrasis siguientes remiten a capítulos y secciones; se indican por separado las páginas físicas del adjunto para facilitar su consulta. No se utiliza un desplazamiento constante para convertir páginas. Este registro contiene síntesis propias, no reproducción de capítulos.

## Fundamento → consecuencia candidata para SIGPP

| Fundamento comprobado | Localizador del texto primario | Aplicación razonada al estudio, no afirmación de los autores sobre SIGPP |
|:--|:--|:--|
| Un atributo debe expresarse mediante fuente, estímulo, entorno, artefacto, respuesta y medida de respuesta. Decir solo «modificable» no especifica qué se evalúa. | Bass et al. (2021), secs. 3.2–3.3; PDF pp. 76–80. | Describir cambios concretos del subcircuito y su esfuerzo de implementación y prueba; no convertir «más modular» en criterio suficiente. |
| Deben distinguirse el costo de introducir un mecanismo de cambio y el de utilizarlo; la conveniencia depende de cambios previstos y restricciones. | Bass et al. (2021), introducción al cap. 8; PDF pp. 178–180. | Separar el costo inicial de incorporar el tipo extraordinario y conectarlo del costo posterior de configurar otra ventana. No prometer ahorro neto midiendo solo la configuración final. |
| Dividir módulos y redistribuir responsabilidades se justifican por cohesión y escenarios de cambio, no por cortar líneas de código. | Bass et al. (2021), sec. 8.2; PDF pp. 185–190. | Evaluar qué responsabilidades cambian juntas y cuáles deben quedar separadas; no contar clases nuevas como mejora demostrada. |
| Diferir la vinculación permite que un desarrollador prepare un mecanismo y un administrador lo utilice después mediante parámetros. | Bass et al. (2021), sec. 8.2, «Defer Binding»; PDF pp. 188–190. | Fundamenta conceptualmente la ventana configurable ya solicitada. No acredita que la extensión esté implementada ni impone una nueva infraestructura de configuración. |
| Testabilidad requiere controlar entradas y observar resultados; admite abstracción de fuentes y control del tiempo en pruebas, con costos de preparación. | Bass et al. (2021), cap. 12 y secs. 12.1–12.2; PDF pp. 284–299. | Proporcionar día de referencia y parámetros controlables; verificar decisión y efectos. Medir preparación/ejecución cuando corresponda, no solo número de pruebas exitosas. |
| Una interfaz incluye semántica, condiciones, efectos y errores, no únicamente firmas de métodos. | Bass et al. (2021), secs. 15.1–15.3; PDF pp. 335–350. | Explicitar día documental, gestión pertinente, motivo de rechazo y ausencia de persistencia ante rechazo. La semántica institucional procede del tesista, no del libro. |
| ADD contempla iteraciones, refinamiento de elementos existentes, alternativas, registro de decisiones y análisis de lo producido. | Bass et al. (2021), secs. 20.1–20.2; PDF pp. 426–434. | Es antecedente del método incremental que debe compararse; no llamar original a la mera sucesión de analizar, diseñar, probar y revisar. No se adopta ADD como proceso de investigación DS por incorporar esta fuente. |
| La evaluación ligera analiza escenarios y riesgos; el libro reconoce menor objetividad de una revisión interna. | Bass et al. (2021), secs. 21.3 y 21.6; PDF pp. 453–454 y 472–475. | Posible apoyo a revisión formativa futura, sujeto a selección metodológica. No equivale por sí sola a evaluación sumativa del método ni sustituye independencia de evaluadores. |
| Las vistas se eligen por finalidad; la justificación registra alternativas, supuestos y riesgos mientras se decide. | Bass et al. (2021), secs. 22.3 y 22.7; PDF pp. 482–489 y 503–505. | Mantener vista de responsabilidades/dependencias y descripción de la secuencia antes de efectos. No exigir todos los diagramas posibles ni registrar justificaciones como si hubieran precedido a intervenciones anteriores. |

## Tensión y límites de inferencia

La fuente fortalece la fundamentación, pero también hace más exigente la justificación de novedad. ADD ya aborda diseño incremental de sistemas existentes, y las tácticas de parametrización y pruebas controlables son antecedentes explícitos (Bass et al., 2021, caps. 8, 12 y 20). La posible contribución debe distinguirse mediante adaptaciones justificadas y evidencia de aplicación, no por combinar nombres de prácticas conocidas. El problema de investigación —que institucionalmente se registrará como problema científico— sigue requiriendo contraste de la brecha; no queda demostrado por disponer de este libro.

Un mecanismo adicional puede reducir el trabajo de cambios posteriores y, al mismo tiempo, aumentar el costo y complejidad iniciales. La evaluación deberá considerar esa tensión si se reclama eficiencia; no se trasladan umbrales ilustrativos del libro a SIGPP. Tampoco se infiere mejora empírica de testabilidad por reducir acoplamiento, ni se interpreta una suite exitosa como ausencia universal de defectos. No se extraen cifras de ahorro de otros casos para atribuirlas al piloto.

## Siguiente trabajo acotado

La carencia de acceso al texto de Bass et al. queda resuelta por el adjunto, aunque su ruta local no fue comunicada. Para el tesista se priorizan las secciones 3.3, 8.2 y 12.1–12.2; los capítulos 20–22 se usan después para contrastar procedimiento y documentación. Corresponde relacionar estas fuentes con las decisiones candidatas ya registradas y distinguir costos iniciales de costos de uso, sin implementar ni fijar metas numéricas retrospectivas. E4 permanece abierta: la recepción del libro no cierra las lecturas recientes pendientes, la defensa del tesista ni la justificación de las decisiones restantes.
