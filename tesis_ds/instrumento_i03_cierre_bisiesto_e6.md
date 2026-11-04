# Instrumento de cierre bisiesto para revisión de la fase B de I03

**Estado actualizado:** preparado después de A2 y revisado por el participante en B; ejecutado posteriormente por el asistente, sin modificar sus datos o expectativas. La versión previa de este documento fue el material de revisión y se conserva el mismo código. Los resultados están separados en `resultado_i03_cierre_bisiesto_e6.md` para el análisis C; no se atribuye al participante una conclusión o duración que aún no informó. La asistencia de generación y ejecución se registra aparte.

## Qué revisar con el cronómetro de B

1. **Datos:** el día del intento es 01/03/2028 en ambos casos; documentos 29/02/2028 y 28/02/2028. La gestión 2028 es supuesto del escenario, no una tarea consultada en SIGPP.
2. **Expectativas:** el 29 es el cierre mensual y no debe activar rechazo local; el 28 no es hoy ni cierre mensual y debe activarlo. El carácter laboral no determina esta decisión.
3. **Código observado:** el instrumento extrae la función JavaScript original de la plantilla; no escribe otra función que ya devuelva los resultados esperados. Las huellas impiden ejecutarlo silenciosamente contra una fuente diferente de la referencia.
4. **Alcance:** se observan aviso y conservación/vaciado de un campo simulado. No se crean certificaciones, llama PHP, consulta la base de datos o valida permiso integral de guardar.

No debe ejecutar el comando durante la revisión B. Puede solicitar explicación o ajustes, separando el tiempo activo de la espera. Al terminar, informe lo revisado, las dudas encontradas y duración activa real. No se proporciona una duración de ejemplo ni se completa el tiempo a partir del chat.

## Condiciones de ejecución previstas

Se usará Node.js y `node:vm`, con un contexto independiente por caso. El proceso fija `TZ=America/La_Paz` y cada contexto recibe una clase `Date` con instante ficticio 01/03/2028 a las 12:00. No se altera el reloj del equipo o del servidor. El horario fija reproducibilidad del instrumento; no representa una comprobación de todas las horas del día.

La fuente corresponde a `templates/poa/emitir_certificacion/new.html.twig` en la revisión de referencia SIGPP `7c0bca084b05c462137fd62c24e6b025bb09a12c`. Antes de ejecutar se reconfirmarán revisión y estado local; el programa comprueba además las huellas exactas de plantilla y fragmento del diagnóstico anterior. Si difieren, se detiene y se revisa la referencia, sin sustituir el código para obtener éxito. No se escribe un archivo dentro de SIGPP.

`expected` expresa la expectativa fijada antes del ensayo; `observed` se calcula a partir de lo que haga la función original. Una excepción de preparación no se confunde con rechazo correcto. El proceso devuelve código 1 si algún caso no coincide, conservando su resultado en lugar de corregir producción. Se mantendrá el comando y la salida real después de autorizar la ejecución.

## Código preparado antes de B y ejecutado después de su revisión

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
if (start < 0 || end <= start) throw new Error("No se localiza la funcion original");
const fragment = template.slice(start, end).trim();
const sha = text => crypto.createHash("sha256").update(text).digest("hex");
if (sha(template) !== "6f0000418c17a48b13584a64c772f30dc46233964b26d38fe922b11fe5cdc864" || sha(fragment) !== "d1d14948a7de977066eee70f7538c9617df723df9c1ad5f9d7ade4e937f9cf9c") throw new Error("Fuente distinta de la referencia: detener y revisar");
const cases = [
 {id:"B01", now:"2028-03-01T12:00:00-04:00", documentary:"2028-02-29", initial:"29/02/2028", expected:"sin_rechazo_local"},
 {id:"B02", now:"2028-03-01T12:00:00-04:00", documentary:"2028-02-28", initial:"28/02/2028", expected:"rechazo_local"}
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
  document:{getElementById(id) {if (id !== "emitir_certificacion_fecha") throw new Error("Campo inesperado: " + id); return field;}},
  swal(args) {notices.push({title:args.title,type:args.type});}
 });
 let error = null;
 try {
  vm.runInContext(fragment, context, {timeout:1000});
  vm.runInContext("verificarDiaAnteriorMes(new Date(" + JSON.stringify(spec.documentary + "T12:00:00-04:00") + "));", context, {timeout:1000});
 } catch(e) {error = {name:e.name,message:e.message};}
 let observed = "inconcluso";
 if (error) observed = "error_instrumento";
 else if (field.value === "" && notices.some(x=>x.type === "error")) observed = "rechazo_local";
 else if (field.value === spec.initial && notices.length === 0) observed = "sin_rechazo_local";
 return {...spec,observed,field_final:field.value,notices,error,concordant:observed === spec.expected};
});
console.log(JSON.stringify({
 started_utc:started,finished_utc:new RealDate().toISOString(),node:process.version,
 timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,
 revision:cp.execFileSync("git",["-C",repo,"rev-parse","HEAD"],{encoding:"utf8"}).trim(),
 template_sha256:sha(template),fragment_sha256:sha(fragment),
 scope:"isolated screen function; no PHP, HTTP or persistence",results
},null,2));
process.exitCode = results.every(x=>x.concordant) ? 0 : 1;'
```

## Relación con la medición de esfuerzo

La escritura de este código es trabajo del asistente y se declara como ayuda automática. B medirá lo que el participante realmente dedique a revisarlo, comprender sus entradas/salidas y solicitar ajustes. La ejecución posterior tendrá duración automática separada; C medirá lectura y análisis humanos de esa salida. No se sumará dos veces un intervalo ni se inferirá tiempo activo por las marcas de los mensajes.

**Actualización posterior a la revisión:** B se recibió con dos vueltas atribuidas a lectura del documento y revisión del Twig. Después se ejecutó exactamente el bloque anterior mediante extracción del Markdown y envío a Bash; la salida y sus límites se guardaron por separado. Los párrafos de preparación previos conservan la secuencia del protocolo, no indican que el ensayo siga pendiente. C todavía no tiene tiempo o análisis informado.

No se amplían O01–O06 o I04 con estos casos auxiliares. El registro de A1 se conserva pendiente de clasificación y no se descarta por contener errores. Una futura comparación necesita equivalencia y condiciones fijadas antes de ejecutarla; este instrumento no acredita ahorro, mejora del método o una comparación entre JavaScript y PHP. E6 sigue abierta.
