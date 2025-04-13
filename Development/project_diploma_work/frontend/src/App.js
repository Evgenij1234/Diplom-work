import React from 'react';
import Header from './Header'
import './style/App.scss';
import { HashRouter, Routes, Route, NavLink } from 'react-router-dom';

function App() {
  return (
    <div>
      <Header></Header>
      <HashRouter>
            <Routes>

            </Routes>
        </HashRouter>
    </div>
  );
}

export default App;
