import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = ({ onFileUpload }) => {
  const [selectedFiles, setSelectedFiles] = useState([]);

  const handleFileChange = (event) => {
    setSelectedFiles(event.target.files);
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
      } catch (error) {
        console.error('Error uploading files', error);
      }
      setSelectedFiles([]);
    }
  };

  return (
    <div>
      <input type="file" webkitdirectory="true" directory multiple onChange={handleFileChange} />
      <button onClick={handleUpload}>Subir archivos</button>
    </div>
  );
};

export default FileUpload;