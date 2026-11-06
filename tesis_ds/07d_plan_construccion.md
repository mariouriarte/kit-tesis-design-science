# E7d. Plan de construcción y versiones

> **Extensión posterior a P01:** las denominaciones V1–V3 inferiores conservan el plan histórico. Se añade una secuencia explícita del método: M-P01 (material aplicado por el practicante), aplicación formativa asistida y ratificada, y M-R1 (rediseño aprobado de P3/P5/P7/P8). Pregunta, hallazgos y cambios están en `registro_redisenio_metodo_mr1.md`. La comprobación posterior de M-R1 y el episodio sumativo siguen pendientes; no se dan por realizados por formalizar esta versión.

**Estado:** en curso. Este documento fija el producto mínimo viable, documenta las versiones construidas y previstas, y establece el criterio de suficiencia para pasar a la evaluación sumativa. Se distingue con honestidad lo ya construido (histórico) de lo que se consolidará (prospectivo), porque parte de la construcción ocurrió antes de la formalización del método.

## 1. Producto mínimo viable

El mínimo artefacto que permite probar los principios de diseño es la composición: **el método formalizado (pasos P1–P8, requisitos R1–R14, trazabilidad) más una instanciación parcial verificada en el subcircuito de certificación**. No se exige una instanciación completa de todos los pasos sobre todas las decisiones del circuito; se exige que la parte intervenida deje evidencia de separación, caracterización y comprobación.

Lo que queda **fuera** del mínimo: la refactorización de tarea y presupuesto, la ampliación completa del circuito, y cualquier migración a núcleo independiente. Lo que queda **dentro**: el método documentado, la extracción de la restricción de subpartida y su caracterización, las comprobaciones de la decisión temporal y la evidencia de un ciclo formativo con rediseño.

## 2. Versiones construidas y previstas

### V1 — exploratoria (octubre de 2026, sobre un antecedente de 2025)

- **Antecedente (marzo de 2025):** separación parcial hacia `src/Service`, commits `815ce6c0`, `6e333e27`, `9d4af430`. Es trabajo técnico previo al encuadre de la tesis; no se presenta como construcción realizada durante el estudio.
- **Pregunta de diseño (octubre de 2026):** ¿el antecedente de separación parcial permite probar el flujo y revela el problema arquitectónico sin reescritura?
- **Qué se hizo:** identificación y evaluación formativa del antecedente; localización del `RestriccionSubPartidaResolver` y de los archivos de prueba sin seguimiento; ejecución de pruebas unitarias satisfactoria.
- **Hallazgo:** separación parcial lograda, pero con mezcla de objetos de valor y de transferencia de datos, y sin prueba directa inicialmente identificada para el servicio principal de creación.
- **Rediseño que produjo:** caracterizar antes de mover, prueba directa para servicios principales, y destino de frontera incremental en lugar de «arquitectura limpia» total.

### V2 — experimental (octubre a noviembre de 2026)

- **Pregunta de diseño:** ¿la caracterización y el control de la decisión permiten verificar el comportamiento y localizar la brecha?
- **Qué se hizo:** caracterización de la restricción de subpartida, comprobaciones aisladas de la decisión temporal (O01–O06, M08/M09, O06 de servidor, interacciones), registro humano I03 y protocolo I04.
- **Hallazgo:** la decisión temporal sigue distribuida entre presentación y servidor; el límite mensual 8/9 no se distingue en un punto; la consulta de habilitados ocurre después de la creación. Este es el insumo del diagnóstico, no una solución.
- **Rediseño que produjo:** autoridad de regla en servidor y controlabilidad explícita del instante (P3), fijadas como requisitos.

### V3 — operacional (a consolidar)

- **Pregunta de diseño:** ¿el método formalizado, con la instanciación parcial documentada, es suficiente para sostener la evaluación sumativa?
- **Qué se incluye:** método P1–P8 formalizado, trazabilidad R1–R14, ficha reproducible, y la evidencia ya generada de V1–V2.
- **Qué se excluye:** rehacer la construcción, completar P4–P6 sobre todas las decisiones, o ejecutar nuevas comprobaciones de fechas.
- **Condición:** no se reescribe la intervención; se formaliza y se verifica la coherencia de lo ya construido.

## 3. Criterio de suficiencia

El artefacto está listo para la evaluación sumativa (E8) cuando se cumplan, en conjunto:

1. El método está formalizado: pasos, roles, entradas, salidas y criterios de cada paso están escritos y son reproducibles por un tercero.
2. La instanciación parcial está documentada y verificada: existe evidencia de separación, caracterización y comprobación, con sus comandos y diferencias.
3. Existe al menos un ciclo formativo con rediseño documentado: V1 → V2, con pregunta de diseño y hallazgo por versión.
4. Los criterios I01–I04 están fijados prospectivamente y su estado de medición declarado, sin fabricar resultados que no existen.

Este criterio no exige una evaluación de campo sumativa en dos contextos, que no es alcanzable en el plazo; exige que lo declarado como hecho esté respaldado y que las limitaciones se nombren en E8.

## 4. Matriz de riesgos

| Riesgo | Probabilidad | Impacto | Mitigación |
|:--|:--|:--|:--|
| Evaluación sumativa más débil que el estándar de maestría | Alta | Alto | Declarar condiciones de contorno, amenazas y acotar la contribución en E10 |
| Instanciación parcial sin completar P4–P6 en toda la decisión | Media | Medio | Declarar qué pasos se ejecutaron y cuáles no, sin fingir completitud |
| Plazo insuficiente para nueva evidencia | Alta | Medio | Priorizar formalización y evaluación documental sobre ejecuciones nuevas |
| Sesgo del constructor en la evaluación | Media | Alto | Revisor independiente y fuente funcional; separar muestra de diseño de muestra de evaluación |
| Riesgo de sobre-reclamar principios a partir de un caso | Media | Alto | Limitación analítica explícita; no transferencia estadística |

## 5. Gate de E7d

El gate exige: producto mínimo viable definido, cada versión con su pregunta de diseño, criterio de suficiencia explícito, riesgos con mitigación, y plan viable en el tiempo disponible. Las secciones anteriores proponen ese cumplimiento. Corresponde al tesista validar o corregir, en particular si el producto mínimo viable y el criterio de suficiencia reflejan lo que él puede sostener.

**Cierre, 4 de noviembre de 2026:** el tesista responde «si, es valido el producto mínimo viable». El gate de E7d se cumple: producto mínimo viable definido, cada versión con su pregunta de diseño, criterio de suficiencia explícito, riesgos con mitigación y plan viable en el tiempo disponible.
