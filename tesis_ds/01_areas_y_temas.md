# E1. Áreas y temas

## Área de experiencia mayor

El área de experiencia mayor declarada por el tesista es **arquitectura de software**, con énfasis práctico en **refactorización** e **implementación de automatización CI/CD**.

Esta área es coherente con el tema tentativo porque el problema preliminar del sistema SIGPP no se limita a corregir defectos puntuales, sino que apunta a una clase de problema propia de Ingeniería de Software: evolución arquitectónica de módulos acoplados en sistemas legacy con restricciones institucionales, tecnológicas y operativas.

## Experiencia declarada

El tesista declara **cuatro años de experiencia** en arquitectura de software, refactorización e implementación de CI/CD. Esa experiencia se desarrolló principalmente sobre sistemas legacy e iniciativas de software propias.

### Contextos organizacionales y proyectos

| Contexto o proyecto | Tipo de experiencia relevante |
|:--|:--|
| Caja Petrolera de Salud | Trabajo sobre sistemas legacy institucionales. |
| Sistema Integral de Seguros | Experiencia en sistemas institucionales de gestión. |
| PayCPS, pasarela de pagos | Sistema desarrollado con DDD, arquitectura planificada desde el inicio, CI/CD, pruebas unitarias y de integración. Actualmente opera con Banco Unión y AGETIC mediante conexión a sus API, y centraliza los sistemas de pago digital de la Caja Petrolera de Salud. |
| Medimedic.net | Emprendimiento propio: plataforma SaaS integral de gestión médica orientada a conectar médicos y pacientes y optimizar flujos de atención y procesos administrativos en salud. |
| AnyGym | Proyecto propio para asistencia a gimnasio y otros deportes, desarrollado en Python con DDD desde el inicio; orientado al aprendizaje de agentes de IA con Claude Code y OpenCode. El backend se encuentra casi terminado. |

Esta trayectoria refuerza la pertinencia práctica del tema porque combina experiencia en sistemas legacy institucionales, evolución arquitectónica, automatización técnica e iniciativas propias donde el tesista ha tomado decisiones de diseño de software.

## Contexto real disponible para construir y evaluar

El contexto real disponible es el sistema **SIGPP**, Sistema Integral de Gestión POA Presupuesto, desplegado en `sigpp.cps.org.bo`. El tesista declara control total sobre el sistema: fue su creador, lideró el proyecto y actualmente es el desarrollador principal. Esta condición ofrece acceso fuerte para una tesis de Design Science, porque permite inspeccionar el código, intervenir una rama de trabajo, construir el artefacto, ejecutar mediciones técnicas y documentar evidencia antes/después.

La trayectoria del sistema también aporta una condición relevante para la investigación: SIGPP fue creado cuando el tesista aún no dominaba arquitectura de software, por lo que constituye un caso real de sistema legacy propio cuya evolución arquitectónica puede analizarse con conocimiento interno profundo. Este acceso es una fortaleza, pero también introduce riesgo de sesgo del constructor; por ello, la evaluación deberá incorporar revisión o validación por actores distintos al tesista cuando se llegue a E8.

## Restricciones y viabilidad declaradas

El tesista declara que los puntos críticos de acceso son viables: puede trabajar en un entorno local, crear datos ficticios para la base de datos, intervenir técnicamente el sistema y documentar evidencia del comportamiento del módulo. Aunque no puede mostrar certificaciones reales, sí puede construir datos sintéticos para reproducir el flujo tarea-presupuesto-certificación sin exponer información sensible.

La información relacionada con el POA institucional suele ser pública en Bolivia; aun así, el trabajo no debe asumir que todo dato operativo puede publicarse. Para controlar el riesgo ético e institucional, el tesista puede solicitar al área dueña del software —la parte interesada institucional— un consentimiento explícito, junto con los alcances y límites de uso de la información, del código y de las evidencias técnicas que podrán aparecer en la tesis.

Esta condición permite formular una estrategia de evaluación con tres capas: medición técnica sobre código y pruebas, demostración local con datos ficticios, y validación institucional acotada mediante consentimiento del área responsable.

## Revisor independiente disponible

Existe un desarrollador del equipo que conoce integralmente el software y ha sido desarrollador principal en varios módulos, entre ellos certificaciones y devengados. Este perfil es relevante para reducir el sesgo del tesista como creador y desarrollador principal de SIGPP, porque puede revisar la propuesta arquitectónica, contrastar la comprensión del flujo tarea-presupuesto-certificación y validar si la mejora es comprensible, aplicable y mantenible desde la perspectiva de otro miembro técnico del equipo.

En etapas posteriores, esta participación deberá formalizarse como revisión técnica o evaluación formativa, con criterios explícitos e instrumento de registro. No basta con una aprobación verbal; la evidencia deberá quedar documentada.

Además, existe apoyo potencial del equipo que realiza pruebas en un servidor controlado de pruebas, así como de los responsables institucionales dueños del software. Esta disponibilidad permite sostener la evaluación con evidencia adicional: verificación técnica en un entorno no productivo, revisión de avances por actores que conocen el uso institucional del sistema y validación de los límites de publicación de la información.

## Alcance funcional corregido del dominio SIGPP

La propuesta inicial no debe reducir el dominio a la secuencia tarea → presupuesto → certificación. En SIGPP, la tarea forma parte de un circuito institucional periódico que se abre a todas las unidades de producción de la Caja Petrolera de Salud, usualmente en agosto, y se articula con tres momentos principales:

1. **Elaboración del POA**, realizada por el área ejecutiva y operativa, incluyendo las unidades de producción.
2. **Validación del POA**, vinculada a la revisión por instancias externas como el Ministerio de Economía.
3. **Ejecución del POA**, habilitada al inicio de la gestión para que el sistema opere financieramente junto con el área de presupuestos, incluyendo procesos de presupuestación y certificación.

El área dueña de SIGPP es el **Departamento Nacional de Gestión y Planificación (DNGP)**. El sistema se encuentra enmarcado en normas y reglamentos del Ministerio de Planificación, del Ministerio de Economía y en leyes del Estado boliviano. Por tanto, la intervención arquitectónica debe respetar no solo relaciones técnicas entre clases y módulos, sino también reglas institucionales de planificación, presupuesto, evaluación y control.

En términos funcionales, las tareas se relacionan con operaciones, y estas con las **Acciones de Corto Plazo (ACP)**, que representan una perspectiva ejecutiva de planificación. Las operaciones y tareas son evaluadas trimestralmente por las unidades de producción y por los responsables de Acción de Corto Plazo (REACP), quienes confirman y validan la información. Esta estructura amplía la clase de problema: no se trata solamente de extraer lógica de un controlador, sino de rediseñar incrementalmente un flujo institucional complejo donde planificación, presupuesto, certificación y evaluación trimestral están acoplados.

## Tipología de artefacto acordada

Se acuerda orientar el artefacto como una **composición**:

- **Método:** una estrategia de refactorización arquitectónica incremental para módulos legacy institucionales con flujos normativos, presupuestarios y de evaluación periódica.
- **Instanciación:** aplicación del método en SIGPP, inicialmente sobre el flujo relacionado con tareas POA y sus conexiones con operaciones, ACP, presupuesto, certificaciones y evaluación trimestral.

Esta decisión evita presentar el trabajo como una simple mejora local del sistema. La instanciación en SIGPP será el vehículo de evaluación; la contribución de maestría deberá formularse como principios o criterios transferibles para intervenir sistemas legacy institucionales de características semejantes.

## Delimitación inicial aceptada

Se acepta como delimitación inicial trabajar el **subcircuito de ejecución POA**, comprendido por tareas vinculadas a operaciones y ACP, presupuesto y certificación. La elaboración del POA, la validación ministerial y la evaluación trimestral se mantendrán como contexto y restricciones del dominio, pero no como alcance directo de intervención arquitectónica en esta primera tesis.

Esta delimitación evita el sobrealcance y conserva la relevancia institucional del problema. También permite declarar, como resultado del diagnóstico y de la experiencia de refactorización, qué módulos adicionales deberían refactorizarse posteriormente, sin convertirlos en objeto de construcción ni evaluación principal.

## Tema elegido para continuar

El tema elegido para avanzar a delimitación es: **refactorización arquitectónica incremental del subcircuito de ejecución POA en SIGPP mediante un método aplicado y evaluado sobre tareas, operaciones/ACP, presupuesto y certificación**.

Este tema queda seleccionado por su ajuste con el área de experiencia del tesista, su acceso completo al contexto real, la disponibilidad de evaluación técnica en entorno controlado y la posibilidad de convertir la intervención en conocimiento transferible para sistemas legacy institucionales.

## Módulos candidatos a refactorización posterior

Estos módulos se registran como resultado de la experiencia técnica del tesista y del conocimiento del circuito SIGPP, pero no forman parte del alcance principal de construcción y evaluación de la tesis:

- **Elaboración POA**, por su relación con la apertura periódica del circuito de tareas POA y la participación de unidades de producción.
- **Evaluación POA**, por su relación con la evaluación trimestral de operaciones y tareas dentro del circuito institucional.

Estos módulos deberán aparecer como **alcance recomendado posterior**, no como promesa de intervención. Si se incorporan al alcance principal, la tesis corre riesgo de sobrealcance para el calendario disponible.

## Cierre de E1

E1 queda cerrada con un tema único, acceso real suficiente y una tipología preliminar de artefacto como composición método + instanciación. La puerta de control se considera cumplida porque el tema no depende de un contexto inaccesible y el tesista tiene control técnico e institucional suficiente para construir y evaluar una primera versión.

## Tema tentativo registrado

El tema tentativo es la mejora arquitectónica del módulo de tareas POA del sistema legacy SIGPP, considerando el flujo presupuestario asociado hasta certificaciones, con el propósito de reducir acoplamiento, mejorar testabilidad y facilitar evolución hacia interfaces web y API mantenibles.

## Evaluación preliminar de pertinencia Design Science


| Criterio | Evaluación preliminar |
|:--|:--|
| Relevancia práctica | Alta, porque el tesista trabaja sobre un sistema real y el módulo de tareas POA afecta planificación, presupuesto y certificaciones. |
| Acceso al contexto | Alto: el tesista tiene control técnico sobre SIGPP, entorno local, datos ficticios, servidor controlado de pruebas y posibilidad de revisión por actores técnicos e institucionales. |
| Factibilidad | Potencialmente viable si el alcance se mantiene en un flujo crítico y no en la refactorización completa del sistema SIGPP. |
| Riesgo metodológico | El tema puede degradarse a proyecto de ingeniería si solo se implementa una refactorización sin extraer principios transferibles de diseño. |
| Tipo de artefacto probable | Composición: método de refactorización arquitectónica incremental más instanciación aplicada al circuito POA seleccionado en SIGPP. |
| Contribución potencial de maestría | Principios de diseño validados para intervenir módulos presupuestarios acoplados en sistemas legacy monolíticos, con evidencia formativa y sumativa. |

## Advertencia metodológica

La propuesta actual todavía está formulada con fuerza técnica, pero debe cuidarse que el resultado no sea solamente una mejora local de SIGPP. En Design Science, la instanciación en SIGPP es el vehículo de aprendizaje; la contribución de maestría debe expresarse como principios de diseño o una estrategia transferible a una clase de contextos semejantes.

## Preguntas pendientes de E1

- Definir en E8 si el revisor independiente participará como evaluador formativo, evaluador sumativo o ambos.
