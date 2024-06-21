import os
import pydicom
import numpy as np
import pyvista as pv

# Ruta al directorio que contiene las imágenes DICOM
directorio_dicom = "./DATOS_DICOM/Gd-MRA"

# Leer las imágenes DICOM
imagenes_dicom = [pydicom.dcmread(os.path.join(directorio_dicom, f)) for f in sorted(os.listdir(directorio_dicom)) if f.endswith('.dcm')]

# Extraer los datos de píxeles de las imágenes DICOM y apilarlos en un arreglo 3D
volumen = np.stack([img.pixel_array for img in imagenes_dicom])

# Crear un objeto PyVista para visualización
p = pv.Plotter(shape=(1, 3))

# Visualizar el volumen en las tres direcciones ortogonales
p.subplot(0, 0)
p.add_volume(volumen, cmap="gray", clim=[0, 255])
p.camera_position = 'xy'

p.subplot(0, 1)
p.add_volume(volumen, cmap="gray", clim=[0, 255])
p.camera_position = 'xz'

p.subplot(0, 2)
p.add_volume(volumen, cmap="gray", clim=[0, 255])
p.camera_position = 'yz'

# Mostrar la visualización
p.show()