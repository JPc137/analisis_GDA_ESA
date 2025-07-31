#!/usr/bin/env python3
'''
Analisis_GDA_ESA - Script Principal
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
    """Verifica que la estructura del proyecto esté completa"""
    print(f"🔍 Verificando estructura del proyecto: Analisis_GDA_ESA")
    print(f"📅 Fecha: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("-" * 60)
    
    # Carpetas críticas que deben existir
    carpetas_criticas = [
        "config",
        "data/raw_Analisis_GDA_ESA",
        "data/processed_Analisis_GDA_ESA",
        "data/outputs",
        "scripts/python/core",
        "scripts/gee",
        "documentation_MIAs"
    ]
    
    estructura_ok = True
    for carpeta in carpetas_criticas:
        if os.path.exists(carpeta):
            print(f"✅ {carpeta}")
        else:
            print(f"❌ {carpeta} - NO ENCONTRADO")
            estructura_ok = False
    
    if estructura_ok:
        print("\n🎉 Estructura del proyecto verificada correctamente")
    else:
        print("\n⚠️  Faltan algunas carpetas críticas del proyecto")
    
    return estructura_ok

def inicializar_configuracion():
    """Inicializa la configuración del proyecto"""
    config_file = "config/config.json"
    
    if os.path.exists(config_file):
        print(f"📋 Configuración encontrada: {config_file}")
    else:
        print(f"⚠️  Archivo de configuración no encontrado: {config_file}")
    
    # Verificar credenciales
    cred_dir = "config/credentials"
    if os.path.exists(cred_dir):
        cred_files = os.listdir(cred_dir)
        if cred_files:
            print(f"🔐 Archivos de credenciales: {len(cred_files)} encontrados")
        else:
            print("⚠️  No se encontraron archivos de credenciales")
    
def main():
    """Función principal del proyecto"""
    print("🌲" * 20)
    print(f"   PROYECTO: ANALISIS_GDA_ESA")
    print(f"   MONITOREO FORESTAL")
    print("🌲" * 20)
    
    # Verificar estructura
    if not verificar_estructura_proyecto():
        print("\n❌ No se puede continuar con estructura incompleta")
        return
    
    # Inicializar configuración
    print("\n" + "=" * 60)
    inicializar_configuracion()
    
    # Aquí agregar la lógica específica del proyecto
    print("\n" + "=" * 60)
    print("🚀 Proyecto listo para desarrollo")
    print("\n📝 Próximos pasos sugeridos:")
    print("   1. Configurar credenciales en config/credentials/")
    print("   2. Agregar datos iniciales en data/raw_Analisis_GDA_ESA/")
    print("   3. Revisar documentación en documentation_MIAs/")
    print("   4. Desarrollar scripts específicos en scripts/python/")
    
    print("\n✨ ¡Proyecto inicializado exitosamente!")

if __name__ == "__main__":
    main()