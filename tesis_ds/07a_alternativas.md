# E7a. Solución conceptual y alternativas de solución

**Estado:** en curso. Este documento formaliza la tipología del artefacto y presenta las alternativas reales de configuración del método, con sus sustentos, supuestos y costos. La elección se cierra cuando el tesista la defienda con sus palabras; la matriz no es una decisión por sí misma.

## 1. Tipología del artefacto y justificación

El artefacto es una **composición: método + instanciación**. El método de refactorización arquitectónica incremental es el vehículo de la contribución; la instanciación es su aplicación al subcircuito de ejecución POA de SIGPP, con la certificación como primer incremento. Esta tipología quedó fijada en E2 y no se reabre aquí.

La elección de esta tipología responde a dos condiciones del problema. Primera: el problema de diseño no es una única corrección de código, sino una forma repetible de delimitar y verificar cambios en subcircuitos cuya lógica atraviesa controlador, configuración, servicio y presentación. Un método captura esa repetición; una herramienta aislada no. Segunda: sin aplicación, un método carece de evidencia, y sin método, una aplicación carece de transferibilidad. La composición resuelve ambas exigencias a la vez, al costo de tener que evaluar por separado la utilidad de la instanciación y la validez de los principios que el método articula.

## 2. Alternativas de configuración del método

El método no se inventa desde cero: la base operativa aceptada es una adaptación explícita del ciclo de Girjoaba y Capiluppi (2024), complementada con el cambio seguro de Feathers (2004) y el razonamiento por atributos de calidad de Bass et al. (2021). Las alternativas que siguen difieren en el grado de adaptación frente a esa base y en el alcance de la intervención, no en si se refactoriza o no.

### M1. Aplicación literal del ciclo heredado

Consiste en adoptar los siete pasos del ciclo de Girjoaba y Capiluppi sin adaptación sustantiva y documentar su aplicación al subcircuito. Su sustento es directo: el ciclo ya está publicado y evaluado en un caso industrial, lo que reduce el costo de diseño a una actividad de seguimiento.

Su supuesto débil es que la unidad funcional del caso de origen —una interfaz obsoleta cuya funcionalidad interna sigue siendo necesaria— es comparable a la unidad de este estudio: un subcircuito donde una decisión institucional se distribuye entre interfaz, configuración y coordinación de efectos. No lo es. En SIGPP el problema no es retirar un componente muerto, sino localizar una decisión viva y sus consumidores antes de moverla.

Su costo es bajo y su riesgo también, pero la contribución se reduce a una aplicación competente de conocimiento ajeno. No supera la prueba de fuego de maestría: otro investigador no obtendría de aquí principios para construir un método distinto ante un problema de la misma clase.

### M2. Adaptación acotada con reglas de selección y verificación

Consiste en conservar el ciclo como base y añadir cuatro adaptaciones —A01 delimitación por decisión funcional y consumidores, A02 distinción observado–requerido–intención, A03 comprobaciones y efectos prohibidos, A04 separación de costo inicial y evolución posterior— junto con el criterio de **selección proporcional**: una errata de presentación no exige reorganización arquitectónica, mientras una decisión de negocio distribuida justifica investigar comportamiento, dependencias y riesgo antes de elegir la intervención.

El sustento combina fuentes con funciones distintas: Feathers aporta la caracterización y la separación mínima para probar; Fowler la distinción entre transformación que conserva comportamiento y capacidad funcional nueva; Bass et al. el razonamiento por escenarios y atributos; el ciclo aporta la secuencia operativa de investigación, migración y comprobación. La adaptación está orientada a la clase de subcircuitos delimitada, no a una reivindicación de originalidad por renombrar pasos.

Su costo es mayor en formalización, porque obliga a operacionalizar cada regla y a declarar sus condiciones de contorno. Su beneficio es una contribución defendible como principios de diseño evaluados, no como aplicación. Su riesgo principal es que la evaluación resulte más débil que la pretensión; ese riesgo se controla acotando la contribución a lo que la evidencia soporte.

### M3. Migración estructural amplia

Consiste en aplicar una estrategia de sustitución gradual por abstracción sobre una frontera completa del subcircuito, o un análisis ADD extenso, buscando una separación terminada de una sola vez. Su sustento existe: la ramificación mediante abstracción de Fowler (2014) y el método ADD de Bass et al. (2021) son estrategias legítimas para transformar sistemas.

Su costo y su riesgo lo descartan para este estudio. Requiere un alcance y un plazo que la evidencia no justifica, introduce interrupción operativa en un sistema institucional en producción, y promete una migración que el encuadre rechazó explícitamente el 28 de septiembre. No es una alternativa real en el sentido de factible; se registra para explicitar por qué se descarta, no como opción abierta.

## 3. Sub-decisión arquitectónica de la instanciación

Dentro del método, la instanciación exige una decisión sobre el destino arquitectónico del primer incremento. Esta decisión es de menor nivel que las tres anteriores y se formaliza aquí porque condiciona E7c.

| Alternativa | Descripción | Juicio |
|:--|:--|:--|
| A. Extracciones puntuales sin contrato | Extraer lógica a servicios sin fijar dónde residen consultas, reglas y presentación. | Insuficiente como destino: desplaza la concentración del controlador al servicio sin ganancia verificable. |
| B. MVC con frontera de aplicación incremental | Conservar el monolito MVC y separar lecturas, reglas y efectos mediante una frontera explícita, declarando las dependencias transitorias. | Recomendada: aprovecha servicios y repositorios existentes, permite imponer reglas locales y probarlas, sin costo de migración. |
| C. Núcleo independiente con puertos y adaptadores | Aislar el núcleo de Symfony y Doctrine mediante contratos propios. | No justificado con la evidencia actual; su costo de migración es desproporcionado para el alcance. |

## 4. Matriz de decisión

| Criterio | M1 literal | M2 adaptación | M3 amplia |
|:--|:--|:--|:--|
| Factibilidad en el plazo y en operación | Alta | Media-alta | Baja |
| Novedad defendible como contribución de maestría | Baja | Media (a evaluar) | Alta, pero sobrealcance |
| Costo de diseño y formalización | Bajo | Medio | Alto |
| Riesgo de interrupción operativa | Bajo | Bajo | Alto |
| Sustento en la base de conocimiento | Directo | Compuesto y trazable | Directo |

La elección es **M2 (adaptación acotada)** con la sub-decisión arquitectónica **B (MVC con frontera incremental)**. M1 no produce contribución; M3 excede el alcance y el plazo. M2 es la única alternativa que mantiene la contribución en el nivel de maestría —principios de diseño evaluados— sin prometer una migración que la evidencia no respalda.

## 5. Defensa del tesista y cierre

**Defensa registrada el 4 de noviembre de 2026, en palabras del tesista.** M1 se descarta porque es un ciclo ya documentado y publicado por Girjoaba y Capiluppi; aplicarlo sería mover archivos y código, lo cual es ingeniería y no conocimiento nuevo, y los propios autores reconocen límites para trasladarlo a otros casos. M3 no es opción porque es una migración amplia que contradice la tesis misma y porque no se puede afirmar independencia del marco Symfony ni del ORM Doctrine. En Design Science el aporte reside en las decisiones de diseño propias y en su evaluación: aplicar el ciclo directamente no deja ninguna decisión propia que evaluar. La aplicación en SIGPP es la instanciación, el lugar donde el método se pone a prueba y deja evidencia; de esa evidencia saldrán después los principios. Sin adaptación, la instanciación no prueba nada propio.

**Cierre:** la elección M2 + B queda formalizada y defendida. Se satisfacen las condiciones del gate de E7a: hay tres alternativas reales con trade-offs explícitos, y la elegida es coherente con la tipología método + instanciación de E2 y con la base de conocimiento. La defensa no demuestra todavía resultados; afirma el compromiso de que la contribución saldrá de las decisiones de adaptación y de su evaluación, lo cual se comprobará en E8.
