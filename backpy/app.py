from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pydicom
import numpy as np
import pyvista as pv
import subprocess  
import shutil
from Creador_Vistas import crear_vistas_para_carpeta 

app = Flask(__name__)
CORS(app)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
carpeta_destino = "vistas"

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
    return send_from_directory(os.path.join(app.root_path, 'vistas'), filename)


@app.route('/folders', methods=['GET'])
def list_folders():
    try:
        folders = [f for f in os.listdir(UPLOAD_FOLDER) if os.path.isdir(os.path.join(UPLOAD_FOLDER, f))]
        return jsonify(folders)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/crear-vistas', methods=['POST'])
def crear_vistas():
    try:
        data = request.json
        carpeta_seleccionada = data.get('carpetaSeleccionada')

        if not carpeta_seleccionada:
            return jsonify({"error": "No se proporcionó la carpeta seleccionada"}), 400

        resultado = crear_vistas_para_carpeta(carpeta_seleccionada)
        return jsonify({"message": resultado}), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/eliminar-vistas', methods=['POST'])
def eliminar_vistas():
    try:
        for filename in os.listdir(carpeta_destino):
            file_path = os.path.join(carpeta_destino, filename)
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        print(f'Carpeta {carpeta_destino} limpiada.')
        return jsonify({"message": f'Carpeta {carpeta_destino} limpiada.'}), 200
    except Exception as e:
        print(f'Error al limpiar la carpeta {carpeta_destino}: {str(e)}')
        return jsonify({"error": f'Error al limpiar la carpeta {carpeta_destino}: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)