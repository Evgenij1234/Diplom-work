import scrapy
from catching_materials.items import CatchingMaterialsItem
from scrapy_playwright.page import PageMethod
import asyncio

class MySpider(scrapy.Spider):
    name = "spider_main"
    allowed_domains = ["baza.124bt.ru"]
    
    def start_requests(self):
        yield scrapy.Request(
            url="https://baza.124bt.ru/",
            callback=self.parse,
        )

    def parse(self, response):
       #Извлекаем ссылки
        product_links = response.css("a::attr(href)").getall()
        for link in product_links:
           yield response.follow(link, self.parse) #Передача всех ссылок в парс
           yield response.follow(link, self.parse_product) #Передача всех ссылок в продукт парс


   # Извлекаем данные с целевой страницы товара
    def parse_product(self, response):
        if '/product/' in response.url:
            item = CatchingMaterialsItem()
            item["category"] = response.css('p em a::text').get(default="").strip() or ""
            item["name"] = response.css('[itemprop="name"]::text').get(default="").strip() or ""
            item["link"] = response.url
            item["price"] = response.css('.price.nowrap::text').get(default="").strip() or ""
            item["unit"] = response.css(".ruble::text").get(default="шт").strip() or "шт"
            item["characteristics"] = "".join(response.css(".features ::text").getall()).strip() or "Нет описания"
            self.logger.info(f"Собран товар: {item['name']} - {item['price']}")
            yield item

