import './App.css';
import Devices from './components/Devices';
import Monitor from "./components/Monitor";
import DeviceInfo from "./components/DeviceInfo"
import PatientInfo from './components/PatientInfo';
import PatientHistory from './components/PatientHistory'
import { Routes,Route } from 'react-router-dom';
function App() {
  return (
    <div className="app" id='devices'>
        <Routes>
            <Route path='/' element={<Devices />} />
            <Route path='/Monitoring' element={<Monitor />} />
            <Route path='/DeviceInfo' element={<DeviceInfo />} />
            <Route path='/PatientInfo' element={<PatientInfo />} />
            <Route path='/PatientHistory' element={<PatientHistory />} />
          </Routes>
    </div>

  );
}

export default App;
