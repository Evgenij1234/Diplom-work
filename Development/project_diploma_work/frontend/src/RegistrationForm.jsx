import React, { useState } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  loginSuccess,
  logout,
  registerSuccess,
} from "./redux/counter/authSlice";

function RegistrationForm({ isFormVisible }) {
  const [activeForm, setActiveForm] = useState("register"); // 'register' | 'login'
  const dispatch = useDispatch();
  const { isAuthenticated } = useSelector((state) => state.auth);

  if (!isFormVisible) return null;

  if (isAuthenticated) {
    return (
      <div className="RegistrationForm">
        <Exit />
      </div>
    );
  }

  return (
    <div className="RegistrationForm">
      <div className="RegistrationForm-menu">
        <button
          className="RegistrationForm-menu-button"
          onClick={() => setActiveForm("login")}
        >
          Вход
        </button>
        <button
          className="RegistrationForm-menu-button"
          onClick={() => setActiveForm("register")}
        >
          Регистрация
        </button>
      </div>
      {activeForm === "register" ? <Register /> : <LogIn />}
    </div>
  );
}

function Register() {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Здесь может быть запрос к API
    dispatch(registerSuccess({ username: login }));
    setLogin("");
    setPassword("");
  };

  return (
    <form className="Register" onSubmit={handleSubmit}>
      <div className="Register-div">
        <input
          className="Register-div-input"
          type="text"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
          placeholder="Логин"
        />
      </div>
      <div className="Register-div">
        <input
          className="Register-div-input"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          placeholder="Пароль"
        />
      </div>
      <button className="Register-div-button" type="submit">
        Зарегистрироваться
      </button>
    </form>
  );
}

function LogIn() {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = (e) => {
    e.preventDefault();
    // Здесь может быть запрос к API
    dispatch(loginSuccess({ username: login }));
    setLogin("");
    setPassword("");
  };

  return (
    <form className="Register" onSubmit={handleSubmit}>
      <div className="Register-div">
        <input
          className="Register-div-input"
          type="text"
          value={login}
          onChange={(e) => setLogin(e.target.value)}
          required
          placeholder="Логин"
        />
      </div>
      <div className="Register-div">
        <input
          className="Register-div-input"
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          placeholder="Пароль"
        />
      </div>
      <button className="Register-div-button" type="submit">
        Войти
      </button>
    </form>
  );
}

function Exit() {
  const dispatch = useDispatch();

  const handleLogout = () => {
    dispatch(logout());
  };

  return (
    <div>
      <button className="Register-div-button" onClick={handleLogout}>
        Выйти
      </button>
    </div>
  );
}

export default RegistrationForm;
