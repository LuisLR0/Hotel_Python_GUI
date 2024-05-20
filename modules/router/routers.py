import os
from PIL import Image

ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_modules = os.path.dirname(ruta_actual)
ruta_padre = os.path.dirname(ruta_modules)

ruta_carpeta_assets = os.path.join(ruta_padre, 'assets')

ruta_imagenLogo1 = os.path.join(ruta_carpeta_assets, 'logo.png')
ruta_imagenLogo2 = os.path.join(ruta_carpeta_assets, 'logo2.png')
ruta_imagenDecoracion = os.path.join(ruta_carpeta_assets, 'deco_inferior.png')
ruta_imagenIconHouse = os.path.join(ruta_carpeta_assets, 'icon_house.png')
ruta_imagenIconFurniture = os.path.join(ruta_carpeta_assets, 'icon_furniture.png')


imagenes = {
    'imagenLogo1': Image.open(ruta_imagenLogo1),
    'imagenLogo2': Image.open(ruta_imagenLogo2),
    'imagenDecoracion': Image.open(ruta_imagenDecoracion),
    'imagenIconHouse': Image.open(ruta_imagenIconHouse),
    'imagenIconFurniture': Image.open(ruta_imagenIconFurniture)
}