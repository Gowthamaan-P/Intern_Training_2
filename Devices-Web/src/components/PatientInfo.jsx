import React from "react";
import './PatientInfo.css'
import { Link } from "react-router-dom";
import { useState } from 'react';
const PatientInfo = ({ deviceID, deviceStatus }) => {
  const [cards] = useState([
    {
      pid:'PA-IV-0198',
      age_gender: '25, Male',
      admitted: 'Admitted on: 5-Dec-2023 10:45 am',
      emergency_status: 'Emergency Patient'
    },
    {
      pid:'PA-IV-0199',
      age_gender: '28, Female',
      admitted: 'Admitted on: 6-Dec-2023 10:45 am',
      emergency_status: ''
    }
  ])
  return (
    <section className="monitor">
      <div className='navbar'>
          <div className="brand">
            <img id='logo' src={process.env.PUBLIC_URL + 'aerobiosys.gif'} alt="Logo"></img>
            <h2 id='title'>Aerobiosys Innovations</h2>
          </div>
        </div>
    <h1>Patient Info</h1>
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
            <li className="tab">
              <Link to='/DeviceInfo'><p>Device Info</p></Link>
            </li>
            <li className="tab active">
              <Link to='/PatientInfo'>Patient Info</Link>
            </li>
          </ul>
        </nav>
        <div className="inner-card-container">
          { 
            <div className="cards">
            {
              cards.map((card, i) => (
                <div key={i} className="monitor-card"> 
                <div className="card-content">
                    <h3 id='id'>{card.pid}</h3>
                    <h4 id='age'>{card.age_gender}</h4>
                    <p id='date'>{card.admitted}</p>
                  </div>
                  <h5 id= 'emergency_status'>{card.emergency_status}</h5>
                  <a href="/PatientHistory"><button id='case-history'>Case History</button></a>
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

export default PatientInfo;