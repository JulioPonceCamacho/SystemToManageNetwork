import sys
import os
from cx_Freeze import setup, Executable

# ADD FILES
files = ['TESJo.ico','Imagenes/','Iconos/','modulos/','Dependencias']

# TARGET
target = Executable(
    script="main.py",
    base=None,
    icon="TESJo.ico"
)

# SETUP CX FREEZE
setup(
    name = "MGRSystem",
    version = "1.0",
    description = "Aplicación para el monitoreo y Gestión de red",
    author = "Julio Ponce Camacho",
    options = {'build_exe' : {'include_files' : files}},
    executables = [target]
    
)
