import './App.css';
import card from './styles/card.css';
import Button from './components/Buttons';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Light Bulb Control</h1>
        <div className="pileofcard">
          <div className="card">
            <div className='name'>
              BEDROOM
            </div>
            <img src="https://www.ikea.com/th/en/images/products/malm-bedroom-furniture-set-of-4-black-brown__1102127_pe866548_s5.jpg"></img>
            <div className='option'>
              Close      Manual
              <Button></Button>
              Open       Auto
            </div>
          </div>
          <div className="card">
            <div className='name'>
              KITCHEN
            </div>
            <img src="https://www.bhg.com/thmb/H2lg9rQKk5QAYcXCh1bhQVbreiQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/white-kitchen-floating-shelves-232ac9fb-fad090ab1f73478589de35a4e9b3b1e9.jpg"></img>
            <div className='option'>
              Close      Manual
              <Button></Button>
              Open       Auto
            </div>
          </div>
          <div className="card">
            <div className='name'>
              LOUNGE
            </div>
            <img src="https://static.asianpaints.com/content/dam/asianpaintsbeautifulhomes/spaces/living-rooms/9-living-room-lounge-designs-to-transform-your-home/Title-living-room-lounge-couch-forming-a-circle.jpg"></img>
            <div className='option'>
              Close      Manual
              <Button></Button>
              Open       Auto
            </div>
          </div>
        </div>
      </header>
    </div>
  );
}

export default App;