# Anexo. Arquitectura de referencia de la instanciación: certificación

**Naturaleza:** este anexo presenta la arquitectura de referencia de la instanciación en el subcircuito de creación de certificación de SIGPP. No es el método de la tesis —el método son los pasos P1–P8 y los requisitos R1–R14 de E7—, sino la materialización concreta del destino arquitectónico B (MVC con frontera de aplicación incremental) para el caso. Es un destino propuesto, no una norma aprobada ni una arquitectura ya alcanzada en su conjunto.

## 1. Relación con el método

Este documento detalla el caso que el método formaliza. La correspondencia con los pasos del método es la siguiente; el método es lo transferible, este anexo es lo específico del piloto.

| Paso del método (E7c) | Concreción en este anexo |
|:--|:--|
| P1 delimitar el incremento | Selección del subcircuito de creación de certificación |
| P2 caracterizar el comportamiento | Selección de restricción (específica → general → ninguna) ya caracterizada |
| P3 hacer controlable la decisión | Responsable único de la precedencia en el servidor |
| P4–P6 migrar, probar, retirar | Delegación compartida en `RestriccionSubPartidaResolver` |
| P7 integrar y verificar | Pruebas del piloto en `tests/Certificacion` |
| P8 registrar costo y versionar | Ficha de hallazgo y checklist de verificación de este anexo |

Los «dos caminos» de la sección 5 no son un método alternativo: son la expresión operativa de la distinción entre transformación conservadora y capacidad nueva (P4, D06), aplicada al caso.

## 2. Responsabilidades de la arquitectura de referencia

| Componente | Responsabilidad | Fuera de su responsabilidad |
|:--|:--|:--|
| Controlador web | Petición y respuesta HTTP, procesamiento del formulario, control de acceso, mapeo de entrada, mensajes, redirecciones y datos de vista | Definir precedencia de restricciones, reglas de elegibilidad o secuencia de persistencia |
| Preparación opcional | Consultas de tarea y saldo y datos para la pantalla, solo si una necesidad concreta lo justifica | Escrituras, creación, seguimiento, autorización |
| Servicio de creación | Coordinar validaciones autoritativas, reglas específicas, creación, persistencia, seguimiento y autorización | Procesar formularios, llamar a controladores, renderizar Twig |
| Regla específica o resolver | Resolver una decisión identificable con entradas y resultado explícitos | Depender de `Request`, Form o Twig; controlar presentación |
| Consultas y persistencia | Recuperar y persistir mediante los repositorios existentes | Definir comportamiento HTTP o política de aplicación |
| Almacenamiento de archivos | Encapsular carga y almacenamiento | Decidir cuándo una certificación requiere adjunto |
| DTO y datos de presentación | Transportar entradas o datos de pantalla explícitos | Autorizar la creación o duplicar la lógica de restricciones |
| Plantilla Twig | Renderizar estructura, formulario y datos preparados | Consultar repositorios, decidir reglas de negocio |

**Autoridad de las reglas:** la operación del servidor valida la creación. La visibilidad de campos y las indicaciones del formulario no conceden permiso ni sustituyen las validaciones de fecha, importe y adjunto. El control de acceso del usuario y la creación de la autorización son asuntos distintos.

## 3. Dependencias y excepciones de transición

| Componente | Dependencias permitidas | Límite o excepción |
|:--|:--|:--|
| Controlador web | HTTP, Form y vistas de Symfony, DTO, operación de creación, resolver; preparación opcional | No añadir reglas de negocio ni coordinar escrituras; sus lecturas de repositorios son excepción transitoria |
| Preparación opcional | Consultas, resolver, entidades y datos explícitos | Sin escrituras, operación de creación, Form, Twig ni HTTP |
| Operación de creación | Reglas, DTO, entidades y repositorios concretos, seguimiento, autorización, archivos | Sin controlador, formularios ni Twig; el uso de `UploadedFile` es acoplamiento reconocido |
| Regla o resolver | Datos y entidades explícitos; puede consultar repositorios concretos | Sin HTTP, Form, Twig, almacenamiento ni escrituras |
| Consultas, persistencia, almacenamiento | Mecanismos de Doctrine o almacenamiento y tipos necesarios | Sin controlador, formularios, vistas ni llamadas a la operación de creación |
| DTO y datos de presentación | Valores explícitos y referencias a entidades necesarias | No introducir decisiones de negocio basadas en formularios |
| Twig | Datos de vista, formularios y recursos de presentación | Sin repositorios ni invocaciones a operaciones de creación |

Esta dirección es pragmática dentro del MVC existente; no acredita adopción de DDD, arquitectura hexagonal ni núcleo independiente. Las entidades de Doctrine y los repositorios concretos permanecen durante la transición.

## 4. Detección de deuda técnica

La deuda arquitectónica es una condición estructural que dificulta cambiar, mantener o probar con seguridad. La antigüedad, PHP 7.4, el MVC o el uso de repositorios concretos no constituyen deuda por sí mismos; tampoco una preferencia estética. Un defecto de comportamiento se trata por separado de una transformación conservadora.

Procedimiento acotado: delimitar el subcircuito y el contexto de cambio; inspeccionar responsabilidades, dependencias, duplicación y capacidad de prueba; contrastar historial y evidencia; registrar rutas, esfuerzo y fuente; priorizar o diferir con justificación cualitativa.

**Ficha reutilizable de un hallazgo:**

| Campo | Contenido mínimo |
|:--|:--|
| Ubicación y alcance | Rutas, operación y consumidores afectados |
| Observación y tipo | Condición verificable y posible deuda de responsabilidades, dependencias, duplicación o protección |
| Evidencia | Código, pruebas, historial; límites de lo inspeccionado |
| Impacto de mantenimiento | Consecuencia observada, separada de la hipótesis |
| Comportamiento y protección | Invariantes, efectos y brecha de pruebas verificada |
| Intervención propuesta | Cambio estructural acotado y límite que lo orienta |
| Beneficio y comprobación | Resultado esperado y comparación antes/después |
| Prioridad | Presión de cambio, impacto, esfuerzo, riesgo, fuente |
| Estado | Sospechado, confirmado, intervenido o efecto pendiente |

Ejemplo del piloto: la duplicación de selección pasó de dos implementaciones a una mediante la delegación en el resolver; es una reducción estructural, no una demostración de ahorro de tiempo. La mezcla de adaptación HTTP y lecturas en el controlador es candidata a análisis, no deuda confirmada. Contar líneas o pruebas no basta para demostrar pago de deuda o productividad.

## 5. Dos caminos de uso

**A. Cambio motivado por un requisito nuevo.** Partir de un requisito aceptado; caracterizar el comportamiento actual y distinguirlo del nuevo; realizar solo la refactorización preparatoria justificada; verificar conservación; implementar la funcionalidad con sus pruebas.

**B. Refactorización independiente.** Documentar el problema de mantenimiento y el beneficio esperado; caracterizar y acordar alcance, protección y riesgo; reestructurar de forma acotada; verificar regresiones y comparar estructura antes/después; aceptar o diferir.

En ambos caminos, la fase estructural conserva el comportamiento observable: retornos, errores, estado, persistencia, permisos y efectos sobre archivos. Corregir un defecto es un cambio de comportamiento que requiere aprobación separada. Estas pautas orientan cambios autorizados; no autorizan por sí mismas ninguna implementación.

## 6. Criterios de verificación de una transición

- Cada regla modificada tiene un responsable identificable y entradas y resultado explícitos.
- La precedencia de restricciones tiene una implementación única; las indicaciones del formulario no la duplican.
- Las reglas específicas no dependen de HTTP, Form o Twig.
- Las operaciones de aplicación no dependen de controladores, formularios o vistas.
- Cada acoplamiento conservado tiene razón y alcance explícitos.
- Antes de mover comportamiento se caracteriza lo pertinente.
- La aceptación distingue conservación del comportamiento, cambio funcional autorizado y resultado estructural.
- El código conserva compatibilidad con PHP 7.4 y Symfony 4.4.
- Se entienden los efectos de persistencia y archivos antes de cambiar su orden.

## 7. Referencias

- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR.
- Fowler, M. (2018). *Refactoring: Improving the design of existing code* (2.ª ed.). Addison-Wesley Professional.
- Fowler, M. (2019). *Technical debt* [Entrada de blog]. Martin Fowler. https://martinfowler.com/bliki/TechnicalDebt.html

Estas fuentes sustentan conceptos concretos —caracterización, separación de dependencias, refactorización frente a cambio funcional, deuda técnica—; no constituyen por sí solas la fundamentación completa ni la validación del método.
