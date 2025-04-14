import React from "react";
import Logo from "./img/logo";
import Person from "./img/Person";

function Header() {
  return (
    <div className="Header">
      <div className="Header-gap"></div>
      <div className="Header-left">
        <div className="Header-left-logo">
          <Logo></Logo>
        </div>
        <div className="Header-left-name">RivalX</div>
      </div>
      <div className="Header-gap"></div>
      <div className="Header-right">
        <div className="Header-right-logo">
          <Person></Person>
        </div>
        <div className="Header-right-name">Войти</div>
      </div>
      <div className="Header-gap"></div>
    </div>
  );
}

export default Header;
