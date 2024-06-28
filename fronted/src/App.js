import './App.css';
import React, { useState } from 'react';
import FileUpload from './FileUpload';
import FileViewer from './FileViewer';
import ImageComponent from './Imagen';
import logo from './logo.svg';
import logoUSM from './LogoUSM.png';

const App = () => {
  const [fileUrls, setFileUrls] = useState([]);
  const [showImage1, setShowImage1] = useState(false);
  const [showImage2, setShowImage2] = useState(false);
  const [showImage3, setShowImage3] = useState(false);
  const [zoomLevel1, setZoomLevel1] = useState(1);
  const [zoomLevel2, setZoomLevel2] = useState(1);
  const [zoomLevel3, setZoomLevel3] = useState(1);

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

  const handleZoomChange1 = (event) => {
    setZoomLevel1(event.target.value);
  };

  const handleZoomChange2 = (event) => {
    setZoomLevel2(event.target.value);
  };

  const handleZoomChange3 = (event) => {
    setZoomLevel3(event.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logoUSM} className="header-logo" alt="logo USM" />
        <img src={logo} className="App-logo" alt="logo" />
        <h1>Visualizador DICOM</h1>
      </header>
      <h1>Upload DICOM Files</h1>
      <main>
        <FileUpload onFileUpload={handleFileUpload} />
        <FileViewer fileUrls={fileUrls} />
        <div>
          {/* Botones para mostrar las imágenes */}
          <button onClick={handleButtonClick1}>Mostrar Imagen Axial</button>
          {showImage1 && (
            <div>
              <ImageComponent imageName="axial.png" zoomLevel={zoomLevel1} />
              <input
                type="range"
                min="1"
                max="3"
                step="0.1"
                value={zoomLevel1}
                onChange={handleZoomChange1}
              />
            </div>
          )}
          
          <button onClick={handleButtonClick2}>Mostrar Imagen Sagital</button>
          {showImage2 && (
            <div>
              <ImageComponent imageName="sagital.png" zoomLevel={zoomLevel2} />
              <input
                type="range"
                min="1"
                max="3"
                step="0.1"
                value={zoomLevel2}
                onChange={handleZoomChange2}
              />
            </div>
          )}
          
          <button onClick={handleButtonClick3}>Mostrar Imagen Coronal</button>
          {showImage3 && (
            <div>
              <ImageComponent imageName="coronal.png" zoomLevel={zoomLevel3} />
              <input
                type="range"
                min="1"
                max="3"
                step="0.1"
                value={zoomLevel3}
                onChange={handleZoomChange3}
              />
            </div>
          )}
        </div>
      <div>
          <h2></h2>
      </div>
      </main>
    </div>
  );
};

export default App;

