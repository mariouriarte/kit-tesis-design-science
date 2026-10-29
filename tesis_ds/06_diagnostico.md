# E6. Diagnóstico, línea base y criterios prospectivos

**Estado:** iniciado el 28 de octubre de 2026, después del cierre de E5. Se organiza la evidencia disponible y se proponen definiciones operacionales para la siguiente intervención; **no se declaran líneas base medidas hoy, umbrales acordados ni cierre de E6**. El diagnóstico no autoriza todavía implementar la adaptación. Las expectativas del tesista y los resultados históricos se distinguen de las mediciones prospectivas.

## 1. Alcance del diagnóstico

El artefacto sigue siendo el método adaptado más su aplicación en SIGPP, no una herramienta de auditoría general. La primera unidad de diagnóstico es la decisión temporal en creación de certificaciones, con habilitación y admisibilidad documental diferenciadas; no se convierten saldo, permisos o todo el sistema en una intervención obligatoria. El criterio explicado por el tesista exige evaluar comportamiento, dependencias y riesgo antes de elegir la actuación. Una corrección de texto confirmada como tal no se clasifica automáticamente como refactorización arquitectónica.

La finalidad es documentar el problema, fijar una versión de referencia y obtener valores comparables antes del próximo cambio. Las propiedades preliminares derivan de la delimitación y del mapa D01–D09: preservación/cambio intencional, aplicación de la decisión antes de efectos, capacidad de prueba y modificabilidad mediante un cambio representativo. Los requisitos detallados y las alternativas de construcción se formalizarán en E7; no se seleccionan métricas porque resulten favorables en el código ya intervenido. Un comportamiento correcto de la instanciación será necesario, pero no suficiente, para validar el método.

## 2. Evidencia disponible y límite de uso

| Fuente de contexto o literatura | Evidencia ya disponible | Uso permitido y pendiente |
|:--|:--|:--|
| Inspección del recorrido de SIGPP, 26 de octubre. | `1294047e`: fecha anual en servicio, predicados adicionales en JavaScript, habilitación visual y consulta posterior a creación; fichas de contraste. | Evidencia estática contextual. Reconfirmar versión/estado y reproducir comportamiento controlado antes de convertirlo en línea base ejecutada; no afirmar vulnerabilidad HTTP. |
| Declaración funcional del tesista. | HU-FEC-01/HU-FEC-02, gestión, ventanas, días permitidos, semántica de día calendario y `America/La_Paz`, en `reglas_fecha_certificacion.md`. | Definición del resultado requerido. Falta confirmación del responsable funcional pertinente o respaldo documental explícito; no volver a preguntar las reglas ya definidas. |
| Documentación propia CPS. | RE-SPO aprobado en 2019, reglamento presupuestario y directrices 2027, con sus límites de vigencia; revisión documental registrada. | Respaldo real de estructura institucional y relación tareas/recursos; no atribuirles automáticamente las excepciones documentales 29/31 de diciembre si no están explicitadas. |
| Pruebas e historial. | Ejecución del 18 de octubre: 188 pruebas y 540 aserciones; prueba directa de creación con dobles y casos de restricción/importe/fecha fuera de gestión. | Evidencia histórica de verificación parcial, no ejecución actual ni cobertura completa. No acredita por sí sola orden TDD previo, integración o concurrencia. |
| Fundamentos y antecedentes. | Feathers (2004), Bass et al. (2021), revisión reciente y ciclo de Girjoaba y Capiluppi (2024). | Derivar propiedades y cautelas de medición. No transferir porcentajes, número de fases de prueba o instrumentos del caso C++/Java como si estuvieran validados en SIGPP. |

Existe evidencia del contexto real además de literatura, pero no todos sus datos sirven todavía como mediciones de línea base. Una deducción de tres funciones o ejemplos no representa una muestra de uso institucional. La declaración del constructor y la validación del responsable funcional cumplen papeles distintos; ninguna sustituye la revisión independiente del método en la evaluación. La confirmación de reglas no debe introducir cambios silenciosos: cualquier diferencia se registrará con su fecha y motivo.

## 3. Indicadores propuestos, todavía por acordar

Estos indicadores corresponden a un conjunto de escenarios definido antes del cambio, no a tasas estimadas de todo el uso institucional. Las definiciones son propuestas de trabajo; no constituyen resultados ni selección definitiva de instrumentos. Se separa lo que exige observar ejecución de lo que puede extraerse de diferencias de código. No se interpreta cero incidentes observados como ausencia universal de defectos.

| ID | Propiedad y definición operacional propuesta | Unidad / fuente prevista | Línea base disponible | Valor esperado / criterio |
|:--|:--|:--|:--|:--|
| I01 | Correspondencia de decisiones temporales: `casos con decisión esperada / casos ejecutados del conjunto definido`, conservando resultado por caso y escenario. | Proporción y registro por caso; invocación de regla y consumidor pertinentes con datos ficticios. | No medida en una ejecución prospectiva. El ejemplo de 14/06 es deducción local, no una medición de este indicador. | Acordar conjunto y criterios antes de intervenir; no confundir fecha admisible con permiso total de creación. |
| I02 | Rechazo antes de efectos: `casos que requieren rechazo, se rechazan y no producen efectos prohibidos / casos ejecutados que requieren rechazo`. | Proporción, motivo y registro de interacciones/estado; pruebas de consumidor e integración según propiedad. | Hay pruebas históricas parciales; no está medido para toda la política temporal prevista. | La ausencia de efectos ante rechazo ya es requisito declarado; falta fijar escenarios, efectos observables y suficiencia de comprobación. No se simula eficacia con una política sustituida que siempre rechaza. |
| I03 | Esfuerzo de preparar y comprobar un escenario temporal: minutos activos de preparación de datos/dobles, escritura/ajuste y análisis de pruebas; registrar espera y ejecución por separado. | Minutos por actividad y escenario; bitácora prospectiva y resultados de herramientas. | No medido. No se reconstruye como duración real a partir de recuerdos o fechas de commits. | Meta y condiciones comparables por acordar; no sumar pausas como trabajo activo ni comparar tareas de complejidad distinta sin declararlo. |
| I04 | Extensión de un cambio posterior: número de componentes existentes modificados y de componentes nuevos, con archivos de producción y pruebas identificados por separado. | Recuentos y mapa de responsabilidades; diferencias de versiones y escenario de cambio previamente definido. | No se ha ejecutado el cambio representativo comparable. | No fijado. Menos archivos no es automáticamente mejor: revisar qué responsabilidades cambiaron y qué conexiones se preservaron. |

I01–I02 derivan del contrato y de la observación de comportamiento/efectos (Feathers, 2004; Bass et al., 2021). I03 se relaciona con la expectativa de testabilidad y la necesidad de distinguir efectividad y esfuerzo, sin adoptar el predictor Java de Zakeri-Nasrabadi y Parsa (2022). I04 operacionaliza parte de un escenario de modificabilidad y debe complementarse con esfuerzo y resultado funcional, no sustituirlos (Bass et al., 2021). El instrumento y la meta de cada indicador requieren discusión y datos: no se inventan valores para completar una tabla.

## 4. Preparación de la línea base

1. Reconfirmar versión de código y cambios locales pertinentes; fijar el punto de referencia del próximo incremento y conservar la evidencia histórica con su fecha.
2. Obtener confirmación funcional de las reglas ya declaradas y registrar su fuente, alcance y restricciones, sin usar datos reales sensibles de certificaciones.
3. Acordar escenarios, resultados y observables; distinguir caracterización existente, corrección funcional y capacidad extraordinaria.
4. Seleccionar instrumentos y recoger línea base reproducible con datos ficticios; declarar entorno, dependencias y qué no prueba cada comprobación.
5. Acordar criterios/valores esperados antes del cambio planificado y reservar evaluación formativa, rediseño y sumativa; no transformar intervenciones previas en cumplimiento prospectivo.

## 5. Condiciones pendientes para cerrar E6

Cada indicador seleccionado deberá tener definición operacional, fuente, línea base y criterio evaluable previo a construir. Las filas anteriores documentan explícitamente qué no se ha medido; por eso E6 permanece abierta. El siguiente paso inmediato es confirmar la fuente funcional de resultados esperados y el punto de referencia técnico, no refactorizar ni ejecutar operaciones en producción. Las diferencias frente a las reglas actuales se documentarán antes de cambiar su implementación.

## Referencias

- Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/
- Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055
- Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079 **[contenido consultado en manuscrito aportado, no equivalencia editorial íntegra certificada]**
- Zakeri-Nasrabadi, M., & Parsa, S. (2022). *An ensemble meta-estimator to predict source code testability* [Prepublicación, versión 2]. arXiv. https://doi.org/10.48550/arXiv.2208.09614

Se reutilizan las verificaciones y pasajes registrados en E4–E5; no se atribuye una nueva lectura o una medición por citarlos en este diagnóstico.
