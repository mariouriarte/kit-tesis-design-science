# Estado de la tesis

## Datos generales

- **Tesista:** Mario Arturo Uriarte Marin
- **Programa:** Maestría en Ingeniería de Software (fijado)
- **Tutor:** Luis Roberto Pérez Rios, Ph.D. (fijado)
- **Institución de destino:** se define durante la traducción al modelo institucional
- **Fecha de inicio:** 2026-09-27
- **Título provisional:** Método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales: instanciación en la ejecución POA de SIGPP
- **Entrega del perfil:** 2026-09-28, según expectativa comunicada por el tutor en el grupo.
- **Predefensa tentativa:** última semana de octubre de 2026 o, como máximo, primera semana de noviembre de 2026.
- **Defensa tentativa:** finales de noviembre de 2026, fecha extraoficial comunicada por el tutor.

## Etapas

| Etapa | Estado | Archivo | Fecha de cierre |
|:--|:--|:--|:--|
| E0. Encuadre | cerrado | `00_estado.md` | 2026-09-27 |
| E1. Áreas y temas | cerrado | `01_areas_y_temas.md` | 2026-09-27 |
| E2. Delimitación | cerrado preliminar para perfil | `02_delimitacion.md` | 2026-09-27 |
| E3. Perfil de investigación DS | cerrado preliminar para perfil | `03_perfil_ds.md` | 2026-09-27 |
| E4. Marco teórico | pendiente | `04_marco_teorico.md` | |
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

## Preguntas abiertas

- Confirmar, si ALSIE lo comunica formalmente, las fechas oficiales de predefensa y defensa.
- Definir más adelante si el desarrollador revisor participará en evaluación formativa, sumativa o ambas.
- Verificar en E4 y E5 la brecha bibliográfica sobre aprendizaje de marcos MVC, arquitectura, testabilidad y refactorización incremental de sistemas legacy.
- Convertir los criterios de éxito preliminares en indicadores operacionales antes de construir.

## Avances previos disponibles

- Existe una propuesta inicial en `tmp/propuesta-tesis.md`.
- El contexto real disponible es el sistema legacy SIGPP, Sistema Integral de Gestión POA Presupuesto, sobre el cual trabaja el tesista.
- Corrección registrada: el sistema no se denomina SIPOA4 en este trabajo, sino SIGPP.

## Restricciones de tiempo

- El perfil inicial debe estar listo para el lunes 28 de septiembre de 2026.
- La predefensa debería ocurrir idealmente la última semana de octubre de 2026 o, como máximo, la primera semana de noviembre de 2026.
- La defensa está prevista de forma extraoficial para finales de noviembre de 2026.

## Próximo paso

- Preparar una versión presentable del perfil inicial y luego iniciar E4/E5 con verificación bibliográfica.
