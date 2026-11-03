# Comprobación aislada del cierre mensual — instrumento y evidencia E6

## 1. Propósito y autorización

El tesista declara «no prepare pruebas, tu contnua» después de la propuesta de comprobar la frontera mensual de los días 8 y 9. Se prepara el instrumento como asistencia automatizada de diagnóstico, sin modificar producción. El objeto observado es la función JavaScript existente `verificarDiaAnteriorMes()` de `templates/poa/emitir_certificacion/new.html.twig`, no el método completo de refactorización ni el recorrido de creación PHP. El protocolo y las expectativas se registran antes de ejecutar los casos.

Esta actividad **no produce una medición de minutos humanos de I03**: preparación, ejecución y análisis los realiza el asistente. La declaración del tesista sobre no haber preparado pruebas no transforma trabajo automatizado en esfuerzo humano ni demuestra independencia del constructor. Se conservarán resultados concordantes, discrepantes y errores del instrumento. E6 permanece abierta y no se construye todavía la solución de E7.

## 2. Referencia y condiciones previas

- Repositorio observado: SIGPP, `/home/mario/dev/sf_projects/sipoa4`.
- Rama y revisión comprobadas antes del ensayo: `feature/propuesta-tesis`, `7c0bca084b05c462137fd62c24e6b025bb09a12c`.
- Git no informa diferencias locales ni divergencia respecto de su referencia remota local; no se consultó el remoto.
- Intérprete disponible: Node.js `v26.13.0`.
- Ejecución aislada mediante `node:vm` y dobles mínimos de campo y aviso; no se abren navegador, servidor, Docker, formulario o base de datos.
- `TZ=America/La_Paz` afecta únicamente al proceso del instrumento. La clase `Date` se sustituye dentro de cada contexto de prueba; no se modifica el reloj del equipo o del servidor.

El servicio PHP inspeccionado comprueba solamente el rango anual y no recibe el día del intento. No se lo invoca rotulando dos ejecuciones idénticas como días distintos. La selección de pantalla se limita a una comprobación existente y no cambia la decisión ya acordada de mantener al servidor PHP como autoridad operativa. El instrumento no afirma que la tarea, permiso, habilitación o saldo se hayan verificado realmente; son condiciones contextuales excluidas del fragmento observado.

## 3. Casos y resultados esperados fijados antes de ejecutar

| Caso | Contexto controlado | Expectativa funcional y observable |
|:--|:--|:--|
| M08, principal | Instante 08/06/2026 12:00, fecha documental 31/05/2026; tarea 2026 como supuesto. | Fecha admisible respecto del plazo: no activar rechazo local ni vaciar el campo. |
| M09, principal | Instante 09/06/2026 12:00, misma fecha documental y supuestos. | Fuera de plazo ordinario: observar rechazo local mediante aviso y vaciado del campo, mecanismos presentes en el fragmento actual. |
| CTRL, control del instrumento | Instante 08/06/2026 12:00, documento 30/05/2026. | Fecha distinta de hoy o cierre permitido: observar rechazo local. Comprueba que el instrumento detecta el mecanismo de aviso y vaciado. |

M08 deriva de la aclaración del tesista de que el día 8 está incluido; M09 deriva del límite «hasta día 8» de la fuente funcional y esa precisión. CTRL utiliza una fecha distinta de los días admitidos ya declarados, no una regla nueva. Su resultado es control técnico y no se mezcla con el denominador de los dos casos de frontera. Una falta de observación o error de preparación no contará como rechazo correcto.

## 4. Procedimiento previsto

1. Leer la plantilla actual sin modificarla; registrar revisión Git y huellas SHA-256 de plantilla y fragmento.
2. Extraer literalmente el texto entre las declaraciones `function verificarDiaAnteriorMes(fecha)` y `function verificarDiaAnteriorMesYAnteriorGestion(fecha)`. Si no se localizan en ese orden o el texto no ejecuta, detener o registrar error; no reemplazarlo por una implementación del resultado requerido.
3. Crear un contexto independiente por caso, con fecha del intento fija, campo ficticio inicial y registro de avisos.
4. Ejecutar la función original con una fecha documental explícita, en horario de Bolivia; observar campo final, avisos y posibles errores.
5. Comparar con las expectativas anteriores. Emitir resultado por caso y código de salida distinto de cero si hay discrepancia o error. No reparar la plantilla para lograr éxito.
6. Comprobar Git después del ensayo para verificar que los archivos de SIGPP sigan sin cambios.

«Sin rechazo local» significa que la función no emite aviso ni vacía el campo; **no significa certificación autorizada o guardada**. «Rechazo local» tampoco demuestra ausencia de efectos del servicio PHP, porque ese servicio no se ejecuta. La comprobación no mide cobertura global, integración ni eficacia del método. No se usará para afirmar ahorro causal comparando capas o instrumentos diferentes.

## 5. Estado anterior a la ejecución

**Registro del corte previo:** protocolo y expectativas preparados antes de ejecutar, sin resultados en ese momento. Se conserva la secuencia; la sección 6 incorpora el ensayo posterior. El procedimiento de minutos humanos I03 sigue aceptado, pero la línea base humana permanece pendiente; no se le atribuye el tiempo del asistente.

## 6. Resultado ejecutado

El instrumento se ejecutó mediante Node.js sobre el fragmento extraído directamente de la plantilla. Inicio informado: `2026-11-03T03:36:44.498Z`; fin: `2026-11-03T03:36:44.502Z`, equivalentes aproximadamente a las 23:36 del **2 de noviembre de 2026 en Bolivia**. Estas marcas identifican el proceso automatizado, no preparación o esfuerzo humano I03 ni un estudio de rendimiento. No hubo errores de instrumento informados en los tres casos.

| Caso | Resultado observado | Correspondencia |
|:--|:--|:--|
| M08: intento 08/06, documento 31/05 | Conserva `31/05/2026`; cero avisos. | Sí: sin rechazo local en el límite incluido. |
| M09: intento 09/06, documento 31/05 | Conserva `31/05/2026`; cero avisos. | No: no se observa el rechazo requerido fuera del plazo. |
| CTRL: intento 08/06, documento 30/05 | Campo vacío; un aviso tipo `error`, título `Fecha incorrecta`. | Sí, como control técnico del instrumento. |

Los dos casos principales tienen una concordancia observada y una discrepancia; el control se informa aparte. **No se presenta 1/2 como I01 global**, tasa del uso institucional o mejora del método. El proceso terminó con código 1 porque M09 discrepa de la expectativa previamente fijada, no por un error de preparación. No se retiró ni reparó ese caso para obtener una salida satisfactoria.

El resultado confirma, para estos contextos y este fragmento, que la función no distingue el límite mensual del día 8. No se afirma que el formulario completo acepte la operación, se guarde una certificación o no existan otras barreras de servidor. I02 no queda verificado por observar un campo y avisos: persistencia, autorización, seguimiento y adjuntos no se ejecutaron. La autoridad futura de PHP y la ausencia de modificaciones productivas se mantienen.

### Identidad y comprobación posterior

- Revisión registrada por el propio instrumento: `7c0bca084b05c462137fd62c24e6b025bb09a12c`.
- SHA-256 de plantilla leída: `6f0000418c17a48b13584a64c772f30dc46233964b26d38fe922b11fe5cdc864`.
- SHA-256 del fragmento ejecutado: `d1d14948a7de977066eee70f7538c9617df723df9c1ad5f9d7ade4e937f9cf9c`.
- Zona del proceso informada por Node: `America/La_Paz`.
- Git después del ensayo mantuvo la misma revisión y no informó cambios; la comprobación de diferencias frente a `HEAD` en `src`, `tests` y la plantilla terminó sin diferencias.

Las huellas identifican el texto examinado, no una auditoría de todo el sistema o del despliegue. El ensayo no accedió a red, producción, base de datos, servidor PHP o navegador. El asistente preparó y ejecutó el instrumento; los minutos humanos activos del tesista no fueron medidos. La actividad produce evidencia diagnóstica, no la línea base humana que I03 necesita.

## 7. Código utilizado para reproducir el ensayo

El programa se ejecutó directamente desde la terminal, sin guardarlo en SIGPP. Puede ejecutarse desde cualquier carpeta si se conservan las rutas y herramientas indicadas. Una reproducción debe comprobar revisión y huellas contra la sección anterior antes de atribuirle identidad con este ensayo; si el archivo cambia, es otra referencia. El código de salida 1 es el resultado esperado mientras M09 conserve la discrepancia.

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
const cases = [
 {id:"M08", role:"principal", now:"2026-06-08T12:00:00-04:00", documentary:"2026-05-31", initial:"31/05/2026", expected:"sin_rechazo_local"},
 {id:"M09", role:"principal", now:"2026-06-09T12:00:00-04:00", documentary:"2026-05-31", initial:"31/05/2026", expected:"rechazo_local"},
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
const primary = results.filter(x => x.role === "principal");
console.log(JSON.stringify({
 started_utc:started,finished_utc:new RealDate().toISOString(),node:process.version,
 timezone:Intl.DateTimeFormat().resolvedOptions().timeZone,
 revision:cp.execFileSync("git",["-C",repo,"rev-parse","HEAD"],{encoding:"utf8"}).trim(),
 source:path,template_sha256:sha(template),fragment_sha256:sha(fragment),
 source_function:"verificarDiaAnteriorMes",results,
 summary:{primary_cases:primary.length,primary_concordant:primary.filter(x=>x.concordant).length,control_concordant:results.find(x=>x.id==="CTRL").concordant}
},null,2));
process.exitCode = results.every(x=>x.concordant) ? 0 : 1;'
```

## 8. Consecuencia para la investigación

Se dispone de una discrepancia ejecutada con contexto temporal explícito en la función de pantalla, adicional a la inspección estática. El comportamiento requerido del día 8 se mantiene y no se ajusta para hacer coincidir M09 con el código. La siguiente intervención deberá distinguir preservar estructura de corregir ese comportamiento y comprobar la conexión de la decisión en el recorrido pertinente. Ese diseño y su construcción no se aprueban automáticamente por este diagnóstico.

E6 sigue abierta: falta completar y ratificar el conjunto funcional, establecer instrumentos de los consumidores y efectos y resolver la medición humana I03 bajo condiciones declaradas. El registro de asistencia no puede utilizarse como comparación causal de testabilidad antes/después entre una función JavaScript y un futuro servicio PHP. No se incorporan nuevas reglas de negocio ni se amplía el alcance a todo SIGPP.
