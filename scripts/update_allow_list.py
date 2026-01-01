# ----------------------------------------------------------------
# Proyecto: Algoritmo de Actualización de Lista de Permisos (IP)
# Descripción: Este script elimina direcciones IP no autorizadas 
#              de un archivo de texto de seguridad.
# ----------------------------------------------------------------

def update_file(import_file, remove_list):
    """
    Lee una lista de direcciones IP desde un archivo y elimina 
    aquellas que se encuentran en una lista de eliminación.
    """
    
    # 1. Abrir el archivo que contiene la lista de permitidos
    # Usamos la sentencia 'with' para asegurar el cierre automático del archivo
    with open(import_file, "r") as file:
        # 2. Leer el contenido del archivo y almacenarlo en una variable
        ip_addresses = file.read()

    # 3. Convertir la cadena de texto en una lista usando .split()
    # Esto permite iterar y eliminar elementos individuales
    ip_addresses = ip_addresses.split()

    # 4. Iterar a través de la lista de direcciones a eliminar
    for element in remove_list:
        # 5. Comprobar si la dirección IP está en la lista de permitidos
        if element in ip_addresses:
            # 6. Eliminar la dirección IP de la lista
            ip_addresses.remove(element)

    # 7. Convertir la lista de nuevo a una cadena separada por saltos de línea
    ip_addresses = "\n".join(ip_addresses)

    # 8. Abrir el archivo en modo escritura ('w') para actualizar el contenido
    with open(import_file, "w") as file:
        file.write(ip_addresses)
    
    print(f"El archivo '{import_file}' ha sido actualizado correctamente.")

# --- Configuración y Ejecución ---

# Ruta al archivo de datos (basado en la estructura sugerida)
path_to_file = "../data/allow_list.txt"

# Lista de direcciones IP que deben perder el acceso
ips_to_remove = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Llamada a la función principal
if __name__ == "__main__":
    update_file(path_to_file, ips_to_remove)
