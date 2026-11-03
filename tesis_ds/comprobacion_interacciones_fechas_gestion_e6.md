# Fechas de la misma gestión e interacciones del servicio — E6

## 1. Protocolo anterior al ensayo

Se invocará `CreateCertificacionService::create()` real para tres fechas documentales de gestión 2026: 31/05, 14/06 y 16/06, todas a las 12:00 en `America/La_Paz`. Los escenarios auxiliares se identifican como S31, S14 y S16. No se ejecutará nuevamente O06 ni se presentarán estos escenarios como O03–O05 completos: el servicio no recibe ni consulta el día operativo, por lo que no se afirmará haber controlado los intentos del 09/06 o 15/06. El objetivo es observar hasta qué interacciones llega el consumidor existente con entradas anuales válidas, no fabricar una política temporal ausente.

Cada escenario usará una tarea ficticia de gestión 2026, presupuesto disponible 100, cantidad 2 y precio unitario 10. Administración ficticia 99, sigla HQ, unidad y establecimiento ficticios permitirán completar la construcción de la certificación. Los seis colaboradores del servicio se sustituirán por dobles de PHPUnit: correlativo, guardado de certificación, resolvedor de restricciones, guardado de seguimiento, autorización y archivo. El resolvedor devolverá ausencia de restricción; esa sustitución aísla un control ajeno a la propiedad temporal y no reemplaza la validación de fecha del servicio real.

La expectativa, derivada de la inspección previa, es que cada llamada retorne una certificación con la fecha documental recibida y el total 20, luego de una consulta al resolvedor y una solicitud de correlativo. Se esperan una llamada a guardar certificación y otra a guardar seguimiento, en ese orden, y cero llamadas de autorización o carga de archivo en el caso sin restricción. Los callbacks conservarán los objetos observados para comprobar identidad y fecha del seguimiento. Estas expectativas caracterizan el flujo existente, no aprueban su admisibilidad funcional para un día operativo determinado.

| Escenario | Fecha documental | Expectativa del instrumento |
|:--|:--|:--|
| S31 | `2026-05-31T12:00:00-04:00` | Retorno normal; resolvedor → correlativo → guardar certificación → guardar seguimiento. |
| S14 | `2026-06-14T12:00:00-04:00` | Misma secuencia; fecha conservada. |
| S16 | `2026-06-16T12:00:00-04:00` | Misma secuencia; fecha conservada. |

Una excepción inesperada o incumplimiento de expectativas se conservará como tal; no se confundirá con un rechazo temporal correcto. No se construye una comparación de días cambiando solo etiquetas. Los dobles no ejecutan persistencia o archivos: una llamada observada a `save()` no se publicará como una escritura real. No se mide I03 humano mediante tiempo del asistente.

## 2. Entorno y aislamiento

Git previo confirma `7c0bca084b05c462137fd62c24e6b025bb09a12c` sin cambios locales. La imagen local `sha256:b2f3c21070e7b3561784370e4dbd7f578eabd7b7214159ba02af8634446f3dad` se comprobó disponible y es la misma utilizada en el ensayo aislado del formulario, no la imagen histórica de O06. Se usará un contenedor efímero sin red, sin descarga, raíz y proyecto de solo lectura, usuario 1000, sin capacidades o privilegios nuevos y `/tmp` temporal. Se cargará únicamente `vendor/autoload.php`; no se inicia el núcleo de Symfony ni se cargan archivos de entorno mediante su arranque.

El programa se transmitirá por entrada estándar, sin guardar una prueba dentro de SIGPP y sin caché de PHPUnit. No se invocará el servicio web habitual, ni se iniciarán o detendrán sus contenedores. Las versiones y huellas pertinentes se registrarán después de ejecutar; un fallo de instrumentación no autoriza cambiar datos o expectativas para obtener éxito.

## 3. Alcance respecto de los indicadores

Esta comprobación puede mostrar que el servicio llega a colaboradores de efectos para fechas de su misma gestión. No establece un porcentaje de correspondencia de decisiones con el calendario funcional ni completa I02 para los rechazos O03–O05, porque no representa su día operativo. Tampoco prueba conexión del formulario con el controlador real, autorización HTTP, transacciones o almacenamiento. Su utilidad diagnóstica es distinguir una validación anual local de una decisión temporal funcional completa y delimitar qué capacidad falta observar o construir después.

Al guardar este protocolo todavía no se han ejecutado S31, S14 o S16. E6 permanece abierta y no se autoriza corregir producción.

## 4. Ejecución y resultados

Se ejecutó el protocolo el **3 de noviembre de 2026, con informe a las 12:30:31 en `America/La_Paz`**, mediante PHP 7.4.29 y PHPUnit 9.6.15. El proceso terminó con código 0 y PHPUnit informó **3 pruebas, 36 aserciones, sin errores, fallos u omisiones**. No hubo ajustes del instrumento entre intentos: esta comprobación produjo el informe completo en su primera ejecución. Los resultados corresponden a expectativas del flujo existente, no a tres decisiones temporales funcionales correctas.

| Escenario | Resultado del servicio | Guardado de certificación | Guardado de seguimiento | Autorización | Archivo |
|:--|:--|--:|--:|--:|--:|
| S31, documento 31/05/2026 | Retorno normal; fecha conservada. | 1 llamada | 1 llamada | 0 llamadas | 0 llamadas |
| S14, documento 14/06/2026 | Retorno normal; fecha conservada. | 1 llamada | 1 llamada | 0 llamadas | 0 llamadas |
| S16, documento 16/06/2026 | Retorno normal; fecha conservada. | 1 llamada | 1 llamada | 0 llamadas | 0 llamadas |

En los tres escenarios se observó una llamada al resolvedor y una solicitud de correlativo, y la secuencia completa fue `resolver → correlative → certification_save → tracking_save`. Las aserciones verificaron identidad del objeto retornado frente al entregado al repositorio, conservación de fecha y total y relación/fecha del seguimiento. Las expectativas de PHPUnit verificaron las llamadas únicas y las ausencias de autorización/archivo. El informe por escenario capturó anticipadamente un campo `assertions: 0`, antes de que PHPUnit consolidara el contador del caso; no es el recuento final ni significa que no se comprobaron aserciones. El total final de 36 se obtuvo después de ejecutar la batería y coincide con la salida de PHPUnit; no se utiliza aquel campo anticipado para métricas individuales.

### Identidad y ausencia de cambios

| Archivo | SHA-256 informado |
|:--|:--|
| `src/Service/Certificacion/CreateCertificacionService.php` | `db0a8066152c72600307fb475484cf5153dec51cc62e35132bc2b3135710cfa7` |
| `src/Service/Certificacion/Dto/CreateCertificacionInput.php` | `7c8f07e98259fa334d202c6a5f41cfb6c1d8924f96462047464e80378b6b1f4f` |
| `composer.lock` | `4ceb38b75ef70d9381a64a552672c64de3a2080fbb021df32e679b80ba0934e6` |

Git posterior mantiene `7c0bca08`, sin cambios locales y sin diferencias de `src`, `tests` o `composer.lock` frente a `HEAD`. No se registraron escrituras en SIGPP: las interacciones ocurrieron con dobles dentro de un contenedor efímero sin red y con montaje de solo lectura. La llamada a un repositorio sustituido no acredita que se guardó una certificación real. La imagen utilizada se mantiene diferenciada de la histórica de O06.

## 5. Conclusión acotada y siguiente compromiso

La validación local del servicio permite llegar a las dos interacciones de guardado para las tres fechas de la misma gestión examinadas. El día operativo sigue sin representarse: no se afirma que el programa ejecutó O03 el día 9 o que reprodujo O04/O05 el día 15, ni se suman estas observaciones a las de pantalla o formulario para calcular un indicador global. La evidencia diagnostica el alcance anual del consumidor y sus conexiones, no una política temporal completa o un fallo de persistencia real. Cero llamadas de autorización y archivo describen la rama sin restricción, no garantizan protección de esas operaciones en todas las ramas.

Este ensayo completa la observación local anunciada, pero no resuelve I03 humano, I04 o la evaluación del método. Seguir repitiendo fechas con el mismo instrumento no proporcionaría el día operativo ausente ni una medición humana. Antes de construir falta fijar y recoger una actividad prospectiva de esfuerzo con participación del tesista y condiciones de comparación explícitas, además del instrumento de configuración extraordinaria. No se cierra E6 con pruebas auxiliares ni se convierte su duración en esfuerzo humano.

## 6. Programa PHP ejecutado

El programa se transmitió por entrada estándar a `php` en la imagen de la sección 2, con directorio de trabajo `/appdata/www` y el montaje de solo lectura de SIGPP. El contenedor se ejecutó con `--rm --pull=never --network=none --read-only --tmpfs /tmp:rw,noexec,nosuid,size=64m --cap-drop=ALL --security-opt=no-new-privileges --no-healthcheck --user 1000`; la entrada habitual de la imagen se sustituyó por PHP. No se guardó este programa dentro del proyecto inspeccionado. El siguiente código conserva incluso el campo anticipado de aserciones, cuyo límite se explica en la sección 4.

```php
<?php
require "vendor/autoload.php";
date_default_timezone_set("America/La_Paz");
class SameManagementInteractionsTest extends PHPUnit\Framework\TestCase {
    public static array $observations = [];
    public function testMay31(): void { $this->exercise("S31", "2026-05-31"); }
    public function testJune14(): void { $this->exercise("S14", "2026-06-14"); }
    public function testJune16(): void { $this->exercise("S16", "2026-06-16"); }
    private function exercise(string $id, string $day): void {
        $events = [];
        $counts = ["resolver"=>0,"correlative"=>0,"certification_save"=>0,"tracking_save"=>0,"authorization_create"=>0,"upload"=>0];
        $saved = null;
        $trackingObject = null;
        $management = $this->createMock(App\Entity\Gestion::class);
        $management->method("getNombre")->willReturn("2026");
        $administration = $this->createMock(App\Entity\Administracion::class);
        $administration->method("getId")->willReturn(99);
        $administration->method("getSigla")->willReturn("HQ");
        $budget = new App\Entity\PresupuestoAsignado();
        $budget->setMontoModificado((new App\Entity\MontoModificado())->setDisponibleCertificacion("100"));
        $task = $this->createMock(App\Entity\Tarea::class);
        $task->method("getGestion")->willReturn($management);
        $task->method("getAdministracion")->willReturn($administration);
        $task->method("getPresupuestosAsignados")->willReturn(new Doctrine\Common\Collections\ArrayCollection([$budget]));
        $task->method("getUnidad")->willReturn(new App\Entity\UnidadProduccion());
        $task->method("getEstablecimiento")->willReturn(new App\Entity\Establecimiento());
        $codes = $this->createMock(App\Repository\CertificacionRepository::class);
        $emissions = $this->createMock(App\Repository\EmitirCertificacionRepository::class);
        $resolver = $this->createMock(App\Service\Certificacion\RestriccionSubPartidaResolver::class);
        $tracking = $this->createMock(App\Repository\SeguimientoCertificacionRepository::class);
        $authorizations = $this->createMock(App\Service\CertificacionAutorizacion\CreateCertificacionAutorizacionService::class);
        $uploads = $this->createMock(App\Service\FileUpload\UploadFileService::class);
        $resolver->expects($this->once())->method("resolve")->with($task)->willReturnCallback(function () use (&$events, &$counts) { $events[]="resolver"; $counts["resolver"]++; return null; });
        $codes->expects($this->once())->method("getNuevoCorrelativoCertificacion")->with("Emitir","2026",99)->willReturnCallback(function () use (&$events, &$counts) { $events[]="correlative"; $counts["correlative"]++; return "7"; });
        $emissions->expects($this->once())->method("save")->willReturnCallback(function ($object) use (&$events, &$counts, &$saved) { $events[]="certification_save"; $counts["certification_save"]++; $saved=$object; });
        $tracking->expects($this->once())->method("save")->willReturnCallback(function ($object) use (&$events, &$counts, &$trackingObject) { $events[]="tracking_save"; $counts["tracking_save"]++; $trackingObject=$object; });
        $authorizationRule = $this->never();
        $uploadRule = $this->never();
        $authorizations->expects($authorizationRule)->method("create");
        $uploads->expects($uploadRule)->method("upload");
        $service = new App\Service\Certificacion\CreateCertificacionService($codes,$emissions,$resolver,$tracking,$authorizations,$uploads);
        $date = new DateTimeImmutable($day."T12:00:00-04:00");
        $input = new App\Service\Certificacion\Dto\CreateCertificacionInput($date,"Fictitious diagnostic","2",10.0,"Fictitious request","Fictitious observation","Emitir","3","Personnel",false,"Contract",null,"/unused/uploads");
        try {
            $result = $service->create($input,$task);
            self::assertSame($saved,$result);
            self::assertSame($date,$result->getFecha());
            self::assertEquals(20,$result->getTotal());
            self::assertSame($result,$trackingObject->getCertificacion());
            self::assertSame($date,$trackingObject->getFecha());
            self::assertSame(["resolver","correlative","certification_save","tracking_save"],$events);
            $counts["authorization_create"] = $authorizationRule->getInvocationCount();
            $counts["upload"] = $uploadRule->getInvocationCount();
            self::$observations[] = ["id"=>$id,"task_management"=>"2026","documentary_date"=>$date->format("c"),"outcome"=>"normal_return","result_date"=>$result->getFecha()->format("c"),"counts"=>$counts,"events"=>$events,"assertions"=>$this->getNumAssertions(),"reference_day_controlled"=>false];
        } catch (Throwable $exception) {
            self::$observations[] = ["id"=>$id,"exception_class"=>get_class($exception),"exception_message"=>$exception->getMessage(),"counts"=>$counts,"events"=>$events];
            throw $exception;
        }
    }
}
$suite = new PHPUnit\Framework\TestSuite();
$suite->setName("Same-management dates diagnostic");
$tests = [];
foreach (["testMay31","testJune14","testJune16"] as $method) { $test = new SameManagementInteractionsTest($method); $tests[]=$test; $suite->addTest($test); }
$runner = new PHPUnit\TextUI\TestRunner();
$result = $runner->run($suite,["cacheResult"=>false,"colors"=>"never","columns"=>80,"verbose"=>true,"extensions"=>[],"loadedExtensions"=>[],"notLoadedExtensions"=>[]],[],false);
$hashes = [];
foreach (["src/Service/Certificacion/CreateCertificacionService.php","src/Service/Certificacion/Dto/CreateCertificacionInput.php","composer.lock"] as $file) $hashes[$file]=hash_file("sha256",$file);
print PHP_EOL.json_encode(["executed_at"=>(new DateTimeImmutable())->format("c"),"php"=>PHP_VERSION,"phpunit"=>PHPUnit\Runner\Version::id(),"tests"=>$result->count(),"assertions"=>array_sum(array_map(static fn($test)=>$test->getNumAssertions(),$tests)),"errors"=>$result->errorCount(),"failures"=>$result->failureCount(),"skipped"=>$result->skippedCount(),"successful"=>$result->wasSuccessful(),"observations"=>SameManagementInteractionsTest::$observations,"hashes"=>$hashes],JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE).PHP_EOL;
exit($result->wasSuccessful() ? 0 : 1);
```
