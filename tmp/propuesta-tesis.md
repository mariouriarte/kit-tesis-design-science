# Informe de propuesta inicial de tesis

## 1. TÍTULO FORMAL PRELIMINAR

**Mejora arquitectónica del módulo de tareas POA para reducir el acoplamiento y mejorar la testabilidad en un sistema Symfony legacy, considerando el flujo presupuestario hasta certificaciones: caso de estudio SIPOA4.**

Este título evita ambigüedad con términos como “casos de uso”, que podrían confundirse con historias de usuario, sprints o gestión ágil. En esta propuesta, el foco no está en Scrum ni en planificación de historias, sino en la mejora técnica del diseño interno del módulo.

El título mantiene un alcance claro:

- **Núcleo de estudio:** módulo de tareas POA.
- **Extensión funcional considerada:** flujo presupuestario asociado hasta certificaciones.
- **Problema técnico:** acoplamiento, baja testabilidad y rigidez de evolución.
- **Caso de estudio:** SIPOA4.

## 2. PLANTEAMIENTO DEL PROBLEMA

### 2.1 Contexto del sistema

SIPOA4 es una aplicación institucional desarrollada en **PHP 7.4** y **Symfony 4.4**, orientada a procesos de planificación operativa y presupuestaria. El repositorio utiliza Doctrine ORM, Symfony Forms, Twig, servicios de aplicación, repositorios, reportes, autenticación web, JWT y algunos endpoints API.

La inspección del proyecto muestra un sistema monolítico de tamaño considerable:

| Evidencia | Observación |
|---|---|
| `composer.json` | Proyecto PHP `^7.4` con Symfony `4.4.*`. |
| `composer.json` | Uso de Doctrine ORM, EasyAdmin, FOSRestBundle, JMS Serializer, Lexik JWT y NelmioApiDoc. |
| `phpunit.xml.dist` | PHPUnit configurado con suite en `./tests` y cobertura sobre `./src`. |
| Estructura del repositorio | 847 archivos PHP en `src/`, 212 controladores, 106 entidades, 112 repositorios y 221 servicios. |

Dentro de este sistema, el **módulo de tareas POA** es funcionalmente relevante porque conecta la planificación con la programación, el presupuesto asignado, el kardex presupuestario, la disponibilidad de fondos y la emisión de certificaciones.

### 2.2 Problema técnico identificado

El problema técnico principal es que el módulo de tareas POA presenta una alta concentración y dispersión de lógica de negocio. Las reglas asociadas a tareas, presupuesto, programación y certificaciones se encuentran distribuidas entre controladores, entidades Doctrine, repositorios, formularios Symfony, servicios y consultas SQL nativas.

Esto genera tres consecuencias importantes:

1. **Alto acoplamiento:** modificar el flujo de tareas requiere conocer controladores, entidades, repositorios, formularios y servicios relacionados.
2. **Baja testabilidad:** muchas reglas quedan atadas a Symfony, Doctrine, Request, Form y persistencia.
3. **Rigidez para evolución:** exponer o adaptar el flujo para API móvil u otros clientes requiere atravesar demasiadas capas acopladas al legacy.

El problema no es únicamente la clase `Tarea`. El problema real está en el flujo funcional alrededor de la tarea: creación, programación, presupuesto asignado, disponibilidad presupuestaria, kardex y certificación.

### 2.3 Evidencias técnicas observadas en el código

#### a) Controlador de creación de tarea con demasiadas responsabilidades

`src/Controller/poa/Tarea/NewTareaController.php` concentra un flujo amplio:

- validación de permisos;
- creación de `Tarea`;
- creación de `KardexPresupuesto`;
- creación de `PresupuestoAsignado`;
- carga de programaciones;
- procesamiento de `TareaType`;
- validación de techo presupuestario;
- generación de código;
- creación de seguimiento;
- persistencia con Doctrine;
- mensajes flash y redirecciones.

Este diseño hace que el controlador no sólo atienda HTTP, sino que también contenga parte importante del flujo de aplicación.

#### b) Entidad `Tarea` extensa y con lógica mezclada

`src/Entity/Tarea.php` tiene aproximadamente **1018 líneas**. Contiene estados, relaciones Doctrine, métodos auxiliares y lógica de programación de tareas.

El propio código contiene una señal explícita de deuda técnica:

```php
// todo separar la logica de la entidad
public function addProgramacionTarea($programaciones)
```

Esto muestra que parte de la lógica debería estar mejor separada de la entidad persistente.

#### c) Repositorio de tareas con múltiples responsabilidades

`src/Repository/TareaRepository.php` tiene aproximadamente **646 líneas** y es utilizado por múltiples controladores, servicios y pruebas. El repositorio contiene consultas de negocio, consultas para modificaciones, cálculos, búsquedas especializadas y acceso a proyecciones complejas.

Además, `src/Repository/Utility/Tarea/TareaOneLineSql.php` contiene aproximadamente **223 líneas** de SQL nativo para listados/proyecciones del módulo. Esto aumenta la dificultad de prueba, mantenimiento y evolución.

#### d) Certificaciones vinculadas al dinero de la tarea

La certificación no debe tratarse como un módulo completamente separado dentro de esta tesis, pero sí debe considerarse como parte del flujo presupuestario asociado a la tarea.

Evidencias:

- `src/Service/Certificacion/CreateCertificacionService.php` recibe una `Tarea` como entrada:

```php
public function create(CreateCertificacionInput $input, Tarea $tarea): Certificacion
```

- La certificación se vincula al presupuesto asignado de la tarea:

```php
$certificacion->setPresupuestoAsignado($tarea->getPresupuestosAsignados()[0]);
$certificacion->setTareas($tarea);
```

- El tope de certificación se calcula desde la disponibilidad del presupuesto asignado:

```php
$topeCertificacion = $tarea->getPresupuestosAsignados()[0]
    ->getMontoModificado()
    ->getDisponibleCertificacion();
```

- La ruta de creación de certificación incluye explícitamente una tarea:

```text
/poa/{gestion}/unidad/{unidad}/tarea/{tarea}/emitirCertificacion
```

Por tanto, certificaciones entra en el alcance sólo como parte del flujo presupuestario de la tarea: disponibilidad, emisión, relación con presupuesto asignado y exposición/listado relacionado.

#### e) API existente para tareas y certificaciones

El repositorio contiene endpoints API relacionados con el flujo:

- `src/Controller/poa/Api/TareaOneLineController.php`
- `src/Controller/poa/Api/CertificacionOneLineController.php`

Esto confirma que el sistema ya tiene necesidad de exponer información del flujo POA mediante API, pero la implementación se apoya todavía en entradas ligadas a `Request`, servicios de listado, serialización y consultas especializadas.

## 3. PREGUNTA DE INVESTIGACIÓN

**¿En qué medida una mejora arquitectónica del módulo de tareas POA, considerando su flujo presupuestario hasta certificaciones, permite reducir el acoplamiento, mejorar la testabilidad y facilitar la evolución del sistema SIPOA4 hacia interfaces web y API más mantenibles?**

Esta pregunta es medible porque permite comparar el estado actual y el estado posterior mediante indicadores de acoplamiento, complejidad, cobertura de pruebas, mantenibilidad y facilidad de extensión.

## 4. OBJETIVOS

### 4.1 Objetivo general

**Proponer e implementar una mejora arquitectónica del módulo de tareas POA en SIPOA4, considerando su flujo presupuestario hasta certificaciones, para reducir el acoplamiento, mejorar la testabilidad y facilitar la evolución del sistema hacia interfaces web y API.**

### 4.2 Objetivos específicos

1. **Diagnosticar** la deuda técnica del módulo de tareas POA mediante el análisis de controladores, entidades, repositorios, servicios, consultas SQL, pruebas y dependencias relacionadas.

2. **Diseñar** una propuesta de organización técnica que separe responsabilidades entre controladores, lógica de aplicación, reglas presupuestarias, persistencia y exposición API.

3. **Implementar** mejoras acotadas en flujos críticos del módulo, considerando creación de tarea, presupuesto asignado, disponibilidad y certificación asociada.

4. **Evaluar** los resultados mediante métricas comparativas antes/después de acoplamiento, complejidad, testabilidad, mantenibilidad y facilidad de exposición API.

## 5. JUSTIFICACIÓN

### 5.1 Valor técnico

La propuesta aporta valor técnico porque aborda problemas reales del código:

- separación de responsabilidades;
- reducción de lógica en controladores;
- mejora de testabilidad de reglas presupuestarias;
- menor acoplamiento con Symfony Forms y Doctrine;
- mejor preparación para API o clientes móviles;
- documentación de una estrategia aplicable a otros módulos legacy.

El flujo seleccionado es suficientemente complejo para una tesis porque no se limita a un CRUD. Incluye tareas, presupuesto, kardex, disponibilidad, certificaciones y endpoints de consulta.

### 5.2 Valor práctico e institucional

Desde el punto de vista institucional, el módulo de tareas POA impacta procesos de planificación y ejecución presupuestaria. Mejorar su arquitectura puede aportar:

- menor riesgo al modificar reglas de presupuesto;
- mayor confiabilidad en la emisión de certificaciones;
- mejor mantenibilidad del sistema;
- mejor base para integración con otros sistemas o clientes móviles;
- menor dependencia de conocimiento implícito del equipo técnico;
- lineamientos para modernizar otros módulos de SIPOA4.

## 6. ALCANCE Y DELIMITACIÓN

### 6.1 Lo que sí se abordará

La propuesta se enfocará en el **módulo de tareas POA**, considerando el flujo presupuestario asociado hasta certificaciones.

Componentes principales:

| Componente | Rol dentro del estudio |
|---|---|
| `src/Controller/poa/Tarea/NewTareaController.php` | Creación de tarea y asignación inicial de presupuesto. |
| `src/Controller/poa/Tarea/EditTareaController.php` | Edición de tarea y ajustes relacionados. |
| `src/Entity/Tarea.php` | Entidad núcleo del módulo. |
| `src/Entity/PresupuestoAsignado.php` | Relación entre tarea, presupuesto, kardex y certificaciones. |
| `src/Entity/KardexPresupuesto.php` | Registro de movimiento presupuestario. |
| `src/Entity/Certificacion.php` | Certificación asociada al presupuesto asignado de la tarea. |
| `src/Service/Certificacion/CreateCertificacionService.php` | Emisión de certificación a partir de una tarea. |
| `src/Controller/poa/Certificacion/CreateCertificacionController.php` | Entrada web para emitir certificación por tarea. |
| `src/Repository/TareaRepository.php` | Consultas y persistencia de tareas. |
| `src/Repository/Utility/Tarea/TareaOneLineSql.php` | Consulta nativa de listado/API de tareas. |
| `src/Controller/poa/Api/TareaOneLineController.php` | API de listado de tareas. |
| `src/Controller/poa/Api/CertificacionOneLineController.php` | API de listado de certificaciones. |

### 6.2 Lo que no se abordará

Para mantener el alcance viable, no se abordará:

- refactorización completa de SIPOA4;
- migración a microservicios;
- actualización mayor de Symfony;
- rediseño completo de base de datos;
- reescritura total del módulo de certificaciones;
- rediseño de reportes Jasper;
- rediseño visual del frontend Twig;
- reemplazo total de Doctrine ORM;
- refactorización completa de todos los módulos de POA, Presupuesto o Administración.

Certificaciones se considera únicamente en su relación directa con la tarea y el presupuesto asignado.

### 6.3 Defensa del alcance

El alcance no se limita por comodidad, sino por rigor. Trabajar todo SIPOA4 sería demasiado amplio para una tesis de maestría y dificultaría medir resultados. En cambio, el módulo de tareas POA, extendido hasta certificaciones, ofrece un flujo suficientemente complejo, medible y representativo.

Respuesta sugerida ante el docente:

> Se toma el módulo de tareas POA como núcleo porque concentra reglas presupuestarias críticas. Sin embargo, no se analiza de forma aislada: se considera el flujo hasta certificaciones porque el código demuestra que la certificación se emite sobre el presupuesto asignado de una tarea. Esto permite un alcance más sólido que un CRUD, pero aún controlado para medición académica.

## 7. METODOLOGÍA Y MÉTRICAS DE EVALUACIÓN

### 7.1 Estrategia técnica sugerida

La estrategia consiste en una **mejora arquitectónica incremental** del módulo, separando responsabilidades y haciendo explícitos los flujos técnicos principales.

No se trata de Scrum ni de historias de usuario. Cuando se habla de flujo o caso funcional, se hace referencia a comportamiento técnico del sistema, por ejemplo:

- crear una tarea POA;
- asignar presupuesto;
- registrar kardex;
- verificar disponibilidad;
- emitir una certificación;
- exponer información por API.

La mejora puede aplicar principios de arquitectura limpia o hexagonal, pero de forma pragmática y compatible con Symfony 4.4/PHP 7.4.

### 7.2 Fases metodológicas

#### Fase 1: Diagnóstico

- Analizar estructura del módulo.
- Identificar clases críticas.
- Medir tamaño, acoplamiento y complejidad.
- Revisar pruebas existentes.
- Documentar flujo tarea-presupuesto-certificación.

#### Fase 2: Diseño

- Definir responsabilidades actuales y propuestas.
- Separar lógica de controladores.
- Definir servicios o componentes de aplicación.
- Definir estrategia de pruebas.
- Definir criterios de comparación.

#### Fase 3: Implementación controlada

- Extraer lógica crítica desde controladores.
- Aislar reglas presupuestarias relevantes.
- Mejorar testabilidad de creación de tarea/certificación.
- Mantener compatibilidad con rutas existentes.
- Agregar pruebas unitarias o de integración.

#### Fase 4: Evaluación

- Medir antes/después.
- Comparar acoplamiento.
- Comparar complejidad.
- Comparar cobertura de pruebas.
- Evaluar facilidad para API.
- Documentar resultados y limitaciones.

### 7.3 Métricas sugeridas

| Dimensión | Indicador | Línea base / fuente | Herramienta sugerida |
|---|---|---|---|
| Tamaño | Líneas por clase | `Tarea.php` ≈ 1018, `TareaRepository.php` ≈ 646, `TareaOneLineSql.php` ≈ 223, `CreateCertificacionService.php` ≈ 277 | `wc`, PhpMetrics |
| Acoplamiento | llamadas a `getDoctrine()` en controladores | 252 en controladores del sistema | script estático / PhpMetrics |
| Acoplamiento | instanciaciones `new` en controladores | 486 en controladores del sistema | script estático |
| Complejidad | complejidad ciclomática por método | medir antes/después | PHPMD / PhpMetrics |
| Testabilidad | cobertura del flujo intervenido | PHPUnit configurado sobre `./src` | PHPUnit + coverage |
| Mantenibilidad | índice de mantenibilidad | medir antes/después | PhpMetrics |
| API | esfuerzo para exponer o modificar respuesta API | cambios requeridos antes/después | análisis comparativo |
| SQL | consultas nativas relevantes | `TareaOneLineSql`, posible `CertificacionOneLineSql` | revisión estática |

### 7.4 Criterios de éxito

La propuesta puede considerarse exitosa si logra:

- reducir lógica en controladores intervenidos;
- aumentar cobertura de pruebas en reglas críticas;
- disminuir dependencias directas de Doctrine/Symfony en lógica de aplicación;
- separar mejor el flujo tarea-presupuesto-certificación;
- mantener compatibilidad funcional;
- documentar una estrategia replicable para otros módulos.

## 8. CRONOGRAMA GENERAL ESTIMADO

Se propone un cronograma de **5 meses**, extensible a 6 meses si se requiere mayor validación.

| Mes | Fase | Actividades principales | Producto esperado |
|---:|---|---|---|
| 1 | Diagnóstico | Revisión de dependencias, pruebas, controladores, entidades, repositorios, servicios y API del flujo tarea-presupuesto-certificación. | Línea base técnica y matriz de deuda. |
| 2 | Diseño | Definición de responsabilidades, propuesta técnica, métricas y estrategia de pruebas. | Diseño de mejora arquitectónica. |
| 3 | Implementación I | Mejora del flujo de tarea y presupuesto asignado. | Primer flujo mejorado con pruebas. |
| 4 | Implementación II | Integración del flujo de certificación asociado y API/listados relacionados. | Flujo tarea-presupuesto-certificación validado. |
| 5 | Evaluación y redacción | Comparación antes/después, análisis de métricas, conclusiones y recomendaciones. | Informe final de tesis/perfil validado. |

## Conclusión

La propuesta se enfoca en el **módulo de tareas POA**, pero no lo trata como una clase aislada ni como un CRUD. El análisis considera el flujo funcional hasta certificaciones porque el código demuestra que la certificación se emite sobre el presupuesto asignado de una tarea.

Este alcance es adecuado para presentar al docente: es más sólido que hablar sólo de `Tarea`, pero más controlado y defendible que intentar intervenir todo SIPOA4.
