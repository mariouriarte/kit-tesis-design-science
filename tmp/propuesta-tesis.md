# Informe de propuesta inicial de tesis

## 1. TÍTULO FORMAL PRELIMINAR

**Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales: instanciación en la ejecución POA de SIGPP.**

El título ubica correctamente la contribución de la tesis: no se trata de una simple mejora técnica de un sistema específico, sino del diseño y evaluación de un **método** aplicable a subcircuitos funcionales críticos en sistemas legacy MVC institucionales.

SIGPP funciona como instancia de aplicación del método, no como el objeto científico completo. El foco de intervención se delimita al **subcircuito de ejecución POA**, donde convergen tareas, operaciones/ACP, presupuesto y certificaciones.

El título mantiene un alcance claro:

- **Artefacto principal:** método de refactorización arquitectónica incremental.
- **Tipo de sistema:** legacy MVC institucional.
- **Instanciación:** ejecución POA de SIGPP.
- **Núcleo funcional:** tareas vinculadas a operaciones/ACP, presupuesto y certificaciones.
- **Problema técnico:** ausencia de frontera arquitectónica explícita, acoplamiento, baja testabilidad y dificultad de evolución controlada.

## 2. PLANTEAMIENTO DEL PROBLEMA

### 2.1 Contexto del sistema

SIGPP, Sistema Integral de Gestión POA Presupuesto, es una aplicación institucional orientada a procesos de planificación, seguimiento y ejecución presupuestaria. En su implementación actual, el repositorio inspeccionado corresponde a una aplicación desarrollada en **PHP 7.4** y **Symfony 4.4**, con Doctrine ORM, Symfony Forms, Twig, servicios de aplicación, repositorios, reportes, autenticación web, JWT y algunos endpoints API.

La inspección del proyecto muestra un sistema monolítico de tamaño considerable:

| Evidencia | Observación |
|---|---|
| `composer.json` | Proyecto PHP `^7.4` con Symfony `4.4.*`. |
| `composer.json` | Uso de Doctrine ORM, EasyAdmin, FOSRestBundle, JMS Serializer, Lexik JWT y NelmioApiDoc. |
| `phpunit.xml.dist` | PHPUnit configurado con suite en `./tests` y cobertura sobre `./src`. |
| Estructura del repositorio | 847 archivos PHP en `src/`, 212 controladores, 106 entidades, 112 repositorios y 221 servicios. |

La versión tecnológica concreta observada es la siguiente:

| Elemento | Versión / tecnología observada | Evidencia |
|---|---|---|
| Lenguaje | PHP `^7.4` | `composer.json` |
| Marco principal | Symfony `4.4.*` | `composer.json` |
| ORM | Doctrine ORM `^2.11` con DoctrineBundle `^1.6.10\|^2.0` | `composer.json` |
| Mapeo ORM | Entidades Doctrine por anotaciones en `src/Entity` y mapeos XML adicionales en `Resources/config/doctrine` | `config/packages/doctrine.yaml` |
| Base de datos | PostgreSQL | `docker-compose.yml`, servicio `sigpp-db`; paquete `martin-georgiev/postgresql-for-doctrine` |
| Versión de base de datos en entorno Docker | PostgreSQL 16, construida desde `docker/postgresql/Dockerfile-postgresql16` | `docker-compose.yml` |
| Servidor web local | Nginx Alpine delante del contenedor PHP | `docker-compose.yml` |
| Pruebas | PHPUnit `^9.5`, suite sobre `./tests` y cobertura sobre `./src` | `composer.json`, `phpunit.xml.dist` |

Dentro de este sistema, el subcircuito de **ejecución POA** es funcionalmente relevante porque conecta tareas, operaciones/ACP, presupuesto asignado, kardex presupuestario, disponibilidad de fondos y emisión de certificaciones.

### 2.2 Problema de diseño identificado

El problema de diseño en SIGPP es que el subcircuito de ejecución POA —tareas vinculadas a operaciones/ACP, presupuesto y certificación— carece de una frontera arquitectónica explícita. Su lógica se encuentra distribuida y acoplada entre controladores MVC, servicios, repositorios, entidades Doctrine y consultas SQL, lo que dificulta modificar una tarea y sus efectos presupuestarios o certificables de manera controlada, trazable y verificable mediante pruebas automatizadas.

Esto genera tres consecuencias importantes:

1. **Alto acoplamiento:** modificar el flujo de ejecución POA requiere conocer controladores, entidades, repositorios, formularios, servicios y consultas especializadas.
2. **Baja testabilidad:** muchas reglas quedan atadas a Symfony, Doctrine, Request, Form y persistencia.
3. **Rigidez para evolución:** adaptar el flujo hacia API, integración móvil u otros clientes requiere atravesar demasiadas capas acopladas al legacy.

El problema no es únicamente la clase `Tarea`. El problema real está en el subcircuito funcional alrededor de la ejecución POA: tareas, operaciones/ACP, presupuesto asignado, disponibilidad presupuestaria, kardex y certificación.

### 2.3 Problema de investigación / problema científico

El problema de investigación —que en el formato institucional puede registrarse como **problema científico**— se ubica en la brecha entre principios generales de arquitectura, refactorización y testabilidad, y la falta de un método incremental, aplicable y evaluable para refactorizar subcircuitos legacy MVC institucionales sin detener ni reescribir el sistema completo.

La tesis no intenta demostrar que arquitectura limpia, separación de responsabilidades, refactorización o pruebas automatizadas sean conceptos nuevos. La contribución está en traducir esos principios conocidos en un método aplicable bajo restricciones reales de continuidad operativa, normativa institucional y datos sensibles.

### 2.4 Evidencias técnicas observadas en el código

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

#### d) Certificaciones vinculadas al presupuesto de la tarea

La certificación no debe tratarse como un módulo completamente separado dentro de esta tesis, pero sí debe considerarse como parte del subcircuito de ejecución POA asociado a la tarea.

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

Por tanto, certificaciones entra en el alcance como parte del flujo presupuestario-certificable de la tarea: disponibilidad, emisión, relación con presupuesto asignado y exposición/listado relacionado.

#### e) API existente para tareas y certificaciones

El repositorio contiene endpoints API relacionados con el flujo:

- `src/Controller/poa/Api/TareaOneLineController.php`
- `src/Controller/poa/Api/CertificacionOneLineController.php`

Esto confirma que el sistema ya tiene necesidad de exponer información del flujo POA mediante API, pero la implementación se apoya todavía en entradas ligadas a `Request`, servicios de listado, serialización y consultas especializadas.

#### f) Componentes actuales más problemáticos del subcircuito

En el subcircuito de ejecución POA, los componentes más problemáticos identificados son:

| Tipo de componente | Evidencia principal | Problema arquitectónico observado |
|---|---|---|
| Controladores extensos | `src/Controller/poa/Tarea/NewTareaController.php` | Mezcla entrada HTTP, validaciones, creación de entidades, reglas de presupuesto, persistencia y navegación. |
| Entidades Doctrine con lógica de negocio | `src/Entity/Tarea.php` | Entidad extensa con relaciones persistentes y comportamiento de programación; el propio código contiene la nota `todo separar la logica de la entidad`. |
| Repositorios con responsabilidad ampliada | `src/Repository/TareaRepository.php` | Combina acceso a datos con consultas especializadas y lógica de recuperación usada por múltiples capas. |
| SQL nativo especializado | `src/Repository/Utility/Tarea/TareaOneLineSql.php` | Consulta de listado/proyección difícil de probar de forma aislada y acoplada a estructura de base de datos. |
| Servicios acoplados al flujo legacy | `src/Service/Certificacion/CreateCertificacionService.php` | La emisión de certificación depende directamente de `Tarea` y de su `PresupuestoAsignado`, lo que confirma el acoplamiento tarea-presupuesto-certificación. |
| APIs apoyadas en estructuras existentes | `src/Controller/poa/Api/TareaOneLineController.php`, `src/Controller/poa/Api/CertificacionOneLineController.php` | La exposición API existe, pero se apoya en consultas y servicios del legacy en lugar de una frontera de aplicación explícita. |
| Pruebas insuficientes sobre reglas críticas | `phpunit.xml.dist`, revisión del flujo intervenido | PHPUnit está configurado, pero el flujo tarea-presupuesto-certificación requiere mayor cobertura específica para reglas presupuestarias y certificables. |

Estos componentes justifican que la tesis no se limite a “mejorar una clase”, sino a proponer una frontera arquitectónica incremental para el subcircuito de ejecución POA.

### 2.5 Métricas iniciales específicas del circuito tarea-presupuesto-certificación

Las métricas globales de SIGPP sirven para contextualizar el tamaño del sistema, pero la línea base de la tesis debe concentrarse en el circuito **tarea → presupuesto → certificación**. Para ese circuito se cuenta con una primera medición estática sobre archivos críticos del repositorio.

#### a) Tamaño y concentración de código en componentes críticos

| Componente | Líneas aprox. | Métodos públicos | Señal relevante |
|---|---:|---:|---|
| `src/Entity/Tarea.php` | 1018 | 110 | Entidad extensa con relaciones, estados y lógica de programación. |
| `src/Entity/Certificacion.php` | 726 | 86 | Entidad extensa vinculada a tarea, presupuesto asignado, administración y datos de certificación. |
| `src/Repository/TareaRepository.php` | 646 | 17 | Repositorio con consultas especializadas y uso de SQL nativo. |
| `src/Entity/PresupuestoAsignado.php` | 447 | 46 | Entidad puente entre tarea, kardex, presupuesto y certificaciones. |
| `src/Service/Certificacion/CreateCertificacionService.php` | 278 | 2 | Servicio con 13 métodos privados y reglas de emisión de certificación. |
| `src/Controller/poa/Tarea/NewTareaController.php` | 269 | 2 | Controlador de creación de tarea con validación, presupuesto, kardex, persistencia y navegación. |
| `src/Entity/KardexPresupuesto.php` | 253 | 33 | Entidad de movimiento presupuestario asociada al circuito. |
| `src/Repository/Utility/Tarea/TareaOneLineSql.php` | 224 | 2 | Constructor de consulta SQL nativa para proyección/listado de tareas. |
| `src/Controller/poa/Tarea/EditTareaController.php` | 216 | 2 | Controlador de edición de tarea con dependencias del flujo legacy. |
| `src/Controller/poa/Api/TareaOneLineController.php` | 49 | 2 | API de consulta de tareas apoyada en servicio/listado existente. |
| `src/Controller/poa/Api/CertificacionOneLineController.php` | 51 | 2 | API de consulta de certificaciones apoyada en servicio/listado existente. |

Esta medición muestra que la complejidad no está concentrada en un único archivo. El circuito cruza entidades persistentes, controladores MVC, repositorios, SQL nativo, servicios y endpoints API.

#### b) Indicadores de acoplamiento y dispersión

| Indicador observado | Resultado inicial | Interpretación |
|---|---:|---|
| Archivos críticos medidos directamente | 11 | Núcleo mínimo del circuito tarea-presupuesto-certificación. |
| Líneas acumuladas en esos archivos críticos | 4177 | Volumen suficiente para justificar intervención arquitectónica acotada. |
| Instanciaciones directas `new` en archivos críticos | 46 | Señal de construcción manual de objetos y acoplamiento procedimental. |
| Llamadas a `getDoctrine()` en controladores críticos de tarea | 2 | Persistencia usada desde controladores en puntos del flujo. |
| Ocurrencias de SQL nativo o construcción SQL en archivos críticos | 9 | Indica dependencia directa de consultas especializadas difíciles de aislar. |
| Rutas/controladores API o MVC en archivos críticos | 8 anotaciones | El circuito está expuesto por entradas web y API. |
| Métodos privados en `CreateCertificacionService` | 13 | La emisión de certificación concentra reglas internas no expuestas como componentes de dominio independientes. |

Estos indicadores sugieren una arquitectura donde el comportamiento del circuito está distribuido entre varias capas, pero sin una frontera de aplicación suficientemente explícita.

#### c) Alcance ampliado por nombres de ruta/archivo relacionados

Además del núcleo mínimo, una búsqueda por nombres de archivo relacionados muestra la amplitud del entorno técnico alrededor del circuito:

| Grupo relacionado | Archivos PHP relacionados | Líneas aprox. acumuladas |
|---|---:|---:|
| Tarea | 103 | 11933 |
| Certificacion | 56 | 7120 |
| Presupuesto | 54 | 6290 |
| Kardex | 8 | 967 |

Estos valores no significan que toda esa superficie será intervenida. Sirven para evidenciar que el circuito se encuentra dentro de una red funcional amplia y que la tesis debe seleccionar un subcircuito controlado para evitar sobrealcance.

#### d) Línea base inicial de pruebas

La configuración de PHPUnit existe, pero la cobertura específica del circuito todavía debe formalizarse. La revisión estática inicial muestra referencias en pruebas, pero con vacíos en puntos críticos:

| Elemento buscado en pruebas | Archivos de prueba con referencia | Ocurrencias |
|---|---:|---:|
| `Tarea` | 11 | 95 |
| `PresupuestoAsignado` | 3 | 14 |
| `Certificacion` | 2 | 24 |
| `KardexPresupuesto` | 0 | 0 |
| `CreateCertificacionService` | 0 | 0 |
| `TareaOneLineSql` | 0 | 0 |

Esto permite formular una línea base honesta: existen pruebas relacionadas con tareas y algunas referencias a presupuesto/certificación, pero no se observa una cobertura focalizada suficiente sobre reglas críticas del circuito tarea-presupuesto-certificación, especialmente en kardex, emisión de certificación y SQL de listado.

#### e) Métricas pendientes para la línea base formal

Antes de aplicar el método, estas métricas deben completarse formalmente:

- complejidad ciclomática por método en controladores, repositorios y servicios del circuito;
- cobertura efectiva de pruebas sobre el flujo tarea-presupuesto-certificación;
- número de archivos modificados para un cambio típico del circuito;
- tiempo de modificación o esfuerzo estimado para cambios representativos;
- errores recurrentes o defectos históricos asociados a presupuesto, kardex o certificación;
- trazabilidad antes/después entre requisito funcional, cambio de código y prueba automatizada.

Por tanto, la tesis ya cuenta con una línea base inicial estática del circuito, pero debe complementar esa línea base con métricas dinámicas y de evolución antes de evaluar el método propuesto.

## 3. PREGUNTA DE INVESTIGACIÓN

**¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos en sistemas legacy MVC institucionales, sin requerir reescritura completa ni interrupción operativa?**

Esta pregunta es medible porque permite comparar el estado actual y el estado posterior mediante indicadores de dispersión de lógica, acoplamiento, complejidad, cobertura de pruebas, trazabilidad del cambio y mantenibilidad.

## 4. OBJETIVOS

### 4.1 Objetivo general

**Diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad, la testabilidad y la trazabilidad de cambios sin reescritura completa del sistema.**

### 4.2 Objetivos específicos

1. **Diagnosticar** la deuda arquitectónica del subcircuito de ejecución POA mediante el análisis de controladores, entidades, repositorios, servicios, consultas SQL, pruebas y dependencias relacionadas con tareas, operaciones/ACP, presupuesto y certificaciones.

2. **Diseñar** un método incremental que defina pasos, criterios, entradas, salidas y condiciones de aplicación para refactorizar subcircuitos legacy MVC institucionales sin interrumpir la operación.

3. **Instanciar** el método en el flujo tarea-presupuesto-certificación de SIGPP, proponiendo una frontera arquitectónica más explícita y separando responsabilidades entre entrada MVC, lógica de aplicación, reglas presupuestarias, persistencia y exposición API.

4. **Evaluar** los resultados mediante métricas comparativas antes/después de acoplamiento, complejidad, testabilidad, mantenibilidad y trazabilidad del cambio.

## 5. JUSTIFICACIÓN

### 5.1 Valor científico y metodológico

La investigación aporta una contribución propia porque no se limita a aplicar buenas prácticas de arquitectura sobre un módulo. El aporte central es formular un método de refactorización arquitectónica incremental para una clase específica de problemas: subcircuitos críticos en sistemas legacy MVC institucionales.

El artefacto de Design Science se compone de:

- **Método:** pasos, criterios, entradas, salidas y condiciones de aplicación.
- **Instanciación:** aplicación del método en el subcircuito de ejecución POA de SIGPP.

Este enfoque permite evaluar si el método mejora modificabilidad, testabilidad y trazabilidad sin exigir una reescritura completa ni detener la operación institucional.

### 5.2 Valor técnico

La propuesta aporta valor técnico porque aborda problemas reales del código:

- separación de responsabilidades;
- reducción de lógica en controladores;
- mejora de testabilidad de reglas presupuestarias;
- menor acoplamiento con Symfony Forms y Doctrine;
- frontera más clara para el flujo tarea-presupuesto-certificación;
- mejor preparación para API o clientes móviles;
- documentación de una estrategia aplicable a subcircuitos legacy semejantes.

El flujo seleccionado es suficientemente complejo para una tesis porque no se limita a un CRUD. Incluye tareas, operaciones/ACP, presupuesto, kardex, disponibilidad, certificaciones y endpoints de consulta.

### 5.3 Valor práctico e institucional

Desde el punto de vista institucional, el subcircuito de ejecución POA impacta procesos de gestión y ejecución presupuestaria. Mejorar su arquitectura puede aportar:

- menor riesgo al modificar reglas de presupuesto;
- mayor confiabilidad en la emisión de certificaciones;
- mejor mantenibilidad del sistema;
- mejor base para integración con otros sistemas o clientes móviles;
- menor dependencia de conocimiento implícito del equipo técnico;
- lineamientos para modernizar otros subcircuitos de SIGPP.

## 6. ALCANCE Y DELIMITACIÓN

### 6.1 Lo que sí se abordará

La propuesta se enfocará en el **subcircuito de ejecución POA**, considerando tareas, operaciones/ACP, presupuesto y certificaciones.

Componentes principales:

| Componente | Rol dentro del estudio |
|---|---|
| `src/Controller/poa/Tarea/NewTareaController.php` | Creación de tarea y asignación inicial de presupuesto. |
| `src/Controller/poa/Tarea/EditTareaController.php` | Edición de tarea y ajustes relacionados. |
| `src/Entity/Tarea.php` | Entidad núcleo para tareas del subcircuito. |
| `src/Entity/PresupuestoAsignado.php` | Relación entre tarea, presupuesto, kardex y certificaciones. |
| `src/Entity/KardexPresupuesto.php` | Registro de movimiento presupuestario. |
| `src/Entity/Certificacion.php` | Certificación asociada al presupuesto asignado de la tarea. |
| `src/Service/Certificacion/CreateCertificacionService.php` | Emisión de certificación a partir de una tarea. |
| `src/Controller/poa/Certificacion/CreateCertificacionController.php` | Entrada web para emitir certificación por tarea. |
| `src/Repository/TareaRepository.php` | Consultas y persistencia de tareas. |
| `src/Repository/Utility/Tarea/TareaOneLineSql.php` | Consulta nativa de listado/API de tareas. |
| `src/Controller/poa/Api/TareaOneLineController.php` | API de listado de tareas. |
| `src/Controller/poa/Api/CertificacionOneLineController.php` | API de listado de certificaciones. |

### 6.2 Lo que queda fuera del alcance principal

Para mantener el alcance viable, no se abordará como intervención principal:

- elaboración POA;
- validación ministerial;
- evaluación POA trimestral;
- refactorización completa de SIGPP;
- migración a microservicios;
- actualización mayor de Symfony;
- rediseño completo de base de datos;
- reescritura total del módulo de certificaciones;
- rediseño de reportes Jasper;
- rediseño visual del frontend Twig;
- reemplazo total de Doctrine ORM;
- refactorización completa de todos los módulos de POA, Presupuesto o Administración.

La elaboración POA, la validación ministerial y la evaluación POA trimestral pueden aparecer como contexto o trabajo posterior recomendado, pero no como promesa de intervención principal. Certificaciones se considera únicamente en su relación directa con la tarea, el presupuesto asignado y la ejecución POA.

### 6.3 Defensa del alcance

El alcance no se limita por comodidad, sino por rigor. Trabajar todo SIGPP o todo el ciclo POA sería demasiado amplio para una tesis de maestría y dificultaría medir resultados. En cambio, el subcircuito de ejecución POA ofrece un flujo suficientemente complejo, medible y representativo.

Respuesta sugerida ante el docente:

> La tesis no propone refactorizar todo SIGPP ni todo el ciclo POA. Propone un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales y lo instancia en ejecución POA, porque allí convergen tareas, operaciones/ACP, presupuesto y certificaciones. Elaboración POA y evaluación POA quedan como contexto o alcance posterior, para evitar sobrealcance y mantener indicadores evaluables.

## 7. METODOLOGÍA Y MÉTRICAS DE EVALUACIÓN

### 7.1 Enfoque metodológico

La tesis se plantea bajo **Design Science**, porque busca diseñar, instanciar y evaluar un artefacto útil para resolver un problema de diseño en un contexto real.

El objeto de estudio no es SIGPP ni el proceso POA en sí mismo. El objeto de estudio es el artefacto propuesto:

> un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en SIGPP.

### 7.2 Estrategia técnica sugerida

La estrategia consiste en una refactorización arquitectónica incremental del subcircuito de ejecución POA, separando responsabilidades y haciendo explícitos los límites técnicos del flujo.

No se trata de Scrum ni de historias de usuario. Cuando se habla de flujo o subcircuito funcional, se hace referencia al comportamiento técnico del sistema, por ejemplo:

- crear o modificar una tarea POA;
- vincular la tarea con operaciones/ACP;
- asignar presupuesto;
- registrar kardex;
- verificar disponibilidad;
- emitir una certificación;
- exponer información por API.

La mejora puede aplicar principios de arquitectura limpia o hexagonal, pero de forma pragmática y compatible con Symfony 4.4/PHP 7.4.

### 7.3 Fases metodológicas

#### Fase 1: Diagnóstico

- Analizar estructura del subcircuito.
- Identificar clases críticas.
- Medir tamaño, acoplamiento y complejidad.
- Revisar pruebas existentes.
- Documentar flujo tarea-operación/ACP-presupuesto-certificación.

#### Fase 2: Diseño del método

- Definir criterios de selección de subcircuitos legacy MVC.
- Definir pasos incrementales de refactorización.
- Definir entradas y salidas por paso.
- Definir condiciones de aplicación y límites del método.
- Definir criterios de comparación antes/después.

#### Fase 3: Instanciación en SIGPP

- Aplicar el método al subcircuito de ejecución POA.
- Proponer una frontera arquitectónica explícita.
- Extraer lógica crítica desde controladores.
- Aislar reglas presupuestarias relevantes.
- Mejorar testabilidad del flujo tarea-presupuesto-certificación.
- Mantener compatibilidad con rutas existentes.

#### Fase 4: Evaluación

- Medir antes/después.
- Comparar acoplamiento.
- Comparar complejidad.
- Comparar cobertura de pruebas.
- Evaluar trazabilidad del cambio.
- Evaluar revisión técnica con un desarrollador independiente cuando sea posible.
- Documentar resultados y limitaciones.

### 7.4 Métricas sugeridas

| Dimensión | Indicador | Línea base / fuente | Herramienta sugerida |
|---|---|---|---|
| Tamaño | Líneas por clase | `Tarea.php` ≈ 1018, `TareaRepository.php` ≈ 646, `TareaOneLineSql.php` ≈ 223, `CreateCertificacionService.php` ≈ 277 | `wc`, PhpMetrics |
| Acoplamiento | llamadas a `getDoctrine()` en controladores | 252 en controladores del sistema | script estático / PhpMetrics |
| Acoplamiento | instanciaciones `new` en controladores | 486 en controladores del sistema | script estático |
| Complejidad | complejidad ciclomática por método | medir antes/después | PHPMD / PhpMetrics |
| Testabilidad | cobertura del flujo intervenido | PHPUnit configurado sobre `./src` | PHPUnit + coverage |
| Mantenibilidad | índice de mantenibilidad | medir antes/después | PhpMetrics |
| Trazabilidad | cantidad de archivos/capas impactadas por cambio funcional | medir antes/después sobre cambios definidos | revisión estática y commits controlados |
| API | esfuerzo para exponer o modificar respuesta API | cambios requeridos antes/después | análisis comparativo |
| SQL | consultas nativas relevantes | `TareaOneLineSql`, posible `CertificacionOneLineSql` | revisión estática |

### 7.5 Criterios de éxito

La propuesta puede considerarse exitosa si logra:

- explicitar una frontera arquitectónica para el subcircuito intervenido;
- reducir lógica en controladores intervenidos;
- aumentar cobertura de pruebas en reglas críticas;
- disminuir dependencias directas de Doctrine/Symfony en lógica de aplicación;
- separar mejor el flujo tarea-presupuesto-certificación;
- mantener compatibilidad funcional;
- documentar un método replicable para subcircuitos legacy MVC institucionales semejantes.

## 8. CRONOGRAMA GENERAL ESTIMADO

Se propone un cronograma de **5 meses**, extensible a 6 meses si se requiere mayor validación.

| Mes | Fase | Actividades principales | Producto esperado |
|---:|---|---|---|
| 1 | Diagnóstico | Revisión de dependencias, pruebas, controladores, entidades, repositorios, servicios y API del flujo tarea-operación/ACP-presupuesto-certificación. | Línea base técnica y matriz de deuda. |
| 2 | Diseño del método | Definición de pasos, criterios, entradas, salidas, límites y métricas del método de refactorización. | Método preliminar de refactorización arquitectónica incremental. |
| 3 | Instanciación I | Aplicación inicial sobre tareas, operaciones/ACP y presupuesto asignado. | Primer subflujo mejorado con pruebas o estrategia de prueba definida. |
| 4 | Instanciación II | Integración del flujo de certificación asociado y API/listados relacionados. | Flujo tarea-presupuesto-certificación validado. |
| 5 | Evaluación y redacción | Comparación antes/después, análisis de métricas, conclusiones y recomendaciones. | Informe final de tesis/perfil validado. |

## Conclusión

La propuesta se enfoca en el **método de refactorización arquitectónica incremental** y lo instancia en el **subcircuito de ejecución POA de SIGPP**. El análisis considera tareas, operaciones/ACP, presupuesto y certificaciones porque allí se observa un flujo funcional suficientemente complejo, medible y representativo.

Elaboración POA y evaluación POA quedan fuera de la intervención principal. Pueden usarse como contexto o como alcance posterior recomendado, pero incluirlas como promesa de trabajo principal rompería la delimitación y debilitaría la evaluación académica.
