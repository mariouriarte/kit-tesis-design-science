# Ampliación del diagnóstico ordinario de pantalla — O01 a O05

## 1. Alcance y condiciones previas

El tesista acepta O01–O06 mediante «aceptamos», después de fijar sus datos y expectativas en `matriz_escenarios_temporales_e6.md`. Se amplía el instrumento aislado anterior a los cinco escenarios del mismo año que la función `verificarDiaAnteriorMes()` puede observar. **O06 no se ejecuta aquí**: la función no recibe la tarea ni su gestión, por lo que un resultado parecido no demostraría esa propiedad. La comprobación tampoco observa los efectos del servicio PHP requeridos por I02.

El protocolo antecede a esta ampliación del ensayo. Se conserva extracción literal de código de la plantilla, contexto temporal por caso, dobles de aviso/campo y horario `America/La_Paz` del proceso; no se modifica el reloj del equipo o producción. Los casos O02/O03 repiten el diagnóstico anterior dentro de este conjunto ampliado, no constituyen observaciones independientes nuevas del mismo fenómeno. El control técnico se mantiene fuera del denominador de casos ordinarios.

Referencia comprobada antes de ejecutar: SIGPP en `feature/propuesta-tesis`, `7c0bca084b05c462137fd62c24e6b025bb09a12c`, sin cambios locales informados ni divergencia frente a la referencia remota local. Intérprete: Node.js `v26.13.0`. Se requiere que las huellas de plantilla y fragmento coincidan con la comprobación anterior; si difieren, se detiene esta reproducción y se registra la nueva referencia antes de continuar. No se ejecutarán PHP, navegador, HTTP o persistencia.

## 2. Expectativas anteriores a la ejecución

Todos los instantes se controlan a las 12:00 de sus respectivos días en Bolivia; ello fija un contexto reproducible, no valida todos los horarios. Permisos, habilitación, elegibilidad, saldo y tarea 2026 son supuestos del escenario, no verificaciones del fragmento. El campo inicial conserva la representación de la fecha documental correspondiente. La correspondencia se observa mediante ausencia de aviso/cambio o aviso de error más vaciado, conforme a los mecanismos del código actual.

| ID | Día del intento | Fecha documental | Observable esperado |
|:--|:--|:--|:--|
| O01 | 08/06/2026 | 08/06/2026 | Sin rechazo local. |
| O02 | 08/06/2026 | 31/05/2026 | Sin rechazo local. |
| O03 | 09/06/2026 | 31/05/2026 | Rechazo local. |
| O04 | 15/06/2026 | 14/06/2026 | Rechazo local. |
| O05 | 15/06/2026 | 16/06/2026 | Rechazo local. |
| CTRL | 08/06/2026 | 30/05/2026 | Rechazo local; control del instrumento, no caso ordinario adicional. |

Se conservarán discrepancias y errores. Una excepción de preparación no se convertirá en rechazo correcto. Un caso que no emite aviso y conserva el campo solo produce la observación «sin rechazo local», no «certificación creada o autorizada». No se computará porcentaje global de I01/I02 con estos resultados.

## 3. Procedimiento y reproducibilidad

Se reutiliza el programa de la sección 7 de `comprobacion_cierre_mensual_e6.md`, ampliando únicamente la lista de casos para O01–O05 y control. Antes de ejecutar la función se comprobarán las huellas SHA-256 de plantilla y fragmento contra los valores registrados en el ensayo anterior. Cada caso tiene contexto y campo independientes; se conservarán fecha de ejecución, revisión y salida. No se guardan archivos de prueba dentro de SIGPP.

El asistente prepara, ejecuta y documenta esta ampliación. No se obtiene una línea base humana I03, ni se repite el trabajo como primera preparación independiente. La salida distinta de cero por discrepancia es parte de la evidencia, no una instrucción para cambiar producción hasta hacerla desaparecer. E6 permanece abierta.

## 4. Registro previo

**Corte anterior a la ejecución:** expectativas y protocolo fijados, sin resultados de la ampliación en ese momento. Se conserva esta secuencia y se incorpora el resultado posterior en la sección 5, sin sustituir el primer ensayo ni atribuir al pasado un conjunto fijado después.

## 5. Resultado de la ampliación

Ejecución iniciada a `2026-11-03T04:15:40.892Z` y finalizada a `2026-11-03T04:15:40.898Z`, aproximadamente las **00:15:40 del 3 de noviembre de 2026 en Bolivia**. Node informó `v26.13.0` y `America/La_Paz`; la revisión y las dos huellas coincidieron con el ensayo anterior. Las marcas corresponden al proceso automatizado, no preparación del instrumento, esfuerzo humano I03 o comparación de rendimiento. No hubo errores de instrumento informados en los seis contextos ejecutados.

| Caso | Observación del fragmento | Correspondencia |
|:--|:--|:--|
| O01 | Conserva `08/06/2026`, sin avisos. | Sí. |
| O02 | Conserva `31/05/2026`, sin avisos. | Sí. |
| O03 | Conserva `31/05/2026`, sin avisos. | No: no activa el rechazo requerido al día 9. |
| O04 | Campo vacío y aviso `Fecha incorrecta`, tipo `error`. | Sí. |
| O05 | Campo vacío y aviso `Fecha incorrecta`, tipo `error`. | Sí. |
| CTRL | Campo vacío y aviso `Fecha incorrecta`, tipo `error`. | Sí como control, no se suma a O01–O05. |

Son cuatro concordancias sobre cinco casos ordinarios del fragmento, con una discrepancia conservada. O06 no fue ejecutado y no cuenta como acierto. No se informa este resultado como I01 completo de O01–O06, cumplimiento del criterio del 100 % o validación de servidor. La salida del programa fue 1 por O03, sin reparar código o retirar ese escenario.

Los resultados confirman el diagnóstico previo y amplían su cobertura local a mismo día, día anterior y fecha futura. No se acumulan O02/O03 del ensayo anterior como observaciones independientes para inflar el denominador. Tampoco se cuenta el control como otro caso de eficacia. La ausencia de efectos PHP, persistencia y archivos de I02 continúa sin comprobarse, e I03 no obtiene minutos humanos del trabajo del asistente.

### Identidad y ausencia de cambios

- Revisión antes, informada por instrumento y después: `7c0bca084b05c462137fd62c24e6b025bb09a12c`.
- Plantilla SHA-256: `6f0000418c17a48b13584a64c772f30dc46233964b26d38fe922b11fe5cdc864`.
- Fragmento SHA-256: `d1d14948a7de977066eee70f7538c9617df723df9c1ad5f9d7ade4e937f9cf9c`.
- Git posterior no informó cambios y la comparación de `src`, `tests` y plantilla contra `HEAD` terminó sin diferencias.

No se ejecutó la aplicación web, PHP, base de datos o almacenamiento real. La creación del contexto JavaScript y sus dobles no modificó relojes externos ni archivos de SIGPP. Las huellas delimitan el texto examinado, no certifican un despliegue de producción. El consumidor de servidor y sus efectos requieren otros instrumentos, no la extrapolación de estos resultados.

## 6. Comando ejecutado para reproducción

Este comando reproduce la ampliación con los casos y protección de identidad de fuente utilizados. Si la plantilla cambia, las comprobaciones de huella detienen el ensayo; una ejecución sobre otro código debe registrarse como otra referencia, no hacerse pasar por esta línea de evidencia. El código 1 conserva el resultado discrepante mientras no exista una intervención posterior autorizada y documentada. No escribe archivos de pruebas en SIGPP.

```bash
TZ=America/La_Paz node -e 'const fs = require("node:fs");
const vm = require("node:vm");
const crypto = require("node:crypto");
const cp = require("node:child_process");
const repo = "/home/mario/dev/sf_projects/sipoa4";
const path = repo + "/templates/poa/emitir_certificacion/new.html.twig";
const RealDate = Date;
const started = new RealDate().toISOString();
const template = fs.readFileSync(path, "utf8");
const start = template.indexOf("function verificarDiaAnteriorMes(fecha)");
const end = template.indexOf("function verificarDiaAnteriorMesYAnteriorGestion(fecha)", start + 1);
if (start < 0 || end <= start) throw new Error("No se localiza el fragmento original esperado");
const fragment = template.slice(start, end).trim();
const sha = text => crypto.createHash("sha256").update(text).digest("hex");
if (sha(template) !== "6f0000418c17a48b13584a64c772f30dc46233964b26d38fe922b11fe5cdc864" || sha(fragment) !== "d1d14948a7de977066eee70f7538c9617df723df9c1ad5f9d7ade4e937f9cf9c") throw new Error("La fuente difiere del diagnostico anterior");
const cases = [
 {id:"O01", role:"ordinario", now:"2026-06-08T12:00:00-04:00", documentary:"2026-06-08", initial:"08/06/2026", expected:"sin_rechazo_local"},
 {id:"O02", role:"ordinario", now:"2026-06-08T12:00:00-04:00", documentary:"2026-05-31", initial:"31/05/2026", expected:"sin_rechazo_local"},
 {id:"O03", role:"ordinario", now:"2026-06-09T12:00:00-04:00", documentary:"2026-05-31", initial:"31/05/2026", expected:"rechazo_local"},
 {id:"O04", role:"ordinario", now:"2026-06-15T12:00:00-04:00", documentary:"2026-06-14", initial:"14/06/2026", expected:"rechazo_local"},
 {id:"O05", role:"ordinario", now:"2026-06-15T12:00:00-04:00", documentary:"2026-06-16", initial:"16/06/2026", expected:"rechazo_local"},
 {id:"CTRL", role:"control_instrumento", now:"2026-06-08T12:00:00-04:00", documentary:"2026-05-30", initial:"30/05/2026", expected:"rechazo_local"}
];
const results = cases.map(spec => {
 const fixed = RealDate.parse(spec.now);
 class FixedDate extends RealDate {
  constructor(...args) { super(...(args.length ? args : [fixed])); }
  static now() { return fixed; }
 }
 const field = {value:spec.initial};
 const notices = [];
 const context = vm.createContext({
  Date:FixedDate,
  document:{getElementById(id) {if(id !== "emitir_certificacion_fecha") throw new Error("Campo inesperado: " + id); return field;}},
  swal(args) {notices.push({title:args.title,type:args.type});}
 });
 let error = null;
 try {
  vm.runInContext(fragment, context, {timeout:1000});
  vm.runInContext("verificarDiaAnteriorMes(new Date(" + JSON.stringify(spec.documentary + "T12:00:00-04:00") + "));", context, {timeout:1000});
 } catch(e) { error = {name:e.name,message:e.message}; }
 let observed = "inconcluso";
 if(error) observed = "error_instrumento";
 else if(field.value === "" && notices.some(x => x.type === "error")) observed = "rechazo_local";
 else if(field.value === spec.initial && notices.length === 0) observed = "sin_rechazo_local";
 return {...spec,observed,field_final:field.value,notices,error,concordant:observed === spec.expected};
});
const ordinary = results.filter(x => x.role === "ordinario");
console.log(JSON.stringify({
 started_utc:started,finished_utc:new RealDate().toISOString(),node:process.version,
 timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,
 revision:cp.execFileSync("git",["-C",repo,"rev-parse","HEAD"],{encoding:"utf8"}).trim(),
 source:path,template_sha256:sha(template),fragment_sha256:sha(fragment),
 source_function:"verificarDiaAnteriorMes",results,
 summary:{ordinary_cases:ordinary.length,ordinary_concordant:ordinary.filter(x=>x.concordant).length,control_concordant:results.find(x=>x.id==="CTRL").concordant,O06:"no ejecutado en este instrumento",I02:"no observado en este instrumento",I03:"sin medicion humana"}
},null,2));
process.exitCode = results.every(x=>x.concordant) ? 0 : 1;'
```
