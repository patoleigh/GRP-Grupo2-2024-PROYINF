import React, { useState } from 'react';
import FileUpload from './FileUpload';
import FileViewer from './FileViewer';

const App = () => {
  const [fileUrls, setFileUrls] = useState([]);

  const handleFileUpload = (urls) => {
    setFileUrls(urls);
  };

  return (
    <div>
      <h1>Upload DICOM Files</h1>
      <FileUpload onFileUpload={handleFileUpload} />
      <FileViewer fileUrls={fileUrls} />
    </div>
  );
};

export default App;
