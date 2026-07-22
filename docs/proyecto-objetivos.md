# DISEÑO DEL PROYECTO


Durante el último año, el Banco Financiero XYZ ha experimentado un incremento en el número de transacciones catalogadas como fraudulentas. Aunque el porcentaje de fraude representa una fracción del total de operaciones, las pérdidas económicas, los costos de investigación y el impacto en la confianza de los clientes han aumentado de manera significativa.

Actualmente, el banco dispone de información histórica sobre sus clientes y de un registro de transacciones previamente clasificadas como fraudulentas y no fraudulentas. Sin embargo, la organización aún no cuenta con un análisis que permita comprender qué características comparten los casos de fraude ni cuáles son los perfiles de mayor riesgo.

La Gerencia de Riesgos y el área de Analítica requieren un estudio que transforme estos datos en información útil para fortalecer sus estrategias de prevención y mejorar la toma de decisiones.


# Problema de negocio

El banco no conoce con precisión qué factores están asociados a las transacciones fraudulentas y, en consecuencia, enfrenta dificultades para definir controles preventivos más efectivos y optimizar la asignación de recursos destinados al monitoreo de operaciones sospechosas



Como entregable principal esperan:

* Comprender mejor el comportamiento de las transacciones fraudulentas.
* Priorizar recursos de monitoreo sobre los perfiles de mayor riesgo.
* Diseñar controles preventivos más efectivos.
* Reducir pérdidas económicas asociadas al fraude.
* Contar con información objetiva para futuras iniciativas de analítica avanzada y modelos de Machine Learning.

> Para cumplir con el objetivo aplicaremos la **metodología de Discovery** y las **técnicas de Business Analytics (BA)**

---

## OBJETIVO

Realizar un análisis exploratorio de datos (EDA) sobre las transacciones históricas del banco con el fin de identificar patrones, tendencias y características asociadas al fraude, generando información que apoye la toma de decisiones del área de riesgos.

---


## KPIs

| KPI                                                | ¿Qué mide?                                              | Valor para el negocio                            |
| -------------------------------------------------- | --------------------------------------------------------- | ------------------------------------------------ |
| **Total de transacciones**                   | Número total de operaciones analizadas                   | Dimensiona el volumen de negocio                 |
| **Total de transacciones fraudulentas**      | Cantidad de operaciones marcadas como fraude              | Mide el problema a analizar                      |
| **Tasa de fraude (%)**                       | Fraudes / Total de transacciones × 100                   | Principal indicador de riesgo                    |
| **Distribución del fraude por segmento**    | Porcentaje de fraude por tipo de cliente                  | Identifica segmentos críticos                   |
| **Distribución del fraude por canal**       | Incidencia de fraude según el canal utilizado            | Permite fortalecer controles específicos        |
| **Distribución del fraude por país**       | Frecuencia de fraude por país                            | Detecta zonas geográficas de mayor riesgo       |
| **Edad promedio de clientes con fraude**     | Perfil demográfico de clientes afectados                 | Ayuda a caracterizar el riesgo                   |
| **Ingresos promedio de clientes con fraude** | Perfil económico de los casos de fraude                  | Permite identificar patrones                     |
| **Top variables asociadas al fraude**        | Variables con mayor relación con la ocurrencia de fraude | Insumo para futuras reglas o modelos predictivos |

---

## DATOS

dato/brutos/train.csv

dato/brutos/test.csv

---

## PREGUNTAS SEMILLA

* ¿Cuál es la proporción de transacciones fraudulentas respecto al total de operaciones?
* ¿Existen segmentos de clientes con mayor incidencia de fraude?
* ¿Hay rangos de ingresos o edades donde el fraude sea más frecuente?
* ¿Qué canales de transacción presentan mayor riesgo?
* ¿Existen diferencias significativas entre países o regiones?
* ¿Qué variables parecen estar más relacionadas con la ocurrencia de fraude?
* ¿Qué información puede utilizar el banco para fortalecer sus mecanismos de control?
