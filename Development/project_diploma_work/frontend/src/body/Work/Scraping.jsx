import React, { useState, useEffect } from "react";
import "../../style/Work.scss";
import { useDispatch, useSelector } from "react-redux";
import Notification from "../../Notification";
import axios from "axios";

function Scraping() {
  const apiDomain = process.env.REACT_APP_API_DOMAIN;
  const { user } = useSelector((state) => state.auth);
  const [inputDataScraping, setInputDataScraping] = useState({
    user_id: user.username,
    start_url: "",
    allowed_domains: "",
    product_path: "",
    category_selector: "",
    name_selector: "",
    price_selector: "",
    unit_selector: "",
    block_selector: "",
    key_selector: "",
    value_selector: "",
  });

  // Добавлено: состояние для хранения логов
  const [logs, setLogs] = useState("");
  // Добавлено: состояние для отслеживания статуса процесса
  const [isRunning, setIsRunning] = useState(false);
  // Добавлено: ссылка на интервал обновления логов
  const [logInterval, setLogInterval] = useState(null);
  // Состяние для уведомления
  const [viewNotification, setNotification] = useState(null);

  // Добавлено: функция для получения логов
  const fetchLogs = async () => {
    try {
      const response = await axios.get(
        `${apiDomain}/logs/${inputDataScraping.user_id}`
      );
      setLogs(response.data.logs);
      setIsRunning(response.data.running || false);
    } catch (error) {
      console.error("Ошибка при получении логов:", error);
    }
  };

  // Добавлено: эффект для очистки интервала при размонтировании
  useEffect(() => {
    return () => {
      if (logInterval) clearInterval(logInterval);
    };
  }, [logInterval]);

  //Функция сбора вводимых данных из инпутов
  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setInputDataScraping({
      ...inputDataScraping,
      [name]: value,
    });
  };

  // Функция для запуска парсинга
  const startScraping = async () => {
    if (isRunning !== true) {
      try {
        const response = await axios.post(
          `${apiDomain}/start-scrapy`,
          inputDataScraping,
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );
        console.log("Парсинг запущен:", response.data);
        setNotification(<Notification message={"Парсинг запущен!"} />);
        setIsRunning(true);

        // Добавлено: запускаем периодическое обновление логов каждые 2 секунды
        if (logInterval) clearInterval(logInterval);
        setLogInterval(setInterval(fetchLogs, 5000));

        // Добавлено: сразу запрашиваем логи
        await fetchLogs();
      } catch (error) {
        console.error("Ошибка при запуске парсинга:", error);
        setNotification(<Notification message={"Ошибка при запуске парсинга!" + error} />);
      }
    }
  };

  // Функция для остановки парсинга
  const stopScraping = async () => {
    try {
      const response = await axios.post(
        `${apiDomain}/stop-scrapy`,
        {
          user_id: user.username,
        },
        {
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      console.log("Парсинг остановлен:", response.data);
      setNotification(<Notification message={"Парсинг остановлен!"} />);
      setIsRunning(false);

      // Добавлено: останавливаем обновление логов
      if (logInterval) clearInterval(logInterval);
      setLogInterval(null);

      // Добавлено: обновляем логи с последними сообщениями
      setLogs(response.data.logs || "");
    } catch (error) {
      console.error("Ошибка при остановке парсинга:", error);
      setNotification(<Notification message={"Ошибка при остановке парсинга!" + error} />);
    }
  };
  //Функция для скачаивания данных
  const downloadScraping = async () => {
    if (isRunning !== true) {
      try {
        const userName = user.username; 
        const apiUrl = `${apiDomain}/files/${userName}`;

        // 1. Запрашиваем файл с сервера
        const response = await fetch(apiUrl);

        if (!response.ok) {
          throw new Error(`Ошибка сервера: ${response.status}`);
        }

        // 2. Получаем данные как Blob
        const blob = await response.blob();

        // 3. Создаем временную ссылку
        const fileUrl = URL.createObjectURL(blob);

        // 4. Создаем скрытую ссылку для скачивания
        const link = document.createElement("a");
        link.href = fileUrl;
        link.download = `${userName}_data.json`;
        link.style.display = "none";

        // 5. Добавляем в документ и эмулируем клик
        document.body.appendChild(link);
        link.click();

        // 6. Убираем ссылку после скачивания
        setTimeout(() => {
          document.body.removeChild(link);
          URL.revokeObjectURL(fileUrl);
        }, 100);

        console.log("Файл успешно скачан в папку загрузок");
      } catch (error) {
        console.error("Ошибка скачивания:", error);
        alert("Не удалось скачать файл: " + error.message);
      }
    }
  };
  //Функция для сохранения данных в базу данных
  const savetoDbScraping = async () => {
    const userName = user.username;
    if (isRunning !== true) {
      try {
        const response = await fetch(`${apiDomain}/savedb/${user.username}`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ username: userName }),
        });

        if (!response.ok) {
          setNotification(<Notification message={`Ошибка: ${response.status}`} />);
          throw new Error(`Ошибка: ${response.status}`);
        }

        const data = await response.json();
        console.log("Успешно сохранено:", data);
        setNotification(<Notification message={"Успешно сохранено:" + data} />);
      } catch (error) {
        console.error("Ошибка при сохранении:", error);
        setNotification(<Notification message={"Ошибка при сохранении:" + error} />);
      }
    }
  };

  return (
    <div className="Scraping">
      <div className="Scraping-left">
        <div className="Scraping-left-box-input">
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Стартовая ссылка</span>
            <input
              className="Scraping-left-input-input"
              name="start_url"
              value={inputDataScraping.start_url}
              onChange={handleInputChange}
              type="text"
              placeholder="https://baza.124bt.ru"
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Домен</span>
            <input
              className="Scraping-left-input-input"
              name="allowed_domains"
              value={inputDataScraping.allowed_domains}
              onChange={handleInputChange}
              type="text"
              placeholder="baza.124bt.ru"
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Идентификатор продукта</span>
            <input
              className="Scraping-left-input-input"
              name="product_path"
              value={inputDataScraping.product_path}
              onChange={handleInputChange}
              type="text"
              placeholder="/product/"
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Категория</span>
            <input
              className="Scraping-left-input-input"
              name="category_selector"
              value={inputDataScraping.category_selector}
              onChange={handleInputChange}
              type="text"
              placeholder="p em a"
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Наименование</span>
            <input
              className="Scraping-left-input-input"
              name="name_selector"
              value={inputDataScraping.name_selector}
              onChange={handleInputChange}
              type="text"
              placeholder='[itemprop="name"]'
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Цена</span>
            <input
              className="Scraping-left-input-input"
              name="price_selector"
              value={inputDataScraping.price_selector}
              onChange={handleInputChange}
              type="text"
              placeholder=".price.nowrap"
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Ед.из</span>
            <input
              className="Scraping-left-input-input"
              name="unit_selector"
              value={inputDataScraping.unit_selector}
              onChange={handleInputChange}
              type="text"
              placeholder=".ruble"
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Блок характеристик</span>
            <input
              className="Scraping-left-input-input"
              name="block_selector"
              value={inputDataScraping.block_selector}
              onChange={handleInputChange}
              type="text"
              placeholder='//table[@id="product-features"]'
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Ключ характеристик</span>
            <input
              className="Scraping-left-input-input"
              name="key_selector"
              value={inputDataScraping.key_selector}
              onChange={handleInputChange}
              type="text"
              placeholder='.//td[@class="name"]'
            />
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">Значение характеристик</span>
            <input
              className="Scraping-left-input-input"
              name="value_selector"
              value={inputDataScraping.value_selector}
              onChange={handleInputChange}
              type="text"
              placeholder='.//td[@class="value"]'
            />
          </div>
        </div>
        <div className="Scraping-left-box-button">
          <button onClick={startScraping} className="Scraping-left-button">
            Старт
          </button>
          <button onClick={stopScraping} className="Scraping-left-button">
            Стоп
          </button>
          <button onClick={savetoDbScraping} className="Scraping-left-button">
            Сохранить
          </button>
          <button onClick={downloadScraping} className="Scraping-left-button">
            Скачать
          </button>
        </div>
      </div>
      <div className="Scraping-right">
        <div className="log-status">
          Статус: {isRunning ? "Выполняется" : "Не выполняется"}
        </div>
        <div className="Scraping-right-log">
          {viewNotification}
          <pre className="log-content">{logs || ""}</pre>
        </div>
      </div>
    </div>
  );
}

export default Scraping;
