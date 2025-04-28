import React, { useState } from "react";
import axios from "axios";

function Test() {
  const [userId, setUserId] = useState("user123");
  const [log, setLog] = useState("");
  const [scrapyData, setScrapyData] = useState("");
  const [apiData, setApiData] = useState(null);
  const [loading, setLoading] = useState(false);
  const [statusMessage, setStatusMessage] = useState("");

  const backendBaseUrl = "http://localhost:5000";

  const handleStartScrapy = async () => {
    try {
      setLoading(true);
      const response = await axios.post(`${backendBaseUrl}/start-scrapy`, {
        user_id: userId,
        start_url: "https://baza.124bt.ru",
        allowed_domains: "baza.124bt.ru",
        product_path: "/product/",
        category_selector: "p em a",
        name_selector: "[itemprop=\"name\"]",
        price_selector: ".price.nowrap",
        unit_selector: ".ruble",
        block_selector: "//table[@id=\"product-features\"]",
        key_selector: ".//td[@class=\"name\"]",
        value_selector: ".//td[@class=\"value\"]"
      });
      setStatusMessage(response.data.status);
    } catch (err) {
      setStatusMessage("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };
  

  const handleStopScrapy = async () => {
    try {
      setLoading(true);
      const response = await axios.post(`${backendBaseUrl}/stop-scrapy`, {
        user_id: userId
      });
      setStatusMessage(response.data.status);
    } catch (err) {
      setStatusMessage("Error: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGetLog = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${backendBaseUrl}/get-log`, {
        params: { user_id: userId }
      });
      setLog(response.data.log || "Лог найден, но пуст.");
    } catch (err) {
      setLog("Ошибка: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleGetData = async () => {
    try {
      setLoading(true);
      const response = await axios.get(`${backendBaseUrl}/get-data`, {
        params: { user_id: userId }
      });
      setScrapyData(JSON.stringify(response.data, null, 2));
    } catch (err) {
      setScrapyData("Ошибка: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  const handleApiTest = async () => {
    try {
      setLoading(true);
      const response = await axios.get("http://localhost:8000/api/test-orm");
      setApiData(response.data);
    } catch (err) {
      setApiData("Ошибка: " + err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Тест Scrapy API и БД</h1>
      <label>
        User ID:{" "}
        <input
          type="text"
          value={userId}
          onChange={(e) => setUserId(e.target.value)}
          style={{ marginBottom: "10px" }}
        />
      </label>

      <div style={{ margin: "10px 0" }}>
        <button onClick={handleStartScrapy} disabled={loading}>
          ▶️ Start Scrapy
        </button>{" "}
        <button onClick={handleStopScrapy} disabled={loading}>
          ⏹️ Stop Scrapy
        </button>{" "}
        <button onClick={handleGetLog} disabled={loading}>
          📜 Get Logs
        </button>{" "}
        <button onClick={handleGetData} disabled={loading}>
          📦 Get Data
        </button>{" "}
        <button onClick={handleApiTest} disabled={loading}>
          🧪 Test DB API
        </button>
      </div>

      {statusMessage && <p>Status: {statusMessage}</p>}

      {log && (
        <div>
          <h3>Logs:</h3>
          <pre style={{ background: "#f4f4f4", padding: "10px" }}>{log}</pre>
        </div>
      )}

      {scrapyData && (
        <div>
          <h3>Scrapy Data:</h3>
          <pre style={{ background: "#f0fff0", padding: "10px" }}>{scrapyData}</pre>
        </div>
      )}

      {apiData && (
        <div>
          <h3>API Test Data:</h3>
          <pre style={{ background: "#f0f8ff", padding: "10px" }}>
            {JSON.stringify(apiData, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
}

export default Test;
