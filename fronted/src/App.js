import React, { useState } from 'react';
import FileUpload from './FileUpload';
import FileViewer from './FileViewer';
import ImageComponent from './Imagen';

const App = () => {
  const [fileUrls, setFileUrls] = useState([]);
  const [showImage1, setShowImage1] = useState(false);
  const [showImage2, setShowImage2] = useState(false);
  const [showImage3, setShowImage3] = useState(false);

  const handleFileUpload = (urls) => {
    setFileUrls(urls);
  };


  const handleButtonClick1 = () => {
    setShowImage1(true);
  };

  const handleButtonClick2 = () => {
    setShowImage2(true);
  };

  const handleButtonClick3 = () => {
    setShowImage3(true);
  };
  


  return (
    <div>
      <h1>Upload DICOM Files</h1>
      <FileUpload onFileUpload={handleFileUpload} />
      <FileViewer fileUrls={fileUrls} />
      
      {/* Botones para mostrar las imágenes */}
      <button onClick={handleButtonClick1}>Mostrar Imagen Axial</button>
      {showImage1 && <ImageComponent imageName="axial.png" />}
      
      <button onClick={handleButtonClick2}>Mostrar Imagen Sagital</button>
      {showImage2 && <ImageComponent imageName="sagital.png" />}
      
      <button onClick={handleButtonClick3}>Mostrar Imagen Coronal</button>
      {showImage3 && <ImageComponent imageName="coronal.png" />}
    </div>
  );
};

export default App;
