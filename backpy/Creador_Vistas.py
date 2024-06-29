import pydicom as dicom
import numpy as np
from PIL import Image
import os

def guardar_vista(volume3d, img_shape, vista, aspecto, filename):
    if vista == 'axial':
        image_array = volume3d[:, :, img_shape[2] // 2]
    elif vista == 'sagital':
        image_array = volume3d[:, img_shape[1] // 2, :]
    elif vista == 'coronal':
        image_array = volume3d[img_shape[0] // 2, :, :].T
    else:
        raise ValueError(f'Vista "{vista}" no reconocida.')

    image_array = (image_array - np.min(image_array)) / (np.max(image_array) - np.min(image_array)) * 255
    image_array = image_array.astype(np.uint8)

    image = Image.fromarray(image_array)
    image.save(filename)

def crear_vistas_para_carpeta(carpeta_seleccionada):
    path = os.path.join("./uploads", carpeta_seleccionada)
    ct_images = os.listdir(path)

    slices = [dicom.read_file(os.path.join(path, s), force=True) for s in ct_images]
    slices = sorted(slices, key=lambda x: x.ImagePositionPatient[2])

    pixel_spacing = slices[0].PixelSpacing
    slices_thickess = slices[0].SliceThickness

    axial_aspect_ratio = pixel_spacing[1] / pixel_spacing[0]
    sagital_aspect_ratio = pixel_spacing[1] / slices_thickess
    coronal_aspect_ratio = slices_thickess / pixel_spacing[0]

    img_shape = list(slices[0].pixel_array.shape)
    img_shape.append(len(slices))
    volume3d = np.zeros(img_shape)

    for i, s in enumerate(slices):
        array2D = s.pixel_array
        volume3d[:, :, i] = array2D

    carpeta_destino = 'vistas'


    os.makedirs(carpeta_destino, exist_ok=True)

    aspecto_seleccionado = 1.0 

    guardar_vista(volume3d, img_shape, 'axial', aspecto_seleccionado, os.path.join(carpeta_destino, 'axial.png'))
    guardar_vista(volume3d, img_shape, 'sagital', aspecto_seleccionado, os.path.join(carpeta_destino, 'sagital.png'))
    guardar_vista(volume3d, img_shape, 'coronal', aspecto_seleccionado, os.path.join(carpeta_destino, 'coronal.png'))

    return "Vistas Creadas correctamente"




