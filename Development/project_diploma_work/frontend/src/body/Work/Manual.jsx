import React from "react";
import Manual1 from "./Manual_text/Manual1";
import Manual2 from "./Manual_text/Manual2";
import Manual3 from "./Manual_text/Manual3";
import Manual4 from "./Manual_text/Manual4";
import Manual5 from "./Manual_text/Manual5";
import { Routes, Route, Link } from "react-router-dom";

function Manual() {
  return (
    <div className="Manual">
      <div className="Manual-left">
        <div className="Manual-left-box">
          <div className="Manual-left-box-title">Туториал</div>
          <Link to="manual1" className="Manual-left-box-link">
          Общая информация
          </Link>
          <Link to="manual2" className="Manual-left-box-link">
            Возможности платформы
          </Link>
          <Link to="manual3" className="Manual-left-box-link">
            Правила скрапинга
          </Link>
          <Link to="manual4" className="Manual-left-box-link">
            Выходные данные
          </Link>
          <Link to="manual5" className="Manual-left-box-link">
            Визаулизация
          </Link>
        </div>
      </div>
      <div className="Manual-right">
        <div className="Manual-right-box">
          <Routes>
            <Route index element={<Manual1 />} />
            <Route path="manual1" element={<Manual1 />} />
            <Route path="manual2" element={<Manual2 />} />
            <Route path="manual3" element={<Manual3 />} />
            <Route path="manual4" element={<Manual4 />} />
            <Route path="manual5" element={<Manual5 />} />
          </Routes>
        </div>
      </div>
    </div>
  );
}

export default Manual;
