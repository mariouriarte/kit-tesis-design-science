# Revisión documental del dominio POA y presupuesto

**Corte:** 25 de octubre de 2026, actualizado tras la segunda incorporación del tesista. **Resultado acumulado:** catorce archivos revisados; trece conservados en `tmp/docs/` y únicamente las directrices de formulación presupuestaria de 2015 trasladadas a `tmp/docs/basura/`, sin eliminarlas. **El RE-SPO de la CPS y su aprobación de 2019 ya están disponibles**; la sección 9 actualiza la falta documental registrada en la revisión inicial. Las fuentes aportan contexto institucional, vocabulario y procedimientos de referencia; no demuestran una mejora arquitectónica ni validan el método de refactorización. E4 permanece abierta y no se modifica el alcance del artefacto.

## 1. Alcance y criterio de revisión

Se priorizaron el borrador CPS, las directrices CPS para 2027, el RE-SPO y la guía FAM–UNICEF. Los manuales ajenos se examinaron como comparación de procedimientos, no como normas aplicables a la CPS. Se revisaron portada, índice y apartados seleccionados; no se declara lectura íntegra de todos los documentos.

La extracción de los PDF permitió localizar los procedimientos de interés. El RE-SPO y las directrices CPS requirieron reconocimiento óptico de caracteres; se contrastaron visualmente la primera página del RE-SPO y la página PDF 6 de las directrices para comprobar institución y clasificación de tareas. Los localizadores siguientes indican **página del archivo PDF**, salvo indicación contraria; la guía FAM–UNICEF contiene dos páginas impresas por página PDF. El reconocimiento óptico no sustituye la comprobación visual de una cita literal o de una fecha normativa.

El clasificador recibió una lectura limitada: portada, índice, presentación y comienzo del objeto del gasto. Se extrajeron las páginas PDF 1–12, 49–51 y 5–7; la inspección sustantiva se concentró en las páginas PDF 1–5 y 51, sin recorrer el catálogo completo de partidas. La hoja de cálculo se inspeccionó sin modificarla, mediante estructura del libro, encabezados y primeras filas; no se recalcularon fórmulas ni se verificó la exactitud de sus metas.

## 2. Inventario y decisión por archivo

Todos los nombres de esta tabla son relativos a `tmp/docs/`.

| Archivo | Revisión y utilidad | Decisión y límite |
|:--|:--|:--|
| `CPS_MPP RESPO 5to BORRADOR AGM.docx.pdf` | 28 páginas. Apartados de vigencia, mapa de procesos, elaboración, seguimiento, modificaciones y certificación; pp. 5, 7–8, 12–13, 15–17 y 27–28. Vincula explícitamente el procedimiento con SIGPP. | **Conservar: prioridad alta.** Borrador institucional, no manual aprobado; no inferir vigencia por tener código y versión. |
| `CPS_DIRECTRICES_ADM_2027_0001.pdf` | 16 páginas, escaneadas. Nota de remisión y directrices: ámbito nacional CPS, programación de operaciones/tareas, responsabilidades, presupuesto y anexos. | **Conservar: prioridad alta.** Fuente institucional directa para formulación 2027; no convertir sus plazos de elaboración en restricciones de certificación. |
| `DOCUMENTO-RE SPO.pdf` | 21 páginas, escaneadas. Texto articulado del MPD en pp. 1–12; las restantes contienen un cuadro comparativo de actualización, con orientación que limita su reconocimiento óptico. Arts. 9, 14–15 y 20–22 especialmente útiles. | **Conservar: prioridad alta como comparación.** Es RE-SPO del MPD, no de CPS. Cita bases de 2005 y no acredita por sí solo vigencia actual, fecha de aprobación ni aplicabilidad a la Caja. |
| `bol_guia planificacion PAI - unicef.pdf` | 31 páginas PDF. Créditos p. 2; conceptos y articulación pp. 6–11; aplicación PAI pp. 14–16; instrumentos pp. 17–22. | **Conservar: prioridad alta para comprender el dominio.** Guía FAM–UNICEF para POA y presupuesto municipal del PAI; no norma interna CPS ni teoría de arquitectura. |
| `Clasificadores_Presupuestarios_2025_MEFP.pdf` | 169 páginas. Alcance general p. 5, objeto del gasto p. 51; no se hizo lectura extensa del catálogo. | **Conservar: consulta puntual.** Edición de gestión 2025, publicada/aprobada en 2024; no usarla automáticamente para validar códigos de 2027. |
| `CPS_Operaciones_DNS_segun_ACP_2027_v2_ADM_Desc.xlsx` | Una hoja: `plantilla operaciones DNS`, dimensión `A1:AN39`. Encabezados ACP, resultado, operación, indicador, fórmula, línea base, meta, tarea, programación física/presupuestaria trimestral, partida y total. | **Conservar: evidencia estructural de contexto.** La propia plantilla declara información referencial, no limitativa. Es de salud/DNS, no inventario exhaustivo de todas las administraciones ni evidencia de ejecución real. |
| `CPS_Certificacion.drawio.png` | Diagrama por unidad solicitante, DNPD, operador POA y contabilidad, con revisión, observaciones y entrega de certificación. | **Conservar: apoyo al contraste funcional.** Sin fecha, autor ni aprobación acreditados. No prueba que SIGPP ejecute todos los controles dibujados. |
| `MANUAL DE PROCESOS Y PROCEDIMIENTOS - CERTIFICACIONES POA_RA INE.pdf` | 31 páginas. Resolución INE/DGE/27/2019, 14 de febrero de 2019; pp. 11–12 y 20–22: insumos, roles, presupuestos actualizados y certificación. | **Conservar: comparación de mayor proximidad funcional.** Distingue certificación POA y posterior certificación presupuestaria; no adoptar sus plazos, formatos o autoridades para la CPS. |
| `Manual Procesos y Proced SPO ministerio de desarrollo productivo.pdf` | 44 páginas. Portada 2020; sec. 8.6, pp. 40–42: solicitud, revisión, aprobación, observaciones y archivo, apoyados por WARA II. | **Conservar: comparación.** Su meta administrativa de un día no es un resultado empírico ni criterio de éxito de nuestra refactorización. |
| `MPP_UF_RM_N°305_de_23.11.2018 MINISTERIO DE PLANIFICACIÓN DEL DESARROLLO.pdf` | 111 páginas. P. 6: separación de presupuesto y contabilidad; sec. 8.1.5, pp. 26–28: certificación presupuestaria y disponibilidad. | **Conservar: consulta secundaria.** No leer íntegramente tesorería/contabilidad. La fecha y resolución del nombre no se confirman como acto de aprobación mediante el propio archivo revisado; el año 2018 sí consta en portada. |
| `Directrices Presupuestarias_2015_0.pdf` | 74 páginas. Portada, arts. 7–9 (p. 6) y anexo conceptual (p. 12): formulación para gestión 2015, objetivos de gestión y articulación presupuestaria. | **Trasladar a `basura/`: prescindible para el análisis actual.** Los conceptos generales ya se cubren mejor con fuentes próximas al caso; las disposiciones anuales de 2015 no sirven como regla operativa de 2026–2027. Se conserva recuperable como antecedente. |

## 3. Hallazgos prioritarios de la CPS

**Ampliación del inventario: segunda incorporación**

| Archivo en `tmp/docs/` | Revisión y utilidad | Decisión y límite |
|:--|:--|:--|
| `CPS_REGLAMENTO ESPEC.SISTEMA PROGRAMAC. OPERACIONES 19.pdf` | 40 páginas. Resolución R.H.D. 003/19, pp. 3–8; reglamento, pp. 11–22; informes y antecedentes posteriores. Arts. 2, 6–18 contrastados mediante texto; parte resolutiva p. 7 comprobada visualmente. | **Conservar: fuente institucional prioritaria.** Resuelve la ausencia del RE-SPO CPS y de su aprobación en el corpus inicial. Modificaciones posteriores y vigencia íntegra actual por verificar. |
| `CPS_RES- A-006-01  SISTEMA DE PRESUPUESTO.pdf` | 18 páginas, principalmente escaneadas. OCR de contenido y comprobación visual de pp. 14–15 de la resolución. Arts. 10 y 16–21: POA, programación, recursos, ejecución y modificaciones. | **Conservar: fuente presupuestaria CPS.** R.D. 023/06, fechada 25 de enero de 2007; conservar esa combinación sin corregirla por inferencia. Vigencia actual por verificar. |
| `CPS_RESPO 20 NOV2018 (1)_Modelo referencial.docx.pdf` | 18 páginas. Lectura de apartados seleccionados frente al reglamento aprobado: responsabilidades, operaciones, tareas, requerimientos, seguimiento y modificaciones. | **Conservar: auxiliar de lectura y comparación.** Sin acto propio de aprobación identificado en el texto extraído. No se certifica identidad completa ni sustituye al ejemplar aprobado de 2019. |

### 3.1 Tarea no equivale a asignación presupuestaria

Caja Petrolera de Salud (2026, sec. 5.4, pp. PDF 6–7) dispone registrar operaciones y tareas, clasificando estas últimas «con o sin presupuesto». La página PDF 6 se contrastó visualmente, además del reconocimiento de texto. El borrador del manual también contempla operaciones y tareas con o sin presupuesto (Caja Petrolera de Salud, s. f., pp. 12–13). En consecuencia, no corresponde formular el dominio como si toda tarea debiera tener necesariamente una asignación monetaria o una subpartida.

La declaración del tesista del 25 de octubre se registra así: cuando una tarea tiene presupuesto, se vincula con la estructura denominada en SIGPP **grupo presupuestario → partida → subpartida**. Es una descripción del sistema aportada por su desarrollador, no un mapeo técnico comprobado en esta revisión. La opcionalidad de la asignación tiene respaldo documental; las cardinalidades, claves, tratamiento de presupuesto cero y posibilidad de varias asignaciones por tarea quedan por contrastar con SIGPP. No se modifica código ni se fija una regla de rechazo a partir de esta lectura.

Ministerio de Economía y Finanzas Públicas (2024, p. impresa 49, p. PDF 51) presenta el ejemplo `10000 Servicios personales → 11000 Empleados permanentes → 11200 Bono de antigüedad → 11210/11220`, por lo que el catálogo tiene una desagregación intermedia que no debe perderse al equipararlo con tres nombres internos. Debe distinguirse también el **objeto del gasto** de la **categoría programática**, la **fuente de financiamiento** y el **organismo financiador**. El modelo de SIGPP puede agrupar niveles de otra manera, pero esa equivalencia no está demostrada todavía.

### 3.2 Cobertura de administraciones sin ampliar la intervención

Caja Petrolera de Salud (2026, sec. 3, p. PDF 3) establece aplicación a las áreas y unidades organizacionales de nivel nacional. La sec. 5.4 diferencia administraciones y unidades y vincula sus operaciones con ACP y REACP; esto respalda que el dominio no corresponde a una sola oficina. La hoja de salud/DNS aporta ejemplos de estructura, no demuestra que todas las administraciones tengan las mismas operaciones o restricciones. La cobertura institucional del POA no cambia el alcance de la tesis: intervención incremental sobre el subcircuito de ejecución y certificación, no reconstrucción del sistema nacional de planificación.

### 3.3 Borrador, responsabilidades y procedimiento de certificación

Caja Petrolera de Salud (s. f., sec. 6, p. 5) condiciona la vigencia a una resolución expresa del Honorable Directorio. Las pp. 27–28 describen solicitud respaldada por operación, tarea, partida, cantidad y precio; autorización, derivación, revisión, emisión y subsanación de observaciones. También incluyen la nota de que una unidad ejecutora solo puede utilizar sus recursos, sin afectar la planificación de otra. Son puntos candidatos a contrastar con práctica, documentación aprobada y controles del servidor; no se convierten automáticamente en requisitos vigentes o en defectos acreditados.

El tesista declara que la CPS todavía no cuenta con MPP aprobado de planificación, aunque dispone de manuales y guías de elaboración y certificación. Esto es compatible con la existencia del quinto borrador aportado. No obstante, el encabezado del borrador y las directrices utilizan **Departamento Nacional de Planificación y Desarrollo (DNPD)** y el borrador menciona la **Unidad Nacional de Gestión y Planificación**; el estado anterior identifica DNGP como área dueña de SIGPP. Se registra la diferencia de denominación sin sustituir la unidad responsable ni atribuir competencias por inferencia.

## 4. Qué aporta el RE-SPO y qué no acredita

**Nota de actualización:** esta sección describe el RE-SPO del MPD del inventario inicial. La segunda incorporación resolvió la falta del RE-SPO propio CPS, según la sección 9; no cambia la identidad ni la autoridad del documento del MPD.

Ministerio de Planificación del Desarrollo (s. f.) delimita en su art. 2 la aplicación al propio ministerio y exige reglamentos propios a instituciones descentralizadas bajo su tuición. Su art. 14 define una operación como conjunto de tareas; los arts. 9 y 15 relacionan operaciones, recursos, partidas y límites presupuestarios. Los arts. 20–22 distinguen seguimiento, evaluación y ajustes por cambios de objetivos, operaciones o recursos. Este conjunto es útil para entender relaciones y variaciones del dominio, pero no acredita el reglamento específico de la CPS.

El documento cita la Resolución Suprema N.º 225557 de 2005, mientras que el borrador CPS remite al Decreto Supremo N.º 3246 de 2017. La diferencia muestra que no deben combinarse ambos textos como si pertenecieran a una única versión normativa. No se verificó en esta revisión la resolución de aprobación, la vigencia actual ni la sustitución formal del RE-SPO del MPD. La falta inicial del **RE-SPO propio de la CPS y su acto de aprobación** quedó resuelta con la segunda incorporación, documentada en la sección 9.

## 5. Lectura prioritaria de la guía FAM–UNICEF

### 5.1 Aportes aprovechables

Federación de Asociaciones Municipales de Bolivia y Fondo de las Naciones Unidas para la Infancia (s. f., pp. impresas 12–21; pp. PDF 7–11) separan acción de corto plazo, operación, actividad e indicador. La guía distingue SPO y Sistema de Presupuesto, representa sus subsistemas y explica su articulación, sin reducir la planificación al gasto. En particular, la p. impresa 19 relaciona programación de ACP, determinación de operaciones y requerimientos con estructura programática y programación presupuestaria. Este esquema ayuda a conservar el significado de las relaciones durante una refactorización, no a decidir por sí solo una arquitectura.

Las herramientas ofrecen una segunda utilidad concreta: memorias de cálculo, programación de operaciones/actividades, presupuesto de recursos y gastos y programación financiera (pp. impresas 31–43; pp. PDF 17–22). Las pp. impresas 38–41 separan partida, costo, fuente, organismo financiador y estructura programática, evitando tratarlos como un único clasificador. También se presentan unidad de medida, fórmula, línea base y meta del indicador. Son ejemplos para contrastar vocabulario y trazabilidad, no evidencia de resultados reales de la CPS.

### 5.2 Límites y atribución

La portada identifica una guía para elaboración del POA y presupuesto **municipal del PAI**, no un manual general de ejecución de todas las instituciones. Los créditos reconocen FAM–Bolivia y UNICEF y atribuyen contenidos a Carla Maritza Hidalgo Lara; no corresponde atribuir toda la obra exclusivamente a UNICEF. No se confirmó un año editorial explícito: los ejemplos de gestión 2024 y la fecha técnica del archivo no bastan para fijarlo. Se utiliza **s. f.** y se conserva pendiente la verificación de publicación pública; la dirección candidata consultada en UNICEF devolvió 404 y no se usa como referencia.

Las competencias del gobierno municipal, la vacunación, el Concejo Municipal y los instrumentos propios del PAI no se trasladan como reglas de la CPS. La guía puede enriquecer la explicación del dominio y el contraste documental, pero no reemplaza literatura sobre refactorización, modificabilidad o testabilidad. Tampoco su calidad expositiva prueba que un diseño informático particular sea superior. Esta separación evita una fundamentación decorativa y mantiene el objeto de estudio en el método más su instanciación, no en la elaboración de un MPP de planificación.

## 6. Consecuencias para la trazabilidad de la tesis

| Hallazgo documentado | Uso permitido ahora | Comprobación pendiente antes de diseñar o evaluar |
|:--|:--|:--|
| Existen tareas con y sin presupuesto. | Corregir vocabulario del contexto y evitar una obligatoriedad monetaria universal. | Mapeo de asignación opcional, cardinalidades y comportamiento vigente en SIGPP. |
| La certificación relaciona operación, tarea y presupuesto. | Seleccionar relaciones y comportamientos que deben preservarse al extraer lógica. | Contrastar borrador, guías aprobadas, práctica y validaciones efectivas. |
| El presupuesto se clasifica por varias dimensiones. | No confundir objeto del gasto con fuente, organismo o categoría programática. | Relacionar niveles oficiales con entidades internas y catálogo de la gestión aplicable. |
| Las modificaciones pueden alterar planificación y recursos. | Identificar escenarios de variación del contexto, sin asumir borrado físico. | Estados de tarea, versiones y efecto real sobre elegibilidad y saldo. |
| Los manuales INE y ministeriales separan actores y certificaciones. | Comparar responsabilidades y diferencias contextuales. | No asumir equivalencia de certificación POA y presupuestaria ni copiar plazos ajenos. |
| Las directrices 2027 regulan formulación. | Acreditar estructura institucional y uso de SIGPP. | No reutilizar ventanas de elaboración como ventanas de certificación ni resolver con ellas fechas extraordinarias. |

No se establece una nueva brecha científica ni se cierra E5 por reunir manuales de dominio. Las fuentes documentan procedimientos administrativos; el contraste de métodos existentes de refactorización sigue pendiente. Tampoco se fijan retrospectivamente criterios de éxito para intervenciones previas ni se acredita un ciclo de evaluación por disponer de esta documentación. La siguiente decisión requiere primero distinguir las reglas CPS aprobadas de sus borradores y referencias externas.

## 7. Referencias y estado de verificación

Las referencias documentales citadas se incorporan a `referencias.md`, en el apartado de fuentes del contexto POA revisadas localmente. **Verificación local** significa que se comprobó contenido del ejemplar aportado; no implica autenticación institucional, publicación pública o vigencia jurídica. Los datos faltantes se declaran allí como **[por verificar]**, sin inventar año, resolución o dirección electrónica.

## 8. Pregunta inicial resuelta con la segunda incorporación

La solicitud del RE-SPO propio y de su resolución de aprobación quedó atendida con `CPS_REGLAMENTO ESPEC.SISTEMA PROGRAMAC. OPERACIONES 19.pdf`. No volver a solicitar estos documentos como si faltaran. La diferencia entre las denominaciones institucionales cuenta ahora con respaldo histórico adicional, pero la estructura orgánica actual no se deduce automáticamente de textos de distintas fechas.

## 9. Segunda incorporación: respaldo propio de la CPS

### 9.1 RE-SPO aprobado en 2019

Caja Petrolera de Salud (2019) reúne el reglamento y la R.H.D. N.º 003/19, de 11 de marzo de 2019. La fecha y denominación aparecen en las pp. PDF 1 y 3; la p. 7 contiene el resuelve primero que lo aprueba, comprobado visualmente, y la p. 8 continúa las firmas. El expediente refiere compatibilidad mediante nota MEFP/VPCF/DGNGP/UNPE/N.º 1975/2018, de 20 de diciembre de 2018 (pp. 4, 6 y 23); esta referencia no se confunde con la resolución institucional de aprobación. La portada interna de 2018 y el encabezado R.M. N.º 1109/2017 no cambian la fecha del acto de aprobación CPS de 2019.

| Materia | Localizador del reglamento aprobado | Uso en la tesis y límite |
|:--|:--|:--|
| Cobertura nacional. | Art. 2, p. PDF 11. | Respalda distintas áreas y unidades CPS; no exige intervenir todos los módulos o administraciones. |
| Elaboración, versiones, revisión y custodia. | Arts. 6–11, pp. PDF 12–13. | La Unidad Nacional de Gestión y Planificación elabora, controla versiones y custodia; DNPD revisa y el Directorio aprueba. No equiparar competencias ni inferir organigrama actual. |
| Articulación con PEI y formulación. | Arts. 12–14, pp. PDF 14–16. | Relaciona ACP, resultados, presupuesto, REACP, operaciones, actividades, tareas, unidad ejecutora y requerimientos. No convierte cada campo del formulario en una entidad obligatoria de SIGPP. |
| Operaciones y tareas. | Art. 14.b, pp. PDF 15–16. | Confirma determinación por REACP y unidades ejecutoras, distingue funcionamiento e inversión y contempla agrupación en actividades. No fija cardinalidades de grupo/partida/subpartida. |
| Seguimiento a ejecución. | Art. 16, p. PDF 18. | Distingue resultados esperados/logrados, presupuesto aprobado/ejecutado y avance temporal. Son indicadores administrativos POA, no medidas de modificabilidad o testabilidad del software. |
| Evaluación periódica. | Art. 17, pp. PDF 19–20. | Describe evaluadores ajenos a unidades ejecutoras y evaluaciones de medio término y conclusión. No demuestra una evaluación realizada del artefacto DS. |
| Modificación del POA. | Art. 18, p. PDF 20. | Documenta requerimiento del REACP, proyecto modificado, conformidad, aprobación y difusión. No implica borrado físico de tareas ni pérdida automática de elegibilidad en SIGPP. |

No se identificó un procedimiento específico de certificación en el índice o en el texto extraído del reglamento. Tampoco se localizó la expresión «sin presupuesto»; el respaldo explícito de esa clasificación continúa siendo la sec. 5.4 de las directrices CPS 2027 y, como apoyo no aprobado, el quinto borrador del MPP. Los períodos de planificación del art. 14 no bastan para derivar una prohibición automática de certificar fuera del trimestre programado. Se conserva la distinción acordada entre planificación, disponibilidad y habilitación de certificación.

### 9.2 Reglamento específico de presupuesto

Caja Petrolera de Salud (2007) incluye la R.D. N.º 023/06, fechada 25 de enero de 2007, en pp. PDF 14–16. Las pp. 14–15 fueron comprobadas visualmente: el resuelve primero aprueba el reglamento y el tercero dispone vigencia desde la fecha de esa resolución. El texto mantiene referencias y denominaciones de su época; se documenta aprobación histórica sin afirmar que todos sus procedimientos y sistemas de registro siguen inalterados en 2026. La numeración terminada en «06» y la fecha de 2007 se conservan fielmente, sin resolver su diferencia mediante conjeturas.

El art. 10 (pp. PDF 8–9) articula POA y presupuesto mediante requerimientos y categorías programáticas; los arts. 16–18 (p. PDF 11) distinguen programación del gasto, disponibilidad efectiva y ajuste cuando los recursos no alcanzan lo previsto. El art. 19 (pp. PDF 11–12) trata modificaciones presupuestarias y su respaldo técnico y legal, mientras los arts. 20–21 (p. PDF 13) abordan reportes y comparación de lo presupuestado con lo ejecutado. Estas distinciones ayudan a no equiparar presupuesto asignado, disponibilidad de caja, certificación y devengamiento. Su traducción en reglas concretas del servidor exige todavía revisar la normativa aplicable a la gestión y el comportamiento de SIGPP.

### 9.3 Prioridad documental actualizada

Para reglas propias del caso se prioriza el **RE-SPO CPS aprobado en 2019**, complementado por las directrices CPS de la gestión pertinente y el reglamento presupuestario con sus límites temporales explícitos. El modelo referencial añadido se conserva como auxiliar, el MPP como borrador y los textos del MPD, INE y otros ministerios como comparación. No se traslada ningún archivo nuevo a `basura/`: el modelo aporta una representación legible para contraste, aunque no tiene la misma autoridad que el ejemplar aprobado. Disponer de reglamentos aprobados no contradice la ausencia de un **MPP de planificación aprobado** declarada por el tesista.
