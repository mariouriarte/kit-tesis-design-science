# Perfil preliminar para revisión — lunes 28 de septiembre de 2026

## Datos generales

- **Tesista:** Mario Arturo Uriarte Marin
- **Programa:** Maestría en Ingeniería de Software
- **Tutor:** Luis Roberto Pérez Rios, Ph.D.
- **Enfoque metodológico:** Design Science
- **Estado del perfil:** preliminar, suficiente para revisión inicial; pendiente de fortalecimiento bibliográfico e indicadores operacionales.

## Título provisional

**Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales: instanciación en la ejecución POA de SIGPP**

## Contexto

SIGPP, Sistema Integral de Gestión POA Presupuesto, es un sistema institucional de la Caja Petrolera de Salud. El área dueña del sistema es el Departamento Nacional de Gestión y Planificación (DNGP). El sistema articula elaboración, validación y ejecución del POA bajo restricciones normativas institucionales y estatales.

El alcance de esta tesis se delimita al subcircuito de ejecución POA, compuesto por tareas vinculadas a operaciones/ACP, presupuesto y certificación. La elaboración POA, la validación ministerial y la evaluación POA trimestral se consideran contexto y alcance posterior recomendado, no intervención principal.

## Problema de diseño

El problema de diseño en SIGPP es que el subcircuito de ejecución POA —tareas vinculadas a operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita. Su lógica se encuentra distribuida y acoplada entre controladores MVC, servicios, repositorios, entidades Doctrine y consultas SQL, lo que dificulta modificar una tarea y sus efectos presupuestarios o certificables de manera controlada, trazable y verificable mediante pruebas automatizadas.

## Problema de investigación

El problema de investigación —que en el formato institucional se registrará como **problema científico**— se ubica en la brecha entre principios generales de arquitectura, refactorización y testabilidad, y la falta de un método incremental, aplicable y evaluable para refactorizar subcircuitos legacy MVC institucionales sin detener ni reescribir el sistema completo.

La tesis no pretende afirmar que la separación de responsabilidades, las pruebas unitarias o la arquitectura de software sean conceptos nuevos. La contribución esperada está en traducir esos principios conocidos en un método aplicable y evaluable bajo restricciones reales de continuidad operativa, normativa institucional y datos sensibles.

## Objeto de estudio

En Design Science, el objeto de estudio no es SIGPP ni el proceso POA, sino el artefacto propuesto. El objeto de estudio es un **método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales**, instanciado en SIGPP.

La tipología del artefacto es una **composición**:

- **Método:** define pasos, criterios, entradas, salidas y condiciones de aplicación.
- **Instanciación:** aplicación del método en el subcircuito de ejecución POA de SIGPP.

## Campo de acción

El campo de acción comprende subcircuitos funcionales críticos de sistemas legacy MVC institucionales, con lógica de negocio dispersa, alto acoplamiento al marco de trabajo y a la persistencia, y necesidad de evolución sin reescritura completa.

## Propuesta

Se propone diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos funcionales críticos en sistemas legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, con el fin de explicitar fronteras funcionales, separar reglas de negocio de controladores y persistencia, e incorporar pruebas automatizadas que permitan evolucionar el flujo sin reescritura completa.

## Pregunta de investigación

¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos en sistemas legacy MVC institucionales, sin requerir reescritura completa ni interrupción operativa?

## Objetivo general

Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.

## Objetivos específicos

1. Diagnosticar el estado arquitectónico y de testabilidad del subcircuito de ejecución POA en SIGPP mediante análisis de controladores, servicios, repositorios, entidades, consultas SQL y pruebas existentes.
2. Sistematizar la base de conocimiento sobre arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas legacy MVC.
3. Diseñar el método de refactorización arquitectónica incremental, definiendo pasos, criterios, entradas, salidas y condiciones de aplicación.
4. Instanciar el método en el subcircuito de ejecución POA de SIGPP, manteniendo compatibilidad funcional y usando datos ficticios en entorno controlado.
5. Evaluar la utilidad del método mediante métricas técnicas, revisión independiente y validación institucional acotada.

## Contribución original preliminar

Esta investigación aporta principios de diseño validados para refactorizar incrementalmente subcircuitos funcionales críticos en sistemas legacy MVC institucionales, mediante un método que explicita fronteras funcionales, separa reglas de negocio de controladores y persistencia, e incorpora pruebas automatizadas sin exigir reescritura completa ni interrupción operativa.

## Estrategia metodológica

El estudio seguirá el enfoque de Design Science. El artefacto será construido y evaluado mediante al menos un ciclo formativo con rediseño documentado y un ciclo sumativo. La evaluación distinguirá la utilidad práctica del método en SIGPP y la contribución de conocimiento expresada como principios de diseño transferibles a sistemas legacy MVC institucionales semejantes.

## Evaluación preliminar prevista

La evaluación podrá combinar:

- medición técnica antes/después sobre dispersión de lógica, acoplamiento, cobertura de pruebas y trazabilidad del cambio;
- instanciación en entorno local o servidor controlado de pruebas con datos ficticios;
- revisión técnica por un desarrollador independiente que conoce SIGPP y módulos como certificaciones y devengados;
- validación institucional acotada con el DNGP, respetando consentimiento, alcances y límites de uso de información.

## Alcance excluido

No se abordará la refactorización completa de SIGPP, ni la reescritura del sistema, ni la migración de framework, ni la intervención completa de elaboración POA, validación ministerial o evaluación POA trimestral. Estos módulos se registran como candidatos a refactorización posterior.

## Pendientes posteriores al perfil

- Verificar bibliografía sobre marcos MVC, arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas legacy.
- Definir indicadores operacionales con línea base antes de construir.
- Formalizar instrumentos de evaluación formativa y sumativa.
- Documentar consentimiento, alcances y límites con el área dueña del software.
