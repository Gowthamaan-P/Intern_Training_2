import { clear } from 'console';
import express from 'express'
import http from 'http'
import * as socketio from 'socket.io'
const port = 4001;

const app = express()
const httpServer = http.createServer(app)

const server = new socketio.Server(httpServer, {
    cors:{
        origin: '*',
    }
})
let timeChange
server.on("connection",(socket)=>{
    console.log("connected")
    if(timeChange) clearInterval(timeChange)
    setInterval(()=>socket.emit("message", new Date()),1000)
})
httpServer.listen(port)