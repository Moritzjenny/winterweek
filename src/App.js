import React, { useState, useEffect } from 'react';
import forest from './images/forest.jpg';
import spinatscha from './images/spinatscha.jpg';
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
          <div className="header-image" style={{ backgroundImage: `url(${forest})`, transform0rigin: '-1000% 100%'}}>
              <div className="container" style={{minHeight: '350px' }}>
                  <div className="container" style={{minHeight: '50px'}}/>
                      <div style={{backgroundColor: 'black', color: 'white', width: 'fit-content', display:"inline-flex"}}>
                        <p className="custom-font-bold" style={{fontSize: 'max(0.5vw, 20px)', margin: 5}}>Register now, before we're booked up!</p>
                      </div>
                  <p className="custom-font-bold" style={{ margin: 0, fontSize: 'min(max(4vw, 60px), 80px)', marginTop: '50px'}}> Winter Week </p>
                  <p className="custom-font-bold" style={{fontSize: 'min(max(1vw, 30px), 40px)'}}> January 27. - February 3.</p>
              </div>
          </div>
          <div className="container" style={{minHeight: '100px'}}/>
          <div style={{maxWidth: '1200px', marginLeft: 'auto', marginRight: 'auto'}}>
              <div style={{paddingLeft: '100px', paddingRight: '100px'}}>
                <p className="custom-font" style={{fontSize: '20px', textAlign: 'left'}}> <span className="custom-font-bold"> &#128176; Our deal contains</span> a great week of skiing with your fellow students for CHF 500, accommodations, meals, travel and ski pass included! </p>
              </div>
          </div>

          <div className="container" style={{minHeight: '100px'}}/>
          <div style={{maxWidth: '1200px', marginLeft: 'auto', marginRight: 'auto'}}>
              <div className="grid-container">
                  <div className='item' style={{paddingLeft: '100px', paddingRight: '100px', margin: 'auto'}}>
                      <p className="custom-font" style={{fontSize: '20px', textAlign: 'left'}}> <span className="custom-font-bold"> &#128716; Nova Casa Spinatscha </span> will be our home base to stay for the week. Nova Casa Spinatscha is situated on the edge of the village of Sedrun. In 2 minutes you are in the village center, the indoor pool and at the train station.</p>
                  </div>
                  <div className='image item' style={{ backgroundImage: `url(${spinatscha})`, backgroundRepeat: 'no-repeat', backgroundPosition: 'center', maxHeight: '100%'}}/>
              </div>
          </div>
      </div>
  );
}

export default App;