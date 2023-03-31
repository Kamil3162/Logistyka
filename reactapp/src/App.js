import logo from './logo.svg';
import './App.css';
import {HashRouter as Router,
Route} from "react-router-dom";
import Users from './components/Users'

function App() {
  return (
    <div className="App">
      <Users/>
    </div>
  );
}

export default App;
