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
    <div>
      <LineChart width={1000} height={400} data={data} margin={{ top: 5, right: 20, left: 10, bottom: 5 }}>
      <XAxis dataKey="name" />
      <Tooltip />
      <CartesianGrid stroke="#f5f5f5" />
      <Line type="monotone" dataKey="x" stroke="#ff7300" yAxisId={0} />
      <Line type="monotone" dataKey="y" stroke="#387908" yAxisId={1} />
      </LineChart>
    </div>
  )
}

export default MonitorScreen;
