import React from "react";
import { Link } from "react-router-dom";
import './DeviceInfo.css'
import { useState } from 'react';
const DeviceInfo = ({ deviceID, deviceStatus }) => {
  const [cards] = useState([
    {
      product:'DuoVent',
      prod_id:'DV-V-01982C',
      lot_no:'12345675',
      mfd_date: '6-Dec-2023',
      model_no:'DV789544D',
      serial_no:'9875642354',
      battery_no: '3544352543',
      battery_mfd_date: 'Emergency Patient'
    },
  ])
  return (
    <section className="monitor">
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
              <Link to="/Monitoring">Monitoring</Link>
            </li>
            <li className="tab active">
              <Link to='/DeviceInfo'>Device Info</Link>
            </li>
            <li className="tab">
              <Link to='/PatientInfo'>Patient Info</Link>
            </li>
          </ul>
        </nav>
        <div className="inner-card-container">
          { 
            <div className="cards">
            {
              cards.map((card, i) => (
                <div key={i}> 
                    <table>
                        <legend>Manufacturer : Aerobiosys Innovations</legend>
                        <br/>
                        <tr>
                            <th>Product:</th>
                            <td>{card.product}</td>
                            <th>Product ID:</th>
                            <td>{card.pid}</td>
                        </tr>
                        <br/>
                        <tr>
                            <th>Lot Number:</th>
                            <td>{card.lot_no}</td>
                            <th>Manufactured Date:</th>
                            <td>{card.mfd_date}</td>
                        </tr>
                        <br/>
                        <tr>
                            <th>Model Number:</th>
                            <td>{card.model_no}</td>
                            <th>Battery Number:</th>
                            <td>{card.battery_no}</td>
                        </tr>
                        <br/>
                        <tr>
                            <th>Serial Number</th>
                            <td>{card.serial_no}</td>
                            <th>Battery Manufacured Date:</th>
                            <td>{card.battery_mfd_date}</td>
                        </tr>
                        <br/>
                    </table>
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