import './App.css';
import React, { useState, useEffect } from 'react';
import FileUpload from './FileUpload';
import BotonConAparicion from './BotonConAparicion';
import logo from './logo.svg';
import logoUSM from './LogoUSM.png';
import axios from 'axios';

const App = () => {
  const [fileUrls, setFileUrls] = useState([]);
  const [folders, setFolders] = useState([]);
  const [selectedFolder, setSelectedFolder] = useState('');



  useEffect(() => {
    fetchFolders();
  }, []);

  const fetchFolders = async () => {
    try {
      const response = await axios.get('http://localhost:5000/folders');
      setFolders(response.data);
    } catch (error) {
      console.error("Hubo un error obteniendo las carpetas: ", error);
    }
  };

  const handleFolderChange = (event) => {
    setSelectedFolder(event.target.value);
  };

  const handleFileUpload = (urls) => {
    setFileUrls(urls);
    fetchFolders();
  };

  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logoUSM} className="header-logo" alt="logo USM" />
        <img src={logo} className="App-logo" alt="logo" />
        <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap" rel="stylesheet"/>
        <h1>Visualizador DICOM</h1>
      </header>
      <h1>Upload DICOM Files</h1>
      <main>
        <FileUpload onFileUpload={handleFileUpload} />
        <div>
          <div>
            <h2>Selecciona la carpeta que deseas visualizar</h2>
            <select onChange={handleFolderChange} value={selectedFolder}>
              <option value="">Selecciona una carpeta</option>
              {folders.map(folder => (
              <option key={folder} value={folder}>
                  {folder}
              </option>
              ))}
            </select>
            <BotonConAparicion BotonConAparicion selectedFolder={selectedFolder}/>
          </div>
        </div>
      </main>
    </div>
  );
};

export default App;

