import React from "react";

function Manual2() {
  return (
    <div className="Manual-left-box-link-text">
      <p className="Manual-left-box-link-tex-Title">Возможности платформы</p>
      <p className="Manual-left-box-link-tex-content">
        <section id="features">
          <h2>Возможности платформы</h2>
          <ul>
            <li>
              <strong>Сбор данных:</strong> Получение информации с указанных
              сайтов с возможностью задания параметров парсинга.
            </li>
            <li>
              <strong>Экспорт в JSON:</strong> Скачивание полученных данных в
              формате JSON.
            </li>
            <li>
              <strong>Сохранение в базу данных:</strong> Автоматическая запись
              собранной информации для последующего анализа.
            </li>
            <li>
              <strong>Поиск по базе:</strong> Доступ к ранее собранным данным с
              возможностью фильтрации по параметрам.
            </li>
            <li>
              <strong>Экспорт в CSV:</strong> Скачивание результатов поиска в
              формате CSV.
            </li>
            <li>
              <strong>Построение графиков:</strong> Визуализация динамики цен по
              ресурсу, категории и названию товара.
            </li>
          </ul>
        </section>
      </p>
    </div>
  );
}

export default Manual2;
