import React from "react";
import './Monitor.css'
import { useState } from 'react';
const PatientHistory = ({ deviceID, deviceStatus }) => {
  const [cards] = useState([
    {
      emergency_status: 'Emergency Patient',
      age:'25',
      gender: 'Male',
      height: '185 cms',
      weight: '85 kgs',
      blood_group: 'B+ve',
      contact:'6985473251',
      admitted: '5-Dec-2023 10:45 am',
      room_bed:'Room 15A - 45',
      ibw:'59.88kgs',
      itv:'341-455ml',
      bmi:'0.00',
      reason:'Injury',
      potential:'Injury'
    }
  ])
  return (
    <section className="monitor">
    <h1>Patient History</h1>
    <div className="monitor-cards">
      <div className="card-container">
        <header className="card-header">
        <a href="/PatientInfo" className="btn"><button className="back-button">Back</button></a>
          <span className="device-id">{deviceID}</span>
          <span className="device-status">{deviceStatus}</span>
        </header>
        <div className="inner-card-container">
          { 
            <div className="cards">
            {
              cards.map((card, i) => (
                <div key={i} className="monitor-card"> 
                <div className="card-content">
                    <p id='id'>{card.emergency_status}</p>
                    <p id='age'>{card.age}</p>
                    <p id='date'>{card.gender}</p>
                    <p id='date'>{card.height}</p>
                    <p id='date'>{card.weight}</p>
                    <p id='date'>{card.blood_group}</p>
                    <p id='date'>{card.contact}</p>
                    <p id='date'>{card.admitted}</p>
                    <p id='date'>{card.room_bed}</p>
                    <p id='date'>{card.ibw}</p>
                    <p id='date'>{card.itv}</p>
                    <p id='date'>{card.bmi}</p>
                    <p id='date'>{card.reason}</p>
                    <p id='date'>{card.potential}</p>
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

export default PatientHistory;