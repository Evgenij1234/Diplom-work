import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Start from "./body/Start";
import Test from "./test/test"; // в проде удалить
import "./style/App.scss";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import { HashRouter, Routes, Route, NavLink } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <Header></Header>
        <HashRouter>
          <Routes>
            <Route path="/" element={<Start />}></Route>
          </Routes>
        </HashRouter>
        <Footer></Footer>
        <Test/>  // в проде удалить
      </Provider>
    </div>
  );
}

export default App;
