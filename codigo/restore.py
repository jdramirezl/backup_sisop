import os
import json
from tkinter import Tk 
from tkinter.filedialog import askdirectory

def valid_path(path):
    return os.path.exists(path) and os.path.isdir(path)

# def setup():
#     backup_folder = input("Ingrese la ruta de la carpeta de backup: ")
#     restore_folder = input("Ingrese la ruta de la carpeta de restauración: ")
#     restore(backup_folder, restore_folder)

def count_files(backup_folder):
    num_files = 0
    for filename in os.listdir(backup_folder):
        file_path = os.path.join(backup_folder, filename)
        if os.path.isfile(file_path):
            num_files += 1
    return num_files

def restore(backup_folder, restore_folder, backup_config):
    restored_files = 0
    num_files = backup_config["num_files"]
    
    print(f"Restaurando {num_files} archivos")
    
    for i in range(num_files):
        restored_files += 1
        restored_file_name = backup_config["files"][i]["file"]
        chunks = backup_config["files"][i]["chunks"]
        
        print(f"Restaurando {restored_file_name} en {restore_folder} en {chunks} fragmentos")
        
        for j in range(chunks):
            fragment_file = os.path.join(backup_folder, f"{restored_file_name}.{j + 1}.backup")
            
            # Verificar que exista el fragmento
            if not os.path.exists(fragment_file):
                print(f"Error: No se encontró el fragmento {i}.backup")
                return
            
            # Leemos el fragmento y lo escribimos en el archivo de recuerado
            with open(fragment_file, "rb") as f: # Leemos en bytes
                data = f.read()
                restored_file = os.path.join(restore_folder, restored_file_name) # Recreamos el archivo
                with open(restored_file, "ab") as restored_f: # Guardamos en bytes de neuvo
                    restored_f.write(data)
    
    return restored_files


def main(backup_folder, restore_folder):
    # Validar las rutas
    if not valid_path(backup_folder) or not valid_path(restore_folder):
        print("Error: Las rutas de la carpeta de backup o de restauración no existen")
        return

    source_folder_name = os.path.basename(backup_folder).split("_backup")[0]
    restored_folder_name = source_folder_name + "_restored"

    # Crear la carpeta de backup
    restored_path = os.path.join(restore_folder, restored_folder_name)
    if not valid_path(restored_path):
        os.makedirs(restored_path)
    
    # Leer el archivo de configuración de la copia de seguridad
    config_file = os.path.join(backup_folder, "config.json")
    print(config_file)
    if not  os.path.exists(config_file):
        print("Error: No se encontró el archivo de configuración de la copia de seguridad")
        return

    # Leemos el JSON de configuracion y lo guardamos como diccionario
    with open(config_file, "r") as f:
        backup_config = json.load(f)

    # Restuaramos los archivos y devolvemos cuantos fueron
    restored_files = restore(backup_folder, restored_path, backup_config)

    print(f"Restauración completada con éxito. {restored_files} archivos restaurados.")

Tk().withdraw()
print("Escoge el directorio del backup", flush=True)
carpeta_de_backup = askdirectory()
print("Escoge el directorio donde poner el directorio recuperado", flush=True)
carpeta_de_restauracion = askdirectory()

main("./prueba_backup", "./")