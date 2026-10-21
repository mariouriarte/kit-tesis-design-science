# Estado de la tesis

## Datos generales

- **Tesista:** Mario Arturo Uriarte Marin
- **Programa:** Maestría en Ingeniería de Software (fijado)
- **Tutor:** Luis Roberto Pérez Rios, Ph.D. (fijado)
- **Institución de destino:** se define durante la traducción al modelo institucional
- **Fecha de inicio:** 2026-09-27
- **Título provisional:** Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales: instanciación en la ejecución POA de SIGPP
- **Entrega del perfil:** 2026-09-28, cumplida mediante repositorio público compartido en el grupo.
- **Próximo hito:** revisión individual anunciada por el tutor el 17 de octubre de 2026; requiere completar el documento final y contar con un avance importante en la propuesta. La fecha individual no fue comunicada en el mensaje aportado.
- **Predefensa tentativa:** última semana de octubre de 2026 o, como máximo, primera semana de noviembre de 2026.
- **Defensa tentativa:** finales de noviembre de 2026, fecha extraoficial comunicada por el tutor.

## Etapas

| Etapa | Estado | Archivo | Fecha de cierre |
|:--|:--|:--|:--|
| E0. Encuadre | cerrado | `00_estado.md` | 2026-09-27 |
| E1. Áreas y temas | cerrado | `01_areas_y_temas.md` | 2026-09-27 |
| E2. Delimitación | cerrado preliminar para perfil | `02_delimitacion.md` | 2026-09-27 |
| E3. Perfil de investigación DS | cerrado preliminar para perfil | `03_perfil_ds.md` | 2026-09-27 |
| E4. Marco teórico | iniciado | `04_marco_teorico.md` | |
| E5. Estado del arte | pendiente | `05_estado_del_arte.md` | |
| E6. Diagnóstico con indicadores | pendiente | `06_diagnostico.md` | |
| E7a. Alternativas de solución | pendiente | `07a_alternativas.md` | |
| E7b. Requisitos del artefacto | pendiente | `07b_requisitos.md` | |
| E7c. Diseño del artefacto | pendiente | `07c_diseno_artefacto.md` | |
| E7d. Plan de construcción y versiones | pendiente | `07d_plan_construccion.md` | |
| E7e. Construcción y verificación interna | pendiente | `07e_construccion_verificacion.md` | |
| E7f. Ficha del artefacto | pendiente | `07f_ficha_artefacto.md` | |
| E8. Evaluación | pendiente | `08_evaluacion.md` | |
| E9. Enlace propuesta ↔ solución | pendiente | `09_enlace_solucion.md` | |
| E10. Contribución y conclusiones | pendiente | `10_contribucion_conclusiones.md` | |

## Decisiones tomadas

| Fecha | Decisión | Justificación |
|:--|:--|:--|
| 2026-09-27 | Trabajar la tesis en este repositorio con el kit de Design Science. | El tutor indicó que el trabajo debe desarrollarse con OpenCode y versionarse en un repositorio propio. |
| 2026-09-27 | Mantener `tesis_ds/` versionado. | El tutor indicó en el grupo que los archivos generados en `tesis_ds/` deben versionarse para revisión en el repositorio propio. |
| 2026-09-27 | Tomar como tema tentativo la mejora arquitectónica del módulo de tareas POA en el sistema legacy SIGPP. | El tesista trabaja sobre el sistema SIGPP, Sistema Integral de Gestión POA Presupuesto, y cuenta con una propuesta inicial en `tmp/propuesta-tesis.md`. |
| 2026-09-27 | Cerrar E0 con fechas extraídas de `tmp/chat.md`. | El chat indica entrega de resultados del agente para el lunes 28 de septiembre, predefensa idealmente a fines de octubre o máximo primera semana de noviembre, y defensa extraoficial a finales de noviembre. |
| 2026-09-27 | Registrar arquitectura de software, refactorización y automatización CI/CD como área de experiencia mayor. | El tesista declaró esa área como su mayor experiencia dentro de Ingeniería de Software. |
| 2026-09-27 | Registrar cuatro años de experiencia aplicada en arquitectura, refactorización y CI/CD. | El tesista informó experiencia en sistemas legacy de la Caja Petrolera de Salud, Sistema Integral de Seguros, PayCPS, Medimedic.net y AnyGym; aclaró que AnyGym fue desarrollado con DDD desde el inicio. |
| 2026-09-27 | Registrar acceso total a SIGPP como contexto real de construcción y evaluación. | El tesista creó SIGPP, lideró el proyecto y actualmente es su desarrollador principal; el sistema está desplegado en `sigpp.cps.org.bo`. |
| 2026-09-27 | Precisar PayCPS como experiencia fuerte en DDD, CI/CD, pruebas e integración institucional. | El tesista aclaró que PayCPS fue diseñado con DDD desde el inicio, tiene CI/CD, pruebas unitarias y de integración, e integra Banco Unión, AGETIC y pagos digitales de la CPS. |
| 2026-09-27 | Registrar viabilidad de evaluación local con datos ficticios y consentimiento institucional. | El tesista indicó que no puede mostrar certificaciones reales, pero sí datos ficticios en entorno local, y que puede solicitar consentimiento al área dueña del software con alcances y límites. |
| 2026-09-27 | Registrar disponibilidad de un revisor técnico independiente. | Existe un desarrollador del equipo que conoce SIGPP y fue desarrollador principal en módulos como certificaciones y devengados, por lo que puede revisar la propuesta y reducir el sesgo del constructor. |
| 2026-09-27 | Orientar el artefacto como composición método más instanciación. | El tesista aceptó que la contribución no sea solo una mejora del sistema, sino un método de refactorización arquitectónica incremental aplicado y evaluado en SIGPP. |
| 2026-09-27 | Ampliar la comprensión del dominio SIGPP más allá de tarea-presupuesto-certificación. | El tesista explicó que SIGPP articula elaboración, validación y ejecución del POA; tareas, operaciones, ACP, REACP, evaluación trimestral, presupuesto y certificación bajo normativa boliviana. |
| 2026-09-27 | Registrar al DNGP como área dueña del sistema SIGPP. | El Departamento Nacional de Gestión y Planificación es la parte interesada institucional que puede definir consentimiento, alcances y límites. |
| 2026-09-27 | Delimitar la tesis al subcircuito de ejecución POA. | El tesista aceptó trabajar tareas vinculadas a operaciones y ACP, presupuesto y certificación; elaboración, validación ministerial y evaluación trimestral quedan como contexto y restricciones. |
| 2026-09-27 | Cerrar E1 con un tema elegido. | El tema seleccionado es la refactorización arquitectónica incremental del subcircuito de ejecución POA en SIGPP mediante un método aplicado y evaluado sobre tareas, operaciones/ACP, presupuesto y certificación. |
| 2026-09-27 | Registrar elaboración POA y evaluación POA como módulos candidatos a refactorización posterior. | Ambos pertenecen al circuito de tareas POA, pero se mantienen fuera del alcance principal para evitar sobrealcance. |
| 2026-09-27 | Formular preliminarmente el problema de diseño de E2. | El problema se centra en la falta de frontera arquitectónica explícita del subcircuito de ejecución POA y su lógica dispersa entre controladores, servicios, repositorios, entidades Doctrine y consultas SQL. |
| 2026-09-27 | Formular preliminarmente el problema de investigación como brecha. | La brecha se plantea entre materiales prácticos de marcos MVC, principios de arquitectura/testabilidad y la falta de un método incremental evaluable para refactorizar subcircuitos legacy institucionales sin reescritura completa. |
| 2026-09-27 | Declarar el objeto de estudio de Design Science. | El objeto de estudio es un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en SIGPP; SIGPP es el contexto de aplicación y evaluación. |
| 2026-09-27 | Declarar el campo de acción. | El campo comprende subcircuitos funcionales críticos de sistemas legacy MVC institucionales con lógica dispersa, acoplamiento al marco y persistencia, y necesidad de evolución sin reescritura completa. |
| 2026-09-27 | Cerrar E2 preliminarmente con propuesta aceptada. | Se propone diseñar y evaluar un método de refactorización arquitectónica incremental, instanciado en el subcircuito de ejecución POA de SIGPP, para explicitar fronteras funcionales, separar reglas de negocio e incorporar pruebas automatizadas. |
| 2026-09-27 | Iniciar E3 con título y perfil preliminar. | El título aceptado fue: “Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales: instanciación en la ejecución POA de SIGPP”. |
| 2026-09-27 | Ajustar la pregunta de investigación para incluir SIGPP como caso de instanciación. | El tesista solicitó que la pregunta principal mencione el caso de estudio sin usar el nombre incorrecto SIPOA4. |
| 2026-09-27 | Formular oración candidata de contribución original. | La contribución se expresa como principios de diseño validados para refactorizar incrementalmente subcircuitos funcionales críticos en sistemas legacy MVC institucionales. |
| 2026-09-27 | Cerrar E3 preliminarmente. | El tesista aceptó la oración de contribución original, cumpliendo el gate de E3 para el perfil inicial. |
| 2026-09-27 | Crear perfil preliminar para revisión del lunes 28. | Se generó `tesis_ds/perfil_presentacion_lunes.md` con los elementos esenciales del perfil inicial. |
| 2026-09-28 | Registrar el nuevo hito del lunes 5 de octubre. | El tutor indicó en el grupo: “Próximo hito, la propuesta. Límite para el borrador Lunes 5 de octubre”; por tanto, el trabajo debe avanzar desde el perfil hacia el desarrollo de la propuesta. |
| 2026-09-28 | Iniciar E4 con tres ejes teóricos. | El marco teórico se orienta a código heredado y cambio seguro, arquitectura como fronteras/dependencias/atributos de calidad, y testabilidad como condición para refactorización incremental. |
| 2026-09-28 | Rechazar como promesa una migración completa a arquitectura limpia o hexagonal. | El tesista aceptó que una migración completa agregaría complejidad y podría empeorar el sistema; la propuesta se concentra en frontera arquitectónica incremental con desacoplamiento y pruebas. |
| 2026-10-04 | Preparar borrador de propuesta para revisión del 5 de octubre. | Se consolidó el perfil preliminar, la línea base técnica inicial, la lectura parcial de Feathers sobre falta de pruebas y la estrategia de evaluación mínima de maestría en `propuesta_borrador_2026-10-05.md`. |
| 2026-10-13 | Registrar aplicación inicial y parcial de la mejora arquitectónica en SIGPP/SIPOA4. | Se creó `src/Service` y se extrajo parcialmente lógica desde controladores en procedimientos de creación de tareas de elaboración y modificación POA; esto se tratará como intervención inicial, verificación técnica preliminar y evaluación formativa, no como solución final. |
| 2026-10-13 | Redirigir la contribución hacia la formalización de la mejora. | La aplicación inicial mostró avances en separación de responsabilidades y posibilidad de pruebas unitarias, pero también inconsistencias por mezcla de objetos de valor y objetos de transferencia de datos; por tanto, la tesis debe formalizar, corregir y sistematizar el método. |
| 2026-10-13 | Registrar archivos y commits concretos de la intervención inicial. | La evidencia preliminar incluye `CreateCertificacionController.php`, `CreateCertificacionService.php`, `CreateCertificacionInput.php`, `CreateCertificacionAutorizacionService.php`, `CreateCertificacionAutorizacionTest.php` y commits `815ce6c0`, `6e333e27`, `9d4af430`; falta revisar diffs y métricas para usarlos como evidencia final. |
| 2026-10-13 | Cuantificar la evidencia Git de la intervención inicial. | Los commits registrados muestran cambios defendibles: `9d4af430` con 12 archivos, +302/-155; `6e333e27` con 16 archivos, +472/-87; `815ce6c0` con 13 archivos, +428/-39. La conclusión se mantiene como evaluación formativa inicial por falta de prueba directa para `CreateCertificacionService.php`. |
| 2026-10-13 | Registrar ejecución satisfactoria de pruebas unitarias. | Se ejecutó `rtk phpunit` con resultado `PHPUnit: OK (151 tests, 235 assertions)`. Esta evidencia respalda testabilidad parcial, pero no valida directamente `CreateCertificacionService.php`, que sigue sin prueba unitaria directa identificada. |
| 2026-10-13 | Definir regla de rediseño para la siguiente versión del método. | No se partirá de nuevas historias de usuario, sino de refactorizar el flujo existente de certificación. Se usarán pruebas de caracterización para lógica heredada y pruebas directas para servicios aislados. La arquitectura objetivo será limpia, mínima e incremental, sin migración completa a DDD ni arquitectura hexagonal. |
| 2026-10-13 | Registrar arquitectura ejemplo para certificación. | La primera arquitectura ejemplo reducirá `CreateCertificacionController.php` a coordinación HTTP, moverá preparación de vista a un servicio, entregará DTOs finales a Twig y aislará consultas Doctrine mediante repositorios o servicios de consulta. |
| 2026-10-13 | Elegir restricción de subpartida como primer comportamiento a caracterizar. | Es una regla de negocio central, actualmente acoplada al controlador y conectada a repositorios Doctrine; decide autorización, tipo de contrato y archivo adjunto, por lo que evidencia mejor el problema arquitectónico que una mejora de presentación. |
| 2026-10-13 | Definir escenarios mínimos de caracterización de restricción de subpartida. | La prueba debe cubrir restricción por actividad, restricción sin actividad y ausencia de restricción. La regla se declara como configuración del Departamento Financiero sobre subpartida, gestión, administración y actividad opcional, no como subpartida fija. |
| 2026-10-13 | Definir salida observable de la primera prueba de caracterización. | La primera prueba verificará la resolución de la restricción: devuelve restricción específica, restricción general o `null`. Los efectos posteriores —autorización, tipo de contrato y archivo adjunto— quedan para pruebas posteriores. |
| 2026-10-13 | Nombrar el componente de extracción de restricción de subpartida. | El componente será `RestriccionSubPartidaResolver`; encapsulará la regla de selección de restricción y no decidirá todavía autorización, tipo de contrato ni archivo adjunto. |
| 2026-10-13 | Definir estrategia de prueba para `RestriccionSubPartidaResolver`. | La primera prueba será directa contra el resolver, formulada como caracterización de la regla observada en el controlador original. No se reclamará como prueba funcional del controlador, para evitar arrastrar infraestructura Symfony, Doctrine, formulario y Twig. |

## Preguntas abiertas

- Se verificó el punto de extensión de parámetros y su selección de gestión: `getGestion()` usa URL con valor alternativo de gestión actual; `getGestionActual()` usa la marcada actual en base de datos, no necesariamente el año del reloj. El tesista delimitó reutilizar administración existente: operador administrador selecciona gestión anterior y crea tipo extraordinario con los períodos existentes, sin rediseñarlos. El formulario tiene lista cerrada de tipos: requiere nueva opción, fábrica/carga y comprobación coherente en presentación/guardado; sin implementación realizada.

- El 20 de octubre el tesista confirmó habilitación extraordinaria configurable para una gestión anterior concreta, en cualquier momento del año actual, conservando fechas documentales 29/31 de diciembre del año inmediatamente anterior. La extraordinaria vigente basta como habilitación temporal aunque la global esté cerrada; no dispensa permisos ni saldo. Se revisó HU-FEC-02 explícitamente: enero–marzo queda como antecedente, no restricción del diseño nuevo. El administrador establecerá inicio/fin mediante el mecanismo existente; falta formalizar la extensión técnica. No se decidió hacer configurables días documentales ni permitir cualquier gestión histórica. Se separará este cambio funcional de la extracción estructural.

- E4 avanzó el 20 de octubre con una búsqueda focalizada sobre criterio de modularización y testabilidad (`busqueda_e4_2026-10-20.md`): Parnas (1972) y Abbasi et al. (2026) contrastados en metadatos/resumen; acceso ACM bloqueado y sin lectura íntegra. Bagheri-Galle et al. (2025) queda como consulta de contenido pendiente. Falta que el tesista defienda el criterio de separación de la política de fechas y completar literatura; no se cierra E4 ni se modifica código.

- Aclaración temporal resuelta por el tesista: los períodos y montos de planificación son referenciales para ejecución y monitoreo, no una nueva prohibición automática de certificar fuera de un trimestre programado. `Operacion` agrupa tareas; el día de registro de referencia del intento no es una fecha de esa entidad. Permanecen las reglas de gestión y de fecha ya declaradas. Falta precisar cómo las modificaciones POA representan técnicamente pérdida de recursos o desaparición de tareas y su efecto sobre elegibilidad; no se presume borrado físico ni regla nueva.

- Verificar la secuencia temporal de caracterización previa y TDD declarada por el tesista: el estado actual del código y sus resultados ya se contrastaron, pero faltan registros intermedios. El 18 de octubre se reprodujeron 188 pruebas y 540 aserciones en PHP 7.4.29, y 37 pruebas y 305 aserciones en el directorio nuevo de certificación. No constituyen validación completa del método. El tesista declaró que no hubo avances adicionales desde el 13 de octubre hasta esta sesión ni avance del documento antes de esta revisión.
- Discutir y defender el contrato candidato de arquitectura registrado en `arquitectura_candidata_certificacion_2026-10-18.md`: MVC con frontera de aplicación incremental, no una migración completa a arquitectura limpia/hexagonal o DDD. Falta elegir y justificar el siguiente escenario de cambio y sus criterios antes de modificar más código.
- Precisar un defecto reproducible de restricción o validación: el tesista identifica restricciones de subpartida y defectos en PHP y JavaScript acoplado a Twig como necesidades reales de cambio. Las conexiones con otros sistemas son requisitos previstos aún sin delimitar; no se autoriza por ello construir una API ni ampliar el alcance.
- Revisar para eventual adopción el borrador del proyecto SIGPP `docs/development/architecture-contract.md`, leído en esta sesión: preparación opcional, separación de responsabilidades PHP/JavaScript, excepciones y pautas de intervención. No está aprobado ni valida el método; falta reconciliarlo con la nota candidata de tesis y convertir sus referencias a APA 7 si se incorpora como anexo.
- El tesista confirmó `America/La_Paz` como zona horaria institucional de operación y que `fecha` representa solo el día; declaró la hora un error de implementación. HU-FEC-01/HU-FEC-02 y el criterio de igualdad de admisibilidad para distintas horas del mismo día están en `reglas_fecha_certificacion.md`. Falta decidir la transición del formulario/almacenamiento tras revisar consumidores, confirmar respaldo institucional y revisar otras barreras del servidor. No se autorizó migración ni se afirmó un defecto HTTP reproducido.

- Completar los requisitos para la revisión individual anunciada el 17 de octubre: documento final y avance importante de propuesta; después se anunció alineación con ALSIE y preparación de informe borrador y predefensa. Fuente: mensaje transcrito y captura aportados por el tesista. El tesista aclaró que la prioridad no es redactar una respuesta al docente, sino completar la investigación.

- Confirmar, si ALSIE lo comunica formalmente, las fechas oficiales de predefensa y defensa.
- Definir más adelante si el desarrollador revisor participará en evaluación formativa, sumativa o ambas.
- Verificar en E4 y E5 la brecha bibliográfica sobre aprendizaje de marcos MVC, arquitectura, testabilidad y refactorización incremental de sistemas legacy.
- Convertir los criterios de éxito preliminares en indicadores operacionales antes de construir.
- Depurar el primer borrador de propuesta para el lunes 5 de octubre de 2026; el archivo base ya fue preparado, pero falta revisión final antes de compartir.
- Completar E4 con literatura reciente verificada sobre refactorización legacy, deuda técnica arquitectónica, testabilidad y evolución de sistemas MVC/monolíticos.
- Revisar y depurar `tesis_ds/propuesta_borrador_2026-10-05.md` antes de compartirlo como entregable de propuesta.
- Cuantificar la evidencia técnica de la intervención inicial: archivos modificados, cantidad de lógica extraída, pruebas unitarias existentes, resultados de ejecución y comparación antes/después.
- Si el tiempo lo permite, medir antes/después de `CreateCertificacionController.php` y `CreateCertificacionService.php`: líneas, complejidad aproximada, dependencias directas y reglas verificables.
- Complementar las pruebas existentes del resolvedor y del servicio con evidencia de integración y revisión independiente, según criterios que se definan antes de la siguiente intervención. Los tres escenarios mínimos del resolvedor ya están implementados y pasan.

## Avances previos disponibles

- Existe una propuesta inicial en `tmp/propuesta-tesis.md`.
- El contexto real disponible es el sistema legacy SIGPP, Sistema Integral de Gestión POA Presupuesto, sobre el cual trabaja el tesista.
- Corrección registrada: el sistema no se denomina SIPOA4 en este trabajo, sino SIGPP.

## Restricciones de tiempo

- El perfil inicial debía estar listo para el lunes 28 de septiembre de 2026 y ya fue compartido en el grupo.
- El primer borrador de propuesta debe estar listo para el lunes 5 de octubre de 2026.
- La predefensa debería ocurrir idealmente la última semana de octubre de 2026 o, como máximo, la primera semana de noviembre de 2026.
- La defensa está prevista de forma extraoficial para finales de noviembre de 2026.

## Próximo paso

### Comprobación de contexto del 20 de octubre de 2026

En SIGPP, `8dc63307` confirma la extracción del resolvedor con pruebas y `1294047e` confirma el contrato borrador; `HEAD` observado es `1294047e`. El estado inspeccionado solo muestra cambios en `.gitignore` y `tmp/propuesta-tesis.md`; ya no se describen resolvedor, pruebas ni contrato como archivos sin seguimiento. No se comprobó envío remoto ni se reprodujeron nuevamente pruebas. La aclaración administrativa posterior resuelve el alcance: reutilizar gestión y períodos existentes con un tipo extraordinario, sin prolongar la discusión de granularidad ni ampliar el mecanismo general.

### Punto de reanudación acordado

El tesista solicitó versionar y enviar el avance del repositorio de tesis, y continuar mañana. Retomar desde E4 y los archivos `arquitectura_candidata_certificacion_2026-10-18.md` y `reglas_fecha_certificacion.md`, sin volver a preguntar zona horaria ni significado de `fecha`: `America/La_Paz` y día calendario están confirmados. Priorizar la fundamentación de la política de fechas y los criterios prospectivos, conservando como pendientes la reproducción controlada, el contraste de soluciones y la transición de formulario/almacenamiento. No modificar código ni datos históricos por el solo hecho de retomar; el contrato del proyecto permanece como borrador discutible y los cambios de SIGPP pertenecen a un repositorio separado.

- Completar E4 y la justificación del camino arquitectónico candidato; después cerrar E5 y E6 antes de ejecutar otra intervención planificada. Conservar los resultados anteriores como exploratorios y los commits de marzo de 2025 como antecedentes, sin presentarlos como construcción prospectiva de la tesis. No iniciar traducción ALSIE mientras E0–E10 no estén cerradas.
- La inspección estática ampliada del recorrido está registrada en `reglas_fecha_certificacion.md`: saldo validado localmente, fecha solo anual, acceso general por rol y controles específicos de permiso/habilitación no acreditados al guardar. Próximo candidato acotado: política de fecha calendario con operación controlable y rechazo sin efectos; aún faltan fundamentación, contraste, reproducción controlada y requisitos previos a implementación. No ampliar el incremento a todos los permisos ni migrar datos por estos hallazgos.
