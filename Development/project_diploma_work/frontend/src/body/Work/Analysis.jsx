import React, { useState } from "react";
import "../../style/Work.scss";
import { useDispatch, useSelector } from "react-redux";
import Notification from "../../Notification";
import Diagram from "./Diagram";

function Analysis() {
  const apiDomain = process.env.REACT_APP_API_DOMAIN;
  const { user } = useSelector((state) => state.auth);
  const [filters, setFilters] = useState({
    resource: "",
    category: "",
    name: "",
    time_start: "",
    time_end: "",
    user: user.username,
  });
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const fetchProducts = async () => {
    setLoading(true);
    setError(null);
    setShowDiagram(false)
    try {
      const params = new URLSearchParams();
      params.append("user", filters.user);

      if (filters.resource) params.append("resource", filters.resource);
      if (filters.category) params.append("category", filters.category);
      if (filters.name) params.append("name", filters.name);

      if (filters.time_start) {
        const startDate = new Date(filters.time_start);
        params.append("time_start", startDate.toISOString().slice(0, 19));
      }

      if (filters.time_end) {
        const endDate = new Date(filters.time_end);
        params.append("time_end", endDate.toISOString().slice(0, 19));
      }

      const response = await fetch(
        `${apiDomain}/products?${params.toString()}`
      );

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }

      const data = await response.json();
      setResults(data.products || []);
    } catch (err) {
      setError(`Ошибка: ${err.message}`);
      console.error("Ошибка при загрузке данных:", err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    fetchProducts();
  };

  const formatDate = (dateString) => {
    if (!dateString) return "";
    const date = new Date(dateString);
    return (
      date.toLocaleDateString("ru-RU") + " " + date.toLocaleTimeString("ru-RU")
    );
  };

  const downloadCSV = () => {
    if (results.length === 0) {
      setError("Нет данных для скачивания");
      return;
    }

    // CSV заголовки
    const headers = [
      "Название",
      "Категория",
      "Ресурс",
      "Цена",
      "Валюта",
      "Дата",
      "Характеристики",
      "Ссылка",
    ];

    // Обработка данных для CSV
    const csvRows = [];

    // Добавляем заголовки
    csvRows.push(headers.join(";"));

    // Формируем строки данных
    results.forEach((product) => {
      const row = [
        `"${(product.name || "").replace(/"/g, '""')}"`,
        `"${(product.category || "").replace(/"/g, '""')}"`,
        `"${(product.resource || "").replace(/"/g, '""')}"`,
        product.price || "",
        `"${(product.unit || "").replace(/"/g, '""')}"`,
        `"${formatDate(product.date_time)}"`,
        `"${JSON.stringify(product.characteristics || {}).replace(
          /"/g,
          '""'
        )}"`,
        `"${(product.link || "").replace(/"/g, '""')}"`,
      ];
      csvRows.push(row.join(";"));
    });

    // Создаем и скачиваем файл
    const csvContent = "\uFEFF" + csvRows.join("\n");
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.setAttribute("href", url);
    link.setAttribute(
      "download",
      `products_${filters.user}_${new Date().toISOString().slice(0, 10)}.csv`
    );
    link.style.visibility = "hidden";
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };
  // Добавьте эту вспомогательную функцию перед компонентом Analysis
  const renderCharacteristics = (characteristics) => {
    if (!characteristics) return null;

    try {
      // Если characteristics уже объект
      if (typeof characteristics === "object") {
        return Object.entries(characteristics).map(([key, value]) => (
          <div key={key} className="characteristic-item">
            <span className="characteristic-key">{key}:</span>
            <span className="characteristic-value">{String(value)}</span>
          </div>
        ));
      }

      // Если characteristics это JSON строка
      const parsed = JSON.parse(characteristics);
      return Object.entries(parsed).map(([key, value]) => (
        <div key={key} className="characteristic-item">
          <span className="characteristic-key">{key}:</span>
          <span className="characteristic-value">{String(value)}</span>
        </div>
      ));
    } catch (e) {
      return (
        <div className="characteristic-error">
          Неверный формат характеристик
        </div>
      );
    }
  };

  const [showDiagram, setShowDiagram] = useState(false);

  return (
    <div className="Analysis">
      <div className="Analysis-left">
        <form className="Analysis-left-box" onSubmit={handleSubmit}>
          <div className="Analysis-left-box-input">
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">Ресурс</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                name="resource"
                value={filters.resource}
                onChange={handleInputChange}
                placeholder="https://baza.124bt.ru"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">Категория</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                name="category"
                value={filters.category}
                onChange={handleInputChange}
                placeholder="Ступени железобетонные"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">Название</span>
              <input
                className="Analysis-left-input-input"
                type="text"
                name="name"
                value={filters.name}
                onChange={handleInputChange}
                placeholder="Ступень железобетонная"
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">Начиная</span>
              <input
                className="Analysis-left-input-input"
                type="datetime-local"
                name="time_start"
                value={filters.time_start}
                onChange={handleInputChange}
              />
            </div>
            <div className="Analysis-left-input">
              <span className="Analysis-left-input-name">Заканчивая</span>
              <input
                className="Analysis-left-input-input"
                type="datetime-local"
                name="time_end"
                value={filters.time_end}
                onChange={handleInputChange}
              />
            </div>
          </div>
          <div className="Analysis-left-box-button">
            <button
              className="Analysis-left-button"
              type="submit"
              disabled={loading}
            >
              {loading ? "Загрузка..." : "Найти"}
            </button>
            <button
              onClick={() => setShowDiagram(true)}
              className="Analysis-left-button"
              type="button"
            >
              Диаграмма
            </button>
            <button
              className="Analysis-left-button"
              type="button"
              onClick={downloadCSV}
              disabled={results.length === 0}
            >
              Скачать CSV
            </button>
          </div>
        </form>
      </div>
      <div className="Analysis-right">
        <div className="Analysis-right-box">
            <div className="Analysis-right-box-data">
              {error ? (
                <div className="error-message">Ошибка: {error}</div>
              ) : results.length === 0 ? (
                <div className="no-results">
                  {loading
                    ? "Загрузка данных..."
                    : "Ничего не найдено, попробуйте изменить параметры поиска..."}
                </div>
              ) : showDiagram ? (
                <div className="diagram-container">
                  <button
                    className="close-diagram"
                    onClick={() => setShowDiagram(false)} // Крестик для закрытия
                  >
                    ×
                  </button>
                  <Diagram data={results} />
                </div>
              ) : (
                <div className="results-list">
                  {results.map((product) => (
                    <div key={product.id} className="product-card">
                      <h3>{product.name}</h3>
                      <p>
                        <strong>Категория:</strong> {product.category}
                      </p>
                      <p>
                        <strong>Ресурс:</strong> {product.resource}
                      </p>
                      <p>
                        <strong>Цена:</strong> {product.price} {product.unit}
                      </p>
                      <p>
                        <strong>Дата:</strong> {formatDate(product.date_time)}
                      </p>
                      <p>
                        <strong>Характеристики:</strong>
                        <div className="characteristics-container">
                          {renderCharacteristics(product.characteristics)}
                        </div>
                      </p>
                      <a
                        className="product-card-link"
                        href={product.link}
                        target="_blank"
                        rel="noopener noreferrer"
                      >
                        Ссылка
                      </a>
                    </div>
                  ))}
                </div>
              )}
            </div>
        </div>
      </div>
    </div>
  );
}

export default Analysis;
