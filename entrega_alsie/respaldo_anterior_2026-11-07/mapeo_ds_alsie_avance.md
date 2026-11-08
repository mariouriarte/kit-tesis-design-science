# Mapa del avance de Design Science al modelo ALSIE

**Avance provisional para revisión docente — corte al momento de generación.** Corte: 22 de octubre de 2026, 18:55:57, UTC−04:00. Nivel de maestría. Documento traducido: [IFI_ALSIE_AVANCE.md](IFI_ALSIE_AVANCE.md). No es cierre de investigación ni modificación de estados.

## 1. Fuentes y criterio de vigencia

Se leyeron `tesis_ds/00_estado.md`, los otros dieciséis Markdown disponibles de esa carpeta y ambas normas: `instituciones/alsie/guia_ifi_contenido.md` e `instituciones/alsie/indicadores_revision_ifi.md`. No se realizó investigación externa ni una nueva inspección de SIGPP. Las ejecuciones técnicas se trasladan como registros de las revisiones originales.

**Orden de interpretación:** el estado rector conserva las etapas; las actualizaciones fechadas corrigen afirmaciones técnicas antiguas. La mera existencia de un archivo E7 no cambia el estado pendiente. Los borradores de septiembre y comienzos de octubre no prevalecen sobre las aclaraciones del 18–21 de octubre y el seguimiento posterior del estado.

| Archivo leído en `tesis_ds/` | Apartados utilizados / función | Fecha y vigencia |
|:--|:--|:--|
| `00_estado.md` | Datos generales, Etapas, Decisiones tomadas, Preguntas abiertas, Restricciones de tiempo, Próximo paso | Registro rector hasta 22/10/2026; contiene historia y aclaraciones posteriores, no una única fecha de observación técnica. |
| `01_areas_y_temas.md` | Contexto real, Restricciones y viabilidad, Revisor, Alcance, Delimitación | E1 cerrada 27/09; referencias a API y evaluación trimestral no amplían el alcance final aceptado. |
| `02_delimitacion.md` | Problemas, Objeto, Campo, Propuesta, Decisión de alcance, Cierre | E2 preliminar 27/09; brecha no verificada; notas de pendientes internas no anulan cierre preliminar del estado. |
| `03_perfil_ds.md` | Título, Pregunta, Objetivos, Estrategia, Criterios, Contribución | E3 preliminar 27/09; «validados» es aspiración, no resultado existente. |
| `04_marco_teorico.md` | Ejes y actualizaciones del 18, 20 y 21/10; incorporación de Bass | E4 iniciada; las actualizaciones corrigen la falta de prueba directa y matizan exigencia de pruebas previas absolutas. |
| `07b_requisitos.md` | Requisitos preliminares y tensiones | Registro del avance del 13/10 según estado; contiene ausencias ya corregidas y expresión arquitectónica discutida. No se adopta como contrato vigente cerrado. |
| `07c_diseno_artefacto.md` | Diseño, componentes, restricción y estrategia de prueba | Preliminar del avance del 13/10; lo previsto del resolvedor ya tiene evidencia posterior; arquitectura no aprobada. |
| `07e_construccion_verificacion.md` | Historial y Actualización verificada del 18/10 | Distingue antecedente 2025 y pruebas actuales; estado «sin seguimiento» corregido por seguimiento del 20/10. |
| `arquitectura_candidata_certificacion_2026-10-18.md` | Evidencia, Verificación reproducida, Alternativas, Contrato candidato, Camino previo | 18/10; no adoptado; datos históricos conservados con correcciones de seguimiento. |
| `reglas_fecha_certificacion.md` | Fuente y alcance, HU, revisión 20/10, extensión, diagnóstico del recorrido, incremento candidato | Sesión 18/10 y revisión 20/10; extraordinaria no limitada a enero–marzo; reglas declaradas, no normativa comprobada. |
| `busqueda_e4_2026-10-20.md` | Protocolo, Fuentes, Síntesis y límites | 20/10; exploratoria, resúmenes/metadatos, no revisión sistemática. Mención de excepción trimestral superada por aclaración funcional. |
| `lectura_fuentes_locales_2026-10-21.md` | Lectura primaria Feathers/Fowler, originalidad | 21/10; no lectura íntegra ni defensa del tesista. Ausencia de Bass en carpeta superada por adjunto posterior. |
| `lectura_bass_clements_kazman.md` | Fuente, fundamentos, costos, límites, siguiente trabajo | Sin fecha explícita propia; incorporación posterior al inventario del 21/10, registrada al corte. No se inventa fecha ni se solicita otra vez el libro. |
| `matriz_coherencia.md` | Cadena, actualizaciones, riesgos y eslabones huérfanos | Incluye registros 13/10 y actualizaciones 18–21/10; se lee con sus reservas. No se altera. |
| `perfil_presentacion_lunes.md` | Contexto y formulación inicial | Perfil para 28/09; no prueba contribución validada ni métodos ejecutados. |
| `propuesta_borrador_2026-10-05.md` | Línea base técnica, seis actividades, plan, alcance | Preparado 04/10 para revisión 05/10; métricas históricas sin protocolo completo; no entrega final. |
| `referencias.md` | Referencias citadas y consultas pendientes | Registro actualizado con lecturas focalizadas; se conserva comprobación parcial y `[por verificar]`. |

**Productos no disponibles:** `05_estado_del_arte.md`, `06_diagnostico.md`, `07a_alternativas.md`, `07d_plan_construccion.md`, `07f_ficha_artefacto.md`, `08_evaluacion.md`, `09_enlace_solucion.md` y `10_contribucion_conclusiones.md`. Sus notas auxiliares no equivalen a productos cerrados.

## 2. Mapa apartado por apartado

Todos los caminos de origen siguientes son relativos a `tesis_ds/`. **[vacío]** significa ausencia de producto o contenido suficiente, no encabezado vacío en el IFI. Los pendientes del IFI explican qué evidencia falta.

| Destino en IFI | Fuente exacta y apartados | Traducción y reserva |
|:--|:--|:--|
| Carátula y título | `00_estado.md`, Datos generales; `03_perfil_ds.md`, Título | Nombres y programa conservados; términos heredados/aplicación. Institución legal, logo, ciudad, país, grado exacto y fecha final pendientes. Título largo con siglas señalado, no aprobado como definitivo. |
| Agradecimientos y Dedicatoria | [vacío] | Notas opcionales; no se atribuyen textos personales. |
| Resumen | `03_perfil_ds.md`, Objetivos/Estrategia; `07e_construccion_verificacion.md`, actualización 18/10; estado | Síntesis de avance, no de resultados finales: pasado para revisión y futuro explícito para lo previsto. Sin hipótesis ni eficacia inventadas. |
| Índice e índice de tablas/figura | Estructura del IFI | Lista de apartados y subapartados, sin preliminares ni páginas inventadas; paginación externa pendiente. |
| Introducción 1.1 | `01_areas_y_temas.md`, Alcance y contexto; `02_delimitacion.md`, Decisión; estado, inicio | Contexto institucional, período de investigación separado de antecedente 2025. |
| Problema científico 1.2 | `02_delimitacion.md`, Problemas; `03_perfil_ds.md`, Planteamiento; `04_marco_teorico.md`, actualización 21/10 y Bass | Fusión situación real–necesidad de conocimiento sin anticipar solución. Se matiza inexistencia de método frente a antecedentes; brecha, costo, población y sede específica aún no cerrados. |
| Objeto 1.3 | `02_delimitacion.md`, Objeto/Campo; `04_marco_teorico.md`, Propósito/Ejes | Traducción inversa: área de evolución arquitectónica; método pasa a propuesta. Formulación editorial provisional, no cambio de matriz científica. |
| Campo 1.3 | `02_delimitacion.md`, Campo/Alcance; `03_perfil_ds.md`, Criterios | Propiedades y relaciones de responsabilidades/dependencias y atributos; clase de contextos no se convierte en universalidad. |
| Objetivo general 1.4 | `03_perfil_ds.md`, Objetivo general; matriz, Cadena | Conservado con equivalencias; no se añade aporte original demostrado a la fórmula. |
| Objetivos específicos 1.4 | `03_perfil_ds.md`, cinco Objetivos específicos | Se mantienen cinco: 1→I, 2→II, 3→método y vacío de modelación III, 4+5→IV. Exigencia de cuatro objetivos no satisfecha; reformulación requiere aprobación. |
| Hipótesis 1.5 | [vacío]: faltan E8/E10 | Fórmula 6.5 pendiente: no hay principios validados ni mecanismo contrastado. |
| Aporte teórico 1.5 | `03_perfil_ds.md`, Contribución preliminar; `04_marco_teorico.md`, contraste originalidad | Solo aspiración; fórmula 6.6 pendiente de conceptos/relaciones originales y evidencia. |
| Significación práctica 1.5 | `02_delimitacion.md`, Costo/Criterios; `07e_construccion_verificacion.md`, 18/10 | Utilidad prevista más capacidad local registrada; fórmula 6.7 no completa por falta de magnitud y enlace E9. |
| Métodos/técnicas 1.6 | `03_perfil_ds.md`, Estrategia; `07e_construccion_verificacion.md`, ejecución; notas de lectura y búsqueda | Reclasificación de análisis-síntesis, análisis documental/código y pruebas; separación realizado/previsto vinculada a objetivos. No se inventa experimento ni revisión sistemática. |
| Población/muestra 1.7 | `01_areas_y_temas.md`, acceso/revisor; borrador 05/10, Línea base | Caso intencional y once archivos históricos, no muestra probabilística; unidades, tamaño y selección formal pendientes. |
| Estado 1.8 | `00_estado.md`, Etapas | Copia fiel de estados; etapas pendientes aunque existan borradores. |
| Capítulo I | Borrador 05/10, Línea base; nota arquitectura, Evidencia; `reglas_fecha_certificacion.md`, Diagnóstico estático | Análisis antes de tabla; cifras iniciales históricas; no ausencia actual de prueba del servicio. [vacío] de operacionalización e instrumentos, sin inventarlos. |
| Capítulo II | `04_marco_teorico.md`, ejes y actualizaciones; tres fichas de búsqueda/lectura | Síntesis relacionada con decisiones, contraste crítico y novedad pendiente; E5 no sustituida por búsqueda breve. |
| Capítulo III | [vacío] de E10 y modelo original; `07c` solo arquitectura preliminar | Se mantienen fundamento, componentes, gráfico, propiedades y texto de cierre como pendientes sustantivos. Fórmula 6.10 no ejecutable; no se inventa gráfico teórico. |
| Capítulo IV 5.1 | `02_delimitacion.md`, Propuesta; borrador 05/10, seis actividades | Método preliminar; estructura reconocida con autor no adoptada. *Resultados científicos* pendiente. |
| Capítulo IV 5.2 | Nota arquitectura 18/10, Alternativas y Contrato/diagrama; `07c`, componentes | Alternativas documentadas candidatas, no E7a cerrada; diagrama técnico existente traducido, no modelo teórico. Preparación opcional. |
| Capítulo IV 5.3–5.4 | `reglas_fecha_certificacion.md`, revisión 20/10, HU y siguiente incremento; lecturas Feathers/Fowler/Bass | Separación cambio estructural–funcional, extraordinaria por gestión concreta, semántica día calendario, no migración autorizada. |
| Capítulo IV 5.5 | `07e`, actualización 18/10; arquitectura, Verificación; reglas, Punto de partida Git | Pruebas reproducidas 18/10 según notas, no ejecución nueva. Estado de seguimiento 20/10 corrige archivos no versionados. [vacío] de evaluación final, revisión independiente y validación institucional. |
| Capítulo IV 5.6 | Matriz, Eslabones huérfanos | Relación parcial I–II; no concreción acreditada de III ni solución probada. |
| Conclusiones | Estado; `07e` 18/10; lecturas, tensión originalidad | Cuatro balances del avance por capítulo; no se inventa resultado de modelo o validación. E10 ausente. |
| Recomendaciones | Estado, Preguntas abiertas/Próximo paso; matriz, Riesgos | Sugerencias ligadas a vacíos constatados y viables, no despliegue de propuesta validada. |
| Referencias | `referencias.md`, Referencias citadas; fichas de lectura | APA 7 de once fuentes realmente citadas. Gregor y Hevner (2013) no se usa en este IFI y no se copia solo por estar en la biblioteca. Consultas pendientes separadas. |
| Anexos | `07e` 18/10; nota arquitectura, comandos; reglas, HU/criterios; estado | Síntesis de sustento con procedencia, no instrumentos aplicados. Ficha reproducible e instrumentos no disponibles. |

## 3. Tensiones resueltas documentalmente, sin nuevas decisiones científicas

1. **Cronología:** las extracciones `815ce6c0` y `9d4af430` datan de marzo de 2025; no son construcción prospectiva de la tesis de septiembre/octubre de 2026. Los volúmenes Git antiguos no se usan como mejora medida.
2. **Prueba directa:** las afirmaciones de ausencia del 13/10 quedan superadas por `CreateCertificacionServiceTest.php` y las ejecuciones del 18/10. No se mantiene ese vacío como actual.
3. **Versionado:** la observación inicial de archivos sin seguimiento queda superada por `8dc63307` y `1294047e` en el seguimiento del 20/10. Esto no prueba secuencia TDD intermedia, envío remoto ni nueva ejecución.
4. **Arquitectura:** «limpia mínima» no se adopta como contrato verificable. La nota candidata conserva MVC con frontera incremental y excepciones. No equivale a elección aceptada ni modelo teórico original.
5. **Fechas:** enero–marzo es antecedente. La revisión del 20/10 admite ventana extraordinaria para gestión inmediatamente anterior en cualquier momento del año actual, conserva días 29/31 y no dispensa permisos/saldo. No hay implementación acreditada de la extensión.
6. **Planificación:** períodos de tarea referenciales; `Operacion` no aporta una supuesta fecha de registro. No se añade rechazo por trimestre ni borrado físico de tareas.
7. **Sustento bibliográfico:** Feathers y Bass ya presentan procedimientos incrementales; se retira cualquier lectura confirmatoria de inexistencia universal. La brecha permanece preliminar.
8. **Acceso a Bass:** resuelto por adjunto posterior. Año 2021 según catálogo, copyright 2022; localizadores por secciones. La ficha posterior prevalece sobre ausencia en inventario.
9. **Cifras:** 37/305 es subconjunto de 188/540; no se suman. La coincidencia con diferencia frente a 151/235 no acredita comparación controlada ni cobertura.
10. **Gráfico:** la figura técnica del IV no se traslada al III como teoría. Falta de modelo implica falta de representación, no autorización para dibujarlo sin sustento.

## 4. Preguntas abiertas y evidencia para desbloquearlas

Registro para revisión posterior; no se solicitan respuestas simultáneas ni se detiene la traducción por datos que pueden declararse pendientes. Estas preguntas no implican opciones científicas aprobadas.

| ID | Pregunta concreta pendiente | Evidencia o decisión necesaria |
|:--|:--|:--|
| P1 | ¿Cuál es la denominación legal de la institución que titula y la sede de presentación? | Nombre/logo autorizado, ciudad/país, modalidad y grado oficial, fecha de presentación. No se inventan por usar modelo ALSIE. |
| P2 | ¿Se valida para ALSIE la formulación editorial de objeto/campo de 1.3? | Confirmación del tesista y asesor, manteniendo distinción área de conocimiento–propuesta. |
| P3 | ¿Se autoriza armonizar los cinco objetivos del perfil en cuatro y explicitar la modelación teórica? | Reformulación científica aprobada y coherente; esta entrega no la ejecuta ni cambia matriz. |
| P4 | ¿Qué adaptación o evidencia distinta de los antecedentes incrementales podrá sostener el aporte? | E4/E5 completas, contraste de alternativas y evaluación; no una respuesta nominal que garantice novedad. |
| P5 | ¿Qué población de componentes o escenarios y qué unidades delimitará el diagnóstico? | Criterios de inclusión, selección, tamaño, justificación analítica o estadística pertinente. |
| P6 | ¿Qué estructura reconocida con autor se asumirá para formalizar la propuesta? | Decisión respaldada en productos científicos; no adopción automática de ADD o de un libro. |
| P7 | ¿Dispone del documento auxiliar *Resultados científicos*? | Documento institucional, necesario antes de suponer estructura detallada exigida. |
| P8 | ¿Dispone de *Normas de redacción del documento científico*? | Fuente oficial para resolver exigencias adicionales sin inferirlas. |
| P9 | ¿Dispone de la *Guía para la elaboración del IFI* de formato? | Confirmar si es documento independiente de la guía de contenido disponible y aportar versión oficial. |
| P10 | ¿Qué respaldo institucional confirma las reglas HU-FEC-01/HU-FEC-02? | Documento o confirmación responsable; no volver a preguntar semántica de fecha ni zona horaria ya confirmadas. |
| P11 | ¿Qué registros intermedios acreditan la caracterización previa declarada? | Versiones/ejecuciones fechadas; cualquier reconstrucción posterior debe rotularse como tal. |
| P12 | ¿Qué alcance y autorización tendrá la revisión independiente y el uso de evidencias? | Consentimiento DNGP, instrumento, rol del revisor y registros; disponibilidad no es participación. |

La transición de formulario/almacenamiento, elegibilidad de tareas modificadas, integración y criterios de suficiencia son cuestiones de investigación aún pendientes; no se resuelven mediante edición del IFI.

## 5. Consultas bibliográficas y controles

- La referencia de Abbasi et al. conserva **[por verificar]** para numeración editorial y texto completo pendiente; las afirmaciones se limitan al resumen registrado.
- Bagheri-Galle, F., Parsa, S., & Zakeri, M. (2025). A systematic literature review on transformation for testability techniques in software systems. *Information and Software Technology, 185*, Article 107788. https://doi.org/10.1016/j.infsof.2025.107788 — consulta pendiente, contenido **[por verificar]**, no fuente de resultados del IFI.
- Literatura reciente sobre deuda técnica arquitectónica, refactorización de monolitos/MVC y caracterización: **[por verificar]**, sin autores ni conclusiones inventados.
- Las once referencias del IFI tienen cita y las citas autor–año tienen referencia. Los archivos internos constituyen procedencia documental, no publicaciones científicas externas ficticias. El fundamento de forma son las dos normas locales, identificadas por ruta, sin atribuirles autoría o datos editoriales no disponibles.
- Tensión formal: la guía local menciona lugar editorial, pero se aplica APA 7 y no se añade ciudad de edición. Paginación, fuente tipográfica, proporción de introducción y conversión de Mermaid permanecen pendientes de comprobación externa.

## 6. Estado de entrega y restauración

Se entregan únicamente los tres Markdown de avance. No se sobrescribe `IFI_ALSIE.md` ni se genera PDF. No se cambian estados, decisiones científicas ni matriz de `tesis_ds/`. La autoevaluación conserva incumplimientos y no constituye aprobación docente.

La excepción exige retirar, tras esta entrega, únicamente los bloques delimitados `TEMP-ALSIE-2026-10-22` en `AGENTS.md`, ambos agentes y `README.md`, conservando este mapa, los otros productos y el registro histórico del estado. El reinicio posterior de OpenCode corresponde al usuario; no se presume realizado. Esta entrega permanece como antecedente provisional y no autoriza futuras traducciones anticipadas.

**Registro de cierre del 22 de octubre de 2026:** generados y revisados los tres Markdown, se retiraron únicamente esos cuatro bloques. Los cuatro archivos de instrucciones quedaron sin diferencias frente a su versión ordinaria en Git; se conservaron las notas históricas preexistentes de `00_estado.md` sin editarlas. El reinicio de OpenCode y la conversión externa siguen pendientes. Se comprobó presencia de los catorce apartados, resumen de 223 palabras, 118 indicadores individuales y diez relaciones esenciales; las comprobaciones de diferencias no informaron errores de espacios. No se ejecutaron pruebas nuevas de SIGPP ni se generaron otros formatos.
