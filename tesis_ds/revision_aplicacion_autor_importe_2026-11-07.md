# Revisión de la aplicación del autor: decisión de importe

> **Aclaración posterior del autor:** confirma que revisó el material pendiente y olvidó actualizar el estado; solicita que lo actualice la asesoría. Se incorpora su confirmación en el registro original sin atribuirla a un momento anterior. Queda resuelta la diferencia documental sobre revisión personal de pruebas/registro, no la suficiencia global de E8 ni la comprensión mediante examen independiente. Las observaciones iniciales se conservan abajo como secuencia de revisión.

## 1. Recepción y alcance

El tesista informa que terminó la actividad y produjo un ejemplo de decisiones para presentación y posible inclusión en la tesis. Se revisan `docs/registro-metodo-importe-autor.md`, `docs/ejemplo-importe-autor-para-diapositivas.md`, el servicio modificado, la prueba nueva y la diferencia respecto de `7ef29a4f438e5d2474d39b67f530cb940c922e76`. Los documentos sitúan la actividad el 7 de noviembre de 2026 y aclaran que P1 fue explorado el día anterior y registrado después. No se atribuye registro contemporáneo a esa entrada inicial.

La rama es `eval/metodo-mr1-importe-autor`; hay un servicio modificado y cuatro archivos nuevos sin commit: las dos guías, el ejemplo y la prueba. No se alteran los originales ni se ejecuta una nueva transformación durante la revisión. El ejecutor es el autor del método y del sistema, con producción sustantiva de código, pruebas y documentación por IA; no es una evaluación independiente ni otro sistema.

## 2. Intervención inspeccionada

Se conserva la clase de servicio y su interfaz pública. `topeCertificacion()` pasa a coordinar lectura del disponible, cálculo del total y dos comprobaciones mediante cuatro métodos privados nuevos. `create()` reutiliza el cálculo de `totalCertificacion()` en vez de repetir la multiplicación. La cláusula redundante de total positivo se retira de la comprobación de exceso y se conserva como comprobación previa separada; los cinco casos examinados no presentan discrepancias.

El cambio es refactorización interna localizada en un servicio existente, no creación de una nueva frontera arquitectónica entre capas. No se impone otra clase como condición de aplicación del método. Su interés para el estudio es mostrar una decisión proporcional y la revisión de fronteras de observación e intervención, sin presentar la descomposición de métodos privados como transformación arquitectónica completa del subcircuito.

## 3. Comprobaciones reproducidas por la asesoría

Se inspecciona la nueva prueba: invoca `CreateCertificacionService::create()` con dobles de sus siete colaboradores y datos ficticios. Antes de la batería se comprueba que `RESUMEN_TEST_PG_DSN` sigue sin configurar, sin revelar credenciales. No se ejecutan procedimientos de persistencia real ni se configuran conexiones adicionales. La revisión estática y esa ausencia no constituyen aislamiento técnico completo de red.

| Comprobación | Resultado reproducido | Alcance |
|:--|:--|:--|
| Prueba de importe | 5 pruebas, 25 aserciones, satisfactorias. | A01–A05 en el consumidor con dobles. |
| `make test` | 164 pruebas, 285 aserciones, 1 omitida, sin fallos o errores informados. | Batería actual, no persistencia real; omisión no satisfactoria. |
| `php bin/console lint:container` en `sigpp-app` | Código de salida 0, sin salida. | Validación de configuración, no comportamiento con base de datos. |
| Diferencia Git | Un servicio, +24/−5; nuevos documentos y prueba sin commit. | No modificaciones realizadas por esta revisión. |

La línea inicial de la asesoría fue 159 pruebas, 260 aserciones y 1 omitida. El incremento de cinco pruebas y 25 aserciones corresponde a los casos nuevos, no a una mejora medida de testabilidad, mantenibilidad o esfuerzo. `debug:container` consta en el registro del autor y no se repite en esta revisión; no se atribuye al autor la validación adicional reproducida aquí.

## 4. Evidencia por criterio

| Criterio aceptado | Evidencia inspeccionada y reproducida | Límite |
|:--|:--|:--|
| A01, total 50/disponible 100 | Devuelve certificación con total esperado; invoca guardado y seguimiento una vez, sin autorización o carga. | Interacciones con dobles, no creación persistida. |
| A02, total 100/disponible 100 | Mismas comprobaciones en el límite inclusivo. | No cubre todos los límites monetarios o condiciones restantes. |
| A03, total 101/disponible 100 | Excepción de importe con fragmento de mensaje de exceso; ninguna llamada a los cuatro efectos acordados. | No se comprueba todo el mensaje ni atomicidad real. |
| A04, total 0/disponible 100 | Excepción con mensaje esperado y ninguna llamada a esos efectos. | El mensaje «menor a 1» se conserva; el predicado observado sigue siendo no positivo. |
| A05, total −1/disponible 100 | Igual comprobación de rechazo previo a efectos. | No se extiende a toda entrada negativa o no numérica posible. |

El resultado anterior a la transformación (5/25, batería 164/285/1) y la comparación temporal de coexistencia (10/30, batería 169/290/1) constan en el registro del autor. La prueba temporal y `topeCertificacionOriginal()` fueron retirados; no están disponibles como archivos actuales para repetir esa comparación. El código inicial puede consultarse en Git y el ejemplo conserva fragmentos, pero esto no equivale a reejecución independiente de la secuencia histórica. La reproducción actual respalda el estado final, mientras el orden previo/coexistencia se sustenta en el registro de aplicación.

## 5. Pasos, decisiones y registro progresivo

| Paso | Respaldo y reserva |
|:--|:--|
| P1 | Frontera inicial identificada y decisión del autor de no crear clase; exploración del día anterior registrada después. |
| P2 | Caracterización a nivel de `create()` para observar efectos. Archivo permanente inspeccionado; ejecución previa relatada, final reproducida. |
| P3 | Datos pertinentes y dependencias controladas; se documenta después de P2, porque se prepararon en la prueba. No se presenta orden idealizado. |
| P4 | Ampliación de la intervención hasta `create()` para reutilizar el cálculo. Coexistencia temporal relatada, sin versión intermedia comprometida. |
| P5 | Comparación original/nueva relatada para A01–A05; estado final reproducido. No se generaliza equivalencia fuera de esos casos. |
| P6 | Vía anterior y prueba temporal retiradas; código actual y diferencia coherentes con la retirada declarada. |
| P7 | Pruebas del consumidor, batería y configuración en alcance aceptado; sin persistencia real, HTTP completo o concurrencia. La configuración no valida por sí sola comportamiento integrado. |
| P8 | Registro por pasos, criterios, decisiones, ayudas y límites. La discrepancia inicial sobre revisión personal de pruebas y entradas queda aclarada por confirmación posterior del autor e incorporada al registro original; no es una revisión independiente ni demuestra por sí sola comprensión completa. |

El material incorpora el suplemento de registro progresivo posterior a P02. Hay productos distribuidos por pasos y una consolidación posterior, pero no comparación equivalente de carga u omisiones frente a P01/P02. Por tanto, no se acredita que el suplemento reduzca esfuerzo o reconstrucción; la entrada P1 fue retrospectiva y P3 quedó registrada después de P2. No se repetirá la actividad para forzar un orden ideal.

## 6. Recuentos estructurales y escenarios añadidos después

Se reproduce el conteo de declaraciones activas de métodos: 14 antes y 18 después, con patrón anclado que excluye declaraciones comentadas. Se reproducen 16 y 21 líneas con llamadas internas mediante el patrón textual, que incluye algunas líneas comentadas presentes en ambos estados. Estas son descripciones de estructura, no mediciones semánticas exhaustivas de complejidad. La multiplicación cantidad por precio pasa de dos lugares de implementación a uno; sus usos son dos.

Los escenarios hipotéticos de cambiar fórmula, origen del disponible o mensajes se añadieron tras construir y conocer el resultado. No fueron ejecutados y no son criterios prospectivos de éxito; se documentan como análisis estructural exploratorio posterior. El descenso de dos a un lugar para modificar la fórmula respalda eliminación de esa duplicación, no una reducción medida de costo, riesgo o tiempo de cambio. Los otros tres escenarios conservan un punto de edición cada uno.

## 7. Uso del ejemplo en tesis y presentación

El archivo puede utilizarse como material explicativo de una aplicación documentada, una vez revisado por el autor y adecuadas sus afirmaciones. No sustituye el registro, las pruebas ni las fuentes de evidencia. Su mejor hilo expositivo es: frontera de decisión en `topeCertificacion()` → observación en `create()` para comprobar efectos → intervención ampliada para reutilizar el cálculo → conservación en cinco casos, con límites. Esa evolución es más informativa que presentar todo el código o contar métodos.

Antes de incorporarlo se requieren estas adecuaciones, sin alterar silenciosamente el original:

- Usar **SIGPP** como nombre del sistema; `sipoa4` identifica la carpeta del proyecto, no otro caso.
- Sustituir «antes de cualquier efecto» por «antes de las llamadas a los cuatro colaboradores de efectos acordados, comprobadas con dobles» cuando se informe el resultado de pruebas.
- Presentar la nueva clase como alternativa descartada por el autor, no como una opción que necesariamente habría tenido que conocer toda la cadena de entidades. Podría diseñarse con datos ya obtenidos; esa necesidad no queda demostrada por descartar la clase.
- Denominar los escenarios de cambio «análisis estructural exploratorio posterior», no evaluación prospectiva de modificabilidad.
- Evitar convertir «más métodos, mejor mantenibilidad» en resultado empírico. La justificación es de diseño y tiene una contrapartida de más conexiones internas.
- Diferenciar expresiones del autor, producción de IA, evidencia reproducida por revisión y resultados solo relatados de estados intermedios.
- Aclarar la revisión personal de pruebas y registros y cotejar las citas textuales antes de reproducirlas.

No se exige convertir las dieciséis secciones del archivo en dieciséis diapositivas. Para una exposición breve puede resumirse en una lámina de decisiones/fronteras y otra de evidencia/límites; el desarrollo completo puede servir de anexo explicativo Markdown, adaptado y vinculado a esta revisión. No se genera aquí una presentación ni se incorpora el original como anexo final sin esas adecuaciones.

## 8. Fuente de diseño invocada y verificación

El autor fundamenta su preferencia por métodos de responsabilidad acotada en Metz (2019). La ficha editorial primaria verifica autora, título, segunda edición, editorial e ISBN, e informa publicación comercial el 22 de agosto de 2018 y copyright 2019. Se conserva 2019 como identificación del ejemplar declarado por el tesista; no se confunde copyright con fecha comercial ni se modifica retrospectivamente su referencia. Las citas de las páginas 29–32 se declaran cotejadas con su PDF en el material recibido, pero ese ejemplar no fue inspeccionado en esta revisión; su literalidad queda **[por verificar por esta asesoría]** antes de reutilizarlas como citas directas.

Metz, S. (2019). *Practical object-oriented design: An agile primer using Ruby* (2nd ed.). Addison-Wesley Professional. https://www.informit.com/store/practical-object-oriented-design-an-agile-primer-using-9780134456478

## 9. Dictamen preliminar y siguiente paso

Hay evidencia favorable del estado final para A01–A05 y de la aplicación del método a una segunda decisión del mismo sistema, por el autor y con asistencia sustantiva de IA. La intervención elegida no impone una nueva clase, revisa fronteras y elimina una duplicación concreta. No demuestra transferencia a otro sistema o practicante, ahorro, superioridad, mantenibilidad empírica, cumplimiento de los indicadores temporales ni suficiencia global de maestría. Tampoco convierte automáticamente la evolución de fronteras en principio original validado.

La revisión personal del archivo de pruebas y las entradas queda confirmada posteriormente por el autor; recepción documental aclarada sin repetir actividad o reaprobar criterios/alcance. Permanecen las adecuaciones del ejemplo y la consolidación del dictamen del episodio, antes de relacionar este aporte con E9/E10 sin ampliar las afirmaciones más allá de la evidencia. La confirmación no modifica los resultados técnicos ni cierra E8 por sí sola.
