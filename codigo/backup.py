import os
import json
import math

def valid_path(path):
    return os.path.exists(path) and os.path.isdir(path)

def get_files(source_folder):
    files = []
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path): # Solo agregar si es archivo, no queremos carpetas
            files.append(file_path)
    return files

def backup(files, backup_path):
    backup_files = []
    
    for file_path in files:
        # Calculamos numero de chunks
        file_size = os.path.getsize(file_path)
        chunks = math.ceil(file_size / (512 * 1024 * 1024))  # 512 MB en bytes

        with open(file_path, "rb") as og_file: # Abrimos el archivo original en Read Bytes
            filename = os.path.basename(file_path) # Sacamos el nombre del archivo
            
            for i in range(chunks):
                chunk_path = os.path.join(backup_path, f"{filename}.{i+1}.backup") # Por cada chunk con nombre secuencial, 
                with open(chunk_path, "wb") as chunk_f: # Abrimos el archivo de chunk en Write Bytes
                    chunk_f.write(og_file.read(512 * 1024 * 1024)) # Guardamos las megas dadas (Ej, 512)
                backup_files.append({"file": file_path, "size": file_size, "chunks": chunks})
    
    return backup_files

def main(source_folder, backup_folder):
    # Validar las rutas
    if not valid_path(source_folder) or not valid_path(backup_folder):
        print("Error: Invalid path")
        return

    # Crear la carpeta de backup
    backup_path = os.path.join(backup_folder, "backup")
    if not valid_path(backup_path):
        os.makedirs(backup_path)

    # Obtener los archivos para hacer backup
    files = get_files(source_folder)

    # Hacer el backup
    backup_files = backup(files, backup_path)

    # Guardar el JSON de configuracion
    with open(os.path.join(backup_folder, "backup.json"), "w") as f:
        json.dump({"files": backup_files}, f, indent=4)

    # Terminar
    print("Copia de seguridad completa")

# TODO: Definir variable de entorno para CHUNK_SIZE
# TODO: Recibir argumentos de la linea de comandos