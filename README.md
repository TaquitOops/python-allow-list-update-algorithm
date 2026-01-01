# Algoritmo de Actualización de Listas de Acceso en Python

## Descripción del Proyecto
Este proyecto consiste en un algoritmo desarrollado en Python para automatizar la gestión de permisos de red en un entorno de atención sanitaria. El objetivo principal es identificar y eliminar direcciones IP no autorizadas de una "lista de permitidos" (allow list) basándose en una "lista de eliminación" (remove list). Esta automatización garantiza que solo el personal autorizado mantenga acceso a la subred restringida con registros de pacientes sensibles.

## Escenario
Como profesional de seguridad, mi tarea es mantener actualizado el archivo `allow_list.txt`. El acceso se revoca regularmente para empleados que cambian de rol o abandonan la organización. Este script procesa ambos archivos y genera una lista actualizada de forma segura y eficiente.

## Tecnologías Utilizadas
* **Lenguaje:** Python 3.x
* **Manejo de Archivos:** Sentencia `with` y métodos `open()`, `.read()`, `.write()`.
* **Estructuras de Datos:** Listas y Cadenas (Strings).
* **Lógica de Control:** Bucles `for` y condicionales `if`.

## Explicación del Algoritmo

### 1. Apertura y Lectura del Archivo
Utilizo la sentencia `with` para abrir el archivo `allow_list.txt` de manera segura. Esto garantiza que el archivo se cierre automáticamente tras la operación.
```python
with open(import_file, "r") as file:
    ip_addresses = file.read()
```
### 2. Procesamiento de Datos
Para poder manipular las direcciones IP, convierto la cadena de texto obtenida en una lista utilizando el método .split().
```python
ip_addresses = ip_addresses.split()
```
### 3. Lógica de Eliminación
Itero a través de la lista de direcciones IP que deben ser eliminadas. Si la dirección se encuentra en la lista de permitidos, utilizo el método .remove() para darla de baja.
```python
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)
```
### 4. Actualización del Archivo Original
Finalmente, convierto la lista actualizada de nuevo a una cadena separada por saltos de línea (\n) y sobrescribo el archivo original utilizando el modo "w" (escritura).
```python
ip_addresses = "\n".join(ip_addresses)
with open(import_file, "w") as file:
    file.write(ip_addresses)
```
## Resumen Operativo
Este algoritmo reduce el riesgo de errores humanos en la administración de accesos y mejora la postura de seguridad de la organización. Al integrar métodos de transformación de datos y manejo seguro de archivos, la solución es escalable para gestionar listas de acceso de mayor volumen.
