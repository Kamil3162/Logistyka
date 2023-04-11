import logo from './logo.svg';
import './App.css';
import axios from "axios";
import {BrowserRouter, Routes, Route} from 'react-router-dom';
import Users from './components/Users';
import SamiTrucks from './components/SamiTrucks';
import LoginUser from './components/LoginUser';

axios.defaults.xsrfCookieName = 'csrftoken';
axios.defaults.xsrfHeaderName = 'X-CSRFToken';
axios.defaults.withCredentials = true;

const client = axios.create({
    baseURL: "http://127.0.0.1:8000"
});

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
