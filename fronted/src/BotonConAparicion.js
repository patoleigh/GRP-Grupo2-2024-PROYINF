import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ImageComponent from './Imagen';

const BotonConAparicion = ({ selectedFolder, handleVistasCreation }) => {
    const [mostrarBotones, setMostrarBotones] = useState(false);
    const [showImage1, setShowImage1] = useState(false);
    const [showImage2, setShowImage2] = useState(false);
    const [showImage3, setShowImage3] = useState(false);
    const [zoomLevel1, setZoomLevel1] = useState(1);
    const [zoomLevel2, setZoomLevel2] = useState(1);
    const [zoomLevel3, setZoomLevel3] = useState(1);
    const [vistasCreadas, setVistasCreadas] = useState(false);
 
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

    const toggleMostrarBotones = () => {
      setMostrarBotones(!mostrarBotones);
    };

    const handleCrearVistas = async () => {
      try {
        const response = await axios.post('http://localhost:5000/crear-vistas', {
          carpetaSeleccionada: selectedFolder
        });
        console.log(response.data.message); 
        setVistasCreadas(true);
      } catch (error) {
        console.error('Error al llamar a la API:', error);
      }
    };

    const otrolimpiar = () => {
      setShowImage1(false);
      setShowImage2(false);
      setShowImage3(false);
      setVistasCreadas(false);

    };

    const handleEliminarVistas = async () => {
      try {
        const response = await axios.post('http://localhost:5000/eliminar-vistas', {
        });
        console.log(response.data.message); 
      } catch (error) {
        console.error('Error al llamar a la API:', error);
      }
    };

    useEffect(() => {
      console.log("Carpeta seleccionada cambió a:", selectedFolder);
    }, [selectedFolder]);

    return (
      <div>
        {!vistasCreadas && (
          <button onClick={() => {
            toggleMostrarBotones();
            handleCrearVistas(); 
          }}>Crear Vistas</button>          
        )}
        {vistasCreadas && (
          <button onClick={() => {
            toggleMostrarBotones();
            handleEliminarVistas();
            otrolimpiar();
          }}>Limpiar</button>  
        )}     
        {mostrarBotones && (
          <div>
          <div>
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
          </div>
        )}
      </div>
    );
  }

export default BotonConAparicion;