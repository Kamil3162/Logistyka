import React from 'react';
import ReactDOM from 'react-dom';
import { createRoot } from "react-dom/client";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {BrowserRouter} from "react-router-dom";
const rootElement = document.getElementById('root');
const root = createRoot(rootElement);

// 👇️ wrap App in Router

root.render(
  <BrowserRouter>
    <App />
  </BrowserRouter>
);

reportWebVitals();
