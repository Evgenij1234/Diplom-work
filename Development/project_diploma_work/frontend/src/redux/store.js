import { configureStore } from '@reduxjs/toolkit';
import counterReducer from './counter/Slice';

export const store = configureStore({
  reducer: {
    counter: counterReducer,
  },
});
