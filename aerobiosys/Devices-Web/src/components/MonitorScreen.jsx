import React, {useState, useEffect} from 'react'
import SocketIOClient from 'socket.io-client'
function MonitorScreen() {
  const [data, setData] = useState("[]")
  useEffect(()=>{
    const socket = SocketIOClient("http://127.0.0.1:4001/")
    socket.on("message",(data)=>{
      setData(data)
    })
  },[])
  return( 
    <div>
      <h1>{data}</h1>
    </div>
  )
}

export default MonitorScreen;
