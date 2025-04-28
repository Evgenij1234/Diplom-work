import React from "react";
import { Routes, Route, Link } from "react-router-dom";
import Scraping from "./Scraping";
import Analysis from "./Analysis";
import Manual from "./Manual";

function Work() {
  return (
    <div className="Work">
      <nav className="work-nav">
        <div className="work-nav-gap"></div>
        <Link to="scraping" className="work-nav-link">
          Скрапинг
        </Link>
        <Link to="analysis" className="work-nav-link">
          Анализ
        </Link>
        <Link to="manual" className="work-nav-link">
          Руководство
        </Link>
      </nav>
      <div className="work-content">
        <Routes>
          <Route index element={<Scraping />} />
          <Route path="scraping" element={<Scraping />} />
          <Route path="analysis" element={<Analysis />} />
          <Route path="manual" element={<Manual />} />
        </Routes>
      </div>
    </div>
  );
}

export default Work;
