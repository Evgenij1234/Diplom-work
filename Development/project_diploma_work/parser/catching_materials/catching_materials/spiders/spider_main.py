import scrapy
from catching_materials.items import CatchingMaterialsItem # Импорт Items

class MySpider(scrapy.Spider):
    name = "spider_main"  # Имя паука
    allowed_domains = ["xn--24-6kce4bvjpfdl.xn--p1ai"]  # Ограничение на домен
    start_urls = ["https://www.xn--24-6kce4bvjpfdl.xn--p1ai/goods/227918898-dvp_dvukhstoronneye_2_5_mm_2710kh1220_mm"]  # Одна страница

    def parse(self, response):
        # Создаем объект CatchingMaterialsItem
        item = CatchingMaterialsItem()
        item["name"] = response.css(".company-header-title::text").get(default="Нет названия").strip()
        item["link"] = response.url
        item["price"] = response.css(".bp-price.fsn::text").get(default="Нет цены").strip()
        item["unit"] = response.css(".price-currency::text").get(default="Нет единиц измерения").strip()
        item["characteristics"] = "".join(response.css(".limited-block.js-limited-block *::text").getall()).strip() or "Нет описания"
       
        yield item  # Отправляем результат
