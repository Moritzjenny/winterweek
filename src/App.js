import React, { useState, useEffect } from 'react';
import forest from './images/forest.jpg';
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
          <div className="header-image" style={{ backgroundImage: `url(${forest})`}}>
              <div className="container" style={{minHeight: '350px'}}>
                  <div className="container" style={{minHeight: '50px'}}></div>
                  <p style={{ margin: 0, fontSize: 'max(3vw, 60px)'}}> Winter Week </p>
                  <p style={{fontSize: 'max(1vw, 20px)'}}> 27.01.2023 - 03.02.2023</p>
              </div>
          </div>

      </div>
  );
}

export default App;