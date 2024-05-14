import os
import pydicom
import numpy as np
import pyvista as pv

# Ruta al directorio que contiene las imágenes DICOM, se recibe con la funcion del programa "Abrir_archivo.py"
directorio_dicom = "DATOS_DICOM/Gd-MRA"

imagenes_dicom = [pydicom.dcmread(os.path.join(directorio_dicom, f)) for f in sorted(os.listdir(directorio_dicom)) if f.endswith('.dcm')]

volumen = np.stack([img.pixel_array for img in imagenes_dicom])

p = pv.Plotter(shape=(1, 3))

p.subplot(0, 0)
p.add_volume(volumen, cmap="gray", clim=[0, 255])
p.camera_position = 'xy'

p.subplot(0, 1)
p.add_volume(volumen, cmap="gray", clim=[0, 255])
p.camera_position = 'xz'

p.subplot(0, 2)
p.add_volume(volumen, cmap="gray", clim=[0, 255])
p.camera_position = 'yz'

p.show()