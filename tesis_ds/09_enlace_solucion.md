# E9. Enlace propuesta ↔ solución

**Estado:** en curso. Esta etapa recorre la cadena problema → requisito → decisión de diseño → criterio → evidencia → grado de cumplimiento → limitación, para mostrar qué quedó resuelto, qué quedó parcial y qué no se midió. No se confunde «el sistema compila y las pruebas pasan» con «el problema está resuelto».

## 1. Matriz de trazabilidad

| Problema de diseño | Requisito | Decisión de diseño | Criterio/indicador | Evidencia | Grado | Limitación |
|:--|:--|:--|:--|:--|:--|:--|
| Selección de restricción duplicada entre controlador y servicio | R3, R4 | Centralización en `RestriccionSubPartidaResolver` (P4) | Prueba directa sobre la regla | `make test` 188/540; `tests/Certificacion` 37/305 | Cumplido parcial | Antecedente de 2025, no producido por el método formalizado |
| Decisión temporal distribuida entre interfaz y servidor | R2, R11, R12 | Frontera incremental + autoridad en servidor (P3–P4) | I01 (100 % de correspondencia) | Comprobaciones O01–O06, M08/M09 | Parcial: el límite 8/9 no se distingue | La corrección no se construyó |
| Rechazo que puede ocurrir después de efectos | R5 | Comprobación de efectos prohibidos (P5) | I02 (100 % sin efectos) | O06 de servidor, rechazo sin llamar a los cuatro efectos | Parcial: un caso con dobles | Sin persistencia real ni atomicidad |
| Costo de cambio en esfuerzo humano | R14 | Registro por fases (P8) | I03 (minutos activos) | Bitácora, 26:33.87 | Descriptivo | Autoinforme, no experimental independiente |
| Modificabilidad ante cambio posterior | R6, R7 | Reutilizar configuración existente (P6) | I04 (cero archivos de código) | No medido | Limitación declarada | La capacidad extraordinaria no existe; construirla sería fabricar evidencia |
| Falta de trazabilidad entre decisión, versión y resultado | R10 | Versionado y design rationale (P8) | Documentación por versión con pregunta y hallazgo | V1–V3 documentadas en E7d/E7e | Cumplido documental | No sustituye evaluación empírica |

## 2. Distinción entre demostración y evaluación

La evidencia disponible demuestra que la instanciación **puede aplicarse**: las pruebas pasan, la extracción de la restricción funciona y el rechazo de O06 se observa con dobles. Eso es **demostración** —el artefacto opera—, no **evaluación** —la comparación sistemática contra los objetivos.

La evaluación propiamente dicha muestra que el problema **no está resuelto**: I01 no se cumple al 100 % porque el límite 8/9 no se distingue. Decir «las pruebas pasan» no equivale a «resuelve el problema». La distinción se mantiene explícita para no inflar el resultado.

## 3. Eslabones sin huérfano

Cada requisito tiene una decisión de diseño que lo atiende; cada criterio tiene evidencia o una limitación declarada. No hay un requisito sin decisión ni un criterio sin destino. Los eslabones que no tienen evidencia de cumplimiento (I04) no se declaran «cumplidos»: se declaran limitación con su razón.

## 4. Gate de E9

El gate exige: matriz de trazabilidad completa sin eslabones huérfanos, cada afirmación de solución respaldada por evidencia, y limitaciones declaradas. La sección 1 propone ese cumplimiento. Corresponde al tesista validar o corregir, en particular si algún grado de cumplimiento le parece inexacto o si falta un eslabón que considere relevante.

**Cierre, 4 de noviembre de 2026:** el tesista valida la matriz —«esta perfecto»—. El gate de E9 se cumple: la matriz de trazabilidad está completa sin eslabones huérfanos, cada afirmación de solución está respaldada por evidencia y las limitaciones están declaradas.
