import React, {useState, useEffect} from 'react'
import './MonitorScreen.css'
import SocketIOClient from 'socket.io-client'
import {LineChart,XAxis,Tooltip,CartesianGrid,Line} from 'recharts'
function MonitorScreen() {
  const [data, setData] = useState([])
  useEffect(()=>{
    const socket = SocketIOClient("http://127.0.0.1:4001/")
    socket.on("message",(data)=>{
      setData(data)
    })
  },[data])
  return( 
    <div id='monitor-div'>
      <div className="head">
        <a href="/Monitoring"><button className="back-button-monitor">Exit</button></a>
      </div>
      <div className="header-line">
        <h2 className='title-m'>DuoVent</h2>
      </div>
      <div className="graph">
      <p id='monitor-p'>Pressure</p>
      <LineChart width={1000} height={200} data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
      <XAxis dataKey="name" />
      <Tooltip />
      <CartesianGrid stroke="#f5f5f5" />
      <Line type="monotone" dataKey="x" stroke="#ff7300" yAxisId={0} />
      </LineChart>

      <p id='monitor-p'>Flow</p>
      <LineChart width={1000} height={200} data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
      <XAxis dataKey="name" />
      <Tooltip />
      <CartesianGrid stroke="#f5f5f5" />
      <Line type="monotone" dataKey="x" stroke="#45ff45" yAxisId={1} />
      </LineChart>
      
      <p id='monitor-p'>Volume</p>
      <LineChart width={1000} height={200} data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
      <XAxis dataKey="name" />
      <Tooltip />
      <CartesianGrid stroke="#f5f5f5" />
      <Line type="monotone" dataKey="x" stroke="#ff7300" yAxisId={0} />
      </LineChart>
      </div>
    </div>
  )
}

export default MonitorScreen;
