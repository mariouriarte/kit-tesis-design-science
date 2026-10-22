# Marco teórico: sustentación del objeto de estudio

## Propósito del marco teórico

> **Vigencia del diagnóstico:** las métricas iniciales y los vacíos de pruebas citados en los ejes siguientes corresponden a la línea base histórica. La revisión del 18 de octubre identificó `CreateCertificacionServiceTest` y verificó 188 pruebas/540 aserciones; no sigue vigente la ausencia de prueba directa de ese servicio. Las precisiones actuales se registran al final, sin tratar la verificación técnica como evaluación completa del método.

Este marco teórico sustenta el objeto de estudio de la tesis: un método de refactorización arquitectónica incremental para subcircuitos legacy MVC institucionales, instanciado en el subcircuito de ejecución POA de SIGPP. El marco no se orienta a describir de forma general la arquitectura de software, Symfony o Doctrine, sino a justificar las decisiones de diseño que debe incorporar el método: selección de un subcircuito crítico, creación de una frontera arquitectónica explícita, desacoplamiento progresivo de reglas de negocio, incorporación de pruebas focalizadas y medición antes/después.

La prueba de eliminación es estricta: si una fuente no modifica el diseño del método, no pertenece al marco teórico principal. Bajo ese criterio, el marco se organiza en tres ejes: código heredado y cambio seguro; arquitectura como gestión de fronteras, dependencias y atributos de calidad; y testabilidad como condición para refactorización incremental.

## Pregunta de búsqueda teórica

¿Qué fundamentos de ingeniería de software permiten diseñar un método incremental para refactorizar subcircuitos funcionales críticos en sistemas legacy MVC institucionales, mejorando modificabilidad y testabilidad sin reescritura completa ni interrupción operativa?

## Criterios preliminares de inclusión y exclusión

Se incluyen fuentes que cumplan al menos una de estas condiciones: definen técnicas para intervenir código heredado con bajo riesgo; explican la arquitectura como conjunto de decisiones estructurales que afectan atributos de calidad; relacionan modificabilidad, testabilidad, acoplamiento y evolución de software; o fundamentan la evaluación de artefactos de Design Science. Se excluyen fuentes que solo describen buenas prácticas genéricas de Symfony, migraciones completas a microservicios o arquitectura hexagonal, o recomendaciones sin conexión directa con decisiones evaluables del método.

## Eje 1: código heredado y cambio seguro

La tesis parte de una condición típica de sistemas legacy: el sistema funciona y sostiene operación institucional, pero su estructura dificulta cambios seguros. En SIGPP, esta condición se observa en el circuito tarea-presupuesto-certificación: 11 archivos críticos acumulan aproximadamente 4177 líneas, existen 46 instanciaciones directas `new`, se identifican consultas SQL nativas o construidas manualmente, y hay ausencia de pruebas focalizadas sobre `KardexPresupuesto`, `CreateCertificacionService` y `TareaOneLineSql`. Esta evidencia orienta el método hacia intervención incremental, no hacia reescritura.

Feathers (2004) es central para este eje porque plantea estrategias prácticas para trabajar con código heredado sin reescribirlo, especialmente mediante pruebas que permitan detectar cambios no intencionales y técnicas para romper dependencias. Esta fuente justifica que el método empiece por identificar puntos de cambio, puntos de prueba y dependencias que impiden aislar reglas críticas. En la tesis, esto se traduce en una decisión de diseño: antes de extraer o reorganizar lógica, el método debe incorporar pruebas de caracterización o pruebas focalizadas que capturen el comportamiento actual del subcircuito intervenido.

La lectura parcial realizada por el tesista en torno a la ausencia de pruebas unitarias refuerza una decisión metodológica clave: la falta de pruebas no debe registrarse solo como defecto técnico del sistema, sino como condición de entrada del método. En un sistema heredado, la primera acción responsable no es mover código para que parezca mejor organizado, sino crear una red mínima de verificación sobre el comportamiento existente. Esta lectura conecta directamente con la línea base de SIGPP, donde existen pruebas relacionadas con tareas y algunas referencias a presupuesto o certificación, pero no se observaron pruebas focalizadas para `KardexPresupuesto`, `CreateCertificacionService` ni `TareaOneLineSql`.

Fowler (2018) complementa este eje al definir la refactorización como una técnica controlada para mejorar el diseño de código existente mediante transformaciones pequeñas que preservan comportamiento. Su aporte no debe usarse como una lista decorativa de técnicas, sino como principio de diseño del método: cada paso de refactorización debe ser pequeño, verificable y reversible en caso de romper comportamiento del circuito. En consecuencia, el método no prometerá “limpiar” todo SIGPP, sino ejecutar una secuencia acotada sobre el subcircuito seleccionado.

## Eje 2: arquitectura como fronteras, dependencias y atributos de calidad

La tesis no usará “arquitectura” como sinónimo de carpetas, capas nominales o adopción completa de una arquitectura limpia o hexagonal. Para este trabajo, arquitectura significa el conjunto de decisiones estructurales que determinan responsabilidades, dependencias, límites y facilidad de cambio. Esta definición operativa es necesaria porque el problema de SIGPP no es la ausencia de un patrón arquitectónico de moda, sino la ausencia de una frontera explícita en el circuito tarea-presupuesto-certificación.

Bass, Clements y Kazman (2021) permiten fundamentar esta lectura porque explican la arquitectura en relación con atributos de calidad como modificabilidad y testabilidad. Esta fuente justifica que el método mida el impacto de la intervención no solo por líneas movidas o clases creadas, sino por la reducción de dependencias directas, la localización de reglas críticas y la capacidad de verificar cambios mediante pruebas. Para SIGPP, esta perspectiva evita una promesa excesiva: no se afirma que el sistema alcanzará arquitectura hexagonal, sino que el subcircuito intervenido tendrá una frontera arquitectónica más explícita y evaluable.

La decisión metodológica derivada es clara: la propuesta debe rechazar migraciones arquitectónicas totales —por ejemplo, microservicios, actualización mayor de Symfony o reemplazo de Doctrine— porque agregarían complejidad y desviarían el problema de investigación —que en el formato institucional se registrará como problema científico—. La contribución de maestría está en formular principios de diseño para introducir frontera, desacoplamiento y pruebas dentro de restricciones reales de continuidad operativa.

## Eje 3: testabilidad, acoplamiento y evaluación técnica

La testabilidad no es un complemento posterior de la refactorización; es una condición para que el cambio sea controlable. En el circuito medido, PHPUnit ya está configurado, pero la línea base muestra vacíos importantes: no se observaron pruebas focalizadas para `KardexPresupuesto`, `CreateCertificacionService` ni `TareaOneLineSql`. Esto permite formular un requisito del método: cada extracción o separación de responsabilidad debe producir una unidad verificable o, al menos, una prueba de comportamiento que reduzca el riesgo de cambio.

Desde Design Science, Hevner et al. (2004), Peffers et al. (2007), Wieringa (2014) y Venable et al. (2016) sustentan que el artefacto debe construirse y evaluarse con criterios explícitos. En esta tesis, esos criterios serán modificabilidad, testabilidad, acoplamiento, complejidad, mantenibilidad y trazabilidad del cambio. La evaluación no puede definirse después de la refactorización; los indicadores deben fijarse antes para evitar racionalización posterior.

La línea base inicial ya ofrece indicadores útiles: tamaño de componentes críticos, instanciaciones directas, llamadas a persistencia desde controladores, ocurrencias de SQL nativo, rutas/controladores expuestos y vacíos de pruebas. Sin embargo, para cerrar E6 se deberán completar métricas dinámicas: complejidad ciclomática por método, cobertura efectiva del flujo, archivos modificados para cambios representativos, esfuerzo de modificación y trazabilidad entre cambio funcional, código y prueba.

## Decisiones de diseño sustentadas por la base teórica

| Decisión de diseño prevista | Fuente teórica principal | Aplicación al método |
|---|---|---|
| Intervenir un subcircuito crítico y no todo SIGPP. | Feathers (2004); Wieringa (2014) | Seleccionar un alcance donde sea posible observar problema, aplicar el método y evaluar antes/después sin reescritura completa. |
| Introducir una frontera arquitectónica incremental, no una migración completa a arquitectura limpia o hexagonal. | Bass et al. (2021); Fowler (2018) | Separar responsabilidades y dependencias donde exista mayor impacto sobre modificabilidad y testabilidad. |
| Proteger comportamiento existente antes de modificarlo. | Feathers (2004); Fowler (2018) | Incorporar pruebas de caracterización o pruebas focalizadas sobre reglas críticas del circuito. |
| Refactorizar mediante pasos pequeños y verificables. | Fowler (2018) | Evitar cambios masivos; cada paso debe tener entrada, salida, criterio de verificación y razón de diseño. |
| Medir antes/después con indicadores definidos previamente. | Hevner et al. (2004); Peffers et al. (2007); Venable et al. (2016) | Usar métricas de acoplamiento, complejidad, cobertura, mantenibilidad y trazabilidad como criterios de evaluación del artefacto. |
| Formular la contribución como principios de diseño, no como mejora local de SIGPP. | Gregor y Hevner (2013); Wieringa (2014) | Extraer conocimiento transferible para subcircuitos legacy MVC institucionales semejantes. |

## Fuentes verificadas inicialmente

Las siguientes fuentes fueron verificadas en fuentes editoriales o institucionales durante esta etapa:

- Bass, Clements y Kazman (2021), verificada en el sitio del Software Engineering Institute de Carnegie Mellon University.
- Feathers (2004), verificada en InformIT/Pearson.
- Fowler (2018), verificada en el sitio oficial de Martin Fowler.
- Hevner et al. (2004), Peffers et al. (2007), Gregor y Hevner (2013), Venable et al. (2016) y Wieringa (2014), tomadas del capítulo de referencias del libro base de Design Science usado en el repositorio.

## Estado de E4

### Actualización del 18 de octubre de 2026

La revisión actual identifica una necesidad de precisión: «arquitectura limpia mínima» no constituye un contrato verificable. Se propone discutir una frontera de aplicación incremental que conserve MVC, Doctrine y entidades existentes, y separe explícitamente entrada HTTP, preparación de datos, coordinación de creación, reglas focalizadas y persistencia. Stafford (2003) fundamenta la capa de servicios como frontera de operaciones y coordinación; Symfony (s. f.) respalda mantener la lógica de negocio fuera del controlador, sin prohibir universalmente que este consulte repositorios. La restricción más fuerte sobre consultas en el controlador sería una elección local del diseño, que deberá justificarse y evaluarse, no atribuirse al marco.

Las páginas primarias de esas dos fuentes y las páginas editoriales de Feathers (2004) y Fowler (2018) se verificaron en esta sesión. La lectura focalizada propuesta y el diagnóstico están en `arquitectura_candidata_certificacion_2026-10-18.md`; su contenido no declara cerradas las etapas posteriores. El número de fuentes recientes verificadas añadidas para satisfacer el requisito de actualización de E4 en esta sesión es **cero**: las fuentes incorporadas son fundacionales o documentación de la versión tecnológica del contexto. E4 permanece abierta y la brecha bibliográfica sigue siendo preliminar.

E4 queda iniciada con un marco teórico estructuralmente coherente, pero no cerrada. Para cerrar la etapa se requiere completar la búsqueda de literatura reciente sobre refactorización de sistemas legacy, deuda técnica arquitectónica, testabilidad y evolución de sistemas MVC o monolíticos, preferentemente con revisiones sistemáticas o estudios empíricos publicados en los últimos cinco años.

### Actualización del 20 de octubre de 2026: criterio de separación y evidencia reciente

La programación por períodos de la tarea es referencial según la aclaración del tesista; no se convierte en una prohibición adicional de certificar. El dato antes llamado «fecha de operación» se denominará día de registro de referencia y no proviene de la entidad `Operacion`. Esta precisión evita introducir un requisito inexistente por confusión entre planificación, registro y fecha del documento. Las modificaciones POA pueden afectar recursos y continuidad de tareas, pero sus consecuencias sobre elegibilidad todavía requieren delimitación funcional.

Parnas (1972), en el resumen editorial contrastado de su obra fundacional, destaca que la utilidad de la modularización depende del criterio de división. Aplicado a este diseño candidato, el límite no se justifica por crear otra clase o reducir líneas: se propone aislar la decisión institucional sobre admisibilidad de fecha, diferenciándola de obtención de datos y efectos. La política temporal recibiría fecha solicitada, gestión y día de registro de referencia; la coordinación conservaría comprobaciones con otras dependencias, como saldo y habilitación. Este reparto es una adaptación por defender, no una decisión que Parnas haya evaluado en SIGPP.

El resumen de la revisión de Abbasi et al. (2026) advierte predominio de estudios sobre clases orientadas a objetos y Java, desacuerdo sobre el efecto de métricas de diseño y vacíos entre niveles de abstracción. Por ello, la prueba de eliminación tiene una consecuencia concreta: no basta usar dependencias o número de clases como sustituto automático de testabilidad. La separación propuesta debe permitir comprobar escenarios pertinentes con entradas controladas, y complementarse con integración para las propiedades que los dobles no cubren. La transferencia de hallazgos a PHP y a este contexto institucional no se presume.

| Decisión candidata | Sustento y límite | Comprobación pendiente |
|:--|:--|:--|
| Separar una decisión institucional identificable, no dividir solo por tamaño. | Parnas (1972): criterio de descomposición; lectura de resumen, no texto íntegro. | Que el cambio de regla pueda localizarse sin trasladar la política a controlador o persistencia. |
| Proporcionar día de registro de referencia controlable y datos explícitos. | Feathers (2004), puntos de prueba y dependencias; aplicación específica razonada para fechas. | Repetibilidad de casos temporales sin reloj del navegador, formulario o base de datos. |
| No equiparar menor acoplamiento local con testabilidad demostrada. | Abbasi et al. (2026): límites de evidencia informados en resumen. | Escenarios comprobables y verificación de límites, no únicamente recuentos estructurales. |
| Distinguir política de fechas de coordinación y efectos. | Stafford (2003) y contrato candidato; requisitos funcionales declarados. | Rechazo antes de guardar o almacenar, y conservación separada de permisos/habilitación/saldo. |

La búsqueda y las restricciones de acceso están registradas en `busqueda_e4_2026-10-20.md`. Se añadió **una fuente reciente con metadatos y resumen contrastados y ninguna con texto íntegro leído** en esta sesión; otra revisión reciente se conserva como consulta de contenido pendiente. E4 permanece abierta: falta ampliar y leer fuentes, justificar las decisiones restantes y contrastar la brecha sin convertir el diagnóstico técnico en prueba de novedad.

**Revisión de requisitos posterior al análisis:** el tesista confirmó una ventana extraordinaria configurable por gestión, situable en cualquier momento del año actual para documentos del 29/31 de diciembre del año inmediatamente anterior. La restricción fija de enero–marzo deja de ser objetivo del diseño nuevo, aunque permanece en el antecedente inspeccionado. La fundamentación debe distinguir lectura de configuración, interpretación de su vigencia y decisión sobre fecha documental; no basta una política de tres entradas para decidir por sí sola la habilitación total. La modificación y sus criterios se detallan en `reglas_fecha_certificacion.md`, sin retrotraerlos a la intervención ya realizada.

### Actualización del 21 de octubre de 2026: contraste con textos primarios disponibles

El tesista aportó el texto de Feathers y acceso a su biblioteca local, lo que permitió contrastar pasajes más allá de resúmenes editoriales. Feathers (2004, pp. 14–20) aborda la necesidad de separaciones conservadoras para poder introducir pruebas; por ello, la regla del método no debe exigir cobertura completa previa a cualquier movimiento mínimo. En las pp. 186–190 distingue comportamiento real caracterizado de intención funcional, y en las pp. 194–195 exige atender tanto a la presencia de lo extraído como a su conexión. Para SIGPP, las pruebas aisladas del componente no eliminan la obligación de verificar que el servicio aplique sus decisiones antes de efectos.

Las heurísticas de responsabilidades de Feathers (2004, pp. 249–251) y su estrategia incremental (pp. 265–268) permiten justificar una selección por necesidad de cambio, no una clase por cada casilla del diagrama. Fowler (2018, pp. 45–47), contrastado en el PDF local de segunda edición, fundamenta distinguir refactorización de adición funcional incluso cuando se alternan en incrementos breves. La parametrización extraordinaria debe tratarse como capacidad nueva del diseño propuesto y no como una extracción que conserva todas las aceptaciones anteriores. Esta distinción mejora la trazabilidad del siguiente incremento, sin acreditar todavía su ejecución ni su éxito.

Existe una tensión bibliográfica: Feathers (2004, pp. 18–20) ya ofrece un procedimiento incremental de cambio con pruebas y ruptura de dependencias. Una secuencia equivalente no puede reclamarse como original solo por aplicarse a un sistema institucional MVC. Debe contrastarse qué adaptación o evidencia aporta el método frente a este antecedente y frente a soluciones recientes; la novedad permanece pendiente, no garantizada. El registro `lectura_fuentes_locales_2026-10-21.md` documenta fuentes, ubicaciones, aplicación y límites de lectura.

En esta sesión se contrastaron pasajes primarios de **dos obras fundacionales**, no se añadieron estudios recientes con lectura íntegra. E4 permanece abierta por las decisiones restantes y por la evidencia reciente pendiente; se conserva explícitamente el riesgo de contribución rutinaria. No se inició E5 ni se declaró una brecha demostrada por la sola ausencia de libros en la carpeta local.

### Incorporación del texto primario de Bass, Clements y Kazman

El adjunto posterior del tesista permite superar la verificación limitada al catálogo editorial para esta obra. Bass et al. (2021, secs. 3.3, 8.2 y 12.1–12.2) fundamentan escenarios evaluables, redistribución por responsabilidades y control/observación en pruebas; se registran los pasajes y su aplicación candidata en `lectura_bass_clements_kazman.md`. La introducción del capítulo 8 distingue costo de preparar el mecanismo y costo de utilizarlo, distinción pertinente para la configuración extraordinaria ya solicitada. No se prometerá eficiencia del método observando solo el uso final y omitiendo el esfuerzo de preparación.

ADD ya comprende refinamiento incremental de sistemas existentes, documentación y análisis por iteración (Bass et al., 2021, secs. 20.1–20.2). Este antecedente refuerza la obligación de justificar qué conocimiento distinto se busca generar, no la presunción de que cualquier método local sea original. La revisión ligera del capítulo 21 es una alternativa de apoyo aún no adoptada, no sustituto de la evaluación DS del método. E4 sigue abierta; el acceso a esta obra queda resuelto, sin atribuir lectura al tesista ni resultados de evaluación inexistentes.
