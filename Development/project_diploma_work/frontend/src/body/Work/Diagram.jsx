import React, { useState, useEffect, useRef } from "react";
import { Chart, registerables } from 'chart.js';
import ChartDataLabels from 'chartjs-plugin-datalabels';
import "../../style/Work.scss";

Chart.register(...registerables, ChartDataLabels);

function Diagram({ data }) {
  const chartRef = useRef(null);
  const [chartInstance, setChartInstance] = useState(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    if (!data || data.length === 0) {
      setError("Нет данных для отображения");
      return;
    }

    const names = new Set(data.map(item => item.name));
    const categories = new Set(data.map(item => item.category));
    const resources = new Set(data.map(item => item.resource));

    let title = '';
    let grouped = {};

    if (names.size === 1 && categories.size === 1 && resources.size === 1) {
      title = `Диаграмма цен на товар ${[...names][0]}`;
      grouped = data.reduce((acc, item) => {
        const date = new Date(item.date_time).toLocaleDateString();
        acc[date] = item.price;
        return acc;
      }, {});
    } else if (categories.size === 1 && resources.size === 1) {
      title = `Диаграмма цен на категорию ${[...categories][0]}`;
      grouped = data.reduce((acc, item) => {
        const date = new Date(item.date_time).toLocaleDateString();
        if (!acc[date]) acc[date] = 0;
        acc[date] += item.price;
        return acc;
      }, {});
    } else if (resources.size === 1) {
      title = `Диаграмма цен на ресурс ${[...resources][0]}`;
      grouped = data.reduce((acc, item) => {
        const date = new Date(item.date_time).toLocaleDateString();
        if (!acc[date]) acc[date] = 0;
        acc[date] += item.price;
        return acc;
      }, {});
    } else {
      setError("Невозможно построить диаграмму: укажите при поиске Ресурс или Ресурс + Котегория или Ресурс + Котегория + Наименование");
      return;
    }

    const sortedDates = Object.keys(grouped).sort((a, b) => new Date(a) - new Date(b));
    const sortedPrices = sortedDates.map(date => grouped[date]);

    const textColor = 'rgba(0, 51, 102, 1)';
    const gridColor = 'rgba(0, 51, 102, 1)';
    const lineColor = 'rgba(0, 51, 102, 1)';
    const fillColor = 'rgba(233, 233, 235, 0.6)';

    const chartData = {
      labels: sortedDates,
      datasets: [{
        label: 'Цена',
        data: sortedPrices,
        borderColor: lineColor,
        backgroundColor: fillColor,
        borderWidth: 2,
        pointBackgroundColor: lineColor,
        tension: 0.1,
        fill: true,
        datalabels: {
          align: 'top',
          anchor: 'end',
          color: textColor,
          font: {
            weight: 'bold'
          },
          formatter: (value) => `${value.toFixed(2)} ₽`
        }
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
              color: textColor
            }
          },
          title: {
            display: true,
            text: title,
            color: textColor,
            font: {
              size: 16
            }
          },
          datalabels: {
            display: true
          },
          tooltip: {
            enabled: true
          }
        },
        scales: {
          x: {
            title: {
              display: true,
              text: 'Дата',
              color: textColor
            },
            ticks: {
              color: textColor
            },
            grid: {
              color: gridColor
            }
          },
          y: {
            title: {
              display: true,
              text: 'Цена',
              color: textColor
            },
            ticks: {
              color: textColor
            },
            grid: {
              color: gridColor
            }
          }
        }
      }
    };

    if (chartInstance) chartInstance.destroy();

    const ctx = chartRef.current.getContext('2d');
    const newChart = new Chart(ctx, config);
    setChartInstance(newChart);
    setError(null);

    return () => {
      if (chartInstance) chartInstance.destroy();
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
