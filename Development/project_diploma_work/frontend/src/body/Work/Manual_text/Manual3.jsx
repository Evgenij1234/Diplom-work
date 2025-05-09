import React from "react";

function Manual3() {
  return (
    <div className="Manual-left-box-link-text">
      <p className="Manual-left-box-link-tex-Title">Правила скрапинга</p>
      <p className="Manual-left-box-link-tex-content">
        <section id="scraping-rules">
          <h2>Правила скрапинга (с использованием Scrapy)</h2>

          <h3>Обязательные параметры конфигурации</h3>
          <ul>
            <li>
              <strong>start_urls</strong> — начальные ссылки для парсинга,
              например: <code>["https://domain.com"]</code>
            </li>
            <li>
              <strong>allowed_domains</strong> — ограничение на обрабатываемые
              домены: <code>["domain.com"]</code>
            </li>
            <li>
              <strong>product_path</strong> — относительный путь к страницам
              товаров: <code>"/product/"</code>
            </li>
            <li>
              <strong>category_selector</strong> — селектор категории товара
              (CSS)
            </li>
            <li>
              <strong>name_selector</strong> — селектор названия товара (CSS)
            </li>
            <li>
              <strong>price_selector</strong> — селектор цены товара (CSS)
            </li>
            <li>
              <strong>unit_selector</strong> — селектор единицы измерения (CSS)
            </li>
            <li>
              <strong>block_selector</strong> — блок, содержащий дополнительные
              параметры (XPath)
            </li>
            <li>
              <strong>key_selector</strong> — селектор ключа параметра внутри
              блока (XPath)
            </li>
            <li>
              <strong>value_selector</strong> — селектор значения параметра
              внутри блока (XPath)
            </li>
          </ul>

          <h3>Примеры CSS-селекторов</h3>
          <ul>
            <li>
              <code>div</code> — все &lt;div&gt;
            </li>
            <li>
              <code>#price</code> — элемент с id="price"
            </li>
            <li>
              <code>.title</code> — элементы с классом title
            </li>
            <li>
              <code>div.product</code> — &lt;div&gt; с классом product
            </li>
            <li>
              <code>span[data-id="123"]</code> — тег с атрибутом data-id="123"
            </li>
            <li>
              <code>li:nth-child(2)</code> — второй элемент внутри списка
            </li>
            <li>
              <code>ul li</code> — вложенные теги (li в ul)
            </li>
            <li>
              <code>.container .price</code> — класс price вложен в container
            </li>
            <li>
              <code>h1, h2</code> — выбрать несколько тегов
            </li>
            <li>
              <code>.col, .row</code> — несколько классов
            </li>
            <li>
              <code>.product.featured</code> — элемент с двумя классами
              одновременно
            </li>
          </ul>

          <h3>Примеры XPath-селекторов</h3>
          <ul>
            <li>
              <code>//div</code> — все &lt;div&gt; на странице
            </li>
            <li>
              <code>//*[@id="price"]</code> — элемент с id="price"
            </li>
            <li>
              <code>//*[contains(@class, "item")]</code> — элементы, содержащие
              класс item
            </li>
            <li>
              <code>//div[contains(@class, "card")]</code> — &lt;div&gt; с
              классом card
            </li>
            <li>
              <code>//span[@data-id="123"]</code> — &lt;span&gt; с определённым
              атрибутом
            </li>
            <li>
              <code>(//li)[3]</code> — третий элемент &lt;li&gt; на странице
            </li>
            <li>
              <code>//ul//li</code> — &lt;li&gt;, вложенные в &lt;ul&gt;
            </li>
            <li>
              <code>
                //*[contains(@class, "block")]//*[contains(@class, "value")]
              </code>{" "}
              — вложенные классы
            </li>
            <li>
              <code>//h1 | //h2</code> — выбрать несколько типов тегов
            </li>
            <li>
              <code>
                //*[contains(@class, "col")] | //*[contains(@class, "row")]
              </code>{" "}
              — выбрать несколько классов
            </li>
            <li>
              <code>
                //*[contains(@class, "price") and contains(@class, "active")]
              </code>{" "}
              — элемент с двумя классами
            </li>
          </ul>

          <h3>Общие правила выбора селекторов</h3>
          <ul>
            <li>
              Выбирайте **уникальные и стабильные** идентификаторы элементов
              (id, class или атрибуты)
            </li>
            <li>
              Используйте **CSS-селекторы**, если HTML разметка простая и
              предсказуемая
            </li>
            <li>
              Используйте **XPath**, если структура сложная или требуется искать
              по частичному совпадению
            </li>
            <li>
              Для динамического контента (подгружаемого через JS) Scrapy не
              подойдёт без дополнительных инструментов (например, Splash или
              Selenium)
            </li>
          </ul>

          <h3>Как работает XPath</h3>
          <p>
            XPath — это язык навигации по XML и HTML-дереву. Он работает по
            древовидной структуре документа:
          </p>
          <ul>
            <li>
              <code>/</code> — абсолютный путь от корня
            </li>
            <li>
              <code>//</code> — поиск по всей структуре
            </li>
            <li>
              <code>@</code> — обращение к атрибуту, например <code>@href</code>
            </li>
            <li>
              <code>[]</code> — фильтрация элементов:{" "}
              <code>//div[@class="box"]</code>
            </li>
            <li>
              <code>text()</code> — извлечение текста из элемента:{" "}
              <code>//h1/text()</code>
            </li>
            <li>
              <code>contains()</code> — частичное совпадение:{" "}
              <code>//div[contains(@class, "item")]</code>
            </li>
          </ul>

          <p>
            XPath позволяет гибко находить элементы по их структуре,
            содержимому, вложенности и атрибутам, и идеально подходит для
            сложных HTML-страниц.
          </p>

          <p>
            Официальная документация Scrapy по работе с селекторами:
            <a className="docunentation-a"
              href="https://docs.scrapy.org/en/latest/topics/selectors.html"
              target="_blank"
            >
              https://docs.scrapy.org/en/latest/topics/selectors.html
            </a>
          </p>
        </section>
      </p>
    </div>
  );
}

export default Manual3;
