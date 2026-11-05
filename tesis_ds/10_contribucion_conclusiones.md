# E10. Contribución y conclusiones

**Estado:** en curso. La contribución de una tesis de maestría en Design Science no es el artefacto, sino los **principios de diseño** que el artefacto permite articular. El método y la instanciación son el vehículo; los principios son el conocimiento. Se formulan con objetivo, contexto y mecanismo, y se declaran sus condiciones de contorno y su grado de validación.

## 1. Naturaleza de la contribución

La contribución es de nivel de clase, no una teoría general ni la aplicación de una técnica ajena. Consiste en **principios de diseño formulados** para refactorizar incrementalmente subcircuitos de aplicaciones MVC heredadas, sustentados por la fundamentación (E4) y por la evidencia técnica parcial (E8). Se declara con honestidad que la validación empírica es limitada: no hubo evaluación de campo, por lo que los principios se presentan como **candidatos sustentados**, no como principios validados en múltiples contextos.

Esta distinción es deliberada. Reclamar principios «validados» sin evaluación de campo excedería la evidencia. Reclamar solo «una mejora en SIGPP» perdería la contribución. La formulación intermedia —principios sustentados y con condiciones de contorno— es la que la evidencia soporta.

## 2. Principios de diseño

Cada principio se expresa con objetivo, contexto, mecanismo y consecuencia. La plantilla sigue el esquema de Wieringa: para lograr O en contexto C, el método debe P, porque M.

**P1 — Selección proporcional del incremento.** Para delimitar un incremento sin sobre-intervenir (O) en subcircuitos MVC heredados con decisiones de negocio distribuidas (C), el método debe seleccionar la intervención por la decisión que motiva el cambio y sus consumidores, no por la estructura de carpetas (P), porque una decisión viva justifica investigar comportamiento y dependencias, mientras una corrección de presentación no lo hace (M).

**P2 — Caracterizar antes de mover.** Para conservar el comportamiento al desplazar lógica heredada (O) cuando la regla reside en controlador o vista (C), el método debe fijar el comportamiento actual con pruebas de caracterización antes de transformar (P), porque sin una red de seguridad que capture lo que el código hace no se distingue preservación de cambio intencional (M).

**P3 — Autoridad de la decisión en el servidor.** Para evitar decisiones divergentes (O) cuando una regla se valida tanto en servidor como en interfaz (C), el método debe aplicar la decisión autoritativa en el servidor y dejar a la interfaz solo representándola (P), porque reglas duplicadas entre capas divergen y dejan de distinguir casos límite, como el límite 8/9 (M).

**P4 — Separar transformación de capacidad nueva.** Para atribuir resultados con trazabilidad (O) cuando una intervención mezcla intenciones distintas (C), el método debe separar la transformación conservadora de la corrección o extensión funcional (P), porque mezclarlas impide saber si el resultado se debe a la refactorización o a la capacidad añadida (M).

**P5 — Evaluar por escenarios, no por recuentos.** Para afirmar modificabilidad y testabilidad sin sobre-afirmar (O) en una aplicación de caso único (C), el método debe evaluar con escenarios de cambio y condiciones explícitas, no con recuentos de clases o de pruebas (P), porque los recuentos locales pueden ser favorables sin que el subcircuito mejore (M).

## 3. Condiciones de contorno

Los principios aplican a la clase delimitada: subcircuitos funcionales críticos de aplicaciones MVC heredadas, con lógica de negocio dispersa entre interfaz, configuración y coordinación, en contextos institucionales que exigen evolución sin reescritura completa. No se generalizan a:

- Sistemas sin marco MVC o con dominio independiente de la infraestructura.
- Migraciones completas a arquitecturas limpias o hexagonales.
- Contextos sin una fuente funcional que ratifique las reglas de negocio.
- Afirmaciones causales o transferencia estadística desde un único caso.

La generalización es **analítica**: un investigador ante un problema estructuralmente similar puede usar estos principios para diseñar un método distinto, pero no se acredita que obtendrá los mismos resultados en otro contexto.

## 4. Amenazas a la validez y límite de la evidencia

Se retoman de E8. La amenaza principal es externa: la evaluación fue técnica y analítica, sin campo. La interna: el antecedente de 2025 no fue producido por el método formalizado, por lo que no se atribuye causalidad al método sobre él. La de constructo: I04 no se midió y la modificabilidad queda argumentada. La de conclusión: se acota la contribución a lo que la evidencia soporta, sin reclamar validación empírica no obtenida.

## 5. Conclusiones

La tesis entregó un método de refactorización incremental formalizado (pasos P1–P8, requisitos R1–R14), una instanciación parcial verificada, un diagnóstico que localizó la brecha de la decisión temporal, y cinco principios de diseño con condiciones de contorno. No entregó una solución completa a la decisión temporal ni una validación de campo; ambas limitaciones están declaradas, no ocultadas.

La contribución defendible es: ante un subcircuito MVC heredado con una decisión distribuida, el conocimiento generado permite **seleccionar el incremento, caracterizarlo, aplicar la autoridad en servidor y evaluarlo por escenarios**, con evidencia de que la dispersión es real y de que la separación parcial es viable. Eso es conocimiento de maestría, no de grado, siempre que se declare su alcance.

## 6. Trabajo futuro

1. Construir la capacidad extraordinaria y medir I04 (modificabilidad por configuración), cerrando la limitación declarada.
2. Corregir el límite 8/9 aplicando P1–P8 y medir I01–I02 con persistencia real.
3. Aplicar el método a un segundo subcircuito o sistema para fortalecer la validez externa.
4. Evaluar el esfuerzo I03 con una comparación equivalente, no solo descriptiva.

## 7. Gate de E10

El gate exige: contribución formulada como principios con contexto y mecanismo; condiciones de contorno explícitas; y ninguna afirmación que exceda la evidencia. Las secciones anteriores proponen ese cumplimiento. Corresponde al tesista validar o corregir, en particular si algún principio no refleja una decisión que él sostenga o si la formulación de la contribución le parece demasiado fuerte o demasiado débil.

**Cierre, 4 de noviembre de 2026:** el tesista valida la formulación de la contribución —«esta perfecto»—. El gate de E10 se cumple: la contribución está formulada como principios con contexto y mecanismo, las condiciones de contorno son explícitas y ninguna afirmación excede la evidencia.
