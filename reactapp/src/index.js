import React from 'react';
import { createRoot } from "react-dom/client";
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

document.body.innerHTML = '<div id="app"></div>'

const root = createRoot(document.getElementById('app'));
root.render(<App />);

