from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import numpy as np
import pyvista as pv

import pydicom as dicom
import matplotlib.pyplot as plt


##############################################################################################################
def leer_y_procesar_carpetas(base_path, destino_base):
    carpetas = [f.path for f in os.scandir(base_path) if f.is_dir()]

    for carpeta in carpetas:
        procesar_carpeta(carpeta, destino_base)

def procesar_carpeta(carpeta, destino_base):
    ct_images = [f for f in os.listdir(carpeta) if f.endswith('.dcm')]
    if not ct_images:
        print(f"No se encontraron archivos .dcm en la carpeta {carpeta}")
        return
    
    slices = [dicom.read_file(os.path.join(carpeta, s), force=True) for s in ct_images]
    slices = sorted(slices, key=lambda x: x.ImagePositionPatient[2])

    pixel_spacing = slices[0].PixelSpacing
    slices_thickess = slices[0].SliceThickness

    sagital_aspect_ratio = pixel_spacing[1] / pixel_spacing[0]
    coronal_aspect_ratio = pixel_spacing[1] / slices_thickess
    axial_aspect_ratio = slices_thickess / pixel_spacing[0]

    img_shape = list(slices[0].pixel_array.shape)
    img_shape.append(len(slices))
    volume3d = np.zeros(img_shape)

    for i, s in enumerate(slices):
        array2D = s.pixel_array
        volume3d[:, :, i] = array2D

    guardar_vistas(volume3d, img_shape, carpeta, destino_base)

def guardar_vistas(volume3d, img_shape, carpeta, destino_base):
    def guardar_vista(volume3d, img_shape, vista, aspecto, filename):
        plt.figure()

        if vista == 'sagital':
            plt.title("Sagital")
            plt.imshow(volume3d[:, :, img_shape[2] // 2], cmap='inferno')
            plt.gca().set_aspect(aspecto)

        elif vista == 'coronal':
            plt.title("Coronal")
            plt.imshow(volume3d[:, img_shape[1] // 2, :], cmap='inferno')
            plt.gca().set_aspect(aspecto)

        elif vista == 'axial':
            plt.title("Axial")
            plt.imshow(volume3d[img_shape[0] // 2, :, :].T, cmap='inferno')
            plt.gca().set_aspect(aspecto)

        plt.savefig(filename)
        plt.close()

    # Crear una carpeta de destino para las vistas transformadas
    nombre_carpeta = os.path.basename(carpeta)
    carpeta_destino = os.path.join(destino_base, nombre_carpeta)
    os.makedirs(carpeta_destino, exist_ok=True)

    aspecto_seleccionado = 1.0  # Ajusta esto según sea necesario

    guardar_vista(volume3d, img_shape, 'sagital', aspecto_seleccionado, os.path.join(carpeta_destino, 'sagital.png'))
    guardar_vista(volume3d, img_shape, 'coronal', aspecto_seleccionado, os.path.join(carpeta_destino, 'coronal.png'))
    guardar_vista(volume3d, img_shape, 'axial', aspecto_seleccionado, os.path.join(carpeta_destino, 'axial.png'))

##############################################################################################################

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


@app.route('/upload', methods=['POST'])
def upload_files():
    files = request.files.getlist('files')
    file_paths = []
    for file in files:
        subdir = os.path.dirname(file.filename)
        full_path_dir = os.path.join(app.config['UPLOAD_FOLDER'], subdir)
        if not os.path.exists(full_path_dir):
            os.makedirs(full_path_dir)
        file_path = os.path.join(full_path_dir, os.path.basename(file.filename))
        file.save(file_path)
        file_paths.append(file_path)
    return jsonify({'files': file_paths})

@app.route('/vistas/<filename>')
def get_image(filename):
    ##########################################################
    # Ruta base de las carpetas a procesar
    base_path = './uploads/DATOS_DICOM'
    # Ruta base para guardar las vistas
    destino_base = './vistas'

    # Crear la carpeta de destino si no existe
    os.makedirs(destino_base, exist_ok=True)

    # Leer y procesar todas las carpetas
    leer_y_procesar_carpetas(base_path, destino_base)
    ##########################################################

    
    return send_from_directory(os.path.join(app.root_path, 'vistas/BSSFP'), filename)


if __name__ == '__main__':
    app.run(port=5000, debug=True)