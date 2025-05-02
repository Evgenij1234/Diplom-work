import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useDispatch, useSelector } from "react-redux";
import Logo from "./img/logo";
import Person from "./img/Person";
import RegistrationForm from "./RegistrationForm";
import { showAuthForm, hideAuthForm } from './redux/counter/authSlice';

function Header() {
  const dispatch = useDispatch();
  const { isFormVisible } = useSelector((state) => state.auth);
  const { isAuthenticated, user } = useSelector((state) => state.auth);

  const handleClick = () => {
    if(isFormVisible === false){
      dispatch(showAuthForm());
    }
    else{
      dispatch(hideAuthForm());
    }
  };
  const navigate = useNavigate();

  const handleLogoClick = () => {
    navigate('/');
  };

  return (
    <div className="Header">
      <div className="Header-gap"></div>
      <div onClick={handleLogoClick} className="Header-left">
        <div className="Header-left-logo">
          <Logo></Logo>
        </div>
        <div className="Header-left-name">RivalX</div>
      </div>
      <div className="Header-gap"><RegistrationForm isFormVisible={isFormVisible}/></div>
      <button onClick={handleClick} className="Header-right">
        <div className="Header-right-logo">
          <Person></Person>
        </div>
        <div className="Header-right-name">
          {isAuthenticated ? user.username : 'Войти'}
        </div>
      </button>
      <div className="Header-gap"></div>
    </div>
  );
}

export default Header;