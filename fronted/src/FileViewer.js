import React, { useEffect, useState } from 'react';
import axios from 'axios';

const FileViewer = ({ fileUrls }) => {
  const [visualizationUrl, setVisualizationUrl] = useState('');

  useEffect(() => {
    const processFiles = async () => {
      try {
        const response = await axios.post('http://localhost:5000/process', {
          file_paths: fileUrls
        });
        setVisualizationUrl(`http://localhost:5000${response.data.visualization_url}`);
      } catch (error) {
        console.error('Error processing files', error);
      }
    };

    if (fileUrls && fileUrls.length > 0) {
      processFiles();
    }
  }, [fileUrls]);

  return (
    <div>
      {visualizationUrl ? (
        <img src={visualizationUrl} alt="3D Visualization" />
      ) : (
        <p>No visualization available</p>
      )}
    </div>
  );
};

export default FileViewer;