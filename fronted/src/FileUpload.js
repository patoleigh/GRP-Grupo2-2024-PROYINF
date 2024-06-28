import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

const FileUpload = ({ onFileUpload }) => {
  const [selectedFiles, setSelectedFiles] = useState([]);
  const [selectedFolderName, setSelectedFolderName] = useState('');

  const handleFileChange = (event) => {
    const files = event.target.files;
    if (files.length > 0) {
      const folderPath = files[0].webkitRelativePath;
      const folderName = folderPath.split('/')[0];
      setSelectedFolderName(folderName);
      setSelectedFiles(files);
    }
  };

  const handleUpload = async () => {
    if (selectedFiles.length > 0) {
      const formData = new FormData();
      Array.from(selectedFiles).forEach(file => {
        formData.append('files', file);
      });

      try {
        const response = await axios.post('http://localhost:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        onFileUpload(response.data.files);

        // After successful upload, fetch updated folders list
        fetchUpdatedFolders();
      } catch (error) {
        console.error('Error uploading files', error);
      }
      setSelectedFiles([]);
      setSelectedFolderName(''); // Clear the selected folder name after upload
    }
  };

  const fetchUpdatedFolders = async () => {
    try {
      const response = await axios.get('http://localhost:5000/folders');
      console.log('Carpetas actualizadas:', response.data);
      // No necesitas setFolders aquí ya que `App` maneja el estado de las carpetas
    } catch (error) {
      console.error("Hubo un error obteniendo las carpetas: ", error);
    }
  };

  return (
    <div>
      <input
        type="file"
        id="file-input"
        webkitdirectory="true"
        directory="true"
        multiple
        onChange={handleFileChange}
        style={{ display: 'none' }}
      />
      <label htmlFor="file-input" className="custom-file-input">
        Seleccionar Carpeta
      </label>
      {selectedFolderName && (
        <p>Carpeta "{selectedFolderName}" seleccionada</p>
      )}
      <button onClick={handleUpload}>Subir Carpeta</button>
    </div>
  );
};

export default FileUpload;