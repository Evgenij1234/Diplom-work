import React from "react";
import "../../style/Work.scss";

function Scraping() {
  return (
    <div className="Scraping">
      <div className="Scraping-left">
        <div className="Scraping-left-box-input">
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">start_url</span>
            <input className="Scraping-left-input-input" type="text" placeholder="https://baza.124bt.ru"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">allowed_domains</span>
            <input className="Scraping-left-input-input" type="text" placeholder="baza.124bt.ru"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">product_path</span>
            <input className="Scraping-left-input-input" type="text" placeholder="/product/"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">category_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder="p em a"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">name_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder="[itemprop=&quot;name&quot;]"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">price_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder=".price.nowrap"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">unit_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder=".ruble"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">block_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder="//table[@id=\&quot;product-features\&quot;]"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">key_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder=".//td[@class=\&quot;name\&quot;]"/>
          </div>
          <div className="Scraping-left-input">
            <span className="Scraping-left-input-name">value_selector</span>
            <input className="Scraping-left-input-input" type="text" placeholder=".//td[@class=\&quot;value\&quot;]"/>
          </div>
        </div>
        <div className="Scraping-left-box-button">
          <button className="Scraping-left-button">Старт</button>
          <button className="Scraping-left-button">Стоп</button>
          <button className="Scraping-left-button">Сохранить</button>
        </div>
      </div>
      <div className="Scraping-right">
        <div className="Scraping-right-log">
        log
        </div>
      </div>
    </div>
  );
}

export default Scraping;
