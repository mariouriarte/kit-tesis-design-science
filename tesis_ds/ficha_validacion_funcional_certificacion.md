# Ficha de validación funcional de fechas de certificación en SIGPP

**Versión:** 1, preparada el 29 de octubre de 2026.  
**Estado:** instrumento preparado; no aplicado y sin respuestas recibidas.  
**Tesista:** Mario Arturo Uriarte Marin.  
**Referente funcional propuesta:** Marlen Terrazas, planificadora. Según declaración del tesista, tiene atribución para aprobar estas reglas funcionales; esta ficha no acredita un nombramiento formal.

## Propósito e instrucciones para la participante

Se solicita precisar cuándo corresponde permitir o rechazar una certificación respecto de su fecha y habilitación temporal. No se evalúa su desempeño ni se solicita valorar la arquitectura del sistema. Los ejemplos son ficticios y no requieren datos reales de certificaciones; puede indicar que una situación no está definida o que requiere consulta. Sus respuestas permitirán corregir la especificación antes de modificar el sistema, sin atribuir automáticamente estas reglas a una norma publicada.

Para cada escenario indique **admitir, rechazar o requiere aclaración**, junto con el motivo o condición faltante. Salvo indicación contraria, suponga usuario con permiso, tarea elegible y saldo suficiente; por ello, admitir respecto de la fecha no significa dispensar los demás controles. «Día de registro» significa el día en que se intenta registrar, mientras que «fecha documental» es el día que figurará en la certificación. Se solicita responder primero los escenarios y después revisar la especificación existente, para reducir la inducción de respuestas.

## 1. Aceptación de participación y registro

Antes de aplicar la ficha, el tesista solicitará autorización para conservar las respuestas y utilizarlas como evidencia académica. Se registrarán la fecha efectiva, el medio de respuesta y la preferencia por identificación nominal o únicamente por cargo; preparar este documento no equivale a contar con esa autorización. No se realizará grabación sin permiso específico ni se incorporarán contactos, credenciales o datos sensibles. La autorización individual no sustituye otras autorizaciones institucionales que correspondan.

## 2. Escenarios para determinar el resultado esperado

En C01–C06 existe habilitación ordinaria vigente. En C07–C12 la habilitación extraordinaria, cuando se menciona, corresponde a la gestión indicada y está vigente en el día del intento. No se presupone que estas capacidades estén implementadas correctamente en SIGPP.

| ID | Día de registro | Gestión de tarea | Fecha documental solicitada | Condición temporal adicional |
|:--|:--|:--|:--|:--|
| C01 | 15/06/2026 | 2026 | 15/06/2026 | Ninguna. |
| C02 | 15/06/2026 | 2026 | 31/05/2026 | Ninguna. |
| C03 | 15/06/2026 | 2026 | 14/06/2026 | Ninguna. |
| C04 | 15/06/2026 | 2026 | 16/06/2026 | Ninguna. |
| C05 | 01/03/2028 | 2028 | 29/02/2028 | Cierre del mes anterior en año bisiesto. |
| C06 | 10/01/2026 | 2026 | 31/12/2025 | No existe habilitación extraordinaria. |
| C07 | 20/08/2026 | 2025 | 29/12/2025 | Extraordinaria para 2025 vigente; ordinaria cerrada. |
| C08 | 20/08/2026 | 2025 | 31/12/2025 | Extraordinaria para 2025 vigente; ordinaria cerrada. |
| C09 | 20/08/2026 | 2025 | 30/12/2025 | Extraordinaria para 2025 vigente; ordinaria cerrada. |
| C10 | 20/08/2026 | 2025 | 31/12/2025 | Ordinaria abierta; extraordinaria para 2025 vencida. |
| C11 | 20/08/2026 | 2025 | 31/12/2025 | Ordinaria cerrada; extraordinaria vigente solo para 2024. |
| C12 | 20/08/2026 | 2024 | 31/12/2024 | Extraordinaria para 2024 vigente; ordinaria cerrada. |

Las respuestas se conservarán por identificador de caso, decisión y explicación. **Actualmente no existen respuestas registradas**; no se completan con las expectativas del tesista.

## 3. Preguntas de aclaración

1. ¿Qué significa institucionalmente la fecha documental y qué papel tiene la hora, si alguno? ¿Qué referencia local debe utilizarse para determinar el día de registro?
2. ¿Quién puede disponer una habilitación extraordinaria, para qué gestiones y en qué momentos del año? Distinga una práctica ya autorizada de una capacidad que se desea incorporar.
3. ¿Cómo se determina el inicio y fin de una habilitación? Describa qué ocurre exactamente en sus límites y, si no está definido, indíquelo.
4. Si la fecha o habilitación obliga a rechazar, ¿qué debe informarse al usuario y qué registros o archivos, si alguno, deben conservarse? Distinga el documento de certificación de un eventual registro de intento rechazado.
5. ¿La programación trimestral de la tarea restringe las fechas admisibles o cumple otra función? ¿Qué excepciones relevantes no representan los casos anteriores?
6. ¿Qué documentos, instrucciones o decisiones respaldan estas respuestas? Indique cuáles describen reglas vigentes y cuáles requieren una aprobación o cambio nuevo; la ausencia de documento se registrará sin inventar una fuente normativa.

## 4. Revisión y confirmación de la síntesis

Después de recibir las respuestas, el tesista elaborará una síntesis con cada regla, casos asociados, fuente y condición de vigente, cambio aprobado o pendiente. La remitirá a la participante para confirmar o corregir su interpretación, conservando el mensaje o acta correspondiente con acceso apropiado. Las discrepancias frente a `reglas_fecha_certificacion.md` se documentarán con fecha y motivo, sin sobrescribir silenciosamente la formulación anterior. Hasta recibir esa confirmación, el resultado seguirá siendo una interpretación pendiente de ratificación.

## 5. Uso de la evidencia y límites

La ficha alimentará la definición de resultados esperados de I01 y de efectos permitidos/prohibidos de I02 en `06_diagnostico.md`. No mide todavía el comportamiento de SIGPP, el esfuerzo de prueba o la modificabilidad, ni demuestra la validez del método de refactorización. Marlen interviene aquí como fuente funcional; no se la presenta automáticamente como evaluadora técnica independiente ni como única evaluadora de la tesis. No se incluyen referencias bibliográficas porque este instrumento recoge conocimiento del contexto y no formula afirmaciones sobre la literatura.
