#!/usr/bin/env python3
import os
import subprocess
import argparse

def convert_mov_to_mp4(directory='.', remove_audio=False):
    """
    Recorre el directorio indicado en busca de archivos .mov y los convierte a .mp4,
    guardando los archivos convertidos en una subcarpeta llamada "mp4".
    Si el archivo de salida ya existe, se omite la conversión.
    Si remove_audio es True, se elimina el audio del video convertido.
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
        if file.lower().endswith('.mov'):
            input_path = os.path.join(directory, file)
            output_file = os.path.splitext(file)[0] + ".mp4"
            output_path = os.path.join(mp4_dir, output_file)

            # Verifica si el archivo mp4 ya existe
            if os.path.exists(output_path):
                print(f"El archivo '{output_path}' ya existe. Se omite la conversión.")
                continue

            # Construye el comando de ffmpeg
            command = [
                'ffmpeg', '-i', input_path,
                '-vcodec', 'libx264',
                '-crf', '36',
                '-preset', 'slow'
            ]
            if remove_audio:
                command.append('-an')
            else:
                command.extend(['-acodec', 'aac', '-b:a', '128k'])
            command.append(output_path)
            
            print(f"Convirtiendo '{input_path}' a '{output_path}'...")
            try:
                subprocess.run(command, check=True)
                print("Conversión completada.\n")
            except subprocess.CalledProcessError as e:
                print(f"Error al convertir {input_path}: {e}\n")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convierte archivos .mov a .mp4, opcionalmente sin audio.'
    )
    parser.add_argument(
        'directory', nargs='?', default='.',
        help='Directorio que contiene los archivos .mov'
    )
    parser.add_argument(
        '-nosoud', action='store_true',
        help='Eliminar audio del video convertido'
    )
    args = parser.parse_args()

    convert_mov_to_mp4(args.directory, remove_audio=args.nosoud)
