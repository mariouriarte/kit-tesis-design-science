# E2. Delimitación

> **Lectura al cierre de DS:** se conserva la delimitación del perfil y su cronología, sin convertirla en descripción de resultados finales. La precisión empírica vigente identifica separación parcial existente, duplicación concreta de selección y discrepancia temporal, no ausencia total de arquitectura o pruebas; fuentes en E6/E8 y E9 T01–T14. El objeto sigue siendo el método, con composición método/instanciación, y SIGPP el contexto. Objetivos y criterios se conservan con cumplimiento parcial; la contribución adoptada es PA1–PA3 en E10. Los pendientes del perfil inferiores son históricos y no reabren etapas cerradas.

> **Precisión aprobada el 28 de octubre de 2026:** MVC caracteriza las aplicaciones heredadas; «institucional» describe su contexto, no una variante arquitectónica. El título aprobado y las formulaciones actuales se armonizan en `03_perfil_ds.md`. El caso continúa siendo ejecución POA de SIGPP; no se añade FastAPI ni se amplía automáticamente la transferibilidad.

## Problema de diseño

### Formulación preliminar

El problema de diseño en SIGPP es que el subcircuito de ejecución POA —tareas vinculadas a operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita. Su lógica se encuentra distribuida y acoplada entre controladores MVC, servicios, repositorios, entidades Doctrine y consultas SQL, lo que dificulta modificar una tarea y sus efectos presupuestarios o certificables de manera controlada, trazable y verificable mediante pruebas automatizadas.

### Componentes del problema de diseño

| Componente | Formulación preliminar |
|:--|:--|
| Contexto | SIGPP, Sistema Integral de Gestión POA Presupuesto de la Caja Petrolera de Salud, administrado funcionalmente por el DNGP. El subcircuito de ejecución POA articula tareas, operaciones/ACP, presupuesto y certificación dentro de un sistema legacy institucional desarrollado en PHP/Symfony. |
| Problema | La ejecución POA vinculada a una tarea no está encapsulada como una unidad funcional clara. La lógica del flujo se encuentra dispersa entre capas del sistema, con dependencias fuertes a controladores, entidades Doctrine, repositorios y consultas SQL; además, el subcircuito no cuenta con cobertura de pruebas suficiente o sistemática. |
| Costo visible | Cada cambio sobre una tarea y sus efectos presupuestarios/certificables exige revisar o tocar múltiples capas acopladas, incrementa la fragilidad del cambio, dificulta la trazabilidad de impacto y reduce la confianza para evolucionar el flujo. |
| Solución conceptual | Diseñar un método de refactorización arquitectónica incremental y aplicarlo en SIGPP como instanciación, definiendo fronteras funcionales explícitas, separación de responsabilidades y pruebas automatizadas sobre el subcircuito seleccionado. |
| Criterios de éxito preliminares | Reducir dispersión de lógica en controladores y capas acopladas; aumentar cobertura de pruebas del flujo intervenido; hacer trazable el cambio tarea–presupuesto–certificación; mantener compatibilidad funcional; permitir revisión técnica independiente en entorno controlado. |

## Nota de control metodológico

Esta formulación aún corresponde al **problema de diseño**: expresa qué debe construirse o modificarse para mejorar una situación práctica. Falta formular el **problema de investigación** —que en el formato institucional se registrará como **problema científico**— como brecha de conocimiento transferible: qué se aprende al diseñar y evaluar este método de refactorización en una clase de sistemas legacy institucionales.

## Problema de investigación preliminar

El problema de investigación —que en el formato institucional se registrará como **problema científico**— busca conocimiento sobre adaptación y evaluación de un método incremental en la clase de aplicaciones y restricciones declaradas. La experiencia de aprendizaje del tesista motiva el caso, pero no demuestra que los marcos o sus materiales oficiales causen concentración de lógica, duplicación o baja cohesión. La documentación histórica de Symfony 3.x contiene tanto ejemplos de persistencia en controladores como recomendaciones explícitas de separar lógica de negocio; el contraste está registrado en `revision_titulo_2026-10-26.md`. El libro concreto utilizado, su edición y la cronología de lectura siguen sin contrastarse, por lo que no se atribuye una causa formativa demostrada al problema arquitectónico.

Formulación preliminar de la brecha:

> Existen principios y procedimientos de refactorización incremental, separación de responsabilidades y testabilidad; este estudio debe contrastar qué adaptación y evidencia adicional requiere aplicarlos a subcircuitos de aplicaciones MVC heredadas bajo restricciones institucionales, sin detener el sistema ni reescribirlo por completo. La insuficiencia de los antecedentes sigue siendo candidata por verificar, no un vacío bibliográfico demostrado. El estudio busca generar evidencia mediante diseño, aplicación y evaluación del método en ejecución POA de SIGPP.

Esta formulación deberá ser refinada con búsqueda bibliográfica. Las fuentes mencionadas por el tesista —*The Definitive Guide to Symfony*, *The Symfony Book*, *Python Crash Course* y *FastAPI: Modern Python Web Development*— quedan como indicios iniciales de experiencia de aprendizaje, no como evidencia académica verificada todavía.

## Objeto de estudio

En Design Science, el objeto de estudio no es SIGPP ni el proceso POA en sí mismo. La resignificación metodológica es obligatoria: el objeto de estudio es el **artefacto propuesto**, con su tipología declarada. En este caso, el objeto de estudio es **un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas, aplicado en SIGPP**.

La tipología del artefacto es una **composición**:

- **Método**, porque define una secuencia de actividades, criterios, decisiones, entradas y salidas para refactorizar incrementalmente un subcircuito legacy.
- **Instanciación**, porque el método se aplicará en SIGPP sobre el subcircuito de ejecución POA para producir evidencia técnica y práctica.

SIGPP y el subcircuito de ejecución POA constituyen el contexto de aplicación y evaluación del artefacto, no el objeto de estudio principal.

## Campo de acción

El campo de acción comprende los **subcircuitos funcionales críticos de aplicaciones MVC heredadas en contextos institucionales, con lógica de negocio dispersa, alto acoplamiento al marco de desarrollo y a la persistencia, y necesidad de evolución sin reescritura completa**. Estas condiciones no definen una variante de MVC ni se atribuyen a todas las aplicaciones construidas con el patrón.

En esta tesis, el campo se concreta en el subcircuito de ejecución POA de SIGPP: tareas vinculadas a operaciones/ACP, presupuesto y certificación. La clase de contextos a la que se aspira transferir analíticamente la contribución no son todos los sistemas legacy, sino aquellos con características estructuralmente semejantes: sistemas institucionales monolíticos, construidos bajo MVC, con reglas de negocio distribuidas en capas técnicas y con restricciones normativas u operativas que impiden detener o reescribir el sistema completo.

## Propuesta

Se propone diseñar y evaluar un **método de refactorización arquitectónica incremental** para subcircuitos funcionales críticos de aplicaciones MVC heredadas, aplicado en el subcircuito de ejecución POA de SIGPP, con el fin de explicitar fronteras funcionales, separar reglas de negocio de controladores y persistencia, e incorporar pruebas automatizadas que permitan evolucionar el flujo sin reescritura completa.

La propuesta se entiende como una composición: el método constituye el artefacto transferible y la instanciación en SIGPP constituye el vehículo de construcción, demostración y evaluación. El alcance de la instanciación se limita al subcircuito de ejecución POA —tareas, operaciones/ACP, presupuesto y certificación— y mantiene elaboración POA, validación ministerial y evaluación POA como contexto y alcance posterior recomendado.

## Decisión de alcance

El alcance principal se limita al subcircuito de ejecución POA: tareas, operaciones/ACP, presupuesto y certificación. La elaboración POA, la validación ministerial y la evaluación POA trimestral se mantienen como contexto y restricciones del dominio, no como módulos de intervención principal.

## Pendiente para cerrar E2

- Formular el problema de investigación como brecha de conocimiento.
- Ajustar criterios de éxito con indicadores operacionales antes de construir, en E6 y E7b.

## Cierre de E2

E2 queda cerrada de forma preliminar para el perfil inicial. Los cuatro componentes del problema de diseño están formulados; el problema de investigación —que en el formato institucional se registrará como problema científico— está planteado como brecha; el objeto de estudio fue resignificado como artefacto de Design Science; el campo de acción está delimitado; y la propuesta declara la tipología compuesta método + instanciación.

La formulación deberá refinarse en E4 y E5 con bibliografía verificada, especialmente en lo referido a marcos MVC, aprendizaje de frameworks, arquitectura de software, refactorización incremental, testabilidad y evolución de sistemas legacy.
