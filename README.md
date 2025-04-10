# Proyecto Personal y Referencia de Algebra Lineal

Este repositorio esta creado con el objetivo de tener una referencia a la 
magnitud del proyecto final de la futura clase "Algebra Lineal", esto con
el objetivo de aprender y tener una referencia de como realizarlo.

```bash
⚠️EL PROYECTO NO ES DE LA MISMA MAGNITUD QUE EL DE LA CLASE
```

## Configuración del Entorno Virtual

Para levantar el servidor local, se necesita crear y activar un entorno virtual. Sigue los pasos a continuación:

### Paso 1: Crear el entorno virtual

Ejecute el siguiente comando dentro del directorio de su proyecto:

```bash
python -m venv venv
```

Esto creará una carpeta llamada `venv` dentro del directorio donde se ejecutó el comando, que servirá como el entorno virtual.

### Paso 2: Activar el entorno virtual

Dependiendo del sistema operativo y la terminal que estés utilizando, usa uno de los siguientes comandos:

- **PowerShell (Windows):**
  ```powershell
  .\venv\Scripts\Activate
  ```
- **CMD (Windows):**
  ```cmd
  venv\Scripts\activate
  ```

Cuando el entorno virtual esté activado, el prompt de la terminal cambiará para reflejarlo, por ejemplo:

```
(venv) PS C:\Users\username\OneDrive\Desktop\Algebra-Lineal>
```

### Paso 3: Instalar las dependencias

Ejecute el siguiente comando para instalar todas las dependencias:

```bash
pip install -r requirements.py
```

## Nota

Para desactivar el entorno virtual, simplemente ejecute en la terminal:

```bash
deactivate
```