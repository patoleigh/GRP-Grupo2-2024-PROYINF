import React, { useState } from 'react';
import FileUpload from './FileUpload';
import FileViewer from './FileViewer';

const App = () => {
  const [files, setFiles] = useState([]);

  const handleFileUpload = (file) => {
    setFiles([...files, file]);
  };

  return (
    <div>
      <h1>Visualizador de Imagenes DICOM</h1>
      <div style={{ display: 'flex' }}>
        <div style={{ flex: 1 }}>
          <FileUpload onFileUpload={handleFileUpload} />
        </div>
        <div style={{ flex: 2 }}>
          <FileViewer files={files} />
        </div>
      </div>
    </div>
  );
};

export default App;
