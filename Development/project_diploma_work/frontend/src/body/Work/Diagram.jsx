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
      // Сортируем данные по дате от меньшего к большему
      const sortedData = [...data].sort((a, b) => 
        new Date(a.date_time) - new Date(b.date_time)
      );

      // Цвета для темы
      const textColor = 'rgba(0, 51, 102, 1)'; // Белый цвет текст
      const gridColor = 'rgba(0, 51, 102, 1)'; // Сетка
      const lineColor = 'rgba(0, 51, 102, 1)'; // Цвет линии графика
      const fillColor = 'rgba(233, 233, 235, 0.6)'; // Заливка под графиком

      // Подготовка данных для диаграммы
      const chartData = {
        labels: sortedData.map(item => new Date(item.date_time).toLocaleDateString()),
        datasets: [{
          label: 'Цена',
          data: sortedData.map(item => item.price),
          borderColor: lineColor,
          backgroundColor: fillColor,
          borderWidth: 2, // Толщина линии
          pointBackgroundColor: lineColor, // Цвет точек
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
            legend: {
              labels: {
                color: textColor // Цвет текста легенды
              }
            },
            title: {
              display: true,
              text: 'Динамика цен',
              color: textColor, // Цвет заголовка
              font: {
                size: 16
              }
            },
          },
          scales: {
            x: {
              title: {
                display: true,
                text: 'Дата',
                color: textColor // Цвет подписи оси X
              },
              ticks: {
                color: textColor // Цвет значений на оси X
              },
              grid: {
                color: gridColor // Цвет сетки оси X
              }
            },
            y: {
              title: {
                display: true,
                text: 'Цена',
                color: textColor // Цвет подписи оси Y
              },
              ticks: {
                color: textColor // Цвет значений на оси Y
              },
              grid: {
                color: gridColor // Цвет сетки оси Y
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