# Salida del instrumento de cierre bisiesto — material para la fase C

## Antes de leer la salida

El instrumento se ejecutó después de recibir la preparación A2 y la revisión B del participante. La ejecución automática no se suma al tiempo humano de I03. Para C, el participante debe iniciar su cronómetro **antes de leer y analizar esta salida** y pausarlo cuando termine o espere ayuda. Si ya vio los resultados antes de empezar a medir, debe declararlo; no se presenta la actividad como ciega ni se reconstruye esa lectura por estimación.

El análisis humano debe explicar, por caso, la correspondencia entre expectativa y observación, qué campos de la salida respaldan su interpretación y qué alcance no quedó comprobado. El objetivo no es copiar una conclusión del asesor. Se puede pedir explicación, conservando el tiempo activo y separando la espera. Este archivo no contiene una duración o conclusión atribuida al participante.

## Salida estructurada obtenida

La salida siguiente procede del único comando de `instrumento_i03_cierre_bisiesto_e6.md`, ejecutado sin cambiar sus casos o expectativas. Se utilizó la función original de pantalla, con fecha controlada dentro del contexto de prueba y dobles de aviso/campo. La revisión Git y las huellas corresponden al código examinado, no a un despliegue productivo.

```json
{
  "started_utc": "2026-11-04T03:40:33.776Z",
  "finished_utc": "2026-11-04T03:40:33.779Z",
  "node": "v26.13.0",
  "timezone": "America/La_Paz",
  "revision": "7c0bca084b05c462137fd62c24e6b025bb09a12c",
  "template_sha256": "6f0000418c17a48b13584a64c772f30dc46233964b26d38fe922b11fe5cdc864",
  "fragment_sha256": "d1d14948a7de977066eee70f7538c9617df723df9c1ad5f9d7ade4e937f9cf9c",
  "scope": "isolated screen function; no PHP, HTTP or persistence",
  "results": [
    {
      "id": "B01",
      "now": "2028-03-01T12:00:00-04:00",
      "documentary": "2028-02-29",
      "initial": "29/02/2028",
      "expected": "sin_rechazo_local",
      "observed": "sin_rechazo_local",
      "field_final": "29/02/2028",
      "notices": [],
      "error": null,
      "concordant": true
    },
    {
      "id": "B02",
      "now": "2028-03-01T12:00:00-04:00",
      "documentary": "2028-02-28",
      "initial": "28/02/2028",
      "expected": "rechazo_local",
      "observed": "rechazo_local",
      "field_final": "",
      "notices": [
        {
          "title": "Fecha incorrecta",
          "type": "error"
        }
      ],
      "error": null,
      "concordant": true
    }
  ]
}
```

## Cómo interpretar los campos, sin ampliar la evidencia

- `expected`: expectativa fijada antes del ensayo.
- `observed`: clasificación obtenida al observar el campo y los avisos de la función original.
- `field_final` y `notices`: evidencias locales que sustentan esa clasificación.
- `error`: excepción de preparación o ejecución del instrumento, si la hubo; no se transforma en rechazo de negocio correcto.
- `concordant`: comparación por caso entre expectativa y clasificación observada.

Las marcas instrumentadas corresponden aproximadamente a las 23:40:33 del 3 de noviembre de 2026 en Bolivia. No representan preparación humana, espera de IA, ejecución completa de una aplicación ni una muestra de rendimiento. La salida del comando terminó con código 0. No se ejecutaron PHP, HTTP, navegador o persistencia, ni se creó una certificación real.

Git posterior mantuvo `7c0bca084b05c462137fd62c24e6b025bb09a12c` sin cambios locales; la comparación de plantilla, `src` y `tests` contra `HEAD` no informó diferencias. Se recibieron posteriormente C1/C2 y C3, este último diferenciando la conservación de 29/02 y rechazo de 28/02; la bitácora conserva los intentos y la aclaración del título del aviso, sin cambiar esta salida. Las unidades de C1 se confirmaron como **04:30.14** y la corrección se informó en **02:35 agregados**. El registro humano por tramos se consolidó en la bitácora con sus límites, no como costo integral auditado o comparación de ahorro. No se incorporan estos dos casos auxiliares al porcentaje de O01–O06 o I04 ni se declara mejora del método por la salida.
