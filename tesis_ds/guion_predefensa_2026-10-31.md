# Predefensa: presentación del avance existente

**Tesista:** Mario Arturo Uriarte Marin.  
**Programa:** Maestría en Ingeniería de Software.  
**Tutor:** Luis Roberto Pérez Rios, Ph.D.  
**Fecha de presentación:** 31 de octubre de 2026.

## Alcance de este borrador

Preparación oral autorizada por el tesista el 30 de octubre, sin abrir trabajo nuevo de investigación. Se utiliza la síntesis documentada en `presentacion_propuesta_2026-10-31.md` y el IFI actualizado documentalmente al 30 de octubre. No es una traducción final a ALSIE, una investigación concluida ni una acreditación de cumplimiento del documento completo solicitado. La plantilla local de defensa final se adapta a una predefensa: no se fabrican hipótesis, modelo teórico o resultados ausentes para llenar sus bloques. El apoyo visual está en `diapositivas_predefensa_2026-10-31.md`; las notas siguientes son apoyos de explicación, no texto para memorizar ni evidencia de dominio del tesista.

**Tiempo objetivo:** 18 minutos de contenido y 2 minutos de margen dentro del máximo de 20. Esta es una distribución propuesta para ensayo, no una duración comprobada. No se programa demostración en vivo en este borrador; el caso se explica con evidencia documental existente, sin nuevas ejecuciones.

## Distribución para ensayo

| Diapositiva | Contenido | Duración | Acumulado |
|:--|:--|:--|:--|
| 1 | Título y compromiso del trabajo | 0:30 | 0:30 |
| 2 | Contexto y problema práctico | 1:30 | 2:00 |
| 3 | Pregunta y delimitación | 2:00 | 4:00 |
| 4 | Objetivo y aporte previsto | 1:30 | 5:30 |
| 5 | Fundamento y antecedentes | 1:30 | 7:00 |
| 6 | Propuesta en desarrollo | 2:00 | 9:00 |
| 7 | Caso documentado: selección de restricciones | 2:00 | 11:00 |
| 8 | Diagnóstico temporal y fuente funcional | 2:00 | 13:00 |
| 9 | Evaluación prevista e indicadores | 2:00 | 15:00 |
| 10 | Estado y límites de la contribución | 1:00 | 16:00 |
| 11 | Trabajo pendiente | 1:30 | 17:30 |
| 12 | Cierre | 0:30 | 18:00 |

## 1. Título y compromiso del trabajo

### Mostrar

**Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP.**

Mario Arturo Uriarte Marin · Maestría en Ingeniería de Software  
Tutor: Luis Roberto Pérez Rios, Ph.D.

### Apoyo oral

«Presento el avance de una propuesta de método para intervenir incrementalmente un sistema existente. El caso de aplicación es SIGPP; la investigación busca producir conocimiento sobre cómo seleccionar, proteger y verificar los cambios, no solamente reorganizar código. Distinguiré la evidencia disponible de los resultados que todavía deben obtenerse».

## 2. Contexto y problema práctico

### Mostrar

- SIGPP: Sistema Integral de Gestión POA Presupuesto, Caja Petrolera de Salud.
- Alcance: ejecución de la planificación operativa anual; certificación como incremento acotado.
- Señal técnica: reglas y consultas distribuidas entre controladores, servicios, persistencia y presentación.
- Restricción: evolucionar sin reescritura completa.

### Apoyo oral

«Soy creador y desarrollador principal de SIGPP, lo que facilita el acceso técnico y también introduce sesgo de constructor. La inspección encontró separación parcial, no ausencia total de arquitectura. El problema práctico es localizar y verificar decisiones distribuidas cuando cambian las reglas; todavía no he cuantificado su costo institucional ni una reducción del esfuerzo humano».

## 3. Pregunta y delimitación

### Mostrar

**Pregunta:** ¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos de aplicaciones MVC heredadas, sin requerir reescritura completa ni interrupción operativa?

- Objeto en Design Science: el método propuesto.
- Campo: subcircuitos MVC heredados con lógica dispersa y restricciones de continuidad.
- Fuera del alcance: migración integral, sustitución del marco y reescritura de SIGPP.

### Apoyo oral

«El problema de investigación, que en el formato institucional se registrará como problema científico, no es la ausencia de técnicas de refactorización. Se concentra en precisar y evaluar una adaptación para esta clase de intervención. En Design Science el objeto es el método; SIGPP es el contexto de aplicación. El IFI provisional utiliza una formulación institucional distinta del objeto, cuya armonización sigue pendiente y no constituye un cambio del compromiso científico».

## 4. Objetivo y aporte previsto

### Mostrar

**Objetivo general:** diseñar y evaluar el método para mejorar modificabilidad, testabilidad y trazabilidad de cambios sin reescritura completa.

**Recorrido de los seis objetivos:** diagnosticar → fundamentar → diseñar → aplicar → evaluar utilidad → formular y evaluar principios.

**Aporte previsto:** conocimiento transferible sobre selección, protección y verificación de incrementos; no el código de SIGPP por sí mismo.

### Apoyo oral

«El sexto objetivo hace explícita la contribución de conocimiento y ya fue incorporado al perfil. El método y su aplicación son el vehículo para evaluar decisiones de diseño. No presento principios validados: esa condición depende de la evaluación y de los límites que permita sostener la evidencia».

## 5. Fundamento y antecedentes

### Mostrar

| Antecedente | Consecuencia para la propuesta |
|:--|:--|
| Feathers (2004) | Proteger comportamiento y distinguir caracterización de comportamiento requerido. |
| Bass et al. (2021) | Evaluar cambios mediante escenarios; separar costo inicial y cambio posterior. |
| Girjoaba y Capiluppi (2024) | Base operativa aceptada para una adaptación acotada del ciclo. |

### Apoyo oral

«Estos antecedentes impiden reclamar como originales las pruebas, las iteraciones o la separación de responsabilidades. La revisión focalizada permitió seleccionar una base explícita en lugar de presentar una secuencia conocida como propia. La contribución potencial deberá estar en la adaptación justificada y su evaluación, no en la simple combinación de autores».

## 6. Propuesta en desarrollo

### Mostrar

- Selección proporcional al problema: una errata no exige reorganización arquitectónica.
- Distinguir comportamiento observado, requerido e intención del cambio.
- Identificar consumidores, dependencias y puntos de comprobación.
- Separar transformación inicial y cambio posterior.

**Estado:** orientaciones y adaptaciones candidatas; formalización completa pendiente.

### Apoyo oral

«La propuesta no obliga a crear una clase por cada regla. Se busca intervenir donde la dispersión de decisiones justifique el costo y el riesgo. Estas orientaciones ya están documentadas, pero no sustituyen la especificación pendiente de pasos, entradas, salidas y criterios; tampoco se presentan como un modelo teórico validado».

## 7. Caso documentado: selección de restricciones

### Mostrar

**Comparación:** `5313c0e1` → `8dc63307`.

| Antes | Después |
|:--|:--|
| Selección en dos consumidores | Delegación en un resolvedor compartido |
| Comportamiento examinado con instrumento común | Mismos casos comprobados tras la extracción |

**Registro:** 13 pruebas y 65 aserciones satisfactorias por estado comparado.

### Apoyo oral

«La comparación documentada permite mostrar centralización y conservación del comportamiento examinado. Es retrospectiva, realizada en el entorno actual con clases históricas y dobles; no reconstruye todo el sistema anterior. No demuestra por sí sola menos acoplamiento global, ahorro de esfuerzo ni eficacia del método completo».

## 8. Diagnóstico temporal y fuente funcional

### Mostrar

| Evidencia registrada | Qué permite afirmar |
|:--|:--|
| Cuestionario respondido por el Planificador Nacional | Se dispone de una fuente funcional y autorización académica acotada. |
| Fecha documental: 1 prueba, 1 aserción, 1 fallo | Se documentó avance hasta solicitar correlativo antes del rechazo requerido, con límites del instrumento. |
| Hora: 3 pruebas, 5 aserciones, 1 fallo | Distintas horas del mismo día produjeron distinta admisibilidad local. |

### Apoyo oral

«Estas comprobaciones permiten delimitar problemas, no validar toda la operación institucional. No son pruebas integrales por HTTP ni de persistencia real; se presentan los registros existentes, sin una nueva ejecución para esta exposición. La aclaración funcional actual se refiere al último día hábil de la gestión anterior; la formulación antigua de días fijos quedó superada y fue corregida en la actualización documental del IFI».

## 9. Evaluación prevista e indicadores

### Mostrar

| Indicador | Estado del avance |
|:--|:--|
| I01. Correspondencia de decisiones | Evidencia parcial; conjunto y criterios completos pendientes. |
| I02. Rechazo antes de efectos | Comprobaciones locales parciales; integración pendiente. |
| I03. Esfuerzo de comprobación | Procedimiento aceptado; sin línea base humana. |
| I04. Extensión de cambio posterior | Ampliación de ventana por configuración acordada; sin ejecución. |

**Secuencia comprometida:** evaluación para mejorar → rediseño documentado → evaluación final.

### Apoyo oral

«En I04 se acordó una ventana ficticia del 1 al 8 de febrero de 2027, ampliada al día 10, con seis casos de frontera. Eso es un escenario de prueba, no una apertura institucional autorizada ni un resultado obtenido. El registro de tiempo asistido no se convierte en esfuerzo humano. La evaluación deberá distinguir aplicabilidad del método, utilidad local y respaldo de los principios».

## 10. Estado y límites de la contribución

### Mostrar

**Disponible:** fundamentación y revisión focalizada; evidencia técnica parcial; fuente funcional recibida.

**No demostrado:** reducción del esfuerzo humano, mejora global de mantenibilidad, integración completa o principios validados.

**Amenazas identificadas:** sesgo del constructor, selección del caso, comparación retrospectiva y alcance local de pruebas.

### Apoyo oral

«No tengo todavía un modelo teórico original validado ni una hipótesis contrastada. La aspiración es una transferencia analítica a contextos semejantes, no una generalización estadística. La fuente funcional consultada tampoco reemplaza la revisión independiente del método».

## 11. Trabajo pendiente

### Mostrar

1. Completar línea base, criterios e instrumentos del diagnóstico.
2. Formalizar y aplicar el método, con alternativas y decisiones trazables.
3. Documentar evaluación para mejorar, rediseño y evaluación final.
4. Formular los principios que la evidencia permita sostener y armonizar el documento institucional.

**E4/E5 cerradas; E6 abierta; E7–E10 pendientes.**

### Apoyo oral

«Esta lista explicita el trabajo restante; no constituye un cronograma aprobado ni un compromiso de completarlo durante la preparación de mañana. El IFI fue actualizado al 30 de octubre con registros existentes, pero continúa siendo un avance provisional y no una investigación concluida. La predefensa permitirá recibir observaciones sobre la delimitación, la adaptación propuesta y la suficiencia de la evaluación prevista».

## 12. Cierre

### Mostrar

**Método propuesto, aplicación acotada y conocimiento por evaluar.**

### Apoyo oral

«El avance permite delimitar una intervención con evidencia técnica y antecedentes explícitos. El compromiso pendiente es formalizar y evaluar el método y determinar qué conocimiento puede sostenerse más allá de este caso. Gracias por sus observaciones».

## Preguntas previsibles del tribunal: respuestas de apoyo

Estas respuestas delimitan lo que permiten afirmar los documentos. El tesista debe explicarlas con sus palabras; no reemplazan comprensión ni constituyen decisiones nuevas. No se ha comprobado que el tribunal vaya a formular estas preguntas.

### ¿Qué tiene de nuevo si ya existen métodos de refactorización?

«No afirmo que las pruebas o los ciclos incrementales sean nuevos. La propuesta adapta una base existente para seleccionar y verificar intervenciones en subcircuitos MVC con decisiones distribuidas. La originalidad y utilidad de esas adaptaciones todavía deben evaluarse; no están demostradas por aplicarlas en otra institución o lenguaje».

**Respaldo:** IFI, secciones 1.2, 3.3 y 5.1; E5.

### ¿Esto es investigación o solamente una mejora de software?

«La mejora técnica por sí sola sería insuficiente. El compromiso de investigación incluye formalizar y evaluar un método y producir principios con contexto, mecanismo y límites que otro investigador pueda utilizar. Ese resultado de conocimiento sigue pendiente; la extracción actual no lo sustituye».

**Respaldo:** sexto objetivo y contribución prevista en el perfil; IFI, secciones 1.4 y 1.5.

### ¿Qué demuestra la comparación de trece pruebas?

«Demuestra que los casos examinados por el instrumento común tuvieron los resultados registrados en ambos estados. Se utilizaron clases históricas en el entorno actual con dobles, no una reconstrucción completa del sistema anterior. Por eso no infiero equivalencia universal, menor esfuerzo o mejora global de calidad».

**Respaldo:** `comparacion_extraccion_restriccion_2026-10-29.md`; IFI, sección 5.5.

### ¿Por qué presenta pruebas que fallan?

«Porque son evidencia de diagnóstico y no pruebas de éxito. Documentan diferencias entre un comportamiento requerido y el observado localmente. Sus límites impiden extrapolar el fallo a todo el recorrido HTTP o a persistencia real; tampoco demuestran que el método haya sido validado».

**Respaldo:** E6, registros temporales; IFI, secciones 2.3 y 5.5.

### ¿La habilitación extraordinaria ya funciona como propone?

«No está acreditada como capacidad implementada conforme a los acuerdos recientes. Se aceptaron definición única en servidor, autoridad temporal PHP y un escenario de ampliación por configuración. Los seis casos de frontera están acordados, pero el instrumento reproducible y la ejecución siguen pendientes».

**Respaldo:** acuerdos del 30 de octubre; IFI, sección 5.3 y anexo 2.

### ¿Dónde están su hipótesis y su modelo teórico?

«En este avance no dispongo de una hipótesis contrastada ni de un modelo teórico original sustentado y validado. El capítulo III mantiene ese vacío explícito. No presento la arquitectura candidata como sustituto ni convierto las orientaciones del método en relaciones teóricas demostradas».

**Respaldo:** IFI, secciones 1.5 y capítulo III. La respuesta reconoce un vacío; no lo resuelve ni garantiza aceptación institucional.

### ¿Cómo controla su sesgo como constructor de SIGPP?

«El sesgo está identificado, no eliminado. Se dispone de una fuente funcional consultada y de disponibilidad declarada de un revisor técnico, pero la revisión independiente del método sigue pendiente. La evaluación deberá separar los papeles de diseño y evaluación y conservar instrumentos y resultados trazables».

**Respaldo:** IFI, secciones 1.7 y 5.5; compromisos metodológicos del perfil.

### ¿Puede asegurar que concluirá en las fechas anunciadas?

«Las fechas comunicadas están registradas, pero todavía no hay un cronograma detallado aprobado que justifique asegurar el cierre de todo lo pendiente. No confundo la preparación de esta exposición con el avance de construcción y evaluación. Presento el estado real para recibir observaciones sin prometer resultados que no tengo».

**Respaldo:** estado general y compromisos pendientes del perfil. No sustituir esta respuesta por una promesa de validación en una semana sin un plan factible.

## Comprobación antes de presentar

- [ ] Explicar con palabras propias el problema, la diferencia frente a los antecedentes y el aporte previsto.
- [ ] Abrir las diapositivas y comprobar que todos los bloques y tablas sean legibles en la herramienta elegida.
- [ ] Ensayar de principio a fin y anotar duración real; el objetivo de 18 minutos no está medido.
- [ ] No alargar artificialmente una exposición breve leyendo notas ni añadir resultados para ocupar tiempo.
- [ ] Tener disponibles el IFI actualizado y los registros de respaldo, sin datos sensibles.
- [ ] Confirmar franja, enlace, audio y pantalla compartida.

**Si se aproxima el límite:** abreviar contexto y lista de antecedentes; conservar pregunta, contribución prevista, evidencia con límites y estado real. Las respuestas anteriores son para preguntas posteriores, no ocho bloques adicionales dentro de los 20 minutos. El margen de dos minutos pertenece al máximo de exposición; no presupone duración de preguntas autorizada por el tutor.

## Referencias para respaldo

Se reutilizan las verificaciones registradas en E4/E5 y en la síntesis de propuesta; no se efectuó una búsqueda bibliográfica nueva para este guion.

Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/

Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055

Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079

**Estado de verificación:** Bass y Feathers, verificados en E4; Girjoaba y Capiluppi, metadatos verificados en E5 y contenido consultado en manuscrito aportado, sin equivalencia editorial íntegra certificada.
