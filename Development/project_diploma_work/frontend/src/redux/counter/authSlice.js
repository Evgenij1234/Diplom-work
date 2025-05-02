import { createSlice } from '@reduxjs/toolkit';

// Проверяем localStorage при инициализации состояния
const getInitialAuthState = () => {
  const token = localStorage.getItem('token');
  const username = localStorage.getItem('username');

  return {
    isAuthenticated: !!token,
    user: username ? { username } : null,
    token: token || null,
    loading: false,
    error: null
  };
};

const authSlice = createSlice({
  name: 'auth',
  initialState: getInitialAuthState(),
  reducers: {
    loginStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    loginSuccess: (state, action) => {
      state.isAuthenticated = true;
      state.user = action.payload.user;
      state.token = action.payload.token;
      state.loading = false;
      state.error = null;
      
      // Сохраняем в localStorage
      localStorage.setItem('token', action.payload.token);
      localStorage.setItem('username', action.payload.user.username);
    },
    loginFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
      
      // Очищаем localStorage при ошибке
      localStorage.removeItem('token');
      localStorage.removeItem('username');
    },
    registerStart: (state) => {
      state.loading = true;
      state.error = null;
    },
    registerSuccess: (state, action) => {
      state.isAuthenticated = true;
      state.user = action.payload.user;
      state.token = action.payload.token;
      state.loading = false;
      state.error = null;
      
      // Сохраняем в localStorage
      localStorage.setItem('token', action.payload.token);
      localStorage.setItem('username', action.payload.user.username);
    },
    registerFailure: (state, action) => {
      state.loading = false;
      state.error = action.payload;
      
      // Очищаем localStorage при ошибке
      localStorage.removeItem('token');
      localStorage.removeItem('username');
    },
    logout: (state) => {
      state.isAuthenticated = false;
      state.user = null;
      state.token = null;
      
      // Очищаем localStorage
      localStorage.removeItem('token');
      localStorage.removeItem('username');
    },
    checkAuth: (state) => {
      const token = localStorage.getItem('token');
      const username = localStorage.getItem('username');
      
      if (token && username) {
        state.isAuthenticated = true;
        state.user = { username };
        state.token = token;
      } else {
        state.isAuthenticated = false;
        state.user = null;
        state.token = null;
      }
    }
  }
});

export const { 
  loginStart, 
  loginSuccess, 
  loginFailure,
  registerStart,
  registerSuccess,
  registerFailure,
  logout,
  checkAuth
} = authSlice.actions;

export default authSlice.reducer;