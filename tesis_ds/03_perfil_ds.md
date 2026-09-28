# E3. Perfil de investigación Design Science

## Título provisional

**Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales: instanciación en la ejecución POA de SIGPP**

El título declara el tipo de artefacto —método—, la clase de problema —refactorización arquitectónica incremental de subcircuitos legacy MVC institucionales— y el contexto de instanciación —ejecución POA de SIGPP—. Evita formular el trabajo como simple desarrollo o mejora de sistema, y orienta la contribución hacia conocimiento transferible.

## Planteamiento preliminar del problema

En SIGPP, el subcircuito de ejecución POA —tareas vinculadas a operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita. La lógica del flujo se encuentra distribuida y acoplada entre controladores MVC, servicios, repositorios, entidades Doctrine y consultas SQL, por lo que modificar una tarea y sus efectos presupuestarios o certificables exige intervenir múltiples capas y resulta difícil de validar con pruebas automatizadas.

El problema de investigación —que en el formato institucional se registrará como **problema científico**— no consiste en afirmar que la arquitectura, la refactorización o las pruebas sean ideas nuevas. La brecha preliminar es que existe una distancia entre principios generales de arquitectura y testabilidad, por un lado, y un método incremental, aplicable y evaluable para refactorizar subcircuitos legacy MVC institucionales sin detener ni reescribir el sistema completo, por otro. Esta brecha deberá verificarse con bibliografía y análisis de soluciones existentes en E4 y E5.

## Objeto de estudio

En Design Science, el objeto de estudio es el artefacto propuesto, no SIGPP ni el proceso POA. El objeto de estudio es un **método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales**, instanciado en SIGPP.

La tipología del artefacto es una **composición**: método + instanciación. El método constituye el componente transferible; la instanciación en SIGPP constituye el vehículo de construcción, demostración y evaluación.

## Campo de acción

El campo de acción comprende subcircuitos funcionales críticos de sistemas legacy MVC institucionales con lógica de negocio dispersa, alto acoplamiento al marco de trabajo y a la persistencia, y necesidad de evolución sin reescritura completa.

En esta tesis, el campo se concreta en el subcircuito de ejecución POA de SIGPP: tareas, operaciones/ACP, presupuesto y certificación. Elaboración POA, validación ministerial y evaluación POA trimestral se consideran contexto y alcance posterior recomendado, no intervención principal.

## Propuesta

Se propone diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos funcionales críticos en sistemas legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, con el fin de explicitar fronteras funcionales, separar reglas de negocio de controladores y persistencia, e incorporar pruebas automatizadas que permitan evolucionar el flujo sin reescritura completa.

## Contribución original preliminar

La contribución original preliminar consiste en formular y evaluar principios de diseño para aplicar refactorización arquitectónica incremental en subcircuitos legacy MVC institucionales, mostrando cómo traducir principios conocidos de separación de responsabilidades y testabilidad en un método aplicable bajo restricciones reales de continuidad operativa, normativa institucional y datos sensibles.

Oración candidata de contribución original, en nivel de maestría:

> Esta investigación aporta principios de diseño validados para refactorizar incrementalmente subcircuitos funcionales críticos en sistemas legacy MVC institucionales, mediante un método que explicita fronteras funcionales, separa reglas de negocio de controladores y persistencia, e incorpora pruebas automatizadas sin exigir reescritura completa ni interrupción operativa.

## Pregunta de investigación preliminar

¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos en sistemas legacy MVC institucionales, sin requerir reescritura completa ni interrupción operativa?

## Subpreguntas preliminares

1. ¿Qué evidencias técnicas muestran la dispersión de lógica, el acoplamiento y la baja testabilidad del subcircuito de ejecución POA en SIGPP?
2. ¿Qué propiedades debe tener un método de refactorización arquitectónica incremental para ser aplicable en subcircuitos legacy MVC institucionales?
3. ¿En qué medida la instanciación del método en SIGPP mejora la separación de responsabilidades, la trazabilidad del cambio y la validación automatizada del flujo intervenido?

## Objetivo general preliminar

Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.

## Objetivos específicos preliminares

1. Diagnosticar el estado arquitectónico y de testabilidad del subcircuito de ejecución POA en SIGPP mediante análisis de controladores, servicios, repositorios, entidades, consultas SQL y pruebas existentes.
2. Sistematizar la base de conocimiento sobre arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas legacy MVC.
3. Diseñar el método de refactorización arquitectónica incremental, definiendo pasos, criterios, entradas, salidas y condiciones de aplicación.
4. Instanciar el método en el subcircuito de ejecución POA de SIGPP, manteniendo compatibilidad funcional y usando datos ficticios en entorno controlado.
5. Evaluar la utilidad del método mediante métricas técnicas, revisión independiente y validación institucional acotada.

## Estrategia metodológica preliminar

El estudio seguirá el enfoque de Design Science, con construcción y evaluación del artefacto. Para nivel de maestría, se planifica al menos un ciclo de evaluación formativa con rediseño documentado y un ciclo sumativo. La evaluación deberá distinguir utilidad práctica del método en SIGPP y contribución de conocimiento mediante principios de diseño transferibles a sistemas legacy MVC institucionales semejantes.

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
