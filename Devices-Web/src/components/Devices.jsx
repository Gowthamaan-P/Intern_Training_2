import './Devices.css';
import DevicesIcon from '@mui/icons-material/Devices';
import NotificationsIcon from '@mui/icons-material/Notifications';
import Button from '@mui/material/Button';
import { useState } from 'react';
import duovent from '../duovent.png';
import jeevanlite from '../jeevanlite.png';
import { Link } from "react-router-dom";
function Devices() {
  const [cards] = useState([
    {
      id:'DV-A-231007',
      status: 'Active',
      timestamp: 'Connected at: 2023-11-28 10:45 am',
      image: duovent
    },
    {
      id:'JL-A-231007',
      status: 'Idle',
      timestamp: 'Connected at: 2023-11-28 10:45 am',
      image: jeevanlite
    },
    {
      id:'DV-A-231008',
      status: 'Idle',
      timestamp: 'Connected at: 2023-11-28 10:45 am',
      image: duovent
    },
    {
      id:'JL-A-231008',
      status: 'Active',
      timestamp: 'Connected at: 2023-11-28 10:45 am',
      image: jeevanlite
    },
    {
      id:'DV-A-231009',
      status: 'Active',
      timestamp: 'Connected at: 2023-11-28 10:45 am',
      image: duovent
    },
    
    
    {
      id:'JL-A-231009',
      status: 'Idle',
      timestamp: 'Connected at: 2023-11-28 10:45 am',
      image: jeevanlite
    },

  ])
  
  const getStatusClass = (status) => status === 'Active' ? 'active-status' : 'inactive-status';

  return (
    <div className="app" id='devices'>
        <div className='navbar'>
          <div className="brand">
            <img id='logo' src={process.env.PUBLIC_URL + 'aerobiosys.gif'} alt="Logo"></img>
            <h2 id='title'>Aerobiosys Innovations</h2>
          </div>
            <div className='buttons'>
              <Button  variant="contained" id='device'><DevicesIcon /></Button>
              <Button  variant="contained" id='notification'><NotificationsIcon /></Button>
            </div>
        </div>
      <section>
        <div className="container">
          <h1>Devices</h1>
          <div className="cards">
            {
              cards.map((card, i) => (
                <div key={i} className="card"> <div className="card-content">
                    <h3 id='id'>{card.id}</h3>
                    <h4 className={getStatusClass(card.status)} id='status'>{card.status}</h4>
                    <p id='timestamp'>{card.timestamp}</p>
                  </div>
                    <Link to="/Monitoring" state={{ id: card.id, status: card.status }}>
                      <img className="ventilator-image" src={card.image} alt="ventilatorImage" />
                    </Link>
                  </div>
              ))
            }
          </div>
        </div>
      </section>
    </div>

  );
}

export default Devices;
