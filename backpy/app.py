from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import os
import pydicom
import numpy as np
import pyvista as pv

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
    return send_from_directory(os.path.join(app.root_path, 'vistas'), filename)


if __name__ == '__main__':
    app.run(port=5000, debug=True)