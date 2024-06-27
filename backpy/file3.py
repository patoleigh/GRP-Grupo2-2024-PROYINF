import pydicom as dicom
import numpy as np
import matplotlib.pyplot as plt
import os

path="./uploads/BSSFP"
ct_images=os.listdir(path)

slices = [dicom.read_file(path+'/'+s,force=True) for s in ct_images]
#print(slices)
slices = sorted(slices,key=lambda x:x.ImagePositionPatient[2])

pixel_spacing = slices[0].PixelSpacing
slices_thickess = slices[0].SliceThickness

axial_aspect_ratio = pixel_spacing[1]/pixel_spacing[0]
sagital_aspect_ratio = pixel_spacing[1]/slices_thickess
coronal_aspect_ratio = slices_thickess/pixel_spacing[0]

#print("Pixel spacing is:",pixel_spacing)
#print("Slices Thickness is:",slices_thickess)

#print("Axial Aspect Ratio:",axial_aspect_ratio)
#print("Sagital Aspect Ratio:",sagital_aspect_ratio)
#print("Coronal Aspect Ratio:",coronal_aspect_ratio)

img_shape = list(slices[0].pixel_array.shape)
img_shape.append(len(slices))
volume3d=np.zeros(img_shape)

for i,s in enumerate(slices):
    array2D=s.pixel_array
    volume3d[:,:,i]= array2D

def guardar_vista(volume3d, img_shape, vista, aspecto, filename):
    plt.figure()

    if vista == 'axial':
        plt.title("Axial")
        plt.imshow(volume3d[:, :, img_shape[2] // 2])
        plt.gca().set_aspect(aspecto)

    elif vista == 'sagital':
        plt.title("Sagital")
        plt.imshow(volume3d[:, img_shape[1] // 2, :])
        plt.gca().set_aspect(aspecto)

    elif vista == 'coronal':
        plt.title("Coronal")
        plt.imshow(volume3d[img_shape[0] // 2, :, :].T)
        plt.gca().set_aspect(aspecto)

    plt.savefig(filename)
    plt.close()

# Ejemplo de uso:
# volume3d es tu volumen 3D
# img_shape es la forma de tu volumen 3D, por ejemplo (dim1, dim2, dim3)
# vista puede ser 'axial', 'sagital' o 'coronal'
# aspecto es la relación de aspecto que quieres aplicar, por ejemplo 1.0
# filename es el nombre del archivo donde quieres guardar la imagen

# Definir la carpeta de destino
carpeta_destino = 'vistas'

# Asegurarse de que la carpeta exista
os.makedirs(carpeta_destino, exist_ok=True)

# Guardar las tres vistas:
aspecto_seleccionado = 1.0  # Ajusta esto según sea necesario

guardar_vista(volume3d, img_shape, 'axial', aspecto_seleccionado, os.path.join(carpeta_destino, 'axial.png'))
guardar_vista(volume3d, img_shape, 'sagital', aspecto_seleccionado, os.path.join(carpeta_destino, 'sagital.png'))
guardar_vista(volume3d, img_shape, 'coronal', aspecto_seleccionado, os.path.join(carpeta_destino, 'coronal.png'))




#plt.show()

#print(array2D.shape)
#print(volume3d.shape)