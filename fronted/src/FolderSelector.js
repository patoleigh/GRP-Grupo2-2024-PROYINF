import React, { useState, useEffect } from 'react';
import axios from 'axios';

const FolderSelector = ({ folders, onFolderSelect }) => {
    console.log('Folders recibidas:', folders);  
    const [selectedFolder, setSelectedFolder] = useState('');

    useEffect(() => {
        setSelectedFolder(''); // Asegúrate de limpiar la selección al actualizar las carpetas
    }, [folders]);

    const handleChange = (event) => {
        const selectedFolder = event.target.value;
        setSelectedFolder(selectedFolder);
        onFolderSelect(selectedFolder);
    };

    if (!folders || folders.length === 0) {
        return (
        <div>
            <h2>Selecciona la carpeta que deseas visualizar</h2>
            <p>No hay carpetas disponibles</p>
        </div>
        );
    }

    return (
        <div>
        <h2>Selecciona la carpeta que deseas visualizar</h2>
        <select onChange={handleChange} value={selectedFolder}>
            <option value="">Selecciona una carpeta</option>
            {folders.map(folder => (
            <option key={folder} value={folder}>
                {folder}
            </option>
            ))}
        </select>
        </div>
    );
    };

export default FolderSelector;