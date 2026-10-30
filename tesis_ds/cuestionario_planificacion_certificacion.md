# Validación funcional de fechas y habilitación de certificaciones en SIGPP

**Dirigido a:** Planificador Nacional, referente funcional de SIGPP.
**Solicitante:** Mario Arturo Uriarte Marin.
**Programa:** Maestría en Ingeniería de Software.
**Versión del cuestionario:** 29 de octubre de 2026.

## Presentación

A la persona que ejerce el cargo de Planificador Nacional:

Como parte de mi tesis, necesito confirmar las reglas funcionales sobre las fechas y la habilitación del registro de certificaciones en SIGPP. El propósito es establecer qué comportamiento debe cumplir el sistema antes de realizar cambios y pruebas; no se evalúa su desempeño ni se le solicita revisar aspectos técnicos de programación. Los ejemplos utilizan datos ficticios y no requieren información de certificaciones reales. Si alguna situación no está definida, necesita consulta o corresponde a una mejora futura, por favor indíquelo en lugar de asumir una respuesta.

## 1. Autorización y datos de la respuesta

**Fecha en que responde:** _29 de octubre del 2026

**Cargo o función desde la que responde:**  Planificador Nacional

**¿Autoriza que sus respuestas se conserven y utilicen como evidencia académica de esta tesis?**

- [ X] Sí.
- [ ] No.
- [ ] Necesito aclarar las condiciones antes de autorizar.

Si no autoriza o necesita aclaraciones, puede detener aquí el llenado y comunicarlo al solicitante. Esta autorización no sustituye otras autorizaciones institucionales que correspondan.

**Si autoriza, ¿cómo permite que se le identifique en el documento académico?**

- [ ] Por mi nombre y cargo.
- [X ] Únicamente por mi cargo, sin publicar mi nombre.
- [ ] Otra condición: ____________________

**Restricciones sobre el uso o difusión de sus respuestas, si corresponde:**

Respuesta: ____________________________________________________________

## 2. Instrucciones para resolver los casos

En cada caso, marque **admitir**, **rechazar** o **requiere aclaración**, y explique brevemente el motivo. Responda según el comportamiento institucional que corresponde, no según lo que actualmente permita la pantalla. Si su respuesta describe un cambio propuesto y no una regla vigente, señálelo expresamente. Puede corregir los supuestos de cualquier caso si no representan la práctica institucional.

Para estos ejemplos:

- **Día de registro:** día en que el usuario intenta registrar la certificación.
- **Fecha documental:** fecha que se solicita consignar en la certificación.
- **Gestión de la tarea:** año al que pertenece la tarea.
- **Habilitación ordinaria:** apertura habitual para registrar certificaciones.
- **Habilitación extraordinaria:** apertura específica para registrar certificaciones de una gestión anterior; su alcance es parte de lo que se desea confirmar.

Suponga que el usuario tiene permiso, la tarea es elegible y existe saldo suficiente. Se consulta únicamente la decisión por fecha y habilitación temporal; admitir en estos ejemplos no significa omitir los demás controles. En los casos 1 a 6, la habilitación ordinaria está vigente.

### Caso 1. Fecha del mismo día

El intento se realiza el **15/06/2026**, para una tarea de la gestión **2026**, y se solicita fecha documental **15/06/2026**.

Decisión: [ X ] Admitir  [ ] Rechazar  [ ] Requiere aclaración

Motivo o condición: ___________________________________________________

### Caso 2. Último día del mes anterior

El intento se realiza el **15/06/2026**, para una tarea de la gestión **2026**, y se solicita fecha documental **31/05/2026**.

Decisión: [  ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición:  solo se permite del dia del mes anterior hasta dia 8 del mes actual

### Caso 3. Día anterior al registro

El intento se realiza el **15/06/2026**, para una tarea de la gestión **2026**, y se solicita fecha documental **14/06/2026**.

Decisión: [ ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición:  Solo certificaciones para este dia

### Caso 4. Fecha futura

El intento se realiza el **15/06/2026**, para una tarea de la gestión **2026**, y se solicita fecha documental **16/06/2026**.

Decisión: [ ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición: solo certificaciones para este dia

### Caso 5. Cierre de febrero en año bisiesto

El intento se realiza el **01/03/2028**, para una tarea de la gestión **2028**, y se solicita fecha documental **29/02/2028**.

Decisión: [ X ] Admitir  [ ] Rechazar  [ ] Requiere aclaración

Motivo o condición: es ultimo dia del anterior mes

### Caso 6. Fecha de otra gestión sin habilitación extraordinaria

El intento se realiza el **10/01/2026**, para una tarea de la gestión **2026**, y se solicita fecha documental **31/12/2025**. No existe habilitación extraordinaria.

Decisión: [ ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición:  la tarea es del 2026, no puede certificarse con fecha del 2025

### Caso 7. Registro extraordinario en agosto con fecha 29 de diciembre

El intento se realiza el **20/08/2026**, para una tarea de la gestión **2025**, y se solicita fecha documental **29/12/2025**. Existe habilitación extraordinaria vigente para **2025**, pero la ordinaria está cerrada.

Decisión: [ ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición: por lo general las certificaciones del año pasado se cierran hasta el primer trimestre del año en curso

### Caso 8. Registro extraordinario en agosto con fecha 31 de diciembre

El intento se realiza el **20/08/2026**, para una tarea de la gestión **2025**, y se solicita fecha documental **31/12/2025**. Existe habilitación extraordinaria vigente para **2025**, pero la ordinaria está cerrada.

Decisión: [ X ] Admitir  [ ] Rechazar  [ ] Requiere aclaración

Motivo o condición: tendría que ser algo realmente extraordinario, que aun no paso que después del primer trimestre se tenga que introducir algo asi, talvez para igualar balances, pero no sucedió

### Caso 9. Registro extraordinario con fecha 30 de diciembre

El intento se realiza el **20/08/2026**, para una tarea de la gestión **2025**, y se solicita fecha documental **30/12/2025**. Existe habilitación extraordinaria vigente para **2025**, pero la ordinaria está cerrada.

Decisión: [ X ] Admitir  [ ] Rechazar  [ ] Requiere aclaración

Motivo o condición: tendría que ser algo realmente extraordinario, que aun no paso que después del primer trimestre se tenga que introducir algo asi, talvez para igualar balances, pero no sucedió

### Caso 10. Apertura ordinaria vigente y extraordinaria vencida

El intento se realiza el **20/08/2026**, para una tarea de la gestión **2025**, y se solicita fecha documental **31/12/2025**. La habilitación ordinaria está abierta, pero la extraordinaria para **2025** ha vencido.

Decisión: [  ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición: Deberia haber una habilitacion extraordinaria, parametro sistema en certificaciones se habre de enero a diciembre, entonces estaria cerrada

### Caso 11. Habilitación extraordinaria de una gestión distinta

El intento se realiza el **20/08/2026**, para una tarea de la gestión **2025**, y se solicita fecha documental **31/12/2025**. La habilitación ordinaria está cerrada y solo existe una extraordinaria vigente para **2024**.

Decisión: [ ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición: No es la gestion correcta

### Caso 12. Tarea de una gestión anterior a la inmediatamente precedente

El intento se realiza el **20/08/2026**, para una tarea de la gestión **2024**, y se solicita fecha documental **31/12/2024**. Existe habilitación extraordinaria vigente para **2024**, pero la ordinaria está cerrada.

Decisión: [ ] Admitir  [ X ] Rechazar  [ ] Requiere aclaración

Motivo o condición: Año muy antiguo

## 3. Aclaraciones de las reglas

### Pregunta 1. Significado de la fecha

¿Qué representa institucionalmente la fecha documental? ¿La hora tiene algún significado para admitir o rechazar el documento? ¿Qué referencia local debe utilizar el sistema para determinar el día en que se registra?

Respuesta: la hora no tiene sentido, la fecha documental representa el dia que se esta solicitando la certificacion, representa que para ese dia existe recursos disponibles

### Pregunta 2. Autorización extraordinaria

¿Quién puede disponer una habilitación extraordinaria, para qué gestiones y en qué momentos del año? Distinga lo que ya está autorizado de lo que se desea incorporar como cambio.

Respuesta: Lo solicita un unidad de produccion, y lo analizan El area de presupuestos y el area de planificacion, se habre por medio de solicitud por jefatura de planificacion

### Pregunta 3. Inicio y fin de una habilitación

¿Qué debe ocurrir exactamente al llegar al inicio y al fin del período habilitado? Si existe una hora límite, indíquela; si no está definido, señálelo.

Respuesta: Al llegar al inicio el operador ingresa las certificaciones, al final no deberia aparecerle el boton de crear certificaciones.

### Pregunta 4. Consecuencias del rechazo

Cuando corresponde rechazar por fecha o habilitación, ¿qué debe informarse al usuario y qué registros o archivos, si alguno, deben conservarse? Distinga la certificación de un eventual registro de intento rechazado.

Respuesta: Por lo general si no esta habilitado el parametro de certificacion, el usuario no puede ni ingresar al formulario

### Pregunta 5. Programación de la tarea y excepciones

¿La programación trimestral de la tarea limita las fechas en las que se puede certificar, o cumple otra función? ¿Qué excepciones relevantes no están representadas en los casos anteriores?

Respuesta: la programacion trimestral no limita, se utiliza para distribuir los recursos para ser evaluados, una certificacion a inicios de año podria gastar todo los que esta distribuido en 4 trimestres, la planificacion es dinamica y la ejecución tambien

### Pregunta 6. Respaldo y vigencia

¿Qué documentos, instrucciones o decisiones respaldan estas reglas? Indique su denominación y fecha si los conoce, sin adjuntar información sensible. Si alguna respuesta corresponde a una decisión nueva o a una propuesta todavía no aprobada, identifíquela.

Respuesta: RE-SPO institucional aprobado por el ministerio de economia y finanzas publicas, circulares internos sobre la POA de la gestion actual

## 4. Observaciones finales

¿Desea corregir algún supuesto del cuestionario o añadir una condición que debamos considerar?

Respuesta: Ninguna

Gracias por su colaboración. Una vez recibidas sus respuestas, le remitiré una síntesis de las reglas para que confirme o corrija mi interpretación antes de utilizarlas como especificación funcional. Completar este cuestionario no implica aprobar una solución técnica ni validar el método de refactorización de la tesis.
