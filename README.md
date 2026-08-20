# Deteccion de Fraude Bancario

Repositorio del proyecto de analitica para explorar patrones de fraude bancario y desarrollar un modelo predictivo de apoyo a la toma de decisiones.

## Estructura

- `docs/`: objetivos del proyecto, planteamiento de negocio y KPIs.
- `notebooks/`: analisis exploratorio y modelado.
- `entregables/informes/`: resumen ejecutivo e informe detallado en Markdown.
- `datos/`: datos brutos, intermedios y procesados. No se versionan por tamano y confidencialidad.
- `funciones/`: espacio para utilidades reutilizables del proyecto.

## Contenido versionado

Este repositorio esta configurado para subir a GitHub:

- documentacion del proyecto;
- notebooks de analisis y modelado;
- informes ejecutivos en formato Markdown.

No se suben los datos, archivos pesados, logs ni carpetas de entorno local.

## Archivos clave

- `docs/proyecto-objetivos.md`
- `notebooks/EDA_Fraude.ipynb`
- `notebooks/modelado_fraude.ipynb`
- `entregables/informes/Resumen_Ejecutivo_Corto_Fraude.md`
- `entregables/informes/Informe_Ejecutivo_Deteccion_Fraude.md`

## Flujo recomendado de Git

```bash
git status
git add README.md .gitignore docs/ notebooks/ entregables/informes/
git commit -m "Organiza estructura del repositorio para GitHub"
git push origin main
```

## Nota sobre el remoto

El remoto actual apunta a un marcador de posicion:

```bash
https://github.com/TU_USUARIO/Fraude.git
```

Antes de hacer `push`, actualizalo con la URL real de tu repositorio:

```bash
git remote set-url origin https://github.com/TU_USUARIO_REAL/Fraude.git
```