import logo from './logo.svg';
import './App.css';
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Users from './components/Users';
import SamiTrucks from './components/SamiTrucks';
import LoginUser from './components/LoginUser';

function App() {
  return (
      <div>
          <a href="/login">
              dsa
          </a>
          Hi this is react main
          <Routes>
            <Route path="/login" element={<LoginUser/>}/>
            <Route path="/samitrucks" component={<SamiTrucks/>}/>
            <Route path="/users" component={<Users/>}/>
          </Routes>
      </div>
  );
}

export default App;
