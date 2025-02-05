#!/usr/bin/env python3
import os
import subprocess
import sys

def convert_mov_to_mp4(directory='.'):
    """
    Recorre el directorio indicado en busca de archivos .mov y los convierte a .mp4,
    guardando los archivos convertidos en una subcarpeta llamada "mp4".
    """
    # Verifica si el directorio existe
    if not os.path.isdir(directory):
        print(f"El directorio '{directory}' no existe.")
        return

    # Crea la carpeta 'mp4' si no existe
    mp4_dir = os.path.join(directory, "mp4")
    if not os.path.exists(mp4_dir):
        os.makedirs(mp4_dir)
        print(f"Se ha creado la carpeta: {mp4_dir}")

    # Itera sobre cada archivo en el directorio
    for file in os.listdir(directory):
        # Se ignoran diferencias de mayúsculas/minúsculas
        if file.lower().endswith('.mov'):
            input_path = os.path.join(directory, file)
            # Genera el nombre de salida cambiando la extensión a .mp4
            output_file = os.path.splitext(file)[0] + ".mp4"
            output_path = os.path.join(mp4_dir, output_file)
            
            # Construye el comando de ffmpeg
            command = [
                'ffmpeg', '-i', input_path,
                '-vcodec', 'libx264',
                '-crf', '36',          # Ajusta este valor (por ejemplo: 18 para mayor calidad o 28 para más compresión)
                '-preset', 'slow',     # 'slow' da mejor compresión; puedes usar 'medium' o 'fast' si prefieres conversiones más rápidas
                '-acodec', 'aac',
                '-b:a', '128k',
                output_path
            ]
            
            print(f"Convirtiendo '{input_path}' a '{output_path}'...")
            try:
                # Ejecuta el comando de ffmpeg
                subprocess.run(command, check=True)
                print("Conversión completada.\n")
            except subprocess.CalledProcessError as e:
                print(f"Error al convertir {input_path}: {e}\n")

if __name__ == '__main__':
    # Si se pasa un directorio como argumento, se usa ese; de lo contrario, se usa el directorio actual.
    if len(sys.argv) > 1:
        target_directory = sys.argv[1]
    else:
        target_directory = '.'
    
    convert_mov_to_mp4(target_directory)
