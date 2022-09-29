import React, { useState, useEffect } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState(0);

  useEffect(() => {
    fetch('/message').then(res => res.json()).then(data => {
        setMessage(data.message);
    });
  }, []);

  return (
      <div className="App">
        <header className="App-header">

          Winter Week 2023

          <p>{message}</p>
        </header>
      </div>
  );
}

export default App;