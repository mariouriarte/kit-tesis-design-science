# E3. Perfil de investigación Design Science

## Título provisional

**Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP.**

El tesista aprobó esta formulación el 28 de octubre de 2026. El título declara el artefacto —método—, las actividades de diseño y evaluación, la clase de aplicaciones —MVC heredadas— y el contexto de aplicación —ejecución POA de SIGPP—. «Institucional» caracteriza las restricciones organizacionales del campo de acción, no una variante arquitectónica de MVC. La revisión terminológica no agrega FastAPI como caso ni extiende la evidencia a todas las aplicaciones MVC; los documentos de entregas anteriores conservan su título histórico.

## Planteamiento preliminar del problema

En SIGPP, el subcircuito de ejecución POA —tareas vinculadas a operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita. La lógica del flujo se encuentra distribuida y acoplada entre controladores MVC, servicios, repositorios, entidades Doctrine y consultas SQL, por lo que modificar una tarea y sus efectos presupuestarios o certificables exige intervenir múltiples capas y resulta difícil de validar con pruebas automatizadas.

El problema de investigación —que en el formato institucional se registrará como **problema científico**— no consiste en afirmar que arquitectura, refactorización o pruebas sean ideas nuevas. Se estudia qué adaptación de los principios conocidos permitiría seleccionar y verificar incrementos en subcircuitos de aplicaciones MVC heredadas, bajo las restricciones del campo definido, sin detener ni reescribir el sistema completo. La insuficiencia de las soluciones existentes sigue siendo una brecha candidata por contrastar en E4 y E5; no se sostiene ausencia genérica de métodos incrementales ni que los marcos obliguen a concentrar lógica de negocio en controladores. Este refinamiento se registra después del contraste bibliográfico del 26 de octubre, no como formulación demostrada desde el encuadre.

## Objeto de estudio

En Design Science, el objeto de estudio es el artefacto propuesto, no SIGPP ni el proceso POA. El objeto de estudio es un **método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas**, cuya aplicación y evaluación se realizarán en SIGPP.

La tipología del artefacto es una **composición**: método + instanciación. El método constituye el componente transferible; la instanciación en SIGPP constituye el vehículo de construcción, demostración y evaluación.

## Campo de acción

El campo de acción comprende subcircuitos funcionales críticos de aplicaciones MVC heredadas en contextos institucionales, con lógica de negocio dispersa, alto acoplamiento al marco de desarrollo y a la persistencia, y necesidad de evolución sin reescritura completa. Son condiciones del contexto y del problema a contrastar, no atributos inherentes a MVC ni a toda aplicación institucional.

En esta tesis, el campo se concreta en el subcircuito de ejecución POA de SIGPP: tareas, operaciones/ACP, presupuesto y certificación. Elaboración POA, validación ministerial y evaluación POA trimestral se consideran contexto y alcance posterior recomendado, no intervención principal.

## Propuesta

Se propone diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos funcionales críticos de aplicaciones MVC heredadas, aplicado en el subcircuito de ejecución POA de SIGPP, con el fin de explicitar fronteras funcionales, separar reglas de negocio de controladores y persistencia, e incorporar pruebas automatizadas que permitan evolucionar el flujo sin reescritura completa.

## Contribución original preliminar

**Base operativa aceptada el 28 de octubre de 2026:** el método se diseñará como una adaptación explícita del ciclo de Girjoaba y Capiluppi (2024), complementada con cambio seguro de Feathers (2004) y razonamiento por atributos y refinamiento de ADD (Bass et al., 2021). No se reclama autoría sobre los pasos heredados ni se presume originalidad por combinarlos. La adaptación y el conocimiento que pueda generar deberán contrastarse y evaluarse dentro del campo definido; no cambia el título ni la tipología método más instanciación.

El tesista precisó que su aplicación debe ser selectiva y proporcional al comportamiento, dependencias y riesgo: no se fuerza reorganización arquitectónica ante una errata de presentación. Cuando una modificación de negocio afecte decisiones dispersas, el método deberá orientar su investigación y protección antes de elegir una intervención focalizada. Un servicio nuevo es una opción de diseño, no una salida obligatoria para todos los cambios; concentrar toda lógica del subcircuito tampoco es el objetivo. La selección y sus efectos deberán documentarse y evaluarse, no darse por correctos por seguir el ciclo.

La contribución original preliminar consiste en formular y evaluar principios de diseño para aplicar refactorización arquitectónica incremental en subcircuitos de aplicaciones MVC heredadas, mostrando cómo traducir principios conocidos de separación de responsabilidades y testabilidad en un método aplicable bajo restricciones reales de continuidad operativa, normativa institucional y datos sensibles. La originalidad y la validación siguen pendientes; el título no las acredita.

Oración candidata de contribución original, en nivel de maestría:

> Esta investigación aporta principios de diseño validados para refactorizar incrementalmente subcircuitos funcionales críticos de aplicaciones MVC heredadas, mediante un método que explicita fronteras funcionales, separa reglas de negocio de controladores y persistencia, e incorpora pruebas automatizadas sin exigir reescritura completa ni interrupción operativa.

## Pregunta de investigación preliminar

¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos de aplicaciones MVC heredadas, sin requerir reescritura completa ni interrupción operativa?

## Subpreguntas preliminares

1. ¿Qué evidencias técnicas muestran la dispersión de lógica, el acoplamiento y la baja testabilidad del subcircuito de ejecución POA en SIGPP?
2. ¿Qué propiedades debe tener un método de refactorización arquitectónica incremental para ser aplicable en subcircuitos de aplicaciones MVC heredadas bajo las restricciones institucionales declaradas?
3. ¿En qué medida la instanciación del método en SIGPP mejora la separación de responsabilidades, la trazabilidad del cambio y la validación automatizada del flujo intervenido?

## Objetivo general preliminar

Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.

## Objetivos específicos preliminares

1. Diagnosticar el estado arquitectónico y de testabilidad del subcircuito de ejecución POA en SIGPP mediante análisis de controladores, servicios, repositorios, entidades, consultas SQL y pruebas existentes.
2. Sistematizar la base de conocimiento sobre arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas legacy MVC.
3. Diseñar el método de refactorización arquitectónica incremental, definiendo pasos, criterios, entradas, salidas y condiciones de aplicación.
4. Instanciar el método en el subcircuito de ejecución POA de SIGPP, manteniendo compatibilidad funcional y usando datos ficticios en entorno controlado.
5. Evaluar la utilidad del método mediante métricas técnicas, revisión independiente y validación institucional acotada.

## Estrategia metodológica preliminar

El estudio seguirá el enfoque de Design Science, con construcción y evaluación del artefacto. Para nivel de maestría, se planifica al menos un ciclo de evaluación formativa con rediseño documentado y un ciclo sumativo. La evaluación deberá distinguir utilidad práctica del método en SIGPP y contribución de conocimiento mediante principios de diseño transferibles analíticamente a aplicaciones MVC heredadas bajo condiciones semejantes a las del campo de acción.

## Criterios preliminares de evaluación

- Reducción de lógica del flujo en controladores o capas técnicas no apropiadas.
- Separación explícita de reglas de negocio respecto al marco MVC y la persistencia.
- Incremento de pruebas automatizadas sobre el flujo intervenido.
- Trazabilidad entre cambio funcional, componente afectado y prueba de validación.
- Comprensibilidad y aplicabilidad revisadas por un desarrollador independiente del equipo.

## Pendientes para cerrar E3

- Completar cronograma preliminar hasta predefensa y defensa.
- Preparar anexos mínimos para presentación del lunes 28 de septiembre.

## Cierre preliminar de E3

E3 queda cerrado de forma preliminar para el perfil inicial. La pregunta de investigación incluye el caso de instanciación en SIGPP sin perder el nivel de clase requerido por Design Science, y la contribución original se formuló en una sola oración aceptada por el tesista. El perfil deberá fortalecerse en E4 y E5 con fuentes verificadas y en E6 con indicadores operacionales antes de iniciar la construcción del artefacto.
