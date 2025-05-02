import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import {
  loginStart,
  loginSuccess,
  loginFailure,
  registerStart,
  registerSuccess,
  registerFailure,
  logout
} from "./redux/counter/authSlice";
import axios from 'axios';

function RegistrationForm({ isFormVisible }) {
  const [activeForm, setActiveForm] = useState("register");
  const dispatch = useDispatch();
  const { isAuthenticated, user } = useSelector((state) => state.auth);

  // Проверяем аутентификацию при загрузке
  useEffect(() => {
    const token = localStorage.getItem('token');
    const username = localStorage.getItem('username');
    
    if (token && username && !isAuthenticated) {
      dispatch(loginSuccess({
        user: { username },
        token
      }));
    }
  }, [dispatch, isAuthenticated]);

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
          className={`RegistrationForm-menu-button ${activeForm === 'login' ? 'active' : ''}`}
          onClick={() => setActiveForm("login")}
        >
          Вход
        </button>
        <button
          className={`RegistrationForm-menu-button ${activeForm === 'register' ? 'active' : ''}`}
          onClick={() => setActiveForm("register")}
        >
          Регистрация
        </button>
      </div>
      {activeForm === "register" ? <Register setActiveForm={setActiveForm} /> : <LogIn />}
    </div>
  );
}

function Register({ setActiveForm }) {
  const [login, setLogin] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const [success, setSuccess] = useState(false);
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    if (login.length < 4) {
      setError("Имя пользователя должно быть не менее 4 символов");
      return;
    }

    if (password.length < 6) {
      setError("Пароль должен быть не менее 6 символов");
      return;
    }

    try {
      dispatch(registerStart());
      const response = await axios.post('http://localhost:5000/register', {
        username: login,
        password
      });

      dispatch(registerSuccess({
        user: { 
          id: response.data.user_id, 
          username: response.data.username 
        },
        token: response.data.access_token
      }));

      localStorage.setItem('token', response.data.access_token);
      localStorage.setItem('username', response.data.username);
      setSuccess(true);

    } catch (err) {
      const errorMessage = err.response?.data?.error || "Ошибка регистрации";
      setError(errorMessage);
      dispatch(registerFailure(errorMessage));
      localStorage.removeItem('token');
      localStorage.removeItem('username');
    }
  };

  const handleGoToLogin = () => {
    setActiveForm("login");
    setSuccess(false);
  };

  if (success) {
    return (
      <div className="Register">
        <div className="registration-success">
          <p>Регистрация прошла успешно!</p>
          <div className="success-buttons">
            <button 
              type="button" 
              className="Register-div-button secondary-button"
              onClick={handleGoToLogin}
            >
              Войти
            </button>
          </div>
        </div>
      </div>
    );
  }

  return (
    <form className="Register" onSubmit={handleSubmit}>
      {error && <div className="error-message">{error}</div>}
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
  const [error, setError] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError("");

    try {
      dispatch(loginStart());
      const response = await axios.post('http://localhost:5000/login', {
        username: login,
        password
      });

      dispatch(loginSuccess({
        user: { 
          id: response.data.user_id, 
          username: response.data.username 
        },
        token: response.data.access_token
      }));

      localStorage.setItem('token', response.data.access_token);
      localStorage.setItem('username', response.data.username);
    } catch (err) {
      const errorMessage = err.response?.data?.error || "Неверный логин или пароль";
      setError(errorMessage);
      dispatch(loginFailure(errorMessage));
      localStorage.removeItem('token');
      localStorage.removeItem('username');
    }
  };

  return (
    <form className="Register" onSubmit={handleSubmit}>
      {error && <div className="error-message">{error}</div>}
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
    localStorage.removeItem('token');
    localStorage.removeItem('username');
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