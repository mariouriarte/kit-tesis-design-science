# E7f. Ficha del artefacto

> **Versión vigente del método: M-R1, rediseñada después de P01 y evaluada posteriormente en el episodio P02.** Manual operativo en `metodo_refactorizacion_incremental_mr1.md`; evidencia, versión anterior y cuatro cambios aprobados en `registro_redisenio_metodo_mr1.md`; resultados y dictamen aceptado en `revision_aplicacion_p02_2026-11-06.md`, sección 7. La aplicación de importe utiliza un suplemento de registro progresivo identificado por separado. La ficha no acredita integración completa, beneficios no medidos o validación general de principios.

**Estado:** ficha documental con referencias de evaluación actualizadas. Debe permitir entender y aplicar el método con sus entradas, productos y condiciones, sin depender de decisiones tácitas del tesista. Consolida lo formalizado en E7a–E7e y distingue el antecedente de software de los episodios posteriores; no añade reglas nuevas o criterios retrospectivos. El cierre documental histórico se conserva en la sección 11.

## 1. Identificación y tipología

- **Nombre:** método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas.
- **Tipología:** composición método + instanciación (Design Science).
- **Base operativa:** ciclo de Girjoaba y Capiluppi (2024), con adaptaciones A01–A04 y selección proporcional, complementado por Feathers (2004), Fowler (2018) y Bass et al. (2021).
- **Contexto de instanciación:** subcircuito de creación de certificación en SIGPP (Caja Petrolera de Salud). Antecedente técnico en `feature/propuesta-tesis`, revisión `7c0bca08`; no es la referencia inicial o final de todos los episodios.
- **Episodios del método:** P01 sobre copia de master `7ef29a4f`; M-R1/P02 en la rama de evaluación correspondiente; aplicación adicional de importe por el autor desde `7ef29a4f`, con suplemento explícito. Referencias y estados de productos en las revisiones de cada episodio; no se presume un commit final cuando los cambios se recibieron locales.
- **Versión de la ficha:** actualización documental posterior a la recepción de P02 e importe; la formulación anterior y las decisiones del método se conservan en sus registros.

## 2. Problema que resuelve

**Problema de diseño:** en subcircuitos funcionales críticos de aplicaciones MVC heredadas, una decisión institucional se distribuye entre controlador, configuración, servicio y presentación, con duplicación y diferencias locales de validación, lo que dificulta delimitar y verificar cambios sin reescribir el sistema.

**Problema de investigación —registrado institucionalmente como problema científico—:** existen procedimientos incrementales (Feathers, el ciclo industrial, ADD), pero falta evidencia sobre qué adaptación requiere seleccionar y verificar incrementos en subcircuitos MVC heredados con decisiones distribuidas y restricciones institucionales. El método genera esa evidencia mediante su formalización y aplicación.

## 3. Requisitos

Método (R1–R10): selección proporcional, delimitación por decisión y consumidores, distinción observado–requerido–intención, caracterización, control/observación, reutilización de mecanismos, separación de costo inicial y evolución, revisión de dependencias, evaluación por escenarios y versionado.

Instanciación (R11–R14): frontera MVC incremental, autoridad de regla en servidor, criterios funcionales I01/I02/I04 y esfuerzo humano I03. Detalle completo en `07b_requisitos.md`.

## 4. Diseño y componentes

### 4.1. Pasos del método

P1 delimitar el incremento; P2 caracterizar el comportamiento; P3 hacer controlable la decisión con datos y dependencias pertinentes; P4 migrar sin retirar el original; P5 comprobar resultados normales, ausencia y fallos con sus efectos; P6 retirar el original y ajustar dependencias; P7 distinguir verificación local e integración en el entorno objetivo; P8 documentar, versionar y registrar mediciones previstas. Entradas, salidas y criterios en `07c_diseno_artefacto.md` y detalles operativos en el manual M-R1.

P3 exige instante solo cuando la decisión depende del tiempo. P7 mantiene estado parcial si falta integración; P8 distingue trazabilidad obligatoria de mediciones con protocolo, sin eliminar las medidas necesarias para una afirmación de mejora. Estas instrucciones no se atribuyen retrospectivamente al participante P01.

Roles: practicante (desarrollador), revisor independiente y fuente funcional.

### 4.2. Componentes de la instanciación

Los componentes de referencia incluyen `CreateCertificacionService` (coordinación), `CreateCertificacionInput` (entrada), `CreateCertificacionAutorizacionService` (autorización), el resolvedor focalizado, repositorios, DTOs y pruebas. Los selectores concretos difieren entre el antecedente, P01 y P02; el método no obliga a copiar un nombre de clase o una extracción específica. Reducir el controlador a coordinación y unificar la autoridad temporal son objetivos de la arquitectura de referencia, no resultados completamente construidos: la corrección temporal sigue pendiente. El detalle de responsabilidades y criterios está en `anexo_arquitectura_referencia_certificacion.md`; el cumplimiento efectivo, en E9 T01–T14.

## 5. Decisiones y alternativas descartadas

- **M1 (aplicación literal del ciclo):** descartada para esta propuesta porque no explicita por sí sola las adaptaciones que el estudio decidió examinar; aplicar un antecedente no se convierte automáticamente en aporte original.
- **M3 (migración estructural amplia):** descartada; contradice el alcance y exige independencia de Symfony/Doctrine no sostenible.
- **Arquitectónica A (extracciones sin contrato):** descartada; desplaza sin verificar.
- **Arquitectónica C (núcleo con puertos y adaptadores):** descartada; costo desproporcionado.
- **Elegida:** M2 (adaptación acotada) + B (frontera incremental).

## 6. Versiones

V1 (antecedente de marzo de 2025, evaluado formativamente en octubre de 2026); V2 (comprobaciones de la decisión temporal, octubre–noviembre); V3 (consolidación del método y de la evidencia). Detalle en `07d_plan_construccion.md`.

Para el rediseño posterior se identifican separadamente M-P01 (instrucciones efectivamente recibidas por el participante) y M-R1 (cuatro ajustes aprobados tras su aplicación). No son nuevas denominaciones del software V1–V3. P01 tiene productos y ratificación recibidos y M-R1 cuenta con P02 posterior; importe examina otra decisión con ejecución del autor y suplemento identificado. PA1–PA3 se formulan después del análisis de resultados, no como otro método o una versión recibida retrospectivamente por los participantes.

## 7. Verificación interna

Los conteos siguientes pertenecen al antecedente técnico; no son la batería vigente de todas las ramas ni la evaluación completa del método:

- `make test`: 188 pruebas, 540 aserciones, PHPUnit 9.6.15.
- `vendor/bin/phpunit tests/Certificacion`: 37 pruebas, 305 aserciones.
- PHP 7.4.29; `git diff --check` sin errores.
- Prueba directa del servicio principal con dobles; comprobaciones aisladas de la decisión temporal en E6.

La evidencia posterior se mantiene por episodio: P01, batería reproducida 183/341/1 omitida; P02, dos clases nuevas reproducidas 7/18 y 7/11, batería final conservada 173/289/1 omitida; importe, prueba final reproducida 5/25 y batería 164/285/1 omitida. Los numeradores son pruebas/aserciones según sus revisiones y las omisiones no cuentan como éxito. No se suman esas baterías ni se utilizan para afirmar mejoras de atributos no medidos.

## 8. Instrucciones de uso

Para aplicar el método a otro subcircuito, seguir P1–P8 en orden, con el revisor independiente en P1/P5 y la fuente funcional ratificando las reglas en P2. Para reproducir la instanciación: clonar SIGPP en la revisión `7c0bca08`, ejecutar `make test` y la batería de certificación en un contenedor con PHP 7.4.29 y PHPUnit 9.6.15. No se requieren credenciales productivas; las comprobaciones usan dobles y datos ficticios.

Para aplicar el método a otra decisión, utilice el manual operativo M-R1 y prepare referencia de código, necesidad, actores, datos, ayudas y comprobaciones antes de transformar. Los comandos del antecedente o P01 no se trasladan automáticamente a otra PC o rama: cada episodio registra su contenedor/configuración y material. Conserve productos, pruebas, salidas y registros antes de limpiar copias, especialmente cuando no exista un commit final; no se certifica disponibilidad pública de originales sensibles. Repetir una batería no sustituye observar la aplicación del método.

P01 se conserva por separado sobre master `7ef29a4f`; su material no se reemplaza retrospectivamente por M-R1. P02 usa la base local y datos/efectos autorizados documentados en su revisión, sin asumir anonimización completa. Importe se realiza en `eval/metodo-mr1-importe-autor`, con guía, registro progresivo y cinco escenarios aceptados antes de transformar; el anexo académico muestra decisiones y límites. La autoría asistida, el punto de observación, la coexistencia relatada y lo que se reproduce posteriormente deben quedar separados en cualquier reproducción o informe.

## 9. Limitaciones conocidas

- I04 (modificabilidad por ampliación de ventana) no se midió: su precondición, una capacidad extraordinaria existente, no está construida.
- La corrección del límite mensual 8/9 no se implementó; es un hallazgo del diagnóstico, no una solución entregada.
- La cronología: la separación a `src/Service` es de marzo de 2025, anterior al encuadre; la tesis la evalúa, no la reclama como construcción propia.
- Los niveles de verificación difieren: P01 no acredita integración real, P02 dispone de procedimientos/salidas de integración en su alcance y de controlador directo, e importe usa consumidor con dobles y configuración. No se afirma HTTP completo o atomicidad por esas comprobaciones.
- No hubo evaluación de campo; P02 es valoración controlada posterior con alcance asistido. E8/E9 están cerradas en sus alcances y E10 tiene PA1–PA3 y conclusiones adoptados. La ficha no convierte esa adopción en aprobación institucional o cumplimiento integral de metas técnicas.

## 10. Relación con la base de conocimiento

Girjoaba y Capiluppi (2024) aportan la secuencia operativa; Feathers (2004) la caracterización y la separación mínima para probar; Fowler (2018) la distinción entre transformación conservadora y capacidad nueva; Bass et al. (2021) el razonamiento por escenarios y atributos. Las adaptaciones A01–A04 y el paso P8 son aportes del estudio, declarados como tales y no atribuidos a los antecedentes. Referencias completas en `referencias.md`.

## 11. Gate de E7f

El gate exige que otro investigador pueda entender y reproducir el artefacto desde esta ficha sin acceso al tesista. Las secciones anteriores proponen ese cumplimiento. Corresponde al tesista validar o corregir, en particular si alguna instrucción de uso no es ejecutable tal como está escrita.

**Cierre, 4 de noviembre de 2026:** el tesista valida la ficha y confirma su comprensión del término «dobles de prueba»: los *mocks* de las pruebas unitarias, objetos sustitutos que verifican interacciones sin tocar la persistencia real. El gate de E7f se cumple: la ficha permite a otro investigador entender y reproducir el artefacto sin acceso al tesista.
