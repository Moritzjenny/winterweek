import React, { useState, useEffect } from 'react';
import forest from './images/forest.jpg';
import spinatscha from './images/spinatscha.jpg';
import sedrun from './images/sedrun.jpg';
import icu from './images/icu.png';
import {useRef} from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState("--");
  const ref = useRef(null);

  useEffect(() => {
    fetch('/api/message').then(res => res.json()).then(data => {
        setMessage(data.message);
    });
  }, []);


    const goToRegisterButtons = () => {
        ref.current?.scrollIntoView({behavior: 'smooth'});
    };

  return (
      <div className="App">

          <div className="header-image" style={{ backgroundImage: `url(${forest})`}}>
              <img className="header-image" src="./logo_transparent.png" className="logo-image"/>
              <div className="container" style={{minHeight: '350px' }}>
                      <div style={{backgroundColor: 'black', color: 'white', display:"inline-flex"}}>
                        <p className="custom-font-bold" style={{fontSize: 'max(0.3vw, 15px)', margin: 5}}>Register now, before we're booked out!</p>
                      </div>
                  <p className="custom-font-bold" style={{ margin: 0, fontSize: 'min(max(4vw, 60px), 80px)', marginTop: '20px'}}> Winter Week </p>
                  <p className="custom-font-bold" style={{fontSize: 'min(max(1vw, 30px), 40px)'}}> January 29. - February 4.</p>
              </div>
          </div>

          <div className="container" style={{minHeight: '30px'}}/>

          <div className="button6" onClick={() => { goToRegisterButtons(); }} style={{cursor: 'pointer'}}> Register
          </div>

          <div>
              <p className="custom-font" style={{fontSize: '20px', color: 'grey'}}>{message} Places left</p>
          </div>

          <div className="container" style={{minHeight: '80px'}}/>
          <div className="grid-wrapper">
             <div className="grid-container">
                  <div className='item'>
                      <p className="custom-font text" style={{fontSize: '20px', textAlign: 'left'}}> <span className="custom-font-bold"> &#128716; Nova Casa Spinatscha</span> will be our home base to stay for the week. Nova Casa Spinatscha is situated on the edge of the village of Sedrun. In 2 minutes you are in the village center, the indoor pool and at the train station.</p>
                  </div>
                 <a style={{textDecoration: 'none', margin: '0 40px'}} href="http://www.spinatscha.ch/neu/de/"> <div className='image item rcorners' style={{ backgroundImage: `url(${spinatscha})`, height: '340px'}}/></a>
              </div>
          </div>

          <div className="container" style={{minHeight: '80px'}}/>

          <div className="grid-wrapper">
              <div className="grid-container">
                  <a className="grid-row2" style={{textDecoration: 'none', margin: '0 40px'}} href="https://www.andermatt.ch/attraktionen/skiarena-andermatt-sedrun-8a9a1e476e"> <div className='image item rcorners' style={{ backgroundImage: `url(${sedrun})`, height: '300px'}}/></a>
                  <div className='item'>
                      <p className="custom-font text" style={{fontSize: '20px', textAlign: 'left'}}> <span className="custom-font-bold"> &#127935; Ski Arena Andermatt Sedrun Disentis</span> is our playground for the week. With 180 km of slopes and 33 lifts up to 3,000 m above sea level, Andermatt+Sedrun+Disentis is the largest ski area in Central Switzerland.</p>
                  </div>
              </div>
          </div>

          <div className="container" style={{minHeight: '100px'}}/>


          <div style={{maxWidth: '1200px', margin: 'auto'}}>
              <div style={{padding: '0 30px'}}>
                  <p className="custom-font" style={{fontSize: '20px', textAlign: 'left'}}> <span className="custom-font-bold"> &#128176; Our deal contains</span> a great week of skiing with your fellow students for CHF 500, accommodations, meals, travel and ski pass included! </p>
              </div>
          </div>

          <div className="container" style={{minHeight: '50px'}}/>

          <div className="grid-wrapper">
              <div className="grid-container-options">
                  <div className="rcorners" ref={ref} >
                      <div className="tile-title custom-font" style={{fontSize: '25px', textAlign: 'left'}}>ICU Members</div>
                      <div className="tile-keyword-row-large">
                          <div className="custom-font text" style={{fontSize: '55px'}}> <span className="custom-font-bold">500</span></div>
                          <div className="custom-font"  style={{fontSize: '25px', marginTop: '20px', marginLeft: '10px'}}>CHF</div>
                      </div>
                      <div className="tile-keyword-row-large">
                          <div className="custom-font" style={{fontSize: '18px', color: "#666666", padding: '0 20px', textAlign: 'left', minHeight: '150px'}}> First things first, you're awesome! We want to give back to our members, that's why you exclusively profit of our best price. You get to experience the magical Winter Week for just 500.-.</div>
                      </div>
                      <div className="" style={{fontSize: '18px'}}>________________________________</div>
                      <div>
                          <a href="https://docs.google.com/forms/d/e/1FAIpQLSdQ2OYju5qvYjHIBVI4-yZu8MlDJc3OZnDDi15wgz___UudzQ/viewform?usp=sf_link"><div className="button6" style={{margin: '20px'}}> Register </div></a>
                      </div>
                  </div>

                  <div className="rcorners" >
                      <div className="tile-title custom-font" style={{fontSize: '25px', textAlign: 'left'}}>Students</div>
                      <div className="tile-keyword-row-large">
                          <div className="custom-font text" style={{fontSize: '55px'}}> <span className="custom-font-bold">650</span></div>
                          <div className="custom-font"  style={{fontSize: '25px', marginTop: '20px', marginLeft: '10px'}}>CHF</div>
                      </div>
                      <div className="tile-keyword-row-large">
                          <div className="custom-font" style={{fontSize: '18px', color: "#666666", padding: '0 20px', textAlign: 'left', minHeight: '150px'}}>Hey fellow students, we know you're on a budget. That's why we made the best deals with our partners. For 650.- you can experience the ski holidays of a lifetime.</div>
                      </div>
                      <div className="" style={{fontSize: '18px'}}>________________________________</div>
                      <div>
                          <a href="https://docs.google.com/forms/d/e/1FAIpQLScil9xHA31qb3SOXWqTc6WHHBiV_B4uNDpGcPx4dRfV5Zwdyg/viewform?usp=sf_link"><div className="button6" style={{margin: '20px'}}> Register </div></a>
                      </div>
                  </div>

                  <div className="rcorners" >
                      <div className="tile-title custom-font" style={{fontSize: '25px', textAlign: 'left'}}>Non-Students</div>
                      <div className="tile-keyword-row-large">
                          <div className="custom-font text" style={{fontSize: '55px'}}> <span className="custom-font-bold">750</span></div>
                          <div className="custom-font"  style={{fontSize: '25px', marginTop: '20px', marginLeft: '10px'}}>CHF</div>
                      </div>
                      <div className="tile-keyword-row-large">
                          <div className="custom-font" style={{fontSize: '18px', color: "#666666", padding: '0 20px', textAlign: 'left', minHeight: '150px'}}>Already working hard in the corporate world, but missing your friends at ICU? Exprience the sudent life again for one exciting week for 750.-</div>
                      </div>
                      <div className="" style={{fontSize: '18px'}}>________________________________</div>
                      <div>
                          <a href="https://docs.google.com/forms/d/e/1FAIpQLSfi_Yy1yQ6JjIs_G5WZAo_388TFiIBxagbGSqs1fRzaCmVfpA/viewform?usp=sf_link"><div className="button6" style={{margin: '20px'}}> Register </div></a>
                      </div>
                  </div>

              </div>
              <div style={{minHeight: '20px'}}/>
              <div className='custom-font text' style={{fontSize: '18px', color: "#666666", padding: '0 20px', textAlign: 'left'}}>If the event can't take place because of new regulations regarding COVID-19, the full cost will be refunded.
                  In case you don't need a ski pass, a discount of 200.- will be offered.</div>
          </div>

          <div className="container" style={{minHeight: '50px'}}/>

          <div className="grid-wrapper">
              <span className="custom-font-bold" style={{fontSize: '30px'}}>All inclusive</span>
              <div className="grid-container-benefits">
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; <span className="custom-font-bold"> 5-day ski pass </span>(Mo-Fr) for the whole Skiarena Andermatt, Sedrun & Disentis</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; 6 nights <span className="custom-font-bold">accommodation</span> including bed-sheets </p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; <span className="custom-font-bold">Delicious food</span> all week: Breakfast, lunch to pack (Sandwiches etc.), dinner, late-night snacks</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; <span className="custom-font-bold">Public transport</span> from Zurich to Sedrun and back</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; Welcome <span className="custom-font-bold">Glühwein</span></p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; Free <span className="custom-font-bold">ski/snowboard lessons</span></p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; <span className="custom-font-bold">Fondue</span> at a fancy restaurant</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#9989; Lots of <span className="custom-font-bold">events</span> on and off the slopes</p>
                  </div>
              </div>
          </div>

          <div style={{minHeight: '50px'}}/>

          <div className="grid-wrapper">
              <span className="custom-font-bold" style={{fontSize: '30px'}}>Not Included</span>
              <div className="grid-container-benefits">
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#10133; <span className="custom-font-bold">Alcoholic beverages, </span>après ski & club entrance fees</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#10133;<span className="custom-font-bold"> Night</span> skiing (CHF10)</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#10133; <span className="custom-font-bold">Guided</span> ski-tours (~CHF80)</p>
                  </div>
                  <div className='text-item' style={{paddingRight: '20px'}}>
                      <p className="custom-font text" style={{fontSize: '15px', textAlign: 'left'}}> &#10133; <span className="custom-font-bold">Spa</span> (~CHF30)</p>
                  </div>
              </div>
          </div>

          <div style={{minHeight: '50px'}}/>

          <div className="footer">
              <div style={{minHeight: '50px'}}/>
              <a style={{textDecoration: 'none'}}href="https://icuzh.ch/"> <div style={{maxWidth: '500px', padding: '0 20px'}}>
                      <div className='image' style={{ backgroundImage: `url(${icu})`, height: '60px', backgroundSize: '300px', backgroundPosition: 'left'}}/>
                      <p className="custom-font" style={{fontSize: '15px', color: '#192c37', textAlign: 'left'}}>© 2022 Fachverein Informatik, All right reserved.</p>
                  </div></a>
          </div>
      </div>
  );
}

export default App;