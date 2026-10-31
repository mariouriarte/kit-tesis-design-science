<!-- Material visual en Markdown. Separadores horizontales delimitan diapositivas.
12 diapositivas de exposición; referencias de respaldo fuera del recorrido oral.
Tiempo objetivo: 18 minutos más 2 de margen; pendiente de ensayo.
No se ha verificado un motor de presentación ni una conversión de este archivo.
Notas orales y tiempos por bloque: guion_predefensa_2026-10-31.md.
-->

# Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas: aplicación en la ejecución POA de SIGPP

**Mario Arturo Uriarte Marin**  
Maestría en Ingeniería de Software  
Tutor: Luis Roberto Pérez Rios, Ph.D.

**Predefensa · 31 de octubre de 2026**

Avance de investigación: evidencia disponible y contribución por evaluar.

---

## 2. El problema: cambiar y comprobar decisiones distribuidas

**SIGPP:** Sistema Integral de Gestión POA Presupuesto, Caja Petrolera de Salud.

Ejecución de la planificación operativa anual → tareas, operaciones, presupuesto y certificación.

- Separación parcial existente, con reglas y consultas distribuidas.
- Certificación como incremento acotado de aplicación.
- Evolución sin reescritura completa como restricción.

**No se ha cuantificado todavía el costo institucional del cambio.**

---

## 3. Pregunta y alcance

¿Qué principios de diseño debe incorporar un método de refactorización arquitectónica incremental, aplicado en el subcircuito de ejecución POA de SIGPP, para mejorar la modificabilidad y testabilidad de subcircuitos funcionales críticos de aplicaciones MVC heredadas, sin requerir reescritura completa ni interrupción operativa?

**Objeto en Design Science:** método propuesto, aplicado en SIGPP.  
**Campo:** subcircuitos MVC heredados con lógica dispersa y restricciones de continuidad.

Fuera del alcance: reescritura y migración arquitectónica integral.

---

## 4. Objetivo y conocimiento previsto

**Diseñar y evaluar el método** para mejorar modificabilidad, testabilidad y trazabilidad de cambios sin reescritura completa.

Diagnosticar → fundamentar → diseñar → aplicar → evaluar utilidad → formular y evaluar principios.

**Contribución prevista:** principios de diseño sobre selección, protección y verificación de incrementos en contextos semejantes.

El código intervenido es el vehículo de aplicación, no la contribución por sí mismo.

---

## 5. Los antecedentes orientan decisiones concretas

| Fundamento | Consecuencia de diseño |
|:--|:--|
| Feathers (2004) | Proteger comportamiento; distinguir lo observado de lo requerido. |
| Bass et al. (2021) | Usar escenarios de calidad; separar costo inicial y cambio posterior. |
| Girjoaba y Capiluppi (2024) | Adaptar un ciclo existente, reconociendo su procedencia. |

**No se reclama novedad por usar pruebas, extraer clases o combinar autores.**

---

## 6. Propuesta en desarrollo: adaptación acotada

| Orientación documentada | Qué distingue |
|:--|:--|
| Selección proporcional | Una errata no exige reorganización arquitectónica. |
| Comportamiento explícito | Observado, requerido e intención de cambio. |
| Frontera funcional | Consumidores, dependencias y puntos de comprobación. |
| Evaluación del cambio | Transformación inicial frente al cambio posterior. |

Base operativa: Girjoaba y Capiluppi (2024).

**Formalización completa y validación pendientes. No es un modelo teórico validado.**

---

## 7. Evidencia: centralización de selección de restricciones

**Antes:** selección implementada en dos consumidores.  
**Después:** ambos delegan en un resolvedor compartido.

| Comparación documentada | Resultado registrado |
|:--|:--|
| `5313c0e1` → `8dc63307` | 13 pruebas y 65 aserciones satisfactorias por estado |

**Sostiene:** conservación del comportamiento examinado y centralización local.

**Límite:** comparación retrospectiva con clases históricas y dobles en el entorno actual; no demuestra ahorro de esfuerzo ni menor acoplamiento global.

---

## 8. Evidencia: fuente funcional y discrepancias temporales

| Registro existente | Hallazgo acotado |
|:--|:--|
| Cuestionario del Planificador Nacional | Fuente funcional recibida; síntesis aún no ratificada íntegramente. |
| Fecha documental: 1 prueba, 1 aserción, 1 fallo | Avance hasta solicitar correlativo antes del rechazo requerido. |
| Hora: 3 pruebas, 5 aserciones, 1 fallo | Distinta admisibilidad local para horas del mismo día. |

**Límites:** sin comprobación integral HTTP o de persistencia; límites del instrumento declarados en el diagnóstico.

No se confunden fallos de comprobación con validación del método.

---

## 9. Cómo se prevé evaluar

| Indicador | Situación actual |
|:--|:--|
| I01. Correspondencia de decisiones | Evidencia y criterios parciales. |
| I02. Rechazo antes de efectos | Comprobaciones locales; integración pendiente. |
| I03. Esfuerzo humano activo | Sin línea base humana. |
| I04. Extensión de cambio posterior | Ampliación por configuración acordada, sin ejecución. |

**Evaluación para mejorar → rediseño documentado → evaluación final.**

Aplicabilidad del método ≠ utilidad local ≠ respaldo de los principios.

---

## 10. Qué se puede afirmar y qué todavía no

**Disponible**

Fundamentación, revisión focalizada, fuente funcional y evidencia técnica parcial.

**No demostrado**

Reducción de esfuerzo, mejora global de mantenibilidad, integración completa o principios validados.

**Amenazas identificadas**

Sesgo del constructor · selección del caso · comparación retrospectiva · alcance local de pruebas.

---

## 11. Trabajo restante, no resultados alcanzados

1. Completar línea base, criterios e instrumentos.
2. Formalizar y aplicar el método con decisiones trazables.
3. Evaluar, rediseñar y realizar evaluación final.
4. Formular principios respaldados y armonizar el documento institucional.

**Estado:** fundamentación y revisión focalizada cerradas; diagnóstico abierto; diseño formal, evaluación y contribución pendientes.

El IFI actualizado es un avance provisional, no un informe final completo.

---

## 12. Cierre

**La propuesta no es reescribir SIGPP.**

Es diseñar y evaluar un método para seleccionar, proteger y verificar incrementos de refactorización.

La evidencia actual delimita la intervención; la evaluación pendiente determinará qué conocimiento puede transferirse.

**Gracias por sus observaciones.**

---

## Respaldo bibliográfico — fuera del recorrido oral

Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional. https://www.sei.cmu.edu/library/software-architecture-in-practice-fourth-edition/

Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR. https://www.informit.com/store/working-effectively-with-legacy-code-9780131177055

Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. In *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079

<!-- Verificaciones reutilizadas de E4/E5. Girjoaba y Capiluppi: metadatos
verificados; manuscrito aportado leído, sin equivalencia editorial íntegra
certificada. No se realizó una búsqueda nueva para las diapositivas. -->
