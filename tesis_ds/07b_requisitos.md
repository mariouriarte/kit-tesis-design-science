# E7b. Requisitos del artefacto

## Enfoque de requisitos

El artefacto propuesto es un método de refactorización arquitectónica incremental, instanciado en SIGPP/SIPOA4. Sus requisitos no se limitan a funcionalidades de software, sino a propiedades que el método debe exigir para que la refactorización sea verificable, repetible y viable en un sistema MVC institucional en operación.

La evaluación formativa inicial mostró una brecha relevante: se extrajo lógica hacia servicios y se incorporaron pruebas unitarias para autorización de certificación, pero el servicio principal de creación de certificación no cuenta todavía con prueba unitaria directa identificada. La versión rediseñada del método no partirá de nuevas historias de usuario, sino de la refactorización del flujo existente de certificación. Por tanto, la regla explícita es que ningún servicio principal extraído desde un controlador debe considerarse completado si no cuenta con prueba unitaria o prueba de caracterización directa sobre sus reglas principales.

## Requisitos preliminares del método

| Propiedad | Tipo | Métrica | Fuente en el problema | Prioridad |
|:--|:--|:--|:--|:--|
| Refactorización incremental por circuito funcional | Contextual | Existencia de una secuencia tarea → presupuesto → certificación, intervenida por pasos verificables. | Necesidad de mejorar SIGPP/SIPOA4 sin reescritura completa ni interrupción operativa. | Alta |
| Refactorización guiada por pruebas de caracterización | Funcional / metodológica | Cada comportamiento existente que será movido desde controlador o vista debe contar con prueba de caracterización antes de modificar la lógica principal. | Riesgo observado de extraer servicios sin cobertura directa suficiente. | Alta |
| Prueba directa para servicios principales extraídos | Funcional / verificabilidad | Todo servicio principal extraído desde controlador debe tener al menos una prueba directa que cubra sus reglas principales o una prueba de caracterización si la lógica heredada impide prueba unitaria pura. | Ausencia de prueba directa identificada para `CreateCertificacionService.php`. | Alta |
| Separación de responsabilidades sin migración arquitectónica compleja | Contextual | Existencia de capas simples y comprensibles: controlador delgado, servicio de aplicación, objeto de entrada, DTO de salida para vista, regla verificable y repositorio aislado. | Restricción práctica: no introducir DDD ni arquitectura hexagonal completa por costo de migración. | Alta |
| Aplicabilidad a otros procedimientos del módulo seleccionado | Contextual | El mismo patrón debe aplicarse al circuito tarea → presupuesto → certificación sin rediseñar la solución en cada procedimiento. | La intervención inicial no mostró todavía uniformidad ni escalabilidad. | Media |
| Evidencia técnica mínima por paso | Verificación | Para cada paso: commit, archivo modificado, prueba ejecutada y resultado. | Necesidad de trazabilidad para defensa y traducción al modelo ALSIE. | Alta |

## Tensiones de diseño

La tensión principal está entre madurez arquitectónica y viabilidad de migración. Una arquitectura limpia completa, entendida como separación estricta de capas y dependencias, puede aportar claridad conceptual; no obstante, una adopción amplia de DDD o arquitectura hexagonal agregaría una carga de migración desproporcionada para el alcance de una tesis de maestría y para un sistema institucional en operación. Por esa razón, el método adopta una arquitectura limpia mínima e incremental: suficiente para separar responsabilidades, introducir pruebas y guiar módulos posteriores, pero sin exigir una reestructuración completa del sistema.

La segunda tensión está entre refactorizar y proteger el comportamiento existente. Para resolverla, el método debe exigir pruebas antes o durante la refactorización: pruebas de caracterización para la lógica heredada que actualmente vive en controlador, Twig o consultas dispersas, y pruebas unitarias para los servicios resultantes cuando la lógica ya pueda aislarse. Así, la prueba no se añade como actividad decorativa posterior, sino como criterio de suficiencia de cada extracción.
