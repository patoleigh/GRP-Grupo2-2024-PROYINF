from flask import Flask, request, jsonify, send_from_directory
import os
import pydicom
import numpy as np
import pyvista as pv

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
VISUALIZATION_FOLDER = 'visualizations'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['VISUALIZATION_FOLDER'] = VISUALIZATION_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
if not os.path.exists(VISUALIZATION_FOLDER):
    os.makedirs(VISUALIZATION_FOLDER)

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

@app.route('/process', methods=['POST'])
def process_files():
    data = request.json
    file_paths = data.get('file_paths')

    dicom_images = [pydicom.dcmread(file_path) for file_path in file_paths]
    volume = np.stack([img.pixel_array for img in dicom_images])

    plotter = pv.Plotter(shape=(1, 3))
    plotter.subplot(0, 0)
    plotter.add_volume(volume, cmap="gray", clim=[0, 255])
    plotter.camera_position = 'xy'
    plotter.subplot(0, 1)
    plotter.add_volume(volume, cmap="gray", clim=[0, 255])
    plotter.camera_position = 'xz'
    plotter.subplot(0, 2)
    plotter.add_volume(volume, cmap="gray", clim=[0, 255])
    plotter.camera_position = 'yz'

    visualization_path = os.path.join(app.config['VISUALIZATION_FOLDER'], 'visualization.png')
    plotter.screenshot(visualization_path)
    plotter.close()

    return jsonify({'message': 'Processing complete', 'visualization_url': f'/visualizations/visualization.png'})

@app.route('/visualizations/<path:filename>')
def get_visualization(filename):
    return send_from_directory(app.config['VISUALIZATION_FOLDER'], filename)

if __name__ == '__main__':
    app.run(port=5000, debug=True)