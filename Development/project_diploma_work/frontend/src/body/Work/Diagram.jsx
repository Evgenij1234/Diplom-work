import React, { useState, useEffect, useRef } from "react";
import { Chart, registerables } from 'chart.js';
import "../../style/Work.scss";

Chart.register(...registerables);

function Diagram({ data }) {
  const chartRef = useRef(null);
  const [chartInstance, setChartInstance] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!data || data.length === 0) {
      setError("Нет данных для отображения");
      return;
    }

    try {
      // Подготовка данных для диаграммы
      const chartData = {
        labels: data.map(item => new Date(item.date_time).toLocaleDateString()),
        datasets: [{
          label: 'Цена',
          data: data.map(item => item.price),
          borderColor: 'rgb(75, 192, 192)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          tension: 0.1,
          fill: true
        }]
      };

      const config = {
        type: 'line',
        data: chartData,
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: 'Динамика цен'
            },
          },
          scales: {
            x: {
              title: {
                display: true,
                text: 'Дата'
              }
            },
            y: {
              title: {
                display: true,
                text: 'Цена'
              }
            }
          }
        }
      };

      // Уничтожаем предыдущий график
      if (chartInstance) {
        chartInstance.destroy();
      }

      // Создаем новый график
      const ctx = chartRef.current.getContext('2d');
      const newChartInstance = new Chart(ctx, config);
      setChartInstance(newChartInstance);

      setError(null);
    } catch (err) {
      setError("Ошибка при построении диаграммы");
      console.error("Chart error:", err);
    }

    // Очистка при размонтировании
    return () => {
      if (chartInstance) {
        chartInstance.destroy();
      }
    };
  }, [data]);

  return (
    <div className="Diagram">
      {error ? (
        <div className="error-message">{error}</div>
      ) : (
        <div className="chart-container">
          <canvas ref={chartRef}></canvas>
        </div>
      )}
    </div>
  );
}

export default Diagram;