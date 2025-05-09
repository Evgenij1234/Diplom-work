import React from "react";

function Manual4() {
  const jsonData = {
    user: "testuser123",
    category: "Канализационные трубы",
    name: "Канализационная труба Rehau Raupiano Plus / Рехау Раупиано Плюс (110D / 1 м)",
    price: "1708",
    unit: "RUB",
    characteristics: {
      Назначение: "Для внутренней канализации",
      Материал: "Полипропилен RAU-PP (усиленный минералами)",
      Тип_канализации: "Бесшумная канализация",
      Диаметр: "110 мм",
      Длина: "1 м",
      Производитель: "Rehau",
      Вес: "2.118 кг",
      Объем: "0.0095 м³"
    },
    link: "https://m-delivery.ru/product/kanalizatsionnaya_truba_rehau_raupiano_plus_rexau_raupiano_plyus_110d_1_m_art14858/",
    resource: "https://m-delivery.ru",
    date_time: "2025-05-09 04:38:00"
  };

  // Преобразование данных JSON в CSV
  const jsonToCsv = (jsonData) => {
    const headers = [
      "user", "category", "name", "price", "unit",
      "characteristics_Назначение", "characteristics_Материал", 
      "characteristics_Тип_канализации", "characteristics_Диаметр", 
      "characteristics_Длина", "characteristics_Производитель", 
      "characteristics_Вес", "characteristics_Объем", "link", "resource", "date_time"
    ];

    const row = [
      jsonData.user, jsonData.category, jsonData.name, jsonData.price, jsonData.unit,
      jsonData.characteristics.Назначение, jsonData.characteristics.Материал,
      jsonData.characteristics.Тип_канализации, jsonData.characteristics.Диаметр,
      jsonData.characteristics.Длина, jsonData.characteristics.Производитель,
      jsonData.characteristics.Вес, jsonData.characteristics.Объем, jsonData.link, jsonData.resource, jsonData.date_time
    ];

    const csvData = [headers, row];
    return csvData;
  };

  const csvData = jsonToCsv(jsonData);

  return (
    <div className="Manual-left-box-link-text">
      <p className="Manual-left-box-link-tex-Title">
        Выходные данные
      </p>
      <p className="Manual-left-box-link-tex-content">
        <strong>Пример выходных данных в формате JSON:</strong>
        <pre style={{ backgroundColor: '#f5f5f5', padding: '10px', borderRadius: '5px', fontFamily: 'monospace', whiteSpace: 'pre-wrap', overflowX: 'auto' }}>
          {JSON.stringify(jsonData, null, 2)}
        </pre>

        <strong>Пример выходных данных в формате CSV:</strong>
        <div style={{ overflowX: 'auto', marginTop: '10px' }}>
          <table style={{ width: '100%', minWidth: '800px', borderCollapse: 'collapse' }}>
            <thead>
              <tr style={{ backgroundColor: '#f5f5f5' }}>
                {csvData[0].map((header, index) => (
                  <th key={index} style={{ padding: '8px', border: '1px solid #ccc', textAlign: 'left', fontSize: '12px' }}>
                    {header}
                  </th>
                ))}
              </tr>
            </thead>
            <tbody>
              <tr>
                {csvData[1].map((cell, index) => (
                  <td key={index} style={{ padding: '8px', border: '1px solid #ccc', fontSize: '12px' }}>
                    {cell}
                  </td>
                ))}
              </tr>
            </tbody>
          </table>
        </div>
      </p>
    </div>
  );
}

export default Manual4;
