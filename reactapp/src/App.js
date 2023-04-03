import logo from './logo.svg';
import './App.css';
import {HashRouter as Router,
Route} from "react-router-dom";
import Users from './components/Users';
import SamiTrucks from './components/SamiTrucks';


function App() {
  return (
    <div className="App">
      <Users/>
        <SamiTrucks/>
    </div>
  );
}

export default App;
