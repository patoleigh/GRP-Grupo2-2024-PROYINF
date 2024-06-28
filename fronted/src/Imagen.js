import React, { useState, useEffect } from 'react';

const ImageComponent = ({ imageName, zoomLevel }) => {
  const [imageSrc, setImageSrc] = useState('');

  useEffect(() => {
    console.log(`Fetching image: ${imageName}`);
    fetch(`http://localhost:5000/vistas/${imageName}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.blob();
      })
      .then(imageBlob => {
        const imageObjectURL = URL.createObjectURL(imageBlob);
        console.log(`Image Object URL: ${imageObjectURL}`);
        setImageSrc(imageObjectURL);
      })
      .catch(error => console.error('Error fetching the image:', error));
  }, [imageName]);

  return (
    <div className="image-container">
      {imageSrc ? (
        <img
          src={imageSrc}
          alt={imageName}
          className="zoomable-image"
          style={{ transform: `scale(${zoomLevel})` }}
        />
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ImageComponent;
