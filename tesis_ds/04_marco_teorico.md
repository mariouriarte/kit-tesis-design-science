# Marco teórico: sustentación del objeto de estudio

## Propósito del marco teórico

Este marco teórico sustenta el objeto de estudio de la tesis: un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP. El marco no se orienta a describir de forma general la arquitectura de software, Symfony o Doctrine, sino a justificar las decisiones de diseño que debe incorporar el método: selección de un subcircuito crítico, creación de una frontera arquitectónica explícita, desacoplamiento progresivo de reglas de negocio, incorporación de pruebas focalizadas y medición antes/después.

La prueba de eliminación es estricta: si una fuente no modifica el diseño del método, no pertenece al marco teórico principal. Bajo ese criterio, el marco se organiza en tres ejes: código heredado y cambio seguro; arquitectura como gestión de fronteras, dependencias y atributos de calidad; y testabilidad como condición para refactorización incremental.

## Pregunta de búsqueda teórica

¿Qué fundamentos de ingeniería de software permiten diseñar un método incremental para refactorizar subcircuitos funcionales críticos en sistemas legacy MVC institucionales, mejorando modificabilidad y testabilidad sin reescritura completa ni interrupción operativa?

## Criterios preliminares de inclusión y exclusión

Se incluyen fuentes que cumplan al menos una de estas condiciones: definen técnicas para intervenir código heredado con bajo riesgo; explican la arquitectura como conjunto de decisiones estructurales que afectan atributos de calidad; relacionan modificabilidad, testabilidad, acoplamiento y evolución de software; o fundamentan la evaluación de artefactos de Design Science. Se excluyen fuentes que solo describen buenas prácticas genéricas de Symfony, migraciones completas a microservicios o arquitectura hexagonal, o recomendaciones sin conexión directa con decisiones evaluables del método.

## Eje 1: código heredado y cambio seguro

La tesis parte de una condición típica de sistemas legacy: el sistema funciona y sostiene operación institucional, pero su estructura dificulta cambios seguros. En SIGPP, esta condición se observa en el circuito tarea-presupuesto-certificación: 11 archivos críticos acumulan aproximadamente 4177 líneas, existen 46 instanciaciones directas `new`, se identifican consultas SQL nativas o construidas manualmente, y hay ausencia de pruebas focalizadas sobre `KardexPresupuesto`, `CreateCertificacionService` y `TareaOneLineSql`. Esta evidencia orienta el método hacia intervención incremental, no hacia reescritura.

Feathers (2004) es central para este eje porque plantea estrategias prácticas para trabajar con código heredado sin reescribirlo, especialmente mediante pruebas que permitan detectar cambios no intencionales y técnicas para romper dependencias. Esta fuente justifica que el método empiece por identificar puntos de cambio, puntos de prueba y dependencias que impiden aislar reglas críticas. En la tesis, esto se traduce en una decisión de diseño: antes de extraer o reorganizar lógica, el método debe incorporar pruebas de caracterización o pruebas focalizadas que capturen el comportamiento actual del subcircuito intervenido.

La lectura parcial realizada por el tesista en torno a la ausencia de pruebas unitarias refuerza una decisión metodológica clave: la falta de pruebas no debe registrarse solo como defecto técnico del sistema, sino como condición de entrada del método. En un sistema heredado, la primera acción responsable no es mover código para que parezca mejor organizado, sino crear una red mínima de verificación sobre el comportamiento existente. Esta lectura conecta directamente con la línea base de SIGPP, donde existen pruebas relacionadas con tareas y algunas referencias a presupuesto o certificación, pero no se observaron pruebas focalizadas para `KardexPresupuesto`, `CreateCertificacionService` ni `TareaOneLineSql`.

Fowler (2018) complementa este eje al definir la refactorización como una técnica controlada para mejorar el diseño de código existente mediante transformaciones pequeñas que preservan comportamiento. Su aporte no debe usarse como una lista decorativa de técnicas, sino como principio de diseño del método: cada paso de refactorización debe ser pequeño, verificable y reversible en caso de romper comportamiento del circuito. En consecuencia, el método no prometerá “limpiar” todo SIGPP, sino ejecutar una secuencia acotada sobre el subcircuito seleccionado.

## Eje 2: arquitectura como fronteras, dependencias y atributos de calidad

La tesis no usará “arquitectura” como sinónimo de carpetas, capas nominales o adopción completa de una arquitectura limpia o hexagonal. Para este trabajo, arquitectura significa el conjunto de decisiones estructurales que determinan responsabilidades, dependencias, límites y facilidad de cambio. Esta definición operativa es necesaria porque el problema de SIGPP no es la ausencia de un patrón arquitectónico de moda, sino la ausencia de una frontera explícita en el circuito tarea-presupuesto-certificación.

Bass, Clements y Kazman (2021) permiten fundamentar esta lectura porque explican la arquitectura en relación con atributos de calidad como modificabilidad y testabilidad. Esta fuente justifica que el método mida el impacto de la intervención no solo por líneas movidas o clases creadas, sino por la reducción de dependencias directas, la localización de reglas críticas y la capacidad de verificar cambios mediante pruebas. Para SIGPP, esta perspectiva evita una promesa excesiva: no se afirma que el sistema alcanzará arquitectura hexagonal, sino que el subcircuito intervenido tendrá una frontera arquitectónica más explícita y evaluable.

La decisión metodológica derivada es clara: la propuesta debe rechazar migraciones arquitectónicas totales —por ejemplo, microservicios, actualización mayor de Symfony o reemplazo de Doctrine— porque agregarían complejidad y desviarían el problema de investigación. La contribución de maestría está en formular principios de diseño para introducir frontera, desacoplamiento y pruebas dentro de restricciones reales de continuidad operativa.

## Eje 3: testabilidad, acoplamiento y evaluación técnica

La testabilidad no es un complemento posterior de la refactorización; es una condición para que el cambio sea controlable. En el circuito medido, PHPUnit ya está configurado, pero la línea base muestra vacíos importantes: no se observaron pruebas focalizadas para `KardexPresupuesto`, `CreateCertificacionService` ni `TareaOneLineSql`. Esto permite formular un requisito del método: cada extracción o separación de responsabilidad debe producir una unidad verificable o, al menos, una prueba de comportamiento que reduzca el riesgo de cambio.

Desde Design Science, Hevner et al. (2004), Peffers et al. (2007), Wieringa (2014) y Venable et al. (2016) sustentan que el artefacto debe construirse y evaluarse con criterios explícitos. En esta tesis, esos criterios serán modificabilidad, testabilidad, acoplamiento, complejidad, mantenibilidad y trazabilidad del cambio. La evaluación no puede definirse después de la refactorización; los indicadores deben fijarse antes para evitar racionalización posterior.

La línea base inicial ya ofrece indicadores útiles: tamaño de componentes críticos, instanciaciones directas, llamadas a persistencia desde controladores, ocurrencias de SQL nativo, rutas/controladores expuestos y vacíos de pruebas. Sin embargo, para cerrar E6 se deberán completar métricas dinámicas: complejidad ciclomática por método, cobertura efectiva del flujo, archivos modificados para cambios representativos, esfuerzo de modificación y trazabilidad entre cambio funcional, código y prueba.

## Decisiones de diseño sustentadas por la base teórica

| Decisión de diseño prevista | Fuente teórica principal | Aplicación al método |
|---|---|---|
| Intervenir un subcircuito crítico y no todo SIGPP. | Feathers (2004); Wieringa (2014) | Seleccionar un alcance donde sea posible observar problema, aplicar el método y evaluar antes/después sin reescritura completa. |
| Introducir una frontera arquitectónica incremental, no una migración completa a arquitectura limpia o hexagonal. | Bass et al. (2021); Fowler (2018) | Separar responsabilidades y dependencias donde exista mayor impacto sobre modificabilidad y testabilidad. |
| Proteger comportamiento existente antes de modificarlo. | Feathers (2004); Fowler (2018) | Incorporar pruebas de caracterización o pruebas focalizadas sobre reglas críticas del circuito. |
| Refactorizar mediante pasos pequeños y verificables. | Fowler (2018) | Evitar cambios masivos; cada paso debe tener entrada, salida, criterio de verificación y razón de diseño. |
| Medir antes/después con indicadores definidos previamente. | Hevner et al. (2004); Peffers et al. (2007); Venable et al. (2016) | Usar métricas de acoplamiento, complejidad, cobertura, mantenibilidad y trazabilidad como criterios de evaluación del artefacto. |
| Formular la contribución como principios de diseño, no como mejora local de SIGPP. | Gregor y Hevner (2013); Wieringa (2014) | Extraer conocimiento transferible para subcircuitos legacy MVC institucionales semejantes. |

## Fuentes verificadas inicialmente

Las siguientes fuentes fueron verificadas en fuentes editoriales o institucionales durante esta etapa:

- Bass, Clements y Kazman (2021), verificada en el sitio del Software Engineering Institute de Carnegie Mellon University.
- Feathers (2004), verificada en InformIT/Pearson.
- Fowler (2018), verificada en el sitio oficial de Martin Fowler.
- Hevner et al. (2004), Peffers et al. (2007), Gregor y Hevner (2013), Venable et al. (2016) y Wieringa (2014), tomadas del capítulo de referencias del libro base de Design Science usado en el repositorio.

## Estado de E4

E4 queda iniciada con un marco teórico estructuralmente coherente, pero no cerrada. Para cerrar la etapa se requiere completar la búsqueda de literatura reciente sobre refactorización de sistemas legacy, deuda técnica arquitectónica, testabilidad y evolución de sistemas MVC o monolíticos, preferentemente con revisiones sistemáticas o estudios empíricos publicados en los últimos cinco años.
