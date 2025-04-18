import { configureStore } from "@reduxjs/toolkit";
import authReducer from "./counter/authSlice";

export const store = configureStore({
  reducer: {
    auth: authReducer,
  },
});