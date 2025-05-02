import React, { useEffect } from "react";
import Header from "./Header";
import Footer from "./Footer";
import Start from "./body/Start";
import "./style/App.scss";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import { HashRouter, Routes, Route } from "react-router-dom";
import Work from "./body/Work/Work";
import axios from 'axios';
import { useDispatch, useSelector } from 'react-redux';
import { loginSuccess, logout } from './redux/counter/authSlice';
import ProtectedRoute from './ProtectedRoute';

function AppWrapper() {
  const dispatch = useDispatch();

  useEffect(() => {
    const token = localStorage.getItem('token');
    const username = localStorage.getItem('username');
    if (token && username) {
      axios.get('http://localhost:5000/validate-token', {
        headers: { Authorization: `Bearer ${token}` }
      })
      .then(response => {
        if (response.data.valid) {
          dispatch(loginSuccess({
            user: { 
              id: response.data.user_id, 
              username: username 
            },
            token
          }));
        }
      })
      .catch(() => {
        localStorage.removeItem('token');
        localStorage.removeItem('username');
        dispatch(logout());
      });
    }
  }, [dispatch]);

  return (
    <div className="App">
      <HashRouter>
        <Header />
        <div className="layout">
          <div className="main-content">
            <Routes>
              <Route path="/*" element={<Start />} />
              <Route 
                path="/work/*" 
                element={
                  <ProtectedRoute>
                    <Work />
                  </ProtectedRoute>
                } 
              />
            </Routes>
          </div>
          <Footer />
        </div>
      </HashRouter>
    </div>
  );
}

function App() {
  return (
    <Provider store={store}>
      <AppWrapper />
    </Provider>
  );
}

export default App;