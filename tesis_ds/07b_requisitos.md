# E7b. Requisitos del artefacto

**Estado:** en curso. Este documento sustituye al borrador del 13 de octubre, que usaba «arquitectura limpia mínima» y «SIPOA4», expresiones ya corregidas a «MVC con frontera de aplicación incremental» y «SIGPP». Los requisitos derivan de las decisiones del método (D01–D09), de las adaptaciones (A01–A04) y de los indicadores del diagnóstico (I01–I04); cada uno es rastreable al problema y a una métrica.

## 1. Enfoque: qué se exige al artefacto y por qué

El artefacto es una composición de método e instanciación. Por tanto, sus requisitos son de dos naturalezas: propiedades que el método debe imponer a cualquier intervención (requisitos del método) y propiedades que el incremento concreto en SIGPP debe satisfacer (requisitos de la instanciación). No se trata solo de funcionalidades de software: el método existe para hacer verificable, repetible y transferible una forma de intervenir, y la instanciación existe para poner a prueba esas reglas y dejar evidencia.

La evaluación formativa inicial mostró la consecuencia de omitir requisitos explícitos: se extrajo lógica hacia servicios sin que el servicio principal de creación contara con prueba directa identificada. El requisito que sigue de ese hallazgo no es «escribir más pruebas», sino fijar una condición de suficiencia por paso, antes de dar una extracción por terminada.

## 2. Requisitos del método

| ID | Requisito | Tipo | Métrica | Fuente en el problema o diagnóstico | Prioridad |
|:--|:--|:--|:--|:--|:--|
| R1 | Seleccionar el incremento por necesidad concreta de cambio y riesgo, no por limpiar carpetas. | Contextual | Existencia de un escenario de cambio identificable que justifique la frontera elegida. | Problema de diseño: decisión distribuida entre interfaz, configuración y coordinación; explicación del tesista sobre selección proporcional. | Alta |
| R2 | Delimitar por decisión funcional y sus consumidores antes de intervenir. | Metodológica | Registro de entradas, consumidores y efectos del incremento, previo a la transformación. | A01; evidencia de duplicación de selección y de consulta posterior a creación. | Alta |
| R3 | Distinguir lo observado, lo requerido y la intención de cada cambio. | Metodológica | Clasificación de cada transformación como preservación, corrección o extensión, con su punto de observación. | A02; D06; riesgo de mezclar extracción estructural con capacidad nueva (enero–marzo). | Alta |
| R4 | Caracterizar el comportamiento existente antes de mover lógica. | Funcional | Todo comportamiento movido cuenta con prueba de caracterización o prueba directa sobre sus reglas principales. | D03; ausencia de prueba directa identificada para el servicio principal. | Alta |
| R5 | Hacer controlables la decisión y observables sus efectos. | Funcional | Entradas de decisión explícitas (gestión, instante) y comprobación de que el rechazo precede a efectos prohibidos. | D04; I01–I02; control temporal aceptado para I04. | Alta |
| R6 | Reutilizar mecanismos existentes de variación antes de introducir infraestructura general. | Contextual | Cambio logrado mediante configuración existente sin añadir reglas nuevas cuando el mecanismo ya existe. | D05; I04 y su criterio de cero archivos de producción. | Alta |
| R7 | Separar el costo inicial de la evolución posterior. | Metodológica | Registro por separado del costo de incorporar la capacidad y del costo de un cambio posterior que la ejercite. | A04; D05; I04. | Media |
| R8 | Revisar componentes y consumidores, conservando dependencias transitorias justificadas. | Contextual | Lista explícita de dependencias transitorias admitidas y de excepciones del contrato. | D07; hallazgo de dependencias desplazadas, no eliminadas. | Media |
| R9 | Evaluar atributos con escenarios y condiciones explícitos, no con recuentos. | Metodológica | Comparación de esfuerzo, comportamiento preservado y efectividad de pruebas bajo condiciones comparables. | D08; I03; advertencia de no transferir métricas de Java a PHP. | Media |
| R10 | Versionar decisiones y evidencia para distinguir aplicación, rediseño y contribución. | Metodológica | Cada versión con pregunta de diseño, hallazgo y cambio documentado. | D09; ciclo formativo planificado con rediseño. | Alta |

## 3. Requisitos de la instanciación

| ID | Requisito | Tipo | Métrica | Fuente en el problema o diagnóstico | Prioridad |
|:--|:--|:--|:--|:--|:--|
| R11 | Conservar el monolito MVC con una frontera de aplicación incremental. | Contextual | Controlador reducido a coordinación; lecturas, reglas y efectos separados; sin migración a núcleo independiente. | Sub-decisión B de E7a; restricción de no afirmar independencia de Symfony/Doctrine. | Alta |
| R12 | Aplicar la decisión autoritativa en el servidor, con la interfaz como representación. | Funcional | Regla temporal única en servidor, reutilizada por consumidores; la interfaz no duplica la regla. | Explicación del tesista en E4; criterio arquitectónico aceptado el 30 de octubre. | Alta |
| R13 | Satisfacer los criterios funcionales del diagnóstico. | Funcional | I01: 100 % de correspondencia de decisiones en el conjunto acordado; I02: 100 % de rechazos sin certificación, seguimiento, autorización ni adjuntos; I04: cero archivos de producción modificados o añadidos para la ampliación. | E6, indicadores I01–I02 e I04, aceptados prospectivamente. | Alta |
| R14 | Hacer medible el esfuerzo humano activo. | Metodológica | I03: minutos humanos activos por fase, con espera y ejecución automática separadas. | E6, indicador I03; registro descriptivo parcial ya obtenido. | Media |

## 4. Tensiones de diseño

La tensión principal opone **madurez arquitectónica a viabilidad de migración**. Una separación estricta de capas con dependencias invertidas aporta claridad conceptual, pero su adopción amplia exigiría contratos y adaptadores nuevos cuyo costo no justifica la evidencia actual y que el encuadre rechazó. El método resuelve esta tensión imponiendo una frontera incremental con dependencias transitorias declaradas, en lugar de una arquitectura «limpia» de una sola vez.

La segunda tensión opone **protección del comportamiento a corrección intencional**. Caracterizar conserva lo existente, pero el problema pide en algunos puntos corregir un comportamiento que el diagnóstico mostró incorrecto (el límite mensual 8/9 no se distingue). El método resuelve esta tensión separando transformación conservadora de corrección funcional (R3), de modo que ninguna se disfrace de la otra.

La tercera tensión opone **generalidad del método a especificidad del caso**. Los principios deben transferirse a subcircuitos semejantes, pero la evidencia proviene de un único incremento en SIGPP. El método resuelve esta tensión declarando condiciones de contorno y limitando la contribución a lo que la evaluación soporte, sin reclamar transferencia estadística (R9, R10).

## 5. Gate de E7b

El gate se cumple cuando todo requisito es rastreable al problema, toda propiedad tiene métrica, los trade-offs están declarados y la tabla cubre la tipología método + instanciación. Las tablas anteriores proponen ese cumplimiento; corresponde al tesista validar o corregir la formulación con sus palabras, en particular si alguna métrica no es operacional o algún requisito no refleja una decisión que él ya asumió.

**Cierre, 4 de noviembre de 2026:** el tesista responde «refleja las decisiones asumidas». La formulación queda validada; el gate de E7b se cumple. Los requisitos son rastreables al problema, toda propiedad tiene métrica, los trade-offs están declarados y las tablas cubren la tipología método + instanciación.
