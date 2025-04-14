import React from 'react';
import Header from './Header';
import Footer from './Footer';
import Start from './body/Start';
import './style/App.scss';
import { HashRouter, Routes, Route, NavLink } from 'react-router-dom';

function App() {
  return (
    <div className='App'>
      <Header></Header>
      <HashRouter>
            <Routes>
            <Route path='/' element={<Start />}></Route>
            </Routes>
        </HashRouter>
      <Footer></Footer>  
    </div>
  );
}

export default App;
