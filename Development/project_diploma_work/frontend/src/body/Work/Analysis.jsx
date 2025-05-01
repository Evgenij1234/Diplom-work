import React from "react";

function Analysis() {
  return (
    <div className="Analysis">
      <div className="Analysis-left">
        <div className="Analysis-left-box">
          <div className="Analysis-left-box-input">
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">time_start</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                placeholder="dd/mm/yyyy"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">time_stop</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                placeholder="dd/mm/yyyy"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">name</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                placeholder="Ступень железобетонная"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">category</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                placeholder="Ступени железобетонные"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">resource</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                placeholder="https://baza.124bt.ru"
              />
            </div>
          </div>
          <div className="Analysis-left-box-button">
            <button className="Analysis-left-button">Найти</button>
          </div>
        </div>
      </div>
      <div className="Analysis-right">
        <div className="Analysis-right-box">
          <div className="Analysis-right-box-data">
            <div className="Analysis-right-box-data-text">
              dataasdd Lorem ipsum dolor sit amet, consectetur adipisicing elit.
              Architecto magnam, porro possimus ea sequi, quam obcaecati
              repudiandae nisi doloremque quas officia placeat iusto accusamus
              veritatis delectus! Necessitatibus enim illo maxime!
            </div>
          </div>
          <div className="Analysis-right-box-button">
            <button className="Analysis-right-box-button-button">
              Построить
            </button>
            <button className="Analysis-right-box-button-button">
              Скачать
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Analysis;
