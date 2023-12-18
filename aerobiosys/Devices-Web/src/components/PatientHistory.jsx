import React from "react";
import './PatientHistory.css'
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
      room_bed:'15A - 45',
      ibw:'59.88kgs',
      itv:'341-455ml',
      bmi:'0.00',
      reason:'Injury',
      potential:'Injury'
    }
  ]);
  const table1Data = cards.slice(0, 5);
  return (
    <section className="monitor">
      <div className='navbar'>
          <div className="brand">
            <img id='logo' src={process.env.PUBLIC_URL + 'aerobiosys.gif'} alt="Logo"></img>
            <h2 id='title'>Aerobiosys Innovations</h2>
          </div>
        </div>
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
                <div key={i}> 
                <div className="card-content">
                <div className="tables-container">
                  <div className="table-container">
                    <table>
                      <thead>
                        <tr>
                          <th>Emergency Status</th>
                          <th>Age</th>
                          <th>Gender</th>
                          <th>Height</th>
                          <th>Weight</th>
                        </tr>
                      </thead>
                      <tbody>
                        {table1Data.map((item, index) => (
                          <tr key={index}>
                            <td>{item.emergency_status}</td>
                            <td>{item.age}</td>
                            <td>{item.gender}</td>
                            <td>{item.height}</td>
                            <td>{item.weight}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                
                  <div className="table-container">
                    <table>
                      <thead>
                        <tr>
                          <th>Blood Group</th>
                          <th>Contact</th>
                          <th>Admitted on</th>
                          <th>Room/Bed</th>
                        </tr>
                      </thead>
                      <tbody>
                          <tr>
                            <td>{card.blood_group}</td>
                            <td>{card.contact}</td>
                            <td>{card.admitted}</td>
                            <td>{card.room_bed}</td>
                          </tr>
                      </tbody>
                    </table>
                  </div>

                  <div className="table-container">
                    <table>
                      <thead>
                        <tr>
                          <th>IBW</th>
                          <th>ITV</th>
                          <th>BMI</th>
                          <th>Reason</th>
                          <th>Potential</th>
                        </tr>
                      </thead>
                      <tbody>
                          <tr>
                            <td>{card.ibw}</td>
                            <td>{card.itv}</td>
                            <td>{card.bmi}</td>
                            <td>{card.reason}</td>
                            <td>{card.potential}</td>
                          </tr>
                      </tbody>
                    </table>
                  </div>
                </div>
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