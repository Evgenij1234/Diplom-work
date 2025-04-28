import React from "react";
import Header from "./Header";
import Footer from "./Footer";
import Start from "./body/Start";
import Test from "./test/test"; // в проде удалить
import "./style/App.scss";
import { Provider } from "react-redux";
import { store } from "./redux/store";
import { HashRouter, Routes, Route, NavLink } from "react-router-dom";
import Work from "./body/Work/Work";

function App() {
  return (
    <div className="App">
      <Provider store={store}>
        <HashRouter>
          <Header />
          <div className="layout">
            <div className="main-content">
              <Routes>
                <Route path="/*" element={<Start />} />
                <Route path="/Work/*" element={<Work />} />
              </Routes>
            </div>
            <Footer />
          </div>
        </HashRouter>
      </Provider>
    </div>
  );
}

export default App;
