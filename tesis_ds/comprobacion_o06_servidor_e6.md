# O06: pertenencia a gestión y rechazo antes de interacciones — E6

## 1. Protocolo anterior al ensayo

Se prepara el caso O06 del conjunto aceptado: tarea de gestión **2026**, fecha documental **31/12/2025** y ausencia de extraordinaria. El resultado requerido es rechazo por fecha de otra gestión, antes de crear certificación, seguimiento, autorización o almacenar adjuntos. Se invocará el método público real `CreateCertificacionService::create()`, sin sustituir su validación por un doble. Todos sus colaboradores se reemplazarán por dobles de PHPUnit para observar llamadas, sin persistencia o archivos reales.

El día de intento 10/01/2026 permanece como contexto funcional del caso. El servicio actual no recibe ni consulta ese día; **no se afirmará que el reloj PHP fue congelado al 10 de enero**. El instrumento comprueba la propiedad que sí recibe: fecha documental de 2025 frente a gestión de tarea 2026. No sirve para presentar los días 8/9 como comprobados en el mismo punto ni para validar aperturas o permisos.

Las expectativas y condiciones se fijan antes de la ejecución de O06. Un error de preparación, de saldo o de otro colaborador no contará como rechazo de fecha correcto. Se comprobarán clase y mensaje de la excepción y los contadores de las interacciones. Esta prueba aporta evidencia acotada del servicio con dobles, no de toda la operación institucional ni del método de refactorización.

## 2. Referencia y aislamiento

- SIGPP: `feature/propuesta-tesis`, `7c0bca084b05c462137fd62c24e6b025bb09a12c`; Git previo sin diferencias locales.
- El contenedor habitual `sigpp-app` se encontró detenido; no se lo inicia ni se usa su servicio web.
- Imagen local existente: `sha256:fbf938bf6ca2b810ad22ac4094dc5f17f0ddd152fd603a23f77047d198e9793c`.
- Comprobación preliminar en contenedor efímero: PHP `7.4.29`, PHPUnit `9.6.15`; clases utilizadas disponibles y no finales.
- Contenedor temporal con `--pull=never`, `--network=none`, raíz `--read-only`, proyecto montado en solo lectura, usuario 1000, capacidades retiradas y sin privilegios nuevos; `/tmp` temporal interno.
- Punto de entrada sobrescrito por el intérprete PHP; sin arrancar servidor, ejecutar scripts de instalación o iniciar otros contenedores.
- Suite de un caso creada en memoria y caché de resultados desactivada; no se escribe un archivo de prueba dentro de SIGPP.

Se importa únicamente `vendor/autoload.php`, sin iniciar Symfony ni cargar un entorno de aplicación mediante su arranque habitual. La red deshabilitada y el montaje de solo lectura limitan el alcance del proceso; no se leen ni publican credenciales o datos productivos. No se declara que este contenedor sea idéntico al entorno histórico completo. La imagen, dependencias locales y versión se registran para reproducir el ensayo acotado.

## 3. Datos y observables fijados

Se preparará una tarea ficticia con gestión 2026 y presupuesto disponible 100; cantidad 2 y precio unitario 10. Se suministrará un doble de adjunto, sin archivo físico. No se reutiliza el auxiliar anterior que recargaba una tarea de gestión 2025: esta prueba no recarga tareas y fija coherentemente la gestión que recibe la validación. Permisos, elegibilidad y apertura son supuestos externos al servicio observado, no controles verificados por el instrumento.

| Propiedad | Expectativa anterior al ensayo |
|:--|:--|
| Decisión | Excepción exactamente de clase `RuntimeException`, mensaje `Fecha en gestión incorrecta`. |
| Certificación | Cero llamadas a `EmitirCertificacionRepository::save()`. |
| Seguimiento | Cero llamadas a `SeguimientoCertificacionRepository::save()`. |
| Autorización | Cero llamadas a `CreateCertificacionAutorizacionService::create()`. |
| Adjunto | Cero llamadas a `UploadFileService::upload()`. |
| Observación auxiliar | Cero llamadas a solicitud de correlativo y resolvedor de restricciones; no se presume que el correlativo tenga por sí mismo un efecto persistente. |

Los contadores de expectativas `never()` se observarán y verificarán en PHPUnit `9.6.15`; el acceso a esa información interna se limita a la versión registrada. Los cuatro primeros colaboradores de efectos permiten comprobar ausencia de interacciones, **no ausencia de escrituras reales en una base o almacenamiento**, que no se utilizan. No se mide I03 humano: preparación y ejecución corresponden al asistente.

## 4. Estado previo

Protocolo y expectativas registrados antes de invocar O06. La comprobación preliminar de intérprete y clases no ejecutó el servicio de creación ni el caso. Se conservará cualquier error del instrumento sin convertirlo en resultado funcional correcto. E6 permanece abierta y no se autoriza construir la solución de E7.

## 5. Primer intento: fallo del reporte del instrumento

El primer intento mostró `OK (1 test, 8 assertions)`, después de avisos del ejecutor por listas de extensiones no suministradas. Al preparar el JSON adicional, el programa llamó a `TestResult::numberOfAssertions()`, inexistente en PHPUnit `9.6.15`, y terminó con error fatal. No se obtuvo el informe estructurado completo de ese intento y no se lo presenta como ejecución integral del instrumento sin errores. No es un fallo funcional del servicio ni un permiso para retirar expectativas.

La lectura de la versión instalada identifica `TestCase::getNumAssertions()` como acceso disponible y permite suministrar explícitamente listas vacías de extensiones al ejecutor. Se corregirán únicamente esos elementos de preparación/reporte. La repetición conservará datos, método público real, dobles, expectativas de cero llamadas y entorno aislado. Los dos intentos no se contarán como casos independientes ni como esfuerzo humano del tesista.

## 6. Ejecución completa después de corregir el reporte

Se repitió el mismo caso sin cambiar datos, expectativas o servicio. Inicio informado: `2026-11-03T05:00:00.578525Z`; fin: `2026-11-03T05:00:00.604115Z`, aproximadamente **01:00 del 3 de noviembre de 2026 en Bolivia**. PHPUnit informó PHP `7.4.29`, versión `9.6.15`, `OK (1 test, 8 assertions)`, sin errores, fallos u omisiones. El reporte estructurado terminó correctamente y el proceso devolvió código 0.

| Observable | Resultado registrado |
|:--|:--|
| Gestión recibida de la tarea ficticia | `2026`. |
| Fecha documental recibida | `2025-12-31T12:00:00-04:00`. |
| Excepción | Clase exacta `RuntimeException`, mensaje `Fecha en gestión incorrecta`. |
| `EmitirCertificacionRepository::save()` | 0 llamadas. |
| `SeguimientoCertificacionRepository::save()` | 0 llamadas. |
| `CreateCertificacionAutorizacionService::create()` | 0 llamadas. |
| `UploadFileService::upload()` | 0 llamadas. |
| Solicitud de correlativo, auxiliar | 0 llamadas. |
| Resolvedor de restricciones, auxiliar | 0 llamadas. |

Las expectativas y sus contadores se verificaron dentro de PHPUnit; no se deducen del tiempo o del mensaje por sí solos. La clasificación de O06 concuerda en la propiedad de pertenencia de fecha a gestión, y se observó ausencia de las cuatro interacciones prohibidas del criterio I02 para este caso. No se observó una base de datos o almacenamiento real: la prueba demuestra flujo con colaboradores sustituidos. Por tanto, no es integración completa ni I02 global para O03–O06.

### Identidad de los archivos y estado posterior

- Servicio SHA-256: `db0a8066152c72600307fb475484cf5153dec51cc62e35132bc2b3135710cfa7`.
- Entrada `CreateCertificacionInput.php` SHA-256: `7c8f07e98259fa334d202c6a5f41cfb6c1d8924f96462047464e80378b6b1f4f`.
- `composer.lock` SHA-256: `4ceb38b75ef70d9381a64a552672c64de3a2080fbb021df32e679b80ba0934e6`.
- Git posterior mantuvo `7c0bca084b05c462137fd62c24e6b025bb09a12c` y no informó cambios; comparación de `src`, `tests` y `composer.lock` frente a `HEAD` sin diferencias.
- `sigpp-app` permaneció detenido; el contenedor de ejecución fue temporal y se eliminó al finalizar mediante `--rm`.

No se arrancó la aplicación ni se ejecutaron sus scripts de instalación. La referencia 10/01/2026 fue contexto del caso, no una entrada de reloj del servicio. Las marcas de ejecución no son esfuerzo humano ni una muestra de rendimiento. La corrección del reporte no es rediseño del artefacto ni modificación de comportamiento del sistema.

## 7. Programa de reproducción de la ejecución completa

El siguiente comando transmite el programa PHP por entrada estándar; no guarda una prueba dentro de SIGPP. Requiere la imagen local indicada, Docker y el proyecto con sus dependencias. Antes de atribuir identidad a una reproducción deben comprobarse revisión y huellas. Se conserva el primer intento y se documentan las dos correcciones de reporte, en lugar de ocultarlas o cambiar expectativas tras observar resultados.

```bash
python3 -c 'import subprocess,sys
program = r"""<?php
require "vendor/autoload.php";
date_default_timezone_set("America/La_Paz");
$started = (new DateTimeImmutable("now", new DateTimeZone("UTC")))->format("Y-m-d\TH:i:s.u\Z");
class O06IsolatedDiagnosticTest extends PHPUnit\Framework\TestCase
{
    public array $rules = [];
    public ?array $observedException = null;
    public array $context = [];
    public function testDateOutsideTaskYearPrecedesEffects(): void
    {
        $gestion = $this->createMock(App\Entity\Gestion::class);
        $gestion->method("getNombre")->willReturn("2026");
        $task = $this->createMock(App\Entity\Tarea::class);
        $task->method("getGestion")->willReturn($gestion);
        $budget = new App\Entity\PresupuestoAsignado();
        $budget->setMontoModificado((new App\Entity\MontoModificado())->setDisponibleCertificacion("100"));
        $task->method("getPresupuestosAsignados")->willReturn(new Doctrine\Common\Collections\ArrayCollection([$budget]));
        $correlatives = $this->createMock(App\Repository\CertificacionRepository::class);
        $emissions = $this->createMock(App\Repository\EmitirCertificacionRepository::class);
        $resolver = $this->createMock(App\Service\Certificacion\RestriccionSubPartidaResolver::class);
        $tracking = $this->createMock(App\Repository\SeguimientoCertificacionRepository::class);
        $authorizations = $this->createMock(App\Service\CertificacionAutorizacion\CreateCertificacionAutorizacionService::class);
        $uploads = $this->createMock(App\Service\FileUpload\UploadFileService::class);
        foreach ([
            "certification_save" => [$emissions, "save"],
            "tracking_save" => [$tracking, "save"],
            "authorization_create" => [$authorizations, "create"],
            "upload" => [$uploads, "upload"],
            "correlative_auxiliary" => [$correlatives, "getNuevoCorrelativoCertificacion"],
            "restriction_auxiliary" => [$resolver, "resolve"],
        ] as $name => $pair) {
            $this->rules[$name] = $this->never();
            $pair[0]->expects($this->rules[$name])->method($pair[1]);
        }
        $service = new App\Service\Certificacion\CreateCertificacionService(
            $correlatives, $emissions, $resolver, $tracking, $authorizations, $uploads
        );
        $file = $this->createMock(Symfony\Component\HttpFoundation\File\UploadedFile::class);
        $input = new App\Service\Certificacion\Dto\CreateCertificacionInput(
            new DateTimeImmutable("2025-12-31T12:00:00-04:00"), "O06 diagnostic", "2", 10.0,
            "Fictitious request", "Fictitious observation", "Emitir", "3", "Personnel",
            false, "Contract", $file, "/unused/uploads"
        );
        $this->context = [
            "task_management" => $task->getGestion()->getNombre(),
            "documentary_date" => $input->getFecha()->format("c"),
            "reference_day" => "2026-01-10 (context only; not a controlled service input)",
            "available_budget" => "100", "quantity" => "2", "unit_price" => 10.0,
        ];
        try {
            $service->create($input, $task);
        } catch (RuntimeException $exception) {
            $this->observedException = ["class" => get_class($exception), "message" => $exception->getMessage()];
        }
        self::assertSame(RuntimeException::class, $this->observedException["class"] ?? null);
        self::assertSame("Fecha en gestión incorrecta", $this->observedException["message"] ?? null);
    }
}
$test = new O06IsolatedDiagnosticTest("testDateOutsideTaskYearPrecedesEffects");
$suite = new PHPUnit\Framework\TestSuite();
$suite->setName("O06 isolated diagnostic");
$suite->addTest($test);
$runner = new PHPUnit\TextUI\TestRunner();
$result = $runner->run($suite, ["cacheResult" => false, "colors" => "never", "columns" => 80, "verbose" => true, "extensions" => [], "loadedExtensions" => [], "notLoadedExtensions" => []], [], false);
$counts = [];
foreach ($test->rules as $name => $rule) $counts[$name] = $rule->getInvocationCount();
echo PHP_EOL . json_encode([
    "case" => "O06", "started_utc" => $started,
    "finished_utc" => (new DateTimeImmutable("now", new DateTimeZone("UTC")))->format("Y-m-d\TH:i:s.u\Z"),
    "php" => PHP_VERSION, "phpunit" => PHPUnit\Runner\Version::id(),
    "timezone" => date_default_timezone_get(), "context" => $test->context,
    "observed_exception" => $test->observedException, "calls" => $counts,
    "tests" => $result->count(), "assertions" => $test->getNumAssertions(),
    "errors" => $result->errorCount(), "failures" => $result->failureCount(),
    "skipped" => $result->skippedCount(), "successful" => $result->wasSuccessful(),
    "service_sha256" => hash_file("sha256", "src/Service/Certificacion/CreateCertificacionService.php"),
    "input_sha256" => hash_file("sha256", "src/Service/Certificacion/Dto/CreateCertificacionInput.php"),
    "composer_lock_sha256" => hash_file("sha256", "composer.lock"),
], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE) . PHP_EOL;
exit($result->wasSuccessful() ? 0 : 1);
"""
args = ["docker", "run", "--rm", "--pull=never", "--network=none", "--read-only", "--tmpfs", "/tmp:rw,noexec,nosuid,size=64m", "--cap-drop=ALL", "--security-opt=no-new-privileges", "--no-healthcheck", "--user", "1000", "--mount", "type=bind,src=/home/mario/dev/sf_projects/sipoa4,dst=/appdata/www,readonly", "--workdir", "/appdata/www", "--interactive", "--entrypoint", "php", "sha256:fbf938bf6ca2b810ad22ac4094dc5f17f0ddd152fd603a23f77047d198e9793c"]
result = subprocess.run(args, input=program.encode())
sys.exit(result.returncode)'
```

## 8. Consecuencia y límites

Se dispone de evidencia ejecutada de O06 en el consumidor PHP y de ausencia de las cuatro interacciones prohibidas para ese rechazo. No se sumará este caso a O01–O05 de pantalla para construir un porcentaje global de seis casos observados en una misma capa: son propiedades e instrumentos distintos. O03 conserva su discrepancia local y las restantes decisiones temporales necesitan comprobación pertinente de servidor. La capacidad extraordinaria I04, su lectura de configuración y la línea base humana I03 siguen pendientes.

La prueba actual verifica rechazo de fecha fuera de la gestión, no la fecha operativa del intento o una habilitación autorizada. Tampoco valida transacciones, concurrencia, archivos reales o un recorrido HTTP. El programa no incorpora ni corrige una regla de negocio: caracteriza una protección ya existente bajo expectativas fijadas previamente. E6 continúa abierta; no se acredita evaluación formativa con rediseño o sumativa del método por este ensayo.
