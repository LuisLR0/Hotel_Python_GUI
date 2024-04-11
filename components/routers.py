import os
from PIL import Image

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_padre = os.path.dirname(ruta_actual)

ruta_carpeta_assets = os.path.join(ruta_padre, 'assets')

ruta_imagenLogo1 = os.path.join(ruta_carpeta_assets, 'logo.png')
ruta_imagenLogo2 = os.path.join(ruta_carpeta_assets, 'logo2.png')
ruta_imagenDecoracion = os.path.join(ruta_carpeta_assets, 'deco_inferior.png')

imagenLogo1 = Image.open(ruta_imagenLogo1)
imagenDecoracion = Image.open(ruta_imagenDecoracion)
