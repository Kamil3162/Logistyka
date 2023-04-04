import logo from './logo.svg';
import './App.css';
import {HashRouter as Router,Routes, Route} from "react-router-dom";
import Users from './components/Users';
import SamiTrucks from './components/SamiTrucks';

function App() {
  return (
    <div className="App">
      <SamiTrucks/>
        <Users/>
    </div>
  );
}

export default App;
