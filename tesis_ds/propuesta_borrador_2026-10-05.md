# Borrador de propuesta para revisión — 5 de octubre de 2026

## Datos generales

- **Tesista:** Mario Arturo Uriarte Marin
- **Programa:** Maestría en Ingeniería de Software
- **Tutor:** Luis Roberto Pérez Rios, Ph.D.
- **Enfoque metodológico:** Design Science
- **Estado del documento:** borrador de propuesta para revisión; requiere todavía fortalecimiento bibliográfico reciente, formalización de indicadores y validación del plan de evaluación.

## Propósito del entregable

Este documento presenta una propuesta preliminar de investigación bajo Design Science. Su propósito es permitir la revisión del tutor sobre la coherencia entre problema, artefacto, alcance, evaluación y contribución esperada. No constituye todavía el perfil institucional final ni el capítulo completo de tesis; es un borrador de trabajo para validar si la dirección elegida es metodológicamente defendible antes de avanzar a construcción y evaluación.

El punto central que debe revisarse es si el artefacto propuesto —un método de refactorización arquitectónica incremental— responde al problema identificado en SIGPP y, al mismo tiempo, produce conocimiento transferible a una clase de sistemas semejantes. Si el documento se lee solo como una mejora técnica de SIGPP, la propuesta queda corta; si promete una teoría general de modernización de sistemas heredados, sobrealcanza. La tesis se ubica deliberadamente en el nivel intermedio exigido para maestría: principios de diseño validados mediante una instanciación evaluada.

## Título provisional

**Método de refactorización arquitectónica incremental para subcircuitos heredados MVC institucionales: instanciación en la ejecución POA de SIGPP**

El título declara el artefacto principal —un método—, la clase de problema —refactorización arquitectónica incremental de subcircuitos heredados MVC institucionales— y el contexto de instanciación —la ejecución POA de SIGPP—. Esta formulación evita presentar la tesis como una mejora local del sistema y orienta el trabajo hacia una contribución de nivel de maestría: principios de diseño derivados del diseño, construcción y evaluación del artefacto.

## Contexto del problema

SIGPP, Sistema Integral de Gestión POA Presupuesto, es un sistema institucional de la Caja Petrolera de Salud usado para procesos de planificación, seguimiento y ejecución presupuestaria. El área dueña del sistema es el Departamento Nacional de Gestión y Planificación. En el alcance de esta propuesta, el foco no es todo SIGPP, sino el subcircuito de ejecución POA, donde convergen tareas, operaciones/ACP, presupuesto asignado, kardex presupuestario, disponibilidad y certificación.

La inspección inicial del repositorio muestra una aplicación PHP 7.4 con Symfony 4.4, Doctrine ORM, controladores MVC, servicios, repositorios, formularios, plantillas Twig, autenticación web y algunos puntos de exposición API. Esta estructura sostiene operación institucional real, pero el subcircuito seleccionado presenta señales de deuda arquitectónica: lógica de negocio distribuida entre capas técnicas, dependencia directa de componentes del marco de trabajo, consultas SQL especializadas y pruebas focalizadas insuficientes sobre reglas críticas.

## Problema de diseño

El problema de diseño en SIGPP es que el subcircuito de ejecución POA —tareas vinculadas a operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita. Su lógica se encuentra distribuida y acoplada entre controladores MVC, servicios, repositorios, entidades Doctrine y consultas SQL, lo que dificulta modificar una tarea y sus efectos presupuestarios o certificables de manera controlada, trazable y verificable mediante pruebas automatizadas.

El costo visible del problema es técnico e institucional. Cada cambio sobre el flujo puede exigir revisar varias capas del sistema, conocer reglas implícitas dispersas y asumir riesgo de regresión en presupuesto, kardex o certificación. La existencia de PHPUnit en el proyecto no resuelve el problema por sí sola, porque la línea base muestra vacíos de pruebas focalizadas en componentes críticos como `KardexPresupuesto`, `CreateCertificacionService` y `TareaOneLineSql`.

## Problema de investigación

El problema de investigación —que en el formato institucional se registrará como **problema científico**— se ubica en la brecha entre principios generales de arquitectura, refactorización y testabilidad, y la falta de un método incremental, aplicable y evaluable para refactorizar subcircuitos heredados MVC institucionales sin detener ni reescribir el sistema completo.

La tesis no sostiene que la separación de responsabilidades, las pruebas automatizadas o la refactorización sean conceptos nuevos. Lo que se busca generar es conocimiento prescriptivo y transferible sobre cómo traducir esos principios en un método aplicable bajo restricciones reales: continuidad operativa, sistema institucional en producción, datos sensibles, normativa administrativa y necesidad de evolución sin reescritura completa.

## Objeto de estudio

En Design Science, el objeto de estudio no es SIGPP ni el proceso POA en sí mismo. La resignificación metodológica es explícita: el objeto de estudio es el artefacto propuesto. En esta investigación, el objeto de estudio es un **método de refactorización arquitectónica incremental para subcircuitos heredados MVC institucionales**, instanciado en SIGPP.

La tipología del artefacto es una composición. El componente principal es el método, porque define pasos, criterios, entradas, salidas y condiciones de aplicación. La instanciación en SIGPP funciona como vehículo de construcción, demostración y evaluación del método, no como contribución aislada.

## Campo de acción

El campo de acción comprende subcircuitos funcionales críticos de sistemas heredados MVC institucionales, con lógica de negocio dispersa, alto acoplamiento al marco de trabajo y a la persistencia, y necesidad de evolución sin reescritura completa.

En esta tesis, el campo se concreta en el subcircuito de ejecución POA de SIGPP. Elaboración POA, validación ministerial y evaluación POA trimestral se mantienen como contexto y alcance posterior recomendado, porque incluirlos en la intervención principal produciría sobrealcance y debilitaría la evaluación.

## Pregunta de investigación

¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos en sistemas heredados MVC institucionales, sin requerir reescritura completa ni interrupción operativa?

## Objetivo general

Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos heredados MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.

## Objetivos específicos

1. Diagnosticar el estado arquitectónico y de testabilidad del subcircuito de ejecución POA en SIGPP mediante análisis de controladores, servicios, repositorios, entidades, consultas SQL y pruebas existentes.
2. Sistematizar la base de conocimiento sobre arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas heredados MVC.
3. Diseñar el método de refactorización arquitectónica incremental, definiendo pasos, criterios, entradas, salidas y condiciones de aplicación.
4. Instanciar el método en el subcircuito de ejecución POA de SIGPP, manteniendo compatibilidad funcional y usando datos ficticios en entorno controlado.
5. Evaluar la utilidad del método mediante métricas técnicas, revisión independiente y validación institucional acotada.

## Fundamentación teórica inicial

El marco teórico se organiza en tres ejes. El primer eje es código heredado y cambio seguro. Feathers (2004) es una fuente central porque plantea que trabajar con código heredado exige introducir puntos de prueba y romper dependencias antes de modificar comportamiento crítico. En esta tesis, ese fundamento se traduce en una decisión de diseño: el método no debe comenzar con una reorganización masiva del código, sino con la captura del comportamiento actual mediante pruebas de caracterización o pruebas focalizadas sobre reglas críticas.

La lectura realizada hasta el momento enfatiza un punto crítico para SIGPP: la ausencia de pruebas unitarias o focalizadas no es solo una carencia técnica, sino una restricción de diseño. Por ello, el método debe tratar la falta de pruebas como condición de entrada y no como actividad opcional al final de la refactorización. En términos prácticos, antes de mover reglas presupuestarias, separar responsabilidades o introducir una frontera de aplicación, el comportamiento actual del flujo debe quedar protegido por pruebas que permitan detectar regresiones.

El segundo eje es arquitectura como gestión de fronteras, dependencias y atributos de calidad. Bass et al. (2021) permiten sostener que la arquitectura no se reduce a carpetas o capas nominales, sino a decisiones estructurales que afectan modificabilidad, testabilidad y evolución. Por ello, la propuesta no promete migrar SIGPP a una arquitectura limpia o hexagonal completa; esa promesa sería metodológicamente excesiva y técnicamente riesgosa. El diseño se concentra en introducir una frontera incremental para el subcircuito seleccionado.

El tercer eje es refactorización controlada y verificable. Fowler (2018) define la refactorización como mejora del diseño interno mediante cambios pequeños que preservan comportamiento. Aplicado al caso, el método debe exigir pasos acotados, reversibles y verificables, con criterios de éxito definidos antes de la construcción. Desde Design Science, Hevner et al. (2004), Peffers et al. (2007), Wieringa (2014) y Venable et al. (2016) sustentan que el artefacto debe construirse y evaluarse con criterios explícitos, evitando definir indicadores después de ver resultados.

## Línea base técnica inicial

La línea base estática inicial del subcircuito tarea-presupuesto-certificación identifica 11 archivos críticos y aproximadamente 4177 líneas acumuladas. La medición evidencia que la complejidad no está concentrada en una sola clase, sino distribuida entre entidades, controladores, servicios, repositorios, SQL nativo y puntos API.

| Indicador observado | Resultado inicial | Interpretación |
|---|---:|---|
| Archivos críticos medidos directamente | 11 | Núcleo mínimo del circuito tarea-presupuesto-certificación. |
| Líneas acumuladas en archivos críticos | 4177 | Volumen suficiente para justificar intervención arquitectónica acotada. |
| Instanciaciones directas `new` en archivos críticos | 46 | Señal de construcción manual de objetos y acoplamiento procedimental. |
| Llamadas a `getDoctrine()` en controladores críticos de tarea | 2 | Persistencia usada desde controladores en puntos del flujo. |
| Ocurrencias de SQL nativo o construcción SQL en archivos críticos | 9 | Dependencia directa de consultas especializadas difíciles de aislar. |
| Métodos privados en `CreateCertificacionService` | 13 | Reglas internas de certificación no expuestas como componentes verificables de forma independiente. |

La línea base de pruebas muestra que existen referencias a tareas, presupuesto y certificación en pruebas, pero también vacíos relevantes. No se observaron pruebas focalizadas para `KardexPresupuesto`, `CreateCertificacionService` ni `TareaOneLineSql`, lo que refuerza la necesidad de incorporar testabilidad como parte constitutiva del método y no como actividad posterior.

## Propuesta de artefacto

El artefacto propuesto es un método de refactorización arquitectónica incremental para subcircuitos heredados MVC institucionales. El método debe guiar la intervención de un subcircuito crítico sin exigir reescritura completa, actualización mayor de marco de trabajo, migración a microservicios ni rediseño total de base de datos.

De forma preliminar, el método se estructura en seis actividades:

1. **Selección del subcircuito crítico:** identificar un flujo funcional con impacto institucional, evidencia de deuda arquitectónica y posibilidad de medición antes/después.
2. **Caracterización del comportamiento actual:** levantar reglas, rutas, datos, dependencias y pruebas existentes; cuando no existan pruebas suficientes, definir pruebas de caracterización.
3. **Definición de frontera funcional:** declarar qué comportamiento pertenece al subcircuito y qué queda fuera, evitando expandir el alcance durante la construcción.
4. **Extracción incremental de responsabilidades:** separar progresivamente lógica de controladores, entidades persistentes, consultas y servicios acoplados, preservando compatibilidad funcional.
5. **Verificación interna:** aplicar pruebas focalizadas, revisión técnica y medición de acoplamiento, complejidad, cobertura y trazabilidad.
6. **Evaluación y rediseño:** ejecutar un ciclo formativo con revisión y ajuste del método, seguido de una evaluación sumativa sobre los criterios definidos.

## Alcance de la instanciación en SIGPP

La instanciación se concentrará en el subcircuito de ejecución POA: tareas, operaciones/ACP, presupuesto asignado, kardex presupuestario y certificación asociada. Los componentes principales observados incluyen `NewTareaController`, `EditTareaController`, `Tarea`, `PresupuestoAsignado`, `KardexPresupuesto`, `Certificacion`, `CreateCertificacionService`, `TareaRepository`, `TareaOneLineSql`, `TareaOneLineController` y `CertificacionOneLineController`.

Quedan fuera de la intervención principal la elaboración POA, la validación ministerial, la evaluación POA trimestral, la refactorización completa de SIGPP, la migración a microservicios, la actualización mayor de Symfony, el rediseño completo de base de datos y el reemplazo total de Doctrine ORM. Esta delimitación no reduce el rigor; lo protege.

## Estrategia de evaluación preliminar

La evaluación debe demostrar utilidad práctica y contribución de conocimiento. Para nivel de maestría, el mínimo metodológico será un ciclo formativo con rediseño documentado y un ciclo sumativo. La evaluación formativa permitirá detectar fallas del método antes de consolidarlo; la evaluación sumativa comparará el resultado contra la línea base y los criterios definidos previamente.

| Momento | Propósito | Evidencia prevista |
|---|---|---|
| Diagnóstico inicial | Confirmar problema y línea base | Métricas estáticas, revisión de pruebas, análisis de componentes críticos. |
| Evaluación formativa | Mejorar el método antes de consolidarlo | Revisión técnica independiente, aplicación piloto parcial, registro de cambios al método. |
| Rediseño | Documentar aprendizaje del ciclo formativo | Decisiones ajustadas, pasos modificados, criterios refinados sin alterar resultados a posteriori. |
| Evaluación sumativa | Comparar antes/después y juzgar utilidad | Métricas técnicas, pruebas focalizadas, trazabilidad del cambio, validación institucional acotada. |

Los criterios preliminares de éxito son: explicitación de una frontera arquitectónica para el subcircuito, reducción de lógica en controladores intervenidos, incremento de pruebas sobre reglas críticas, disminución de dependencias directas del marco de trabajo y la persistencia en lógica de aplicación, mantenimiento de compatibilidad funcional y documentación de un método replicable para subcircuitos semejantes.

Para evitar evaluación definida a posteriori, estos criterios deberán convertirse en indicadores operacionales antes de construir. La propuesta no puede declarar éxito únicamente porque el código “quedó más limpio” o porque el sistema continúa funcionando. Debe mostrar evidencia antes/después sobre propiedades observables: dispersión de lógica, acoplamiento, cobertura o existencia de pruebas focalizadas, complejidad, trazabilidad del cambio y revisión técnica independiente.

## Contribución esperada

La contribución original preliminar consiste en formular y evaluar principios de diseño para aplicar refactorización arquitectónica incremental en subcircuitos heredados MVC institucionales. El aporte no es solamente que SIGPP quede mejor organizado, sino que otro investigador o practicante pueda usar los principios del método para diseñar un artefacto distinto ante un problema de la misma clase.

La oración candidata de contribución es la siguiente:

> Esta investigación aporta principios de diseño validados para refactorizar incrementalmente subcircuitos funcionales críticos en sistemas heredados MVC institucionales, mediante un método que explicita fronteras funcionales, separa reglas de negocio de controladores y persistencia, e incorpora pruebas automatizadas sin exigir reescritura completa ni interrupción operativa.

## Riesgos y mitigaciones

| Riesgo | Impacto | Mitigación |
|---|---|---|
| Sobrealcance por incluir todo SIGPP o todo el ciclo POA. | Alto | Mantener la intervención en ejecución POA; registrar otros módulos como contexto o trabajo futuro. |
| Sesgo del constructor por ser el tesista creador y desarrollador principal de SIGPP. | Alto | Incorporar revisión técnica independiente y evidencia técnica reproducible. |
| Datos sensibles de certificaciones o presupuesto. | Alto | Usar datos ficticios y consentimiento institucional acotado. |
| Falta de pruebas existentes en componentes críticos. | Medio | Introducir pruebas de caracterización antes de refactorizar comportamiento relevante. |
| Prometer arquitectura limpia o hexagonal completa. | Alto | Declarar explícitamente que la intervención busca frontera incremental, no migración total. |

## Puntos que deben defenderse ante el tutor

| Punto crítico | Defensa breve |
|---|---|
| Por qué no se refactoriza todo SIGPP. | Una tesis de maestría requiere alcance evaluable; el subcircuito de ejecución POA es suficientemente complejo, medible y representativo. |
| Por qué el objeto de estudio no es SIGPP. | En Design Science, el objeto de estudio es el artefacto; SIGPP es la instanciación que permite construir y evaluar el método. |
| Por qué no se promete arquitectura limpia o hexagonal completa. | Una migración completa agregaría complejidad, riesgo y sobrealcance; el aporte es una frontera incremental verificable. |
| Por qué Feathers es relevante. | Justifica proteger comportamiento mediante pruebas antes de intervenir código heredado con dependencias fuertes. |
| Cómo se evita que sea solo ingeniería. | La tesis extrae principios de diseño validados, no solo una mejora local del sistema. |
| Cómo se evaluará. | Con línea base, ciclo formativo con rediseño, ciclo sumativo, métricas técnicas y revisión independiente. |

## Pendientes antes de cerrar la propuesta

- Completar literatura reciente verificada sobre deuda técnica arquitectónica, testabilidad y refactorización de sistemas heredados MVC o monolíticos.
- Formalizar indicadores de E6 con fórmula, herramienta, fuente de datos, línea base y valor esperado.
- Definir el alcance exacto del ciclo formativo y del ciclo sumativo.
- Preparar instrumentos de revisión técnica independiente.
- Actualizar la matriz de coherencia cuando se definan requisitos y alternativas del artefacto.

## Criterio de revisión del borrador

Este borrador está listo para revisión inicial si el tutor puede responder afirmativamente a tres preguntas: primero, si el problema práctico está suficientemente situado en SIGPP; segundo, si el artefacto propuesto es un método y no solo una intervención técnica local; tercero, si la evaluación prevista puede producir evidencia antes/después sin depender de datos sensibles reales. Si alguna de esas respuestas es negativa, la propuesta debe ajustarse antes de avanzar a construcción.

## Referencias citadas

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/
- Feathers, M. C. (2004). *Working effectively with legacy code*. Pearson. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055
- Fowler, M. (2018). *Refactoring: Improving the design of existing code* (2nd ed.). Addison-Wesley Professional. https://martinfowler.com/books/refactoring.html
- Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. *MIS Quarterly, 28*(1), 75–105. https://doi.org/10.2307/25148625
- Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. *Journal of Management Information Systems, 24*(3), 45–77. https://doi.org/10.2753/MIS0742-1222240302
- Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: A framework for evaluation in design science research. *European Journal of Information Systems, 25*(1), 77–89. https://doi.org/10.1057/ejis.2014.36
- Wieringa, R. J. (2014). *Design science methodology for information systems and software engineering*. Springer. https://doi.org/10.1007/978-3-662-43839-8
