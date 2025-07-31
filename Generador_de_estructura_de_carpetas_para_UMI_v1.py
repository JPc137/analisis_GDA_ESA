#!/usr/bin/env python3
"""
Generador de Estructura de carpetas para Proyectos de la GTSMRV - para las UMIs de Monitoreo Forestal
Creación de carpetas, archivos y configuración inicial para proyectos de monitoreo forestal con análisis geoespacial.

Versión: v1.0
Fecha: 2025/07/30
Autor: Juan Pablo Avila
Contacto: pablo.dealba@conafor.gob.mx
"""

import os
import sys
from datetime import datetime

def create_project(project_name):
    """Crea la estructura completa del proyecto"""
    
    print(f"\n🌲 Creando proyecto: {project_name} 🌲")
    print("="*50)
    
    # Lista de todas las carpetas a crear
    folders = [
        
        # Data
        f"data/raw_{project_name}/vectorial/",  #nunca modificar
        f"data/raw_{project_name}/raster/",     #nunca modificar
        f"data/raw_{project_name}/tabular",     #nunca modificar
        f"data/processed_{project_name}/vectorial_procesada/",
        f"data/processed_{project_name}/raster_procesada",
        f"data/processed_{project_name}/tabular_procesada",
        f"data/temp_{project_name}/",
        f"outputs/{project_name}_análisis_geo",
        f"outputs/{project_name}_mapas",
        f"outputs/{project_name}_figuras",
        f"outputs/{project_name}_statistics",
        
        # Scripts
        "scripts",
        # notebooks
        "notebooks",
        
        # Documentation
        f"documentation_MIAs/{project_name}_sop",
        f"documentation_MIAs/{project_name}_technical",
        f"documentation_MIAs/{project_name}_metadata",
        
        # Reports
        f"outputs/reports_{project_name}/{datetime.now().year}",
        
        # Git config
        "git_config",
        
        # Environments
        "environments/docker",
        "environments/conda",
        "environments/virtualenv",
    ]
    
    # Crear carpetas
    base_path = os.path.join(os.getcwd(), project_name)
    
    for folder in folders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"✓ {folder}")
    
    # Crear archivos
    print("\n📄 Creando archivos principales...")
    create_all_files(base_path, project_name)
    
    print("\n" + "="*50)
    print(f"✅ PROYECTO '{project_name}' CREADO EXITOSAMENTE")
    print(f"📁 Ubicación: {base_path}")
    print("\n🚀 Próximos pasos:")
    print(f"   1. cd {project_name}")
    print(f"   2. pip install -r requirements.txt")
    print(f"   3. git init")
    print(f"   4. python main.py")
    print("="*50)

def create_all_files(base_path, project_name):
    """Crea todos los archivos del proyecto"""
    
    # README.md
    readme_content = f"""# {project_name}

## Descripción
Proyecto de monitoreo forestal con análisis geoespacial desarrollado con herramientas avanzadas de procesamiento de datos espaciales.

## Estructura del Proyecto
- `config/`: Configuración y credenciales
- `data/`: Datos organizados por tipo y estado de procesamiento
  - `raw_{project_name}/`: Datos originales (NUNCA modificar)
  - `processed_{project_name}/`: Datos procesados y validados
  - `temp_{project_name}/`: Archivos temporales
  - `outputs/`: Resultados finales y productos
- `scripts/`: Scripts Python, ArcGIS y Google Earth Engine
- `documentation_MIAs/`: Documentación técnica y SOPs
- `reports/`: Reportes generados por fecha
- `testing/`: Pruebas unitarias e integración

## Tecnologías Utilizadas
- **Python**: Procesamiento y análisis de datos
- **Google Earth Engine**: Análisis de imágenes satelitales
- **ArcGIS Pro**: Análisis espacial avanzado
- **Git**: Control de versiones con LFS para archivos grandes

## Instalación y Configuración

### 1. Instalar Dependencias
```bash
# Crear ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# o
venv\\Scripts\\activate     # Windows

# Instalar librerías
pip install -r requirements.txt
```

### 2. Configurar Credenciales
- Editar `config/credentials/gee_service_account.json`
- Configurar credenciales de ArcGIS Online en `config/credentials/`

### 3. Configurar Git con LFS
```bash
git init
git lfs install
git add .
git commit -m "Estructura inicial del proyecto {project_name}"
```

## Uso
```bash
# Ejecutar análisis principal
python main.py

# Ejecutar pruebas
python -m pytest testing/

# Ver documentación
# Revisar documentation_MIAs/{project_name}_sop/
```

## Autor y Fecha
- **Proyecto**: {project_name}
- **Creado**: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
- **Generador**: Sistema automatizado de estructura de proyectos forestales

## Notas Importantes
- Los datos originales en `raw_{project_name}/` NUNCA deben modificarse
- Usar siempre Git LFS para archivos grandes (*.tif, *.shp, etc.)
- Documentar todos los procedimientos en los SOPs correspondientes
"""
    
    # main.py
    main_content = f"""#!/usr/bin/env python3
'''
{project_name} - Script Principal
Monitoreo Forestal con Análisis Geoespacial
'''

import os
import sys
from datetime import datetime
from pathlib import Path

# Agregar directorio de scripts al path
script_dir = Path(__file__).parent / "scripts" / "python"
sys.path.append(str(script_dir))

def verificar_estructura_proyecto():
    \"\"\"Verifica que la estructura del proyecto esté completa\"\"\"
    print(f"🔍 Verificando estructura del proyecto: {project_name}")
    print(f"📅 Fecha: {{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}}")
    print("-" * 60)
    
    # Carpetas críticas que deben existir
    carpetas_criticas = [
        "config",
        "data/raw_{project_name}",
        "data/processed_{project_name}",
        "data/outputs",
        "scripts/python/core",
        "scripts/gee",
        "documentation_MIAs"
    ]
    
    estructura_ok = True
    for carpeta in carpetas_criticas:
        if os.path.exists(carpeta):
            print(f"✅ {{carpeta}}")
        else:
            print(f"❌ {{carpeta}} - NO ENCONTRADO")
            estructura_ok = False
    
    if estructura_ok:
        print("\\n🎉 Estructura del proyecto verificada correctamente")
    else:
        print("\\n⚠️  Faltan algunas carpetas críticas del proyecto")
    
    return estructura_ok

def inicializar_configuracion():
    \"\"\"Inicializa la configuración del proyecto\"\"\"
    config_file = "config/config.json"
    
    if os.path.exists(config_file):
        print(f"📋 Configuración encontrada: {{config_file}}")
    else:
        print(f"⚠️  Archivo de configuración no encontrado: {{config_file}}")
    
    # Verificar credenciales
    cred_dir = "config/credentials"
    if os.path.exists(cred_dir):
        cred_files = os.listdir(cred_dir)
        if cred_files:
            print(f"🔐 Archivos de credenciales: {{len(cred_files)}} encontrados")
        else:
            print("⚠️  No se encontraron archivos de credenciales")
    
def main():
    \"\"\"Función principal del proyecto\"\"\"
    print("🌲" * 20)
    print(f"   PROYECTO: {project_name.upper()}")
    print(f"   MONITOREO FORESTAL")
    print("🌲" * 20)
    
    # Verificar estructura
    if not verificar_estructura_proyecto():
        print("\\n❌ No se puede continuar con estructura incompleta")
        return
    
    # Inicializar configuración
    print("\\n" + "=" * 60)
    inicializar_configuracion()
    
    # Aquí agregar la lógica específica del proyecto
    print("\\n" + "=" * 60)
    print("🚀 Proyecto listo para desarrollo")
    print("\\n📝 Próximos pasos sugeridos:")
    print("   1. Configurar credenciales en config/credentials/")
    print("   2. Agregar datos iniciales en data/raw_{project_name}/")
    print("   3. Revisar documentación en documentation_MIAs/")
    print("   4. Desarrollar scripts específicos en scripts/python/")
    
    print("\\n✨ ¡Proyecto inicializado exitosamente!")

if __name__ == "__main__":
    main()
"""
    
    # requirements.txt COMPLETO
    requirements_content = """# ================================================
# LIBRERÍAS PRINCIPALES PARA ANÁLISIS GEOESPACIAL
# ================================================

# Procesamiento geoespacial básico
geopandas>=0.14.0
pandas>=2.0.0
numpy>=1.24.0
shapely>=2.0.0
pyproj>=3.6.0
rasterio>=1.3.0

# Visualización y mapas
matplotlib>=3.7.0
seaborn>=0.12.0
folium>=0.14.0
plotly>=5.15.0
contextily>=1.4.0

# Google Earth Engine
earthengine-api>=0.1.350

# Análisis estadístico y machine learning
scikit-learn>=1.3.0
scipy>=1.11.0
xarray>=2023.6.0
statsmodels>=0.14.0

# Procesamiento de imágenes
opencv-python>=4.8.0
scikit-image>=0.21.0
pillow>=10.0.0

# Bases de datos y formatos
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0
fiona>=1.9.0
pyogrio>=0.7.0

# Utilidades y productividad
tqdm>=4.65.0
python-dotenv>=1.0.0
pyyaml>=6.0
requests>=2.31.0
click>=8.1.0
rich>=13.5.0

# Desarrollo y testing
pytest>=7.4.0
pytest-cov>=4.1.0
black>=23.7.0
flake8>=6.0.0

# Jupyter y notebooks
jupyter>=1.0.0
ipykernel>=6.25.0
jupyterlab>=4.0.0

# Reportes y documentación
reportlab>=4.0.0
jinja2>=3.1.0
"""
    
    # .gitignore AVANZADO
    gitignore_content = """# ================================================
# CONFIGURACIÓN GIT PARA PROYECTOS FORESTALES GIS
# ================================================

# CREDENCIALES Y CONFIGURACIÓN SENSIBLE
config/credentials/*.json
config/credentials/*.key
config/credentials/*.pem
!config/credentials/*_template.json
.env
.env.local
.env.production
secrets.yaml

# DATOS GEOESPACIALES (MUY PESADOS PARA GIT)
data/raw_*/
data/temp_*/
data/processed_*/
!data/**/README.md
!data/**/metadata.xml

# Archivos específicos GIS
*.tif
*.tiff
*.tfw
*.img
*.bil
*.bip
*.bsq
*.shp
*.shx
*.dbf
*.prj
*.cpg
*.sbn
*.sbx
*.xml
*.aux
*.ovr
*.rrd
*.lyr
*.lyrx
*.qml
*.qgs

# Geodatabases y bases de datos
*.gdb/
*.mdb
*.accdb
*.sqlite
*.db

# ArcGIS
*.mxd.bak
*.aprx.bak
*.tbx.bak
*.style.bak
*.lyrx.bak
Scratch.gdb/
*.lock
*.sr.lock

# QGIS
*.qgs~
*.qgz

# PYTHON
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# AMBIENTES VIRTUALES
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/
conda_env/
.conda/

# JUPYTER NOTEBOOK
.ipynb_checkpoints
*.ipynb_checkpoints/
.jupyter/

# LOGS Y TEMPORALES
*.log
logs/
temp/
tmp/
*.tmp
*.temp
*.swp
*.swo

# CACHE Y COMPILADOS
*.cache
.cache/
.pytest_cache/
.coverage
htmlcov/
.tox/
.nox/

# SISTEMA OPERATIVO
# Windows
ehthumbs.db
Thumbs.db
Desktop.ini
$RECYCLE.BIN/

# macOS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
.fseventsd
.VolumeIcon.icns
.com.apple.timemachine.donotpresent

# Linux
*~
.directory
.Trash-*

# IDEs Y EDITORES
# VSCode
.vscode/
*.code-workspace

# PyCharm
.idea/
*.iws
*.iml
*.ipr

# Sublime Text
*.sublime-project
*.sublime-workspace

# Vim
*.swp
*.swo
*~
.netrwhist

# DOCUMENTOS TEMPORALES
~$*.docx
~$*.xlsx
~$*.pptx
.~lock.*

# ARCHIVOS DE CONFIGURACIÓN LOCAL
local_settings.py
local_config.json
"""
    
    # .gitattributes
    gitattributes_content = """# ================================================
# GIT LFS Y ATRIBUTOS PARA PROYECTOS FORESTALES
# ================================================

# GIT LFS - ARCHIVOS GRANDES AUTOMÁTICO
# Datos raster
*.tif filter=lfs diff=lfs merge=lfs -text
*.tiff filter=lfs diff=lfs merge=lfs -text
*.img filter=lfs diff=lfs merge=lfs -text
*.bil filter=lfs diff=lfs merge=lfs -text
*.bip filter=lfs diff=lfs merge=lfs -text
*.bsq filter=lfs diff=lfs merge=lfs -text

# Datos vectoriales grandes
*.shp filter=lfs diff=lfs merge=lfs -text
*.gdb/** filter=lfs diff=lfs merge=lfs -text

# Archivos comprimidos
*.zip filter=lfs diff=lfs merge=lfs -text
*.rar filter=lfs diff=lfs merge=lfs -text
*.7z filter=lfs diff=lfs merge=lfs -text
*.tar.gz filter=lfs diff=lfs merge=lfs -text

# Datos tabulares grandes (>10MB típicamente)
*.csv filter=lfs diff=lfs merge=lfs -text
*.xlsx filter=lfs diff=lfs merge=lfs -text
*.parquet filter=lfs diff=lfs merge=lfs -text

# Archivos de datos geoespaciales
*.geojson filter=lfs diff=lfs merge=lfs -text
*.kml filter=lfs diff=lfs merge=lfs -text
*.kmz filter=lfs diff=lfs merge=lfs -text
*.gpx filter=lfs diff=lfs merge=lfs -text

# Imágenes y multimedia
*.png filter=lfs diff=lfs merge=lfs -text
*.jpg filter=lfs diff=lfs merge=lfs -text
*.jpeg filter=lfs diff=lfs merge=lfs -text
*.bmp filter=lfs diff=lfs merge=lfs -text
*.gif filter=lfs diff=lfs merge=lfs -text
*.mp4 filter=lfs diff=lfs merge=lfs -text
*.avi filter=lfs diff=lfs merge=lfs -text
*.mov filter=lfs diff=lfs merge=lfs -text

# Modelos y datos científicos
*.nc filter=lfs diff=lfs merge=lfs -text
*.hdf filter=lfs diff=lfs merge=lfs -text
*.h5 filter=lfs diff=lfs merge=lfs -text

# CONFIGURACIÓN DE LÍNEAS DE FINAL
# Archivos de texto que siempre deben usar LF (Unix)
*.py text eol=lf
*.js text eol=lf
*.json text eol=lf
*.md text eol=lf
*.yml text eol=lf
*.yaml text eol=lf
*.txt text eol=lf
*.csv text eol=lf
*.sql text eol=lf
*.sh text eol=lf

# Archivos que siempre deben tratarse como binarios
*.exe binary
*.dll binary
*.so binary
*.dylib binary
*.pkl binary
*.pickle binary
"""
    
    # config.json
    config_content = f"""{{
    "project_info": {{
        "name": "{project_name}",
        "version": "1.0.0",
        "created_date": "{datetime.now().isoformat()}",
        "description": "Proyecto de monitoreo forestal con análisis geoespacial",
        "author": "Equipo de Monitoreo Forestal",
        "contact": "monitoreo@forestales.org"
    }},
    "spatial_config": {{
        "coordinate_system": "EPSG:4326",
        "utm_zone": "14N",
        "study_area": {{
            "name": "Área de estudio {project_name}",
            "bounds": {{
                "min_lat": 0.0,
                "max_lat": 0.0,
                "min_lon": 0.0,
                "max_lon": 0.0
            }}
        }}
    }},
    "data_sources": {{
        "satellite_imagery": {{
            "landsat": true,
            "sentinel2": true,
            "sentinel1": true,
            "modis": false
        }},
        "vector_data": {{
            "forest_boundaries": true,
            "protected_areas": true,
            "administrative_limits": true,
            "infrastructure": true
        }},
        "auxiliary_data": {{
            "dem": true,
            "climate_data": false,
            "soil_data": false
        }}
    }},
    "processing_config": {{
        "cloud_cover_threshold": 20,
        "temporal_range": {{
            "start_year": 2020,
            "end_year": 2024
        }},
        "spatial_resolution": 30,
        "buffer_distance_m": 100
    }},
    "output_config": {{
        "coordinate_system": "EPSG:32614",
        "raster_format": "GeoTIFF",
        "vector_format": "Shapefile",
        "compression": "LZW"
    }}
}}"""
    
    # environment.yml para conda
    environment_yml = f"""name: {project_name.lower()}
channels:
  - conda-forge
  - defaults
dependencies:
  - python>=3.9
  - geopandas
  - pandas
  - numpy
  - matplotlib
  - rasterio
  - folium
  - jupyter
  - scikit-learn
  - scipy
  - pip
  - pip:
    - earthengine-api>=0.1.350
    - python-dotenv
    - plotly>=5.15.0
    - tqdm
    - rich
"""
    
    # Crear todos los archivos
    files_to_create = [
        ("README.md", readme_content.strip()),
        ("main.py", main_content.strip()),
        ("requirements.txt", requirements_content.strip()),
        (".gitignore", gitignore_content.strip()),
        (".gitattributes", gitattributes_content.strip()),
        ("config/config.json", config_content.strip()),
        ("environments/environment.yml", environment_yml.strip())
    ]
    
    for file_path, content in files_to_create:
        full_path = os.path.join(base_path, file_path)
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ {file_path}")

def main():
    """Función principal con manejo de argumentos"""
    
    if len(sys.argv) < 2:
        print("❌ Error: Debes proporcionar el nombre del proyecto")
        print("Uso: python script.py 'NombreDelProyecto'")
        print("\nEjemplos:")
        print("  python script.py 'MonitoreoAmazonia2024'")
        print("  python script.py 'GDA_ESA_v1'")
        print("  python script.py 'BosquesUrbanos'")
        sys.exit(1)
    
    project_name = sys.argv[1]
    
    # Validar nombre del proyecto
    if not project_name or project_name.strip() == "":
        print("❌ Error: El nombre del proyecto no puede estar vacío")
        sys.exit(1)
    
    # Verificar si ya existe
    if os.path.exists(project_name):
        print(f"⚠️  El directorio '{project_name}' ya existe.")
        response = input("¿Deseas sobrescribir el contenido? (y/N): ")
        if response.lower() != 'y':
            print("Operación cancelada.")
            sys.exit(0)
    
    try:
        create_project(project_name)
    except Exception as e:
        print(f"❌ Error al crear el proyecto: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

if __name__ == "__main__":
    main()
