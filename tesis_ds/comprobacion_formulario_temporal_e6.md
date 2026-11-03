# Comprobación aislada del formulario temporal — E6

## 1. Protocolo fijado antes del ensayo

Se comprobará el formulario real `EmitirCertificacionType`, con la entidad real `EmitirCertificacion`, mediante los componentes locales Form y Validator de Symfony y lectura de anotaciones. La finalidad es observar si transforma, conserva y acepta fechas documentales concretas, no acreditar una petición HTTP, permisos, persistencia o creación de certificaciones. Se usará `submit()` directamente, sin iniciar el núcleo de la aplicación, sin extensión CSRF y sin base de datos. Estas exclusiones son límites del instrumento, no controles que se declaren superados.

El instrumento no controla el día operativo. La fecha inicial de la entidad será un dato ficticio fijo, `15/06/2026 12:00`, y no se presentará como sustitución del reloj PHP. Los casos F01–F04 toman fechas del conjunto ordinario, pero no son ejecuciones completas de O01–O05: en particular, una sola fecha 31/05 no se contará dos veces como intentos de los días 8 y 9. La deducción previa de retorno siempre verdadero en `verificarDia()` permanece como evidencia estática independiente.

Se crearán formularios y entidades separados por caso, con descripción y nota ficticias, cantidad 2, precio unitario 10 y total inicial 20. Las opciones serán `esVeatico=false` y `esRestringido=null`; no se activan campos de contrato o adjunto. Se observarán envío, sincronización, validez, estado habilitado del campo, fecha final y todos los errores. No se llamará al servicio de creación.

| Caso | Fecha enviada | Expectativa del instrumento, derivada de inspección previa |
|:--|:--|:--|
| F01 | `08/06/2026 12:00` | Formulario válido y fecha conservada. |
| F02 | `31/05/2026 12:00` | Formulario válido y fecha conservada. No representa dos relojes distintos. |
| F03 | `14/06/2026 12:00` | Formulario válido y fecha conservada; no acredita admisibilidad funcional para un intento de día 15. |
| F04 | `16/06/2026 12:00` | Formulario válido y fecha conservada; no acredita admisibilidad funcional para un intento de día 15. |
| C01 | Cadena vacía | Formulario no válido por fecha ausente. Control técnico separado. |
| C02 | `fecha-invalida` | Formulario no válido por transformación de fecha. Control técnico separado. |

Las expectativas describen el comportamiento previsto del componente existente, no sustituyen las decisiones funcionales aceptadas de O01–O06. Un error de montaje o excepción del instrumento se conservará y no se contará como rechazo temporal correcto. Cualquier corrección de instrumentación se documentará sin cambiar datos o expectativas para obtener un resultado favorable.

## 2. Referencia y preparación

Git confirmó `7c0bca084b05c462137fd62c24e6b025bb09a12c` sin cambios locales. La imagen histórica `sha256:fbf938bf6ca2b810ad22ac4094dc5f17f0ddd152fd603a23f77047d198e9793c` no está disponible en el motor Docker consultado ahora; no se descargó ni se reconstruyó. El contenedor habitual figura actualmente en ejecución, a diferencia del registro histórico de O06; no se lo inicia, detiene o usa para el ensayo. Su imagen local es `sha256:b2f3c21070e7b3561784370e4dbd7f578eabd7b7214159ba02af8634446f3dad` y se declara como entorno distinto, sin atribuir identidad completa con la ejecución anterior.

Una comprobación preliminar en contenedor efímero confirmó PHP 7.4.29, extensión `intl` y disponibilidad de Form y Validator mediante `vendor/autoload.php`; todavía no ejecutó los seis casos. El ensayo usará esa imagen local con `--pull=never`, `--network=none`, raíz y montaje del proyecto de solo lectura, usuario 1000, capacidades retiradas, sin privilegios nuevos y directorio `/tmp` temporal. No se utiliza el PHP 8.5.10 del equipo anfitrión ni se carga un archivo de entorno de la aplicación. La preparación y ejecución automatizadas no miden esfuerzo humano I03.

## 3. Revisión estática complementaria

`Certificacion.php`, líneas 29–34, declara `NotNull` para fecha y su asignador de líneas 205–209 conserva la fecha recibida. La búsqueda de anotaciones y métodos de validación en `Certificacion.php` y `EmitirCertificacion.php` no identificó otra restricción temporal. `config/packages/validator.yaml` solo contiene una opción de validación de correo; el inventario de `config/` no mostró archivos adicionales cuyo nombre contenga `validat`. La búsqueda acotada en `src/` de validadores, extensiones de formulario y suscriptores de solicitud/controlador solo identificó un suscriptor JWT, cuyo contenido se revisó y no comprueba fechas de certificación. Este alcance no es una auditoría exhaustiva de dependencias o servicios externos.

En `config/packages/security.yaml`, la regla visible de `/poa/` exige `ROLE_POA`; el formulario aislado no la ejecuta. `services.yaml` registra carga automática de servicios, pero no muestra una conexión temporal específica de la ruta en sus definiciones explícitas. La inspección no demuestra acceso permitido por HTTP ni reemplaza el control de autenticación.

## 4. Sustento técnico del instrumento

La documentación de Symfony 4.x confirma la integración independiente de Form con Validator mediante `ValidatorExtension` y la habilitación de lectura de anotaciones (Symfony, s. f.-d, s. f.-f). Se consultó el 3 de noviembre de 2026 a través de Context7; el ensayo depende además de las versiones locales efectivas que se registrarán. Esta documentación respalda el montaje técnico, no constituye evidencia de utilidad o validación del método de tesis.

Symfony. (s. f.-d). *The Form component* (documentación 4.x). https://symfony.com/doc/4.x/components/form.html

Symfony. (s. f.-f). *Validation resources* (documentación 4.x). https://symfony.com/doc/4.x/components/validator/resources.html

Estado de verificación: pasajes técnicos consultados; no se afirma lectura íntegra. Los resultados del ensayo están pendientes al guardar este protocolo.

## 5. Primer intento y ajuste del reporte

El primer intento se interrumpió con `InvalidArgumentException` al intentar asignar `null` a `Certificacion::setFecha()`, cuyo parámetro exige `DateTimeInterface`. No produjo el informe estructurado final y no se declara como batería completa satisfactoria. El control de fecha ausente puede provocar una excepción de mapeo en lugar del resultado no válido previsto; el siguiente intento capturará excepciones por caso para conservar ese comportamiento y permitir observar los demás. No se modifican el formulario, la entidad, los seis datos o las expectativas previas; una excepción quedará diferenciada de un formulario inválido y no contará como rechazo temporal correcto.

## 6. Resultados del segundo intento

El informe completo se obtuvo el **3 de noviembre de 2026 a las 11:53:58, zona `America/La_Paz`**. Versiones informadas: PHP 7.4.29, `symfony/form` v4.4.48, `symfony/validator` v4.4.48 y `doctrine/annotations` 1.14.3. Se conservaron los seis datos y se añadió únicamente captura de excepciones por caso. El proceso devolvió código **1**, porque C01 no cumplió la expectativa de formulario inválido sin excepción; no se presenta el conjunto como íntegramente satisfactorio.

| Caso | Resultado observado | Comparación con expectativa del instrumento |
|:--|:--|:--|
| F01 | Enviado, sincronizado y válido; campo habilitado; fecha final `2026-06-08T12:00:00-04:00`; sin errores. | Coincide. |
| F02 | Enviado, sincronizado y válido; campo habilitado; fecha final `2026-05-31T12:00:00-04:00`; sin errores. | Coincide. |
| F03 | Enviado, sincronizado y válido; campo habilitado; fecha final `2026-06-14T12:00:00-04:00`; sin errores. | Coincide. |
| F04 | Enviado, sincronizado y válido; campo habilitado; fecha final `2026-06-16T12:00:00-04:00`; sin errores. | Coincide. |
| C01 | Excepción `Symfony\Component\PropertyAccess\Exception\InvalidArgumentException`: `Expected argument of type "DateTimeInterface", "null" given at property path "fecha".` | No coincide; no se oculta ni redefine como rechazo temporal correcto. |
| C02 | No válido; campo de fecha no sincronizado y error `This value is not valid.`; conserva fecha inicial de la entidad. | Coincide como control de transformación, no como rechazo de negocio. |

El formulario real con validación por anotaciones aceptó y conservó las cuatro fechas sintácticamente válidas. Esto aporta evidencia ejecutada de ese componente, sin atribuirle una comparación contra el día del intento que el instrumento no controla. La excepción de C01 se conserva como hallazgo colateral, no se incorpora automáticamente al alcance de corrección de la tesis. Ninguno de estos casos invocó creación, repositorios o almacenamiento.

### Identidad y estado posterior

| Archivo | SHA-256 informado |
|:--|:--|
| `src/Form/poa/EmitirCertificacionType.php` | `401027bd48e83ea271c71bd3fd38cdb864906e14753662f89230a609f6a3168b` |
| `src/Entity/Certificacion.php` | `eb64a6604deb6b4562daa08484f49555242a28f5b340037c4e50d21c7ce49a53` |
| `src/Entity/EmitirCertificacion.php` | `65b538b0069f59ca62b855c07d3082e36fd1b7e0f38cdf125a9831866fbe78b6` |
| `composer.lock` | `4ceb38b75ef70d9381a64a552672c64de3a2080fbb021df32e679b80ba0934e6` |

Git posterior mantuvo `7c0bca08`, sin cambios locales, y la comparación de `src`, `tests` y `composer.lock` frente a `HEAD` no informó diferencias. El contenedor habitual continuó en ejecución; el instrumento utilizó otro contenedor efímero y no envió solicitudes al servicio habitual. No se modificó el reloj del equipo ni se usaron datos productivos. Los resultados no son I01 global, I02 de efectos o I03 humano y no cierran E6.

## 7. Programa PHP del segundo intento

El programa se suministró por entrada estándar al intérprete PHP del contenedor efímero descrito en la sección 2, con el proyecto montado en `/appdata/www` y ese directorio como ubicación de ejecución. No se guardó un archivo de prueba dentro de SIGPP. Para reproducirlo deben preservarse la imagen, las dependencias, las huellas y las restricciones de aislamiento; no debe ejecutarse mediante el arranque de la aplicación o contra un servicio productivo.

```php
<?php
require "vendor/autoload.php";
date_default_timezone_set("America/La_Paz");
$validator = Symfony\Component\Validator\Validation::createValidatorBuilder()->enableAnnotationMapping()->getValidator();
$factory = Symfony\Component\Form\Forms::createFormFactoryBuilder()->addExtension(new Symfony\Component\Form\Extension\Validator\ValidatorExtension($validator))->getFormFactory();
$cases = ["F01"=>"08/06/2026 12:00", "F02"=>"31/05/2026 12:00", "F03"=>"14/06/2026 12:00", "F04"=>"16/06/2026 12:00", "C01"=>"", "C02"=>"fecha-invalida"];
$results = [];
foreach ($cases as $id=>$date) {
    try {
        $entity = new App\Entity\EmitirCertificacion();
        $entity->setFecha(new DateTimeImmutable("2026-06-15T12:00:00-04:00"));
        $entity->setTotal(20);
        $form = $factory->create(App\Form\poa\EmitirCertificacionType::class, $entity, ["esVeatico"=>false,"esRestringido"=>null]);
        $disabled = $form->get("fecha")->isDisabled();
        $form->submit(["fecha"=>$date,"descripcion"=>"Comprobacion ficticia del formulario", "notaSolicitud"=>"Solicitud ficticia", "observacion"=>"Diagnostico aislado", "cantidad"=>"2", "precioUnitario"=>"10"]);
        $errors = [];
        foreach ($form->getErrors(true) as $error) $errors[] = ["field"=>$error->getOrigin()->getName(),"message"=>$error->getMessage()];
        $actual = $entity->getFecha();
        $valid = $form->isValid();
        $expected = substr($id,0,1)==="F";
        $expectedDate = $expected ? DateTimeImmutable::createFromFormat("!d/m/Y H:i",$date,new DateTimeZone("America/La_Paz"))->format("c") : null;
        $matches = $valid === $expected && !$disabled && (!$expected || ($actual && $actual->format("c")===$expectedDate));
        $results[] = ["id"=>$id,"submitted_date"=>$date,"submitted"=>$form->isSubmitted(),"synchronized"=>$form->isSynchronized(),"valid"=>$valid,"date_disabled"=>$disabled,"date_synchronized"=>$form->get("fecha")->isSynchronized(),"entity_date"=>$actual ? $actual->format("c") : null,"errors"=>$errors,"matches_instrument_expectation"=>$matches];
    } catch (Throwable $exception) {
        $results[] = ["id"=>$id,"submitted_date"=>$date,"exception_class"=>get_class($exception),"exception_message"=>$exception->getMessage(),"matches_instrument_expectation"=>false];
    }
}
$versions = [];
foreach (["symfony/form","symfony/validator","doctrine/annotations"] as $package) $versions[$package] = Composer\InstalledVersions::getPrettyVersion($package);
$hashes = [];
foreach (["src/Form/poa/EmitirCertificacionType.php","src/Entity/Certificacion.php","src/Entity/EmitirCertificacion.php","composer.lock"] as $file) $hashes[$file] = hash_file("sha256",$file);
print json_encode(["executed_at"=>(new DateTimeImmutable())->format("c"),"php"=>PHP_VERSION,"versions"=>$versions,"results"=>$results,"hashes"=>$hashes], JSON_PRETTY_PRINT | JSON_UNESCAPED_UNICODE).PHP_EOL;
exit(count(array_filter($results,static fn($r)=>!$r["matches_instrument_expectation"])) ? 1 : 0);
```
