import './DeviceInfo.css'
import React from "react";
import { Link } from "react-router-dom";
import 'swiper/css';
import 'swiper/css/pagination';

import { useState } from 'react';
const DeviceInfo = ({ deviceID, deviceStatus }) => {
  const [cards] = useState([
    {
      manufacturer:'Aerobiosys Innovations',
      product:'DuoVent',
      prod_id:'C8:C6:79:9A:04:F7',
      lot_no:'DV-LL-2310006',
      mfd_date: '6-Dec-2023 02:30PM',
      model_no:'DV-LTS-01',
      serial_no:'DV-A-2310001',
      battery_no: 'DV-BAT231008',
      battery_mfd_date: '1-Dec-2023 03:23PM'
    },
  ])
  return (
    <section className="monitor">
      <div className='navbar'>
          <div className="brand">
            <img id='logo' src={process.env.PUBLIC_URL + 'aerobiosys.gif'} alt="Logo"></img>
            <h2 id='title'>Aerobiosys Innovations</h2>
          </div>
        </div>
    <h1>Device Info</h1>
    <div className="monitor-cards">
      <div className="card-container">
        <header className="card-header">
        <a href="/"><button className="back-button">Back</button></a>
          <span className="device-id">{deviceID}</span>
          <span className="device-status">{deviceStatus}</span>
        </header>
        <nav className="nav-tabs">
          <ul>
            <li className="tab">
              <Link to="/Monitoring"><p>Monitoring</p></Link>
            </li>
            <li className="tab active">
              <Link to='/DeviceInfo'>Device Info</Link>
            </li>
            <li className="tab">
              <Link to='/PatientInfo'><p>Patient Info</p></Link>
            </li>
          </ul>
        </nav>
        <div className="inner-card-container">
          { 
            <div className="cards">
            {
              cards.map((card, i) => (
                <div className="card-content" key={i}>  
                  <div className="table-container">
                    <table>
                      <thead>
                          <th colSpan={2}>Manufacturer</th>
                          <td>{card.manufacturer}</td>
                      </thead>
                      <tbody>
                        <tr>
                          <th>Product</th>
                          <td>{card.product}</td>
                          <th>Product ID</th>
                          <td>{card.prod_id}</td>
                          </tr>
                        <tr>
                          <th>Lot Number</th>
                          <td>{card.lot_no}</td>
                          <th>Manufactured Date</th>
                          <td>{card.mfd_date}</td>
                        </tr>
                        <tr>
                          <th>Model Number</th>
                          <td>{card.model_no}</td>
                          <th>Battery Number</th>
                          <td>{card.battery_no}</td>
                        </tr>
                        <tr>
                          <th>Serial Number</th>
                          <td>{card.serial_no}</td>
                          <th>Battery Manufactured Date</th>
                          <td>{card.battery_mfd_date}</td>
                        </tr>
                      </tbody>
                    </table>
                  </div>
              </div>  
              ))
            }
          </div>
            
          }
        </div>
      </div>
    </div>
    </section>
  );
};

export default DeviceInfo;