import React, { useState, useRef, useEffect, } from 'react';
import { useNavigate } from 'react-router-dom';
import Logo from "./img/logo";
import Person from "./img/Person";
import RegistrationForm from "./RegistrationForm";

function Header() {
  const [isFormVisible, setIsFormVisible] = useState(false);

  const handleClick = () => {
    if(isFormVisible === false){
      setIsFormVisible(true);
    }
    else{
      setIsFormVisible(false);
    }
  };
  const navigate = useNavigate();

  const handleLogoClick = () => {
    navigate('/');
  };

  return (
    <div className="Header">
      <div className="Header-gap"></div>
      <div  onClick={handleLogoClick} className="Header-left">
        <div className="Header-left-logo">
          <Logo></Logo>
        </div>
        <div className="Header-left-name">RivalX</div>
      </div>
      <div className="Header-gap"><RegistrationForm isFormVisible={isFormVisible} /></div>
      <button  onClick={handleClick} className="Header-right">
        <div className="Header-right-logo">
          <Person></Person>
        </div>
        <div className="Header-right-name">Войти</div>
      </button>
      <div className="Header-gap"></div>
    </div>
  );
}

export default Header;
