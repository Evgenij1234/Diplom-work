import { createSlice } from "@reduxjs/toolkit";

// Проверяем localStorage при инициализации
const initialState = {
  isAuthenticated: localStorage.getItem("isAuthenticated") === "true",
  user: JSON.parse(localStorage.getItem("user")) || null,
};

const authSlice = createSlice({
  name: "auth",
  initialState,
  reducers: {
    loginSuccess(state, action) {
      state.isAuthenticated = true;
      state.user = action.payload;
      // Сохраняем в localStorage
      localStorage.setItem("isAuthenticated", "true");
      localStorage.setItem("user", JSON.stringify(action.payload));
    },
    logout(state) {
      state.isAuthenticated = false;
      state.user = null;
      // Удаляем из localStorage
      localStorage.removeItem("isAuthenticated");
      localStorage.removeItem("user");
    },
    registerSuccess(state, action) {
      state.isAuthenticated = true;
      state.user = action.payload;
      // Сохраняем в localStorage
      localStorage.setItem("isAuthenticated", "true");
      localStorage.setItem("user", JSON.stringify(action.payload));
    },
  },
});

export const { loginSuccess, logout, registerSuccess } = authSlice.actions;
export default authSlice.reducer;