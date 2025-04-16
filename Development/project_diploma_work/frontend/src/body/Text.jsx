// ConstructionParserInfo.jsx
import React from 'react';

const ConstructionParserInfo = () => {
  return (
    <div className="construction-parser-info">
      <div className="parser-header">
        <h1 className="parser-main-title">Парсер данных строительных материалов</h1>
        <p className="parser-description">
          Python-решение для автоматического сбора и анализа информации о строительных материалах
          с различных онлайн-источников
        </p>
      </div>

      <section className="parser-features">
        <h2 className="parser-section-title">Основные возможности</h2>
        
        <div className="feature-block">
          <h3 className="feature-title">Сбор актуальных данных</h3>
          <p className="feature-text">
            Автоматизированный сбор информации о ценах, наличии и характеристиках строительных материалов:
            кирпича, бетона, металлопроката, пиломатериалов и других
          </p>
        </div>

        <div className="feature-block">
          <h3 className="feature-title">Анализ рыночной ситуации</h3>
          <p className="feature-text">
            Систематизация данных для сравнения предложений разных поставщиков
            и выявления рыночных тенденций
          </p>
        </div>

        <div className="feature-block">
          <h3 className="feature-title">Гибкие форматы выгрузки</h3>
          <p className="feature-text">
            Получение данных в удобных форматах для дальнейшей обработки:
            CSV, JSON
          </p>
        </div>
      </section>

      <section className="parser-tech">
        <h2 className="parser-section-title">Техническая реализация</h2>
        <div className="tech-details">
          <p className='tech-details-p'>
            Решение разработано на Python с использованием надежных библиотек для парсинга:
          </p>
          <ul className="tech-list">
            <li>Scrapy - для сложных парсинговых задач</li>
            <li>Scrapy-playwright- для работы с динамическим контентом</li>
            <li>Pandas - для обработки и анализа данных</li>
          </ul>
        </div>
      </section>

      <section className="parser-applications">
        <h2 className="parser-section-title">Применение</h2>
        <div className="applications-grid">
          <div className="application-card">
            <h3 className="application-title">Для поставщиков</h3>
            <p>Мониторинг цен конкурентов на рынке</p>
          </div>
          <div className="application-card">
            <h3 className="application-title">Для строительных компаний</h3>
            <p>Оптимизация закупочной деятельности и бюджетирования</p>
          </div>
          <div className="application-card">
            <h3 className="application-title">Для аналитиков</h3>
            <p>Исследование рыночных тенденций в строительной отрасли</p>
          </div>
        </div>
      </section>
    </div>
  );
};

export default ConstructionParserInfo;