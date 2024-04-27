import React from 'react';

const FileViewer = ({ files }) => {
  return (
    <div>
      <h2>(aqui va la visualización de la imagen)</h2>
      <ul>
        {files.map((file, index) => (
          <li key={index}>{file.name}</li>
        ))}
      </ul>
    </div>
  );
};

export default FileViewer;