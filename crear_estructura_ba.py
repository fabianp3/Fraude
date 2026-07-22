import os
from pathlib import Path

def crear_estructura():
    # Carpeta donde se encuentra este script
    base = Path(__file__).resolve().parent

    carpetas = [
        "datos/brutos",
        "datos/intermedios",
        "datos/procesados",
        "notebooks",
        "entregables/graficos",
        "entregables/informes",
        "entregables/dashboards",
        "funciones",
        "docs",
        ".github",  # para el archivo de instrucciones de Copilot
    ]

    for carpeta in carpetas:
        ruta = base / carpeta
        ruta.mkdir(parents=True, exist_ok=True)
        print(f"✅ Creada: {ruta}")

    # Crear .gitignore en la raíz (si no existe)
    gitignore_path = base / ".gitignore"
    if not gitignore_path.exists():
        gitignore_content = """# Archivos del sistema
desktop.ini
Thumbs.db

# Entornos
.env
.venv/
venv/
__pycache__/
*.py[cod]

# Jupyter
.ipynb_checkpoints/
.notebooks/

# Datos
datos/
*.csv
*.xlsx
*.parquet
*.feather
*.db
*.sqlite
*.duckdb

# Entregables
entregables/
reports/

# Archivos de log
*.log

# Configuración de IDE
.vscode/
.idea/
"""
        gitignore_path.write_text(gitignore_content, encoding="utf-8")
        print(f"✅ Creado: {gitignore_path}")
    else:
        print(f"ℹ️ Ya existe: {gitignore_path}")

    # Crear .github/copilot-instructions.md (si no existe)
    copilot_md_path = base / ".github" / "copilot-instructions.md"
    if not copilot_md_path.exists():
        copilot_md_content = (
            "- Me responderas siempre en español de España.\n"
            "- Comenzarás cada mensaje con este emogi 🤖 \n"
            "- Siempre genera código para el script abierto, nunca para la ventana interactiva, salvo que se indique explícitamente lo contrario.\n"
            "- La ventana interactiva solo se usará para verificar resultados o mensajes de error, pero no para generar código.\n"
            "- No expliques el código si no se solicita.\n"
        )
        copilot_md_path.write_text(copilot_md_content, encoding="utf-8")
        print(f"✅ Creado: {copilot_md_path}")
    else:
        print(f"ℹ️ Ya existe: {copilot_md_path}")

if __name__ == "__main__":
    crear_estructura()
