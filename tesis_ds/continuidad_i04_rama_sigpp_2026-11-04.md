# Continuidad de I04: copia local distinta de la referencia de tesis

## Actualización: referencia de tesis recuperada

Tras informar el tesista que volvió a la rama de tesis, una nueva comprobación Git confirma `feature/propuesta-tesis`, revisión `7c0bca084b05c462137fd62c24e6b025bb09a12c`, sin cambios locales informados. La salida no muestra adelanto o atraso frente a `gitlab-com/feature/propuesta-tesis`; no se consultó el remoto. El asistente no cambió de rama. Queda resuelto el bloqueo por referencia distinta descrito más abajo, que se conserva como antecedente.

Se leyó `CreateCertificacionController.php` en esta referencia: el método `new()` llama a `CreateCertificacionService::create()` en la línea 137, dentro del procesamiento de formulario válido. La consulta `findArrayDeHabilitados($gestion)` está en las líneas 150–151, después de ese bloque; su resultado se entrega a la vista en la línea 172. Por orden de ejecución, esa consulta posterior no constituye la barrera previa a la creación en el bloque mostrado. No se afirma ausencia de toda barrera global o vulnerabilidad HTTP a partir de esta lectura.

El recorrido visible de esta consulta utiliza `ParametroSistemaRepository::findArrayDeHabilitados()`, no una llamada a `ParametroSistemaService`. La lectura previa del repositorio identifica `CURRENT_TIMESTAMP()` en ese método. `git diff c20fba5440d25be91ae42f9a45fd9c5f16bb12b4 HEAD -- src/Service/ParametroSistemaService.php src/Repository/ParametroSistemaRepository.php` no muestra diferencias entre ambos estados para esos dos archivos. Esto permite atribuir a la referencia recuperada las observaciones de esos archivos, sin extender igualdad al resto de la aplicación. La plantilla `new.html.twig`, líneas 27–38, muestra formulario y botón Guardar sin condicional de habilitación en ese fragmento; no se auditan todas sus inclusiones o herencia.

**Recomendación pendiente de elección del tesista:** delimitar el consumidor principal del nivel B a la decisión de habilitación usada antes de invocar la creación en el recorrido de certificación, comprobando lectura real del cierre configurado; no aceptar únicamente un cambio en menú o colección general como evidencia de conexión. Esto fija el alcance de observación, no una clase, contrato o implementación de E7. La consulta actual dependiente del reloj de base de datos sigue requiriendo estrategia de control o separación para el futuro instrumento; no se resuelve sustituyendo manualmente sus resultados esperados. No se ejecutaron pruebas, modificó SIGPP o cerró E6.

## Comprobación de solo lectura

El 4 de noviembre de 2026, al continuar la selección del consumidor I04, se ejecutaron `git status --short --branch` y `git rev-parse HEAD` en `/home/mario/dev/sf_projects/sipoa4`. La copia local informa rama `hotfix/bsip-163-tarea-calculo`, revisión `c20fba5440d25be91ae42f9a45fd9c5f16bb12b4`, sin cambios locales informados. No es la rama `feature/propuesta-tesis` ni la referencia diagnóstica previa `7c0bca08`.

La exploración mostró una versión de `CreateCertificacionService` con selección de restricción dentro del servicio, diferente del recorrido de tesis registrado previamente con resolvedor extraído. No se atribuye esta diferencia a una regresión, pérdida de trabajo o cambio del tesista dentro de esta sesión; son estados distintos y no se compararon sus historiales completos.

## Lectura acotada del consumidor de configuración

En esta copia, `ParametroSistemaService.php`, líneas 38–59, carga al construirse dos consultas: `findByGestionByAmpliacionFechaActual()` y `findParamatrosByActivoEnProceso()`. Las líneas 62–94 construyen y filtran una colección estática; `estaActivo()` y `getParametro()`, líneas 120–141, consultan esa colección. Por ello, repetir una consulta sobre la misma colección no acredita por sí solo lectura del cierre actualizado. Esta observación es estática y corresponde a la copia local identificada, no a una nueva ejecución de la referencia de tesis.

Las inspecciones anteriores de esta sesión que no fijaron Git no deben presentarse como reconfirmación de `7c0bca08`. Antes de completar el instrumento es necesario volver a la copia de tesis o seleccionar explícitamente otra ubicación que contenga esa referencia. No se cambia de rama, modifica código o configuración, ejecutan pruebas, consultan datos productivos o autoriza construcción. E6 permanece abierta; el protocolo I04 y los criterios aceptados no cambian.
