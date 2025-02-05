# Conversor de MOV a MP4

Este script en Python permite convertir archivos de video en formato `.mov` a formato `.mp4` utilizando **ffmpeg**. El objetivo es reducir el tamaño de los archivos manteniendo una buena calidad de video, gracias a la utilización de parámetros de compresión como el `CRF` y el `preset`. Además, los videos convertidos se guardan en una subcarpeta llamada `mp4` dentro del directorio de origen.

## Características

- **Búsqueda automática:** Escanea el directorio especificado en busca de archivos `.mov`.
- **Conversión optimizada:** Utiliza `ffmpeg` con parámetros que optimizan la calidad y el tamaño del video.
- **Organización:** Los archivos convertidos se almacenan en una subcarpeta `mp4`, manteniendo el directorio principal ordenado.

## Requisitos

- **Python 3.x**  
- **ffmpeg** instalado y accesible en el PATH.
  
  En sistemas basados en Debian/Ubuntu, puedes instalarlo con:
```bash
  sudo apt-get update
  sudo apt-get install ffmpeg
```

  En sistemas MacOS, puedes instalarlo con:
```bash
  brew install ffmpeg
```


Instalación de ffmpeg en Windows desde el terminal:
1.	Abre PowerShell como administrador.
2.	Si tienes Chocolatey instalado, ejecuta:

```bash
choco install ffmpeg -y
```
Si no tienes Chocolatey, instálalo siguiendo las instrucciones en chocolatey.org/install y luego ejecuta el comando anterior.

Instalación:

1.	Descarga o clona este repositorio o simplemente descarga el script convert_mov_to_mp4.py.
2.	Asigna permisos de ejecución (en sistemas Unix/Linux):

```bash
chmod +x convert_mov_to_mp4.py
```


Uso

Abre una terminal y ejecuta el script. Puedes especificar el directorio donde se encuentran los archivos .mov o, si no lo haces, se usará el directorio actual.
	
• Para convertir archivos en el directorio actual:
```bash
./convert_mov_to_mp4.py
```

• Para convertir archivos en un directorio específico:
```bash
./convert_mov_to_mp4.py /ruta/al/directorio
```


El script creará (si no existe) una carpeta llamada mp4 en el directorio especificado, y ahí se guardarán los archivos convertidos.

Parámetros de Conversión

El script utiliza los siguientes parámetros de ffmpeg para la conversión:

Video:
•	-vcodec libx264: Codifica el video en H.264, lo que permite una buena relación calidad/tamaño.
•	-crf 23: Controla la calidad del video; valores menores (por ejemplo, 18) aumentan la calidad (y el tamaño), mientras que valores mayores (por ejemplo, 28) reducen la calidad (y el tamaño).
•	-preset slow: Optimiza la compresión a costa de mayor tiempo de procesamiento. Puedes cambiarlo a medium o fast para conversiones más rápidas.
•	Audio:
•	-acodec aac: Codifica el audio en formato AAC.
•	-b:a 128k: Define el bitrate del audio en 128 kbps.

Puedes ajustar estos parámetros en el script según tus necesidades para balancear la calidad y el tamaño de los videos resultantes.

---

### Notas adicionales

- **Personalización:**  
  Puedes modificar el script para ajustar los parámetros de `ffmpeg` según tus necesidades o para añadir nuevas funcionalidades, como la conversión recursiva en subdirectorios.

- **Uso en otros entornos:**  
  Este script está diseñado para usarse desde la línea de comandos. Si deseas integrarlo en una aplicación mayor o con una interfaz gráfica, puedes importar la función `convert_mov_to_mp4()` en otro módulo y adaptarla según tus requerimientos.
