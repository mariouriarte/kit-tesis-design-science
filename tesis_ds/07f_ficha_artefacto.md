# E7f. Ficha del artefacto

**Estado:** en curso. Esta ficha es el documento de diseño reproducible que servirá de anexo. Debe permitir a otro investigador entender y reproducir el artefacto sin acceso al tesista. Consolida lo formalizado en E7a–E7e; no añade decisiones nuevas.

## 1. Identificación y tipología

- **Nombre:** método de refactorización arquitectónica incremental para subcircuitos de aplicaciones MVC heredadas.
- **Tipología:** composición método + instanciación (Design Science).
- **Base operativa:** ciclo de Girjoaba y Capiluppi (2024), con adaptaciones A01–A04 y selección proporcional, complementado por Feathers (2004), Fowler (2018) y Bass et al. (2021).
- **Instanciación:** subcircuito de creación de certificación en SIGPP (Caja Petrolera de Salud), rama `feature/propuesta-tesis`, revisión `7c0bca08`.
- **Versión de la ficha:** consolidada al 4 de noviembre de 2026.

## 2. Problema que resuelve

**Problema de diseño:** en subcircuitos funcionales críticos de aplicaciones MVC heredadas, una decisión institucional se distribuye entre controlador, configuración, servicio y presentación, con duplicación y diferencias locales de validación, lo que dificulta delimitar y verificar cambios sin reescribir el sistema.

**Problema de investigación —registrado institucionalmente como problema científico—:** existen procedimientos incrementales (Feathers, el ciclo industrial, ADD), pero falta evidencia sobre qué adaptación requiere seleccionar y verificar incrementos en subcircuitos MVC heredados con decisiones distribuidas y restricciones institucionales. El método genera esa evidencia mediante su formalización y aplicación.

## 3. Requisitos

Método (R1–R10): selección proporcional, delimitación por decisión y consumidores, distinción observado–requerido–intención, caracterización, control/observación, reutilización de mecanismos, separación de costo inicial y evolución, revisión de dependencias, evaluación por escenarios y versionado.

Instanciación (R11–R14): frontera MVC incremental, autoridad de regla en servidor, criterios funcionales I01/I02/I04 y esfuerzo humano I03. Detalle completo en `07b_requisitos.md`.

## 4. Diseño y componentes

### 4.1. Pasos del método

P1 delimitar el incremento; P2 caracterizar el comportamiento; P3 hacer controlable la decisión; P4 migrar sin retirar el original; P5 probar comportamiento y efectos; P6 retirar el original y ajustar dependencias; P7 integrar y verificar; P8 registrar costo y versionar. Entradas, salidas y criterios de cada paso en `07c_diseno_artefacto.md`.

Roles: practicante (desarrollador), revisor independiente y fuente funcional.

### 4.2. Componentes de la instanciación

`CreateCertificacionService` (coordinación), `CreateCertificacionInput` (entrada), `CreateCertificacionAutorizacionService` (autorización), `RestriccionSubPartidaResolver` (regla focalizada), repositorios, DTOs y archivos de prueba. El controlador se reduce a coordinación HTTP; la autoridad de la regla temporal reside en el servidor.

## 5. Decisiones y alternativas descartadas

- **M1 (aplicación literal del ciclo):** descartada; es ingeniería sin decisión propia que evaluar.
- **M3 (migración estructural amplia):** descartada; contradice el alcance y exige independencia de Symfony/Doctrine no sostenible.
- **Arquitectónica A (extracciones sin contrato):** descartada; desplaza sin verificar.
- **Arquitectónica C (núcleo con puertos y adaptadores):** descartada; costo desproporcionado.
- **Elegida:** M2 (adaptación acotada) + B (frontera incremental).

## 6. Versiones

V1 (antecedente de marzo de 2025, evaluado formativamente en octubre de 2026); V2 (comprobaciones de la decisión temporal, octubre–noviembre); V3 (consolidación del método y de la evidencia). Detalle en `07d_plan_construccion.md`.

## 7. Verificación interna

- `make test`: 188 pruebas, 540 aserciones, PHPUnit 9.6.15.
- `vendor/bin/phpunit tests/Certificacion`: 37 pruebas, 305 aserciones.
- PHP 7.4.29; `git diff --check` sin errores.
- Prueba directa del servicio principal con dobles; comprobaciones aisladas de la decisión temporal en E6.

## 8. Instrucciones de uso

Para aplicar el método a otro subcircuito, seguir P1–P8 en orden, con el revisor independiente en P1/P5 y la fuente funcional ratificando las reglas en P2. Para reproducir la instanciación: clonar SIGPP en la revisión `7c0bca08`, ejecutar `make test` y la batería de certificación en un contenedor con PHP 7.4.29 y PHPUnit 9.6.15. No se requieren credenciales productivas; las comprobaciones usan dobles y datos ficticios.

## 9. Limitaciones conocidas

- I04 (modificabilidad por ampliación de ventana) no se midió: su precondición, una capacidad extraordinaria existente, no está construida.
- La corrección del límite mensual 8/9 no se implementó; es un hallazgo del diagnóstico, no una solución entregada.
- La cronología: la separación a `src/Service` es de marzo de 2025, anterior al encuadre; la tesis la evalúa, no la reclama como construcción propia.
- La verificación usa dobles y datos ficticios; no acredita persistencia real, respuesta HTTP ni atomicidad en base.
- La evaluación sumativa prevista es más débil que el estándar pleno de maestría; las condiciones de contorno se declaran en E8 y E10.

## 10. Relación con la base de conocimiento

Girjoaba y Capiluppi (2024) aportan la secuencia operativa; Feathers (2004) la caracterización y la separación mínima para probar; Fowler (2018) la distinción entre transformación conservadora y capacidad nueva; Bass et al. (2021) el razonamiento por escenarios y atributos. Las adaptaciones A01–A04 y el paso P8 son aportes del estudio, declarados como tales y no atribuidos a los antecedentes. Referencias completas en `referencias.md`.

## 11. Gate de E7f

El gate exige que otro investigador pueda entender y reproducir el artefacto desde esta ficha sin acceso al tesista. Las secciones anteriores proponen ese cumplimiento. Corresponde al tesista validar o corregir, en particular si alguna instrucción de uso no es ejecutable tal como está escrita.

**Cierre, 4 de noviembre de 2026:** el tesista valida la ficha y confirma su comprensión del término «dobles de prueba»: los *mocks* de las pruebas unitarias, objetos sustitutos que verifican interacciones sin tocar la persistencia real. El gate de E7f se cumple: la ficha permite a otro investigador entender y reproducir el artefacto sin acceso al tesista.
