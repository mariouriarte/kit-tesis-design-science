<!-- Presentación de defensa final en Markdown, conforme al modelo ALSIE.
Separadores horizontales delimitan las 16 diapositivas del recorrido principal,
desde la portada hasta las recomendaciones. Tiempo objetivo: 20 minutos máximo.
Las secciones posteriores son material de preparación, no diapositivas. Notas de orador como
citas bajo cada diapositiva; no son texto para leer. Sin términos de Design Science:
se habla de modelo, hipótesis, propuesta, validación y aporte (regla 8 de la plantilla
ALSIE). Las figuras ya están renderizadas como PNG en `figuras/` y se referencian en
cada diapositiva. Fuente de contenido: entrega_alsie/IFI_ALSIE.md, que es el
documento ya entregado; nada se inventa aquí. -->

# Diseño y evaluación de un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones heredadas modelo-vista-controlador

**Postulante:** Mario Arturo Uriarte Marin  
**Tutor:** Luis Roberto Pérez Rios, Ph.D.  
**Programa:** Magíster en Ingeniería de Software

**Universidad Autónoma del Beni «José Ballivián» · ALSIE Consultores Pedagógicos**

**Defensa final · noviembre de 2026 · Cochabamba, Bolivia**

> [Me presento y anuncio que voy a recorrer, en veinte minutos, la cadena completa: problema, objeto, campo, objetivo, hipótesis, modelo, propuesta, validación y aporte. Voy a distinguir, desde el inicio, lo que el estudio demuestra de lo que deja abierto, porque esa honestidad es parte del resultado.]

---

## 2. Relevancia y problema

**SIGPP:** sistema de planificación y presupuesto de la Caja Petrolera de Salud; subcircuito de ejecución del plan operativo anual (tareas, operaciones, presupuesto, certificación).

- Decisiones funcionales repartidas entre controladores, servicios, repositorios, entidades y vistas.
- Duplicación concreta de la selección de restricciones; diferencias locales en la validación temporal.
- Restricción institucional: evolucionar **sin reescritura completa** del sistema.

**El costo institucional agregado del cambio no fue cuantificado; esa ausencia se declara, no se disimula.**

> [El problema no es que SIGPP carezca de arquitectura o de pruebas: hay una separación parcial. El problema es que las decisiones de negocio están distribuidas, y quien mantiene el sistema no tiene una manera explícita de delimitar y comprobar un cambio sin arrastrar todo el flujo. No vengo a decir cuánto cuesta ese mantenimiento, porque no lo medí; vengo a aportar una manera de delimitarlo y verificarlo.]

---

## 3. Problema científico, objeto y campo

- **Problema científico:** delimitación y comprobación insuficientemente explícitas de cambios sobre decisiones funcionales distribuidas en el subcircuito de ejecución del plan operativo anual de SIGPP, en el caso de aplicación y evaluación realizado en La Paz, Bolivia.
- **Objeto de estudio:** la refactorización arquitectónica incremental de aplicaciones heredadas organizadas bajo modelo-vista-controlador.
- **Campo de acción:** las relaciones entre fronteras (decisión, observación, intervención), la semántica de los escenarios y la acreditación de propiedades según el nivel de comprobación.

*Cadena:* una situación real de distribución de decisiones → una brecha de explicitación → un objeto (la refactorización incremental) → un campo (las relaciones que la hacen verificable).

> [La brecha de conocimiento no es que falten técnicas de refactorización o de prueba: existen y las reconozco. La brecha está en explicitar y examinar reglas de adaptación para decisiones distribuidas, sus consumidores y sus niveles de evidencia. El objeto es la refactorización incremental; el método que diseñé es la propuesta para estudiarlo, y SIGPP es el contexto. No confundo el objeto con la herramienta.]

---

## 4. Objetivos de la investigación

**Objetivo general:** diseñar y evaluar un método de refactorización arquitectónica incremental para subcircuitos de aplicaciones heredadas modelo-vista-controlador, aplicado en la ejecución del plan operativo anual de SIGPP, con la finalidad de mejorar modificabilidad, testabilidad y trazabilidad sin reescritura completa.

*«Mejorar» expresa la finalidad original, no el resultado alcanzado.*

1. **Caracterizar** el estado de la refactorización y su comprobación en el subcircuito de ejecución de SIGPP mediante los indicadores y registros documentados.
2. **Sistematizar** los fundamentos de cambio seguro, responsabilidades arquitectónicas, testabilidad y métodos incrementales que sustentan el objeto y el campo.
3. **Precisar** los componentes y relaciones esenciales entre fronteras, escenarios y acreditación de propiedades, con su respaldo contextual y sus límites.
4. **Elaborar** la propuesta metodológica que concreta esas relaciones y documentar su aplicación y validación para atender las dificultades de delimitación y comprobación del caso.

> [Los cuatro objetivos organizan los resultados de los capítulos: diagnóstico, fundamentos, modelo y propuesta aplicada. La finalidad original de mejorar atributos se contrasta con los resultados efectivamente obtenidos; no se presenta como una mejora integral medida.]

---

## 5. Hipótesis de diseño

**Hipótesis de diseño:** el método de refactorización arquitectónica incremental, estructurado en ocho pasos y caracterizado por la diferenciación de fronteras de decisión, observación e intervención, la selección de escenarios según la semántica del comportamiento y la acreditación de propiedades por nivel de comprobación, permite delimitar y sustentar la verificación de cambios sobre las decisiones seleccionadas de creación de certificaciones del sistema institucional de planificación operativa y presupuesto de la Caja Petrolera de Salud, en La Paz, Bolivia, porque vincula explícitamente cada decisión con sus consumidores, efectos observables y evidencia pertinente.

> [La hipótesis no promete ahorro ni mejora medida de atributos: promete delimitación y sustento de la verificación, y su mecanismo es la correspondencia explícita entre decisión, consumidores, efectos y evidencia. Se formuló después del análisis de las aplicaciones; lo digo con claridad y no la presento como una predicción prospectiva que nunca existió.]

---

## 6. Diseño metodológico

| Método | Objetivo institucional | Técnica representativa |
|:--|:--|:--|
| Teórico: análisis y síntesis | Sistematizar | Contraste focalizado de antecedentes |
| Teórico: modelación documental | Precisar | Matrices de relaciones y evidencia |
| Empírico: análisis de documentos, código e historial | Caracterizar | Inspección de diferencias |
| Empírico: aplicaciones controladas | Elaborar | Escenarios, dobles de prueba, ejecución automatizada |

**Población y selección:** intencional. Tres familias de decisión (temporal, selección de restricciones, importe) y tres episodios de aplicación (P01, P02, aplicación del autor). No es un censo ni una muestra probabilística.

> [Métodos teóricos para fundamentar y precisar; métodos empíricos para caracterizar y aplicar. La selección fue intencional por acceso al código y relevancia de decisiones distribuidas; no pretendo estimar una prevalencia poblacional, y lo digo para acotar desde ahora el alcance de toda generalización.]

---

## 7. Diagnóstico: línea base y hallazgos

| Indicador | Estado documentado |
|:--|:--|
| I01. Correspondencia de decisiones | Con discrepancia temporal (parcial) |
| I02. Rechazo antes de efectos | Parcial, con dobles de prueba |
| I03. Esfuerzo humano | Descriptivo: 26 min 33,87 s |
| I04. Extensión de cambio posterior | Sin medición |

**Hallazgos que evidencian el problema:** O03 no distinguió el límite mensual; O06 acreditó rechazo con dobles; la hora alteró una admisibilidad local. La evidencia justificó separar decisión, observación e intención.

> [El diagnóstico no describe un sistema roto: describe alcances de comprobación no equivalentes. Una misma decisión se validaba distinto según el punto desde el que se miraba. Esa diferencia es el dato que motiva el modelo y la propuesta. Los cuatro indicadores quedan con estados parciales o sin medición, y lo conservo así en lugar de inflar el resultado.]

---

## 8. Marco teórico esencial

| Fundamento | Toma de posición |
|:--|:--|
| Feathers (2004) | Cambio seguro: caracterizar antes de mover; conexión con consumidores. |
| Fowler (2018) | Refactorización sin cambiar comportamiento; distinguir intención. |
| Bass et al. (2021) | Escenarios de calidad; separar control y observación. |
| Girjoaba y Capiluppi (2024) | Transformación gradual con comprobación, adaptada al caso. |

**El estudio no inventa estas prácticas: las explicita de forma conjunta y contextual, y esa explicitación es lo que se somete a examen.**

> [Cito pocos autores, los que realmente fundamentan el modelo, y tomo posición: la novedad incremental no está en la caracterización ni en las pruebas, que son anteriores, sino en explicitar las relaciones que las articulan para este tipo de decisión. No pretendo presentarme como el primero en usar un ciclo de refactorización.]

---

## 9. Modelo teórico: componentes

**Figura 1 — Modelo relacional de delimitación, observación y acreditación del incremento**

![Modelo relacional de delimitación, observación y acreditación del incremento](figuras/figura_1.png)

*Nota.* Representación conceptual propia de las relaciones del modelo. Las flechas expresan correspondencia, alcance y restricción; no prueban causalidad.

<!-- Composición: figura grande y legible; número y título arriba, nota debajo. -->

> [Este es el corazón de la tesis. Tres grupos de componentes: las fronteras diferenciadas, la semántica de los escenarios y la acreditación por nivel de comprobación. El contexto condiciona a los tres, y la evidencia retroalimenta la revisión de la frontera y limita lo que se puede afirmar. Las flechas son relaciones de correspondencia y restricción, no causalidad.]

---

## 10. Modelo teórico: relaciones esenciales

**Fronteras diferenciadas y revisables** — distinguir dónde se decide, desde dónde se observan los efectos y qué se interviene; el lugar de una condición no coincide necesariamente con el de sus consecuencias.

**Comprobaciones según la semántica** — identificar entradas realmente determinantes y resultados/efectos por escenario; no confundir ausencia válida con fallo, ni imponer un rechazo de dominio donde no corresponde.

**Acreditación por propiedad y nivel** — cada propiedad se liga a condiciones, comprobación y evidencia; una prueba con dobles no es persistencia real, y una configuración que retorna no es un recorrido de negocio.

*El modelo es una representación conceptual de estas relaciones, no un flujo de pasos ni la arquitectura de SIGPP.*

> [Cada relación explica una de las dificultades del diagnóstico: por qué observar desde un punto distinto de la decisión es pertinente; por qué los escenarios deben fijarse antes de ejecutar; y por qué niveles distintos de comprobación no acreditan propiedades equivalentes. Es conocimiento de adaptación de nivel de clase, con respaldo contextual, no una ley universal ni una relación causal aislada.]

---

## 11. Propuesta: método rediseñado M-R1

**Método de ocho pasos (P1–P8) y catorce requisitos.**

**Estructura de referencia:** ciclo de Girjoaba y Capiluppi (2024), adaptado al caso. M-R1 identifica la versión rediseñada tras la primera aplicación.

| Paso | Acción esencial |
|:--|:--|
| P1 Delimitar | Localizar decisión, consumidores y efectos; alcance proporcional. |
| P2 Caracterizar | Fijar observado, requerido e intención antes de mover. |
| P3 Controlar | Inventariar datos y dependencias determinantes. |
| P4 Migrar sin retirar | Implementación coexistente; original conservada. |
| P5 Comprobar | Escenarios con resultados/efectos normales, ausencia, rechazo, fallo. |
| P6 Retirar y conectar | Sustituir vía, ajustar consumidores y dependencias. |
| P7 Integrar y verificar | Separar comprobación local (P7-L) de integración (P7-I). |
| P8 Documentar y versionar | Trazabilidad completa y estado de cada medición. |

*El método concreta el modelo: las fronteras (P1–P2), la semántica (P3, P5) y la acreditación (P7–P8).*

<!-- Usar la tabla como representación principal. La figura 2, en figuras/figura_2.png,
queda como respaldo fuera del recorrido oral: no comprimir tabla y diagrama vertical
en una misma diapositiva. El retorno por discrepancia exige revisar contrato e intención. -->

> [La propuesta es una guía que otro practicante puede seguir, no una lista de clases de SIGPP. Cada paso tiene entrada, producto y condición de salida, y el retorno por discrepancia obliga a revisar contrato e intención antes de continuar. No es un flujo rígido: admite justificar que una comprobación no aplique.]

---

## 12. Demostración: decisión de importe

**Importe frente al disponible** — cinco escenarios (admisión y rechazo antes de efectos) con veinticinco aserciones reproducidas satisfactoriamente.

**Recorrido del ejemplo:** delimitar la decisión → fijar escenarios y efectos → comprobar desde el consumidor público → localizar la evidencia.

**Figura D1 — Coordinación y reutilización del cálculo del importe**

![Coordinación y reutilización del cálculo del importe](figuras/figura_4.png)

*Nota.* Ejemplo de la aplicación del autor en SIGPP; no constituye otro sistema ni otra muestra.

<!-- Antes de exponer: localizar el registro de ejecución y preparar una captura
verificada si existe. No afirmar que un video o captura está preparado sin comprobarlo.
La imagen explica la estructura; el registro respalda las cinco pruebas/25 aserciones.
No ejecutar escrituras reales ni mostrar datos institucionales durante la demostración. -->

> [Muestro una sola aplicación: la decisión de importe. Explico qué se delimitó, qué escenarios se fijaron y desde dónde se observaron los efectos. El resultado reproducido fue de cinco pruebas y veinticinco aserciones satisfactorias. La centralización del cálculo es un resultado estructural observado; no mide por sí sola el costo de un cambio futuro.]

---

## 13. Validación y resultados

**Tres episodios:** P01 (primer participante) → cuatro ajustes → M-R1 → P02 (segundo participante) → aplicación adicional del autor (importe).

| Afirmación | Respaldo | Límite |
|:--|:--|:--|
| Aplicación asistida | Los tres episodios se realizaron y registraron | Asistencia de IA documentada; sin autonomía |
| Conservación acotada | Escenarios acordados, reproducidos | Solo casos examinados, no equivalencia universal |
| Trazabilidad | T01–T14 cubren los requisitos | No cumple requisitos no medidos |

**No se demostró:** mejora conjunta de modificabilidad, testabilidad y trazabilidad; ahorro de esfuerzo; mantenibilidad empírica; solución temporal completa.

> [La validación distingue lo que se sostiene de lo que no. Se sostiene que el método pudo aplicarse y produjo cambios verificables con conservación acotada. No se sostiene una mejora conjunta de atributos ni un ahorro, y no lo maquillo: la discrepancia temporal, el rechazo parcial y la medición ausente siguen declarados.]

---

## 14. Aporte teórico y significación práctica

**Aporte teórico:** la explicitación conjunta de tres relaciones contextualizadas —fronteras diferenciadas y revisables, comprobaciones según la semántica y acreditación por nivel de comprobación— que explican cómo adaptar la delimitación y verificación del incremento sin copiar una estructura de clases.

**Significación práctica:** una guía de ocho pasos aplicada con asistencia en tareas delimitadas, con cambios comprobables, conservación acotada y registro de límites.

*El nexo:* fronteras y consumidores identificados, escenarios pertinentes y separación de comprobación local e integración.

> [El aporte no es la herramienta ni el número de pruebas: es el conocimiento —las tres relaciones y su comportamiento en este tipo de contexto—, formulado de modo que oriente otra guía u otra implementación sin copiar SIGPP. Su desempeño fuera del caso no está comprobado, y lo declaro como parte del aporte, no como un defecto oculto.]

---

## 15. Conclusiones: síntesis por objetivo

**Conclusiones, por objetivo institucional:**

1. **Caracterizar:** la distribución de decisiones produjo alcances de comprobación no equivalentes; la evidencia justificó separar decisión, observación e intención.
2. **Sistematizar:** se fundamentaron nueve decisiones y se compararon los antecedentes relevantes; la adaptación se delimitó como explicitación contextual, no invención.
3. **Precisar:** las tres relaciones articulan fronteras, escenarios y acreditación, con validación contextual de su operacionalización.
4. **Elaborar:** se formalizó un método de ocho pasos y catorce requisitos; P01 motivó cuatro ajustes, valorados luego por P02 y por la aplicación del autor.

<!-- Síntesis oral, NO transcripción literal de las conclusiones del IFI. Se conserva
la adaptación autorizada «los antecedentes relevantes». La guía pide conclusiones
literales: esta síntesis constituye una diferencia pendiente de decisión antes de
generar la versión definitiva. No modificar el IFI para hacerla coincidir. -->

> [Cada objetivo institucional tiene su resultado en el mismo orden en que fue planteado, y cada resultado conserva su límite. Las conclusiones son resultados, no sugerencias: la sugerencia va en las recomendaciones, y la principal es seguir el estudio fuera del caso antes de generalizar.]

---

## 16. Recomendaciones y cierre

**Recomendación seleccionada del IFI (texto literal):**

En relación con las conclusiones 2 y 3, sería pertinente contrastar las relaciones en decisiones y sistemas independientes, caracterizando experiencia y asistencia, para examinar condiciones de transferencia sin prometer los mismos resultados.

**Gracias por su atención.**

> [El estudio aporta una manera explícita de delimitar, comprobar y acreditar cambios en un sistema heredado sin reescribirlo, y reconoce con la misma claridad qué no demostró. Gracias por su atención; quedo a disposición de sus preguntas.]

---

## Notas de preparación (fuera del recorrido oral)

- **IFI cerrado:** el documento impreso y entregado no se modifica. Consultar `../entrega_alsie/CIERRE_IFI.md`. Toda mejora de este archivo afecta únicamente a la defensa.
- **Tiempo objetivo: 19 minutos, con un minuto de reserva.** Portada 0,25; relevancia 1; problema/objeto/campo 1,5; objetivos 1; hipótesis 1; metodología 1; diagnóstico 1,5; marco 1; modelo gráfico 2; relaciones 1,5; propuesta 2; demostración 1,5; validación 1,5; aporte 1,25; conclusiones 0,5; recomendaciones/cierre 0,5. Es una planificación, no un ensayo acreditado; comprobar con cronómetro.
- **Figuras:** `figura_1.png` (modelo, diapositiva 9) y `figura_4.png` (importe, diapositiva 12) están referenciadas con sintaxis de imagen. `figura_2.png` (secuencia) y `figura_3.png` (arquitectura) quedan como respaldo. Verificar inserción y legibilidad en el resultado generado; número/título arriba y nota debajo.
- **Sin términos de Design Science:** ya traducidos (artefacto → propuesta; principios de diseño → relaciones del modelo; evaluación formativa → validación para el rediseño).
- **Fidelidad al IFI:** título, objetivos específicos, hipótesis y recomendación seleccionada conservan el texto fuente. El objetivo general, el problema/campo y las conclusiones están sintetizados para exposición; no presentarlos como citas literales. El IFI se consulta en `../entrega_alsie/IFI_ALSIE.md`, sin editarlo.
- **Discrepancia editorial conocida:** la tabla 5 enumera ocho antecedentes y la conclusión segunda dice siete. La síntesis oral evita repetir el recuento. Si preguntan, reconocer la discrepancia de recuento; no inventar una exclusión deliberada de la base metodológica.
- **Composición de diapositivas:** fondo claro, contraste alto, títulos aproximadamente 38–40 pt y cuerpo 24–28 pt conforme a la sección C de la guía. No reducir la letra para hacer caber tablas o párrafos; resolver la distribución visual y registrar si requiere otra diapositiva y otro ajuste de tiempo. No convertir estas notas, los comentarios HTML o las referencias de respaldo en parte del recorrido principal.
- **Demostración con respaldo:** preparar captura o video por si no hay ejecución en vivo.
- **Honestidad como argumento:** no afirmar éxito sin dato; si una pregunta excede la evidencia, responder con el límite declarado y no inventar un resultado.

## Referencias para respaldo (APA 7)

Bass, L., Clements, P., & Kazman, R. (2021). *Software architecture in practice* (4th ed.). Addison-Wesley Professional.

Feathers, M. C. (2004). *Working effectively with legacy code*. Prentice Hall PTR.

Fowler, M. (2018). *Refactoring: Improving the design of existing code* (2nd ed.). Addison-Wesley Professional.

Girjoaba, A. V., & Capiluppi, A. (2024). Refactoring legacy code using cleaning up cycles: An experience report. En *2024 IEEE International Conference on Software Maintenance and Evolution (ICSME)* (pp. 753–764). IEEE. https://doi.org/10.1109/ICSME58944.2024.00079
