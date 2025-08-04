# Analisis_GDA_ESA

## Descripción
Proyecto de monitoreo forestal con análisis geoespacial desarrollado con herramientas avanzadas de procesamiento de datos espaciales.

## Estructura del Proyecto
- `config/`: Configuración y credenciales
- `data/`: Datos organizados por tipo y estado de procesamiento
  - `raw_Analisis_GDA_ESA/`: Datos originales (NUNCA modificar)
  - `processed_Analisis_GDA_ESA/`: Datos procesados y validados
  - `temp_Analisis_GDA_ESA/`: Archivos temporales
  - `outputs/`: Resultados finales y productos
- `scripts/`: Scripts Python, ArcGIS y Google Earth Engine
- `documentation_MIAs/`: Documentación técnica y SOPs


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
venv\Scripts\activate     # Windows

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
git commit -m "Estructura inicial del proyecto Analisis_GDA_ESA"
```

## Uso
```bash
# Ejecutar análisis principal
python main.py

# Ejecutar pruebas
python -m pytest testing/

# Ver documentación
# Revisar documentation_MIAs/Analisis_GDA_ESA_sop/
```

## Autor y Fecha
- **Proyecto**: Analisis_GDA_ESA
- **Creado**: 2025-07-31 08:58:52
- **Generador**: Sistema automatizado de estructura de proyectos forestales

## Notas Importantes
- Los datos originales en `raw_Analisis_GDA_ESA/` NUNCA deben modificarse
- Usar siempre Git LFS para archivos grandes (*.tif, *.shp, etc.)
- Documentar todos los procedimientos en los SOPs correspondientes
