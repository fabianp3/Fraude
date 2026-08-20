# RESUMEN EJECUTIVO: DETECCIÓN DE FRAUDE BANCARIO

**Para:** Gerencia General  
**Fecha:** 19 de Agosto de 2026

---

## ¿Qué encontramos?

El fraude no está distribuido al azar: se concentra en **puntos específicos** de operación.

- **País:** Estados Unidos concentra el **70.5%** de los fraudes detectados.
- **Canal:** Los cajeros automáticos internacionales (ATM_INT) representan el **67.9%** de los casos.
- **Segmento:** Los clientes "Personal" tienen una incidencia de fraude del **44.3%**.
- **Edad:** Mayor riesgo en clientes de 20-29 años (31.5%) y 70-79 años (32.7%).
- **Ingresos:** Clientes con ingresos bajos (0-2M) presentan un 40.9% de los casos.

**Conclusión de negocio:** el fraude está más ligado al **canal y ubicación de la transacción** que al perfil demográfico del cliente. Esto permite enfocar controles en puntos concretos en vez de vigilar a todos los clientes por igual.

---

## ¿Qué modelo funciona mejor?

Se probaron 3 modelos. El más efectivo es **XGBoost**, que logra:

- **Detecta 89% de los fraudes reales** (antes se perdían muchos más).
- **78% de precisión**, es decir, la mayoría de las alertas que genera son fraudes reales.
- Reduce las falsas alarmas en un **93%** frente a un enfoque manual/tradicional.

---

## ¿Cuál es el impacto para el negocio?

Con base en un volumen estimado de 10,000 transacciones/mes:

| Indicador | Antes | Con el modelo | Mejora |
|---|---|---|---|
| Fraudes detectados | 60% | 89% | **+48%** |
| Fraudes no detectados | 80 casos | 22 casos | **-72%** |
| Falsas alarmas | 500 casos | 36 casos | **-93%** |
| Carga de revisión manual | 620 casos | 214 casos | **-65%** |

**Ahorro estimado: ~$116 millones COP al mes** solo en fraudes evitados, sin contar la reducción de horas de revisión manual.

---

## ¿Qué se necesita para llevarlo a producción?

1. **Aprobar** el desarrollo del modelo XGBoost (umbral de decisión 0.4).
2. **Iniciar un piloto** de 2 meses en modo de observación (sin bloquear transacciones), enfocado en ATM internacionales y transacciones en EE.UU.
3. **Activar gradualmente** por segmentos, ampliando cobertura según resultados.
4. **Monitorear y reentrenar el modelo mensualmente** para mantener su efectividad.

**Inversión estimada:** equipo técnico dedicado por 3-4 meses + infraestructura cloud (~$2,000-5,000 USD/mes).

---

## Recomendación final

Aprobar la implementación en fases del modelo XGBoost. El riesgo es bajo (piloto no intrusivo primero) y el retorno esperado es alto, tanto en pérdidas evitadas como en eficiencia operativa del equipo de fraude.

*Informe detallado disponible en: `Informe_Ejecutivo_Deteccion_Fraude.md`*
