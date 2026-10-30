# Comparación retrospectiva de la extracción de restricción de subpartida

**Fecha de análisis:** 29 de octubre de 2026.  
**Estado:** comparación de código y comprobación actual del estado posterior; no experimento antes/después ejecutado.  
**Repositorio inspeccionado:** `/home/mario/dev/sf_projects/sipoa4`.

## 1. Unidad y referencias de comparación

El tesista aceptó comparar la extracción acotada en vez de las ramas completas, porque `master` incorporó correcciones productivas posteriores. Se seleccionó el padre inmediato del commit de extracción como estado anterior y el propio commit como posterior. La selección es retrospectiva, realizada después de construir, y no se presenta como un criterio experimental fijado en octubre antes de la intervención. La unidad es la selección de restricción específica, general o ausente y sus dos consumidores, no toda la creación de certificaciones ni la política de fechas.

| Referencia | Identificador | Uso |
|:--|:--|:--|
| Antes | `5313c0e150859d86dd9d82b1df21f719d2242076` | Padre inmediato de la extracción; comparación estática mediante Git. |
| Después | `8dc63307f3164e67de7e837f5cd191d097e6acfd` | Extracción del 18 de octubre de 2026, con pruebas incorporadas en el mismo commit. |
| Copia actual ejecutada | `5e0fec3d854f0cf74feaa4935caeb19736b40bbb` | Rama `feature/propuesta-tesis`; `git diff --quiet 8dc63307 HEAD -- src tests` terminó satisfactoriamente, sin diferencias en esos árboles. |

No se cambió de rama, modificó código de aplicación ni reconstruyó el estado anterior en esta sesión. La ausencia de diferencias en `src` y `tests` no comprueba por sí sola igualdad de dependencias, configuración, datos o entorno. La copia de producción no se inspeccionó. El código montado en el contenedor aún no se contrastó directamente con los identificadores Git.

## 2. Cambio estructural observado

| Aspecto | Antes: `5313c0e1` | Después: `8dc63307` | Alcance de la evidencia |
|:--|:--|:--|:--|
| Ubicación del algoritmo de selección | Implementación repetida en `CreateCertificacionController::estaRestringidaLaSubpartida()` y `CreateCertificacionService::estaRestringidaLaSubpartida()`. | Una implementación en `RestriccionSubPartidaResolver::resolve()`; ambos métodos delegan. | Dos implementaciones observadas pasan a una dentro de los archivos comparados; no es un censo de duplicación de todo SIGPP. |
| Colaboradores de selección en consumidores | Ambos reciben directamente `TareaRepository` y `RestriccionSubPartidaRepository`. | Reciben el resolvedor; este conserva ambos repositorios. | Se desplaza y centraliza el acceso, no se elimina la dependencia global de persistencia ni se obtiene una política pura. |
| Precedencia | Se recarga tarea por ID; se consulta restricción con actividad; si no existe, se consulta sin actividad. | Misma secuencia visible en el resolvedor, con retorno de restricción o `null`. | Correspondencia estática del algoritmo para el recorrido inspeccionado, no equivalencia universal demostrada. |
| Resultado en controlador | Retorna restricción específica, general o `null`. | Retorna lo obtenido del resolvedor. | Sin cambio funcional intencional identificado en el diff de selección. |
| Estado del servicio | Asigna el resultado a `esRestringido`, incluida la ausencia de restricción. | Asigna el retorno del resolvedor a la misma propiedad. | La prueba actual comprueba además limpieza de un resultado restringido anterior. |
| Fallos de colaboradores | Sin captura local de las excepciones en el algoritmo inspeccionado. | El resolvedor tampoco las captura ni transforma. | Pruebas actuales ejercitan propagación en recarga, consulta específica y consulta general. |

### Tamaño del cambio, no medida autosuficiente de calidad

`git diff --numstat 5313c0e1 8dc63307 -- src tests` identifica tres archivos de producción: controlador (+6/−31), servicio (+5/−32) y resolvedor nuevo (+46/−0). El saldo es **57 líneas añadidas y 63 eliminadas en producción**, una reducción neta de seis líneas; incluye importaciones, constructores y formato, no solo instrucciones de negocio. Se incorporan cuatro clases de prueba y una estructura auxiliar compartida, por 552 líneas añadidas. El commit completo comprende ocho archivos, con 609 inserciones y 63 eliminaciones; estos recuentos describen su extensión, no demuestran menor esfuerzo de cambio o mejor arquitectura.

## 3. Comprobaciones existentes y ejecución actual

La lectura de `RestrictionSelectionCharacterizationTest.php` identifica escenarios específico/general/ausente en ambos consumidores, propagación de excepciones y limpieza de estado del servicio. `RestrictionSelectionFixture.php` prepara dobles de entidades y repositorios, construye el resolvedor y utiliza reflexión para invocar métodos privados y observar la propiedad del servicio. La prueba verifica la selección a través de consumidores actuales, pero no recorre una petición HTTP, un formulario real o consultas reales a la base de datos. Su denominación como caracterización no acredita cuándo se escribió ni que se ejecutara contra la versión anterior.

| Ejecución del 29 de octubre | Resultado | Límite |
|:--|:--|:--|
| `make test`, invocado mediante `rtk`, en la rama de tesis | 188 pruebas, 540 aserciones; OK, sin omisiones informadas; PHPUnit 9.6.15. | Batería completa disponible en ese estado; no validación del método. |
| `rtk docker exec --user 1000 sigpp-app vendor/bin/phpunit tests/Certificacion` | 37 pruebas, 305 aserciones; OK; 0,221 s, 10 MB; PHPUnit 9.6.15. | Directorio de certificación del estado posterior; no ejecución del anterior. |

El auxiliar actual construye `RestriccionSubPartidaResolver` al preparar los consumidores, mientras esa clase no existe en el estado anterior. Por ello, no basta copiar sin adaptación estos archivos para afirmar una ejecución comparable sobre el padre del commit. Cualquier instrumento retrospectivo deberá separar la adaptación de construcción de objetos de las condiciones y resultados que se comparan. En esta sesión no se construyó ese instrumento ni se ejecutó la versión anterior.

## 4. Conclusión proporcional

Se documenta una extracción que centraliza el algoritmo duplicado de selección y mantiene una secuencia estáticamente correspondiente en los consumidores inspeccionados. Las pruebas actuales pasan y aportan evidencia parcial de selección, delegación y comportamiento del servicio en el estado posterior. No se ha medido el esfuerzo antes/después, realizado un cambio posterior comparable o comprobado integración real, por lo que no se afirma mejora demostrada de modificabilidad, testabilidad integral o continuidad operativa. Tampoco se acredita la secuencia prueba–implementación–refactorización: código y pruebas aparecen juntos en el commit y faltan registros intermedios.

## 5. Relación con E6 y trabajo pendiente

Esta comparación caracteriza una intervención histórica y no sustituye la línea base prospectiva de la próxima intervención temporal. No produce valores definitivos de I01–I04 ni criterios nuevos atribuidos al pasado. Falta contrastar el montaje del contenedor, decidir si es necesario ejecutar la selección anterior mediante un instrumento retrospectivo equivalente y fijar los escenarios del siguiente incremento antes de construir. La confirmación funcional de Marlen sobre fechas y habilitaciones sigue pendiente y no condiciona la lectura de esta extracción histórica.

## Fuentes de evidencia

La evidencia primaria es el historial Git y los archivos indicados del repositorio, junto con las salidas de comandos ejecutados en esta sesión; los identificadores permiten localizar los estados. No se introducen afirmaciones bibliográficas ni fuentes externas nuevas en este registro. La fundamentación teórica permanece en E4; aquí se documentan observaciones técnicas y sus límites.

## 6. Actualización: comprobación retrospectiva ejecutada el 29 de octubre

Esta actualización sustituye el estado inicial de «sin ejecución anterior» únicamente para la selección acotada. No se levantó la aplicación histórica completa: se ejecutaron las dos clases consumidoras históricas en el entorno actual de pruebas. Se conserva el relato inicial para distinguir los pasos y no atribuir a la primera inspección una ejecución que ocurrió después. La selección de escenarios y del instrumento sigue siendo retrospectiva.

### Entorno y correspondencia comprobada

`docker inspect` mostró montaje directo de `/home/mario/dev/sf_projects/sipoa4` en `/appdata/www`, con este último como directorio de trabajo de `sigpp-app`. El intérprete del contenedor informó PHP 7.4.29. Los SHA-256 del controlador, servicio, prueba de caracterización y auxiliar dentro del contenedor coincidieron con los obtenidos de sus objetos en `HEAD`; ello comprueba estos cuatro archivos, no la identidad de todo el entorno histórico. `phpunit.xml.dist` utiliza `vendor/autoload.php` como preparación y descubre `tests`; no se cambió su configuración.

| Archivo | SHA-256 comprobado en contenedor y `HEAD` |
|:--|:--|
| `src/Controller/poa/Certificacion/CreateCertificacionController.php` | `7e2eac0e96734e873cfb8e3cc0224c9ebb4ea807e3ec8fbc1246f35dd1df0736` |
| `src/Service/Certificacion/CreateCertificacionService.php` | `db0a8066152c72600307fb475484cf5153dec51cc62e35132bc2b3135710cfa7` |
| `tests/Certificacion/RestrictionSelectionCharacterizationTest.php` | `a07d03edff44961f199fa5b446df6dc1c00293bf6f3a216c2fff12b0ccfbe505` |
| `tests/Certificacion/RestrictionSelectionFixture.php` | `8858b9550ad0c5b44d31edc344d5825b200f4248a367e508e9022c2c73b95bd3` |

### Instrumento común y carga histórica

Se mantuvieron sin modificación `RestrictionSelectionCharacterizationTest.php` y `RestrictionSelectionFixture.php`, con sus datos, expectativas y construcción de consumidores mediante reflexión. Para el estado anterior se recuperó con `git show` el texto de controlador y servicio en `5313c0e1` y se cargó en memoria, antes de ejecutar PHPUnit, bajo sus nombres de clase originales. Se conservaron las dependencias y los dobles actuales; el auxiliar también construye un resolvedor actual, pero los constructores históricos reciben los repositorios y no utilizan ese objeto. Esto resuelve el problema de ausencia de clase sin simular que se trasladó toda la batería a una instalación histórica.

Los trece casos comprueban seis selecciones —específica, general y ausente en dos consumidores—, seis propagaciones de excepción —recarga, consulta específica y general en ambos— y una limpieza del estado anterior del servicio. El acceso usa reflexión sobre métodos privados y la propiedad pertinente; no constituye una prueba pública de extremo a extremo. La carga en memoria adapta el modo de ejecutar las clases históricas, no los escenarios para favorecer uno de los estados. No hubo cambio de rama, archivos de aplicación, dependencias o reglas funcionales.

| Estado de consumidores | Casos | Aserciones | Resultado | Tiempo informado, no indicador de rendimiento |
|:--|--:|--:|:--|:--|
| Histórico `5313c0e1`, cargado en memoria con entorno actual | 13 | 65 | OK, sin omisiones informadas | 0,104 s; 8 MB. |
| Posterior en `HEAD`, árboles `src/tests` iguales a `8dc63307` | 13 | 65 | OK, sin omisiones informadas | 0,109 s; 10 MB. |

Los dos procesos utilizaron PHPUnit 9.6.15, el mismo contenedor y las opciones `--do-not-cache-result --no-coverage --testdox`. Los tiempos incluyen carga y preparación diferentes, provienen de una sola ejecución por estado y no se comparan como rendimiento. El estado Git antes y después permaneció limpio en `feature/propuesta-tesis`, adelantada un commit respecto de su referencia remota local. La ausencia de cambios versionados no equivale a una auditoría de escrituras de toda la aplicación.

### Reproducción de la comprobación

Desde la raíz del repositorio SIGPP, ejecutar el siguiente código mediante Python en la terminal, sin guardarlo como archivo. Recupera únicamente objetos Git y transmite el programa PHP por entrada estándar; no sobrescribe la copia de trabajo. Requiere la revisión indicada, el contenedor disponible y los archivos de prueba con los contenidos identificados arriba.

```python
import base64
import subprocess

revision = "5313c0e150859d86dd9d82b1df21f719d2242076"
paths = [
    "src/Controller/poa/Certificacion/CreateCertificacionController.php",
    "src/Service/Certificacion/CreateCertificacionService.php",
]
program = ['<?php require "vendor/autoload.php";']
for path in paths:
    source = subprocess.check_output(["git", "show", revision + ":" + path])
    encoded = base64.b64encode(source.removeprefix(b"<?php")).decode()
    program.append('eval(base64_decode("' + encoded + '"));')
program.append(r'''
$_SERVER["argv"] = $GLOBALS["argv"] = [
    "phpunit", "--do-not-cache-result", "--no-coverage", "--testdox",
    "tests/Certificacion/RestrictionSelectionCharacterizationTest.php"
];
$_SERVER["argc"] = $GLOBALS["argc"] = count($_SERVER["argv"]);
PHPUnit\TextUI\Command::main();
''')
result = subprocess.run(
    ["docker", "exec", "-i", "--user", "1000", "sigpp-app", "php"],
    input="\n".join(program).encode(),
)
raise SystemExit(result.returncode)
```

Para el estado posterior se ejecutó:

```bash
rtk docker exec --user 1000 sigpp-app vendor/bin/phpunit --do-not-cache-result --no-coverage --testdox tests/Certificacion/RestrictionSelectionCharacterizationTest.php
```

### Conclusión actualizada y límites

Se dispone ahora de evidencia ejecutada de que las dos versiones de los consumidores satisfacen el mismo conjunto de expectativas de selección examinado, además de la correspondencia estática documentada. No se concluye equivalencia universal, validación de reglas institucionales o integración real de persistencia, formularios, archivos y HTTP. El entorno actual y las expectativas del constructor pueden compartir supuestos erróneos; emplear un instrumento común no elimina ese sesgo ni prueba TDD previo. No se midió esfuerzo de modificación ni se ejecutó un cambio representativo posterior, por lo que I03–I04 y los criterios prospectivos siguen pendientes.
