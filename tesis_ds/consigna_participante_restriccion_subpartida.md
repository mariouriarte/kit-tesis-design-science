# Consigna de aplicación del método: selección de restricción de subpartida

**Estado:** borrador para revisión del tesista; no entregar ni ejecutar todavía. Debe completarse la preparación del entorno y aprobarse el protocolo antes de la sesión. Esta cabecera podrá sustituirse por la identificación de la sesión cuando esas condiciones estén resueltas.

## 1. Contexto funcional y técnico

SIGPP apoya la gestión del POA y el presupuesto de la Caja Petrolera de Salud. En el subcircuito de certificación se consulta si existe una restricción aplicable a la subpartida asociada con una tarea. Para esta actividad se estudia únicamente cómo se selecciona esa restricción, no todas las consecuencias posteriores de la certificación.

La decisión observada utiliza información de la tarea y de las restricciones configuradas. En el recorrido documentado se recarga la tarea por su identificador, se consulta una restricción específica para su actividad y, si no existe, se consulta una restricción general sin actividad. El resultado puede ser una restricción específica, una general o ausencia de restricción. Este es un contrato técnico observado que se comprobará en la copia preparada, no una nueva aprobación normativa.

El estado de partida contiene lógica de selección repetida en un controlador y en un servicio. El problema de mantenimiento consiste en que una misma decisión debe examinarse en más de un lugar y podría evolucionar de manera divergente. No se ha medido un costo de mantenimiento atribuible a esa repetición; corresponde examinar y justificar la intervención, no asumir que cualquier duplicación exige una arquitectura nueva.

## 2. Historia de usuario de mantenimiento

> **Como** desarrollador encargado del mantenimiento del subcircuito de certificación de SIGPP, **quiero** intervenir de forma acotada la lógica repetida de selección de restricciones de subpartida, **para** reducir el riesgo de divergencia entre sus consumidores y poder verificar la conservación del comportamiento durante el cambio.

Es una historia de mantenimiento para una tarea de investigación controlada. No representa una nueva solicitud institucional ni exige ampliar las funciones que reciben los usuarios del sistema.

## 3. Encargo

Aplique el método de refactorización incremental entregado por separado. Delimite la decisión y sus consumidores, compruebe su comportamiento actual, justifique la intervención mínima que considere pertinente y verifique sus resultados. Si encuentra que una instrucción no es aplicable, es ambigua o exige información que no tiene, registre la dificultad y su motivo; no improvise silenciosamente un significado.

La solución no tiene que adoptar un nombre de clase ni una estructura predeterminados. Puede conservar dependencias del sistema existente si justifica esa decisión. Si concluye que no conviene transformar la lógica, documente el análisis y las pruebas que lo sustentan; esa conclusión también se registrará, sin presentarla como implementación realizada.

## 4. Alcance y restricciones

- Trabajar solo en la copia aislada y la referencia entregadas al iniciar la sesión; no intervenir producción ni utilizar datos o credenciales productivas.
- Examinar la selección de restricción y sus consumidores identificados. No modificar fechas de habilitación, ventanas extraordinarias, reglas presupuestarias o funcionalidades ajenas al incremento.
- No introducir cambios funcionales intencionales en esta tarea. Si observa una posible anomalía del comportamiento, documentarla y separarla de la transformación conservadora; no corregirla silenciosamente.
- No se exige migrar toda la aplicación, sustituir Symfony o Doctrine ni demostrar independencia total de la infraestructura.
- Se permite consultar documentación y asistentes de IA, conservando las consultas y respuestas relevantes para las decisiones, los cambios y las pruebas. No introducir información institucional sensible en esos servicios.
- Explicar y comprobar las decisiones adoptadas, incluidas las sugeridas por IA. La ayuda del tesista y las incidencias del entorno se registrarán por separado; no se interpretarán como desempeño autónomo.

## 5. Comportamientos que se propone comprobar

**Criterios aceptados por el tesista el 5 de noviembre de 2026**, mediante la respuesta «acepto», antes de ejecutar la nueva aplicación controlada. Son criterios de conservación para una tarea histórica seleccionada retrospectivamente; su aceptación previa a esta sesión no los convierte en criterios prospectivos de la extracción histórica. No son resultados obtenidos ni exigencias de reproducir una implementación anterior.

| Situación | Resultado técnico esperado según el antecedente documentado |
|:--|:--|
| C01. Hay restricción específica para la actividad de la tarea. | Se selecciona la específica. |
| C02. No hay específica, pero existe una general sin actividad. | Se selecciona la general. |
| C03. No existe restricción específica ni general. | Se obtiene ausencia de restricción. |
| C04. Se produce una excepción al recargar la tarea o consultar la restricción. | Se conserva la propagación observada, sin convertir silenciosamente el fallo en ausencia de restricción. |
| C05. El servicio conserva previamente un resultado restringido y una nueva selección no encuentra restricción. | El resultado de la nueva selección no conserva indebidamente la restricción anterior. |

Las comprobaciones deben cubrir los consumidores pertinentes al alcance confirmado y compararse antes y después donde corresponda. No se impone un número de pruebas, uso de reflexión ni estructura del conjunto histórico; el participante justificará sus puntos de observación. Lo que no pueda verificarse deberá declararse como límite.

## 6. Productos de trabajo solicitados

Entregue una nota Markdown con delimitación, comportamiento observado, intención de cambio, decisiones y alternativas, dudas y ayudas recibidas, y correspondencia entre los pasos del método y lo realizado. Adjunte la identificación de la referencia inicial y final, las diferencias de código y pruebas, y los resultados verificables de las comprobaciones. El código y las pruebas se conservarán en la copia de trabajo; la nota registrará cómo localizarlos y reproducirlos.

Cuando corresponda registrar esfuerzo, se utilizará únicamente el procedimiento fijado antes de comenzar. Los tiempos no se reconstruirán después. Al finalizar, explique con sus palabras qué instrucciones le ayudaron a decidir y cuáles necesitaron aclaración, sin obligación de emitir una valoración favorable.

## 7. Material y consulta durante la sesión

Recibirá una copia identificada del método, el entorno preparado y esta consigna. Podrá pedir aclaraciones funcionales o técnicas, que se conservarán junto con su respuesta. No recibirá la implementación histórica resuelta ni sus pruebas como modelo que deba copiar; si accede a ellas por cualquier vía, deberá informarlo para registrar el momento y su posible influencia.
