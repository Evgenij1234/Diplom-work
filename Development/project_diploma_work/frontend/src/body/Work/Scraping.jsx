import React, { useState, useEffect } from "react";
import "../../style/Work.scss";
import { useDispatch, useSelector } from "react-redux";
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
      setIsRunning(true);

      // Добавлено: запускаем периодическое обновление логов каждые 2 секунды
      if (logInterval) clearInterval(logInterval);
      setLogInterval(setInterval(fetchLogs, 2000));

      // Добавлено: сразу запрашиваем логи
      await fetchLogs();
    } catch (error) {
      console.error("Ошибка при запуске парсинга:", error);
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
      setIsRunning(false);

      // Добавлено: останавливаем обновление логов
      if (logInterval) clearInterval(logInterval);
      setLogInterval(null);

      // Добавлено: обновляем логи с последними сообщениями
      setLogs(response.data.logs || "");
    } catch (error) {
      console.error("Ошибка при остановке парсинга:", error);
    }
  };

  return (
    <div className="Scraping">
      <div className="Scraping-left">
        {/* Левая часть осталась без изменений */}
        <div className="Scraping-left-box-input">
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">start_url</span>
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
            <span className="Scraping-left-input-name">allowed_domains</span>
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
            <span className="Scraping-left-input-name">product_path</span>
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
            <span className="Scraping-left-input-name">category_selector</span>
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
            <span className="Scraping-left-input-name">name_selector</span>
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
            <span className="Scraping-left-input-name">price_selector</span>
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
            <span className="Scraping-left-input-name">unit_selector</span>
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
            <span className="Scraping-left-input-name">block_selector</span>
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
            <span className="Scraping-left-input-name">key_selector</span>
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
            <span className="Scraping-left-input-name">value_selector</span>
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
          <button className="Scraping-left-button">Сохранить</button>
        </div>
      </div>
      {/* Правая часть с логами - добавлен вывод логов и статуса */}
      <div className="Scraping-right">
        <div className="log-status">
          Статус: {isRunning ? "Выполняется" : "Не выполняется"}
        </div>
        <div className="Scraping-right-log">
          <pre className="log-content">{logs || ""}</pre>
        </div>
      </div>
    </div>
  );
}

export default Scraping;
