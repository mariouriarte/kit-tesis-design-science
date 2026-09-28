# Matriz de coherencia y trazabilidad

## Cadena de coherencia

| Eslabón | Contenido |
|:--|:--|
| Problema de diseño | El subcircuito de ejecución POA de SIGPP —tareas, operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita; su lógica está dispersa entre controladores, servicios, repositorios, entidades Doctrine y consultas SQL, con pruebas insuficientes para validar cambios con confianza. |
| Problema de investigación (institucional: "problema científico") | Brecha preliminar: existe literatura técnica sobre uso de marcos MVC y literatura de arquitectura sobre separación de responsabilidades y testabilidad, pero falta evidencia suficiente sobre cómo traducir esos principios en un método incremental y evaluable para refactorizar subcircuitos institucionales legacy sin detener ni reescribir el sistema completo. |
| Objeto de estudio (artefacto + tipología) | Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en SIGPP; tipología compuesta: método + instanciación. |
| Campo de acción (clase de contextos) | Subcircuitos funcionales críticos de sistemas legacy MVC institucionales, con lógica de negocio dispersa, alto acoplamiento al marco de trabajo y a la persistencia, y necesidad de evolución sin reescritura completa. |
| Objetivo general | Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema. |
| Pregunta de investigación | ¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos en sistemas legacy MVC institucionales, sin requerir reescritura completa ni interrupción operativa? |
| Alternativas de solución consideradas | Pendiente para E7a. |
| Artefacto propuesto (tipología) | Método de refactorización arquitectónica incremental + instanciación aplicada al subcircuito de ejecución POA en SIGPP. |
| Requisitos del artefacto | Pendiente para E7b. |
| Decisiones de diseño principales | Pendiente para E7c. |
| Criterio de suficiencia del artefacto | Pendiente para E7d. |
| Método de evaluación | Preliminar: medición técnica, entorno controlado con datos ficticios, revisión técnica independiente y validación institucional acotada. |
| Criterios de éxito e indicadores | Pendiente para E6. |
| Contribución reclamada (nivel de maestría) | Preliminar: principios de diseño para refactorización arquitectónica incremental en módulos legacy institucionales. |

## Trazabilidad propuesta ↔ solución

| Problema de diseño | Requisito | Alternativa descartada | Decisión de diseño | Componente | Indicador | Verificación interna | Evidencia de evaluación | Cumplimiento | Limitación |
|:--|:--|:--|:--|:--|:--|:--|:--|:--|:--|
| Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente | Pendiente |

## Riesgos de construcción

| Riesgo | Tipo (técnico, acceso, tiempo) | Probabilidad | Impacto | Mitigación |
|:--|:--|:--|:--|:--|
| Sobrealcance por incluir elaboración POA, validación ministerial y evaluación POA dentro de la intervención principal. | Tiempo / alcance | Alta | Alto | Mantenerlos como contexto y alcance posterior; intervenir solo el subcircuito de ejecución POA. |
| Sesgo del constructor por ser el tesista creador y desarrollador principal de SIGPP. | Validez | Media | Alto | Incorporar revisión técnica independiente, entorno controlado de pruebas y validación del DNGP. |
| Exposición de datos sensibles de certificaciones o ejecución financiera. | Institucional / ético | Media | Alto | Usar datos ficticios y consentimiento explícito del área dueña del software. |

## Eslabones huérfanos (sin evidencia o sin correspondencia)

- Problema de investigación formulado preliminarmente; falta verificación bibliográfica en E4 y E5.
- Indicadores y criterios de éxito aún no fijados.
