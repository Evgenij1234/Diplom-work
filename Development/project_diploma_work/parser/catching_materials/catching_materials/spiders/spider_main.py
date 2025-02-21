import scrapy
from catching_materials.items import CatchingMaterialsItem
from scrapy_playwright.page import PageMethod
import asyncio

class MySpider(scrapy.Spider):
    name = "spider_main"
    allowed_domains = ["baza.124bt.ru"]
    custom_settings = {
        'CONCURRENT_REQUESTS': 30,  # Максимум 30 одновременных запросов
        'DOWNLOAD_DELAY': 1,  # Задержка 1 секунда между запросами
    }
    
    # Множество для хранения уже посещенных ссылок
    visited_urls = set()

    def start_requests(self):
        yield scrapy.Request(
            url="https://baza.124bt.ru/",
            callback=self.parse,
        )

    def parse(self, response):
        # Извлекаем ссылки
        product_links = response.css("a::attr(href)").getall()
    
        for link in product_links:
            # Если ссылка не была посещена, обрабатываем её
            if link not in self.visited_urls:
                self.visited_urls.add(link)  # Добавляем ссылку в множество посещенных
                # В одном запросе передаем ссылку в один callback
                yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        if '/product/' in response.url:
            # Это страница продукта, собираем данные
            item = CatchingMaterialsItem()
            item["category"] = response.css('p em a::text').get(default="").strip() or ""
            item["name"] = response.css('[itemprop="name"]::text').get(default="").strip() or ""
            item["link"] = response.url
            item["price"] = response.css('.price.nowrap::text').get(default="").strip() or ""
            item["unit"] = response.css(".ruble::text").get(default="шт").strip() or "шт"
            item["characteristics"] = "".join(response.css(".features ::text").getall()).strip() or "Нет описания"
            self.logger.info(f"Собран товар: {item['name']} - {item['price']}")
            yield item
        else:
            # Если это не страница продукта, повторно отправляем ссылку в метод parse
            self.logger.info(f"Нет товара на странице: {response.url}")
            yield response.follow(response.url, self.parse, dont_filter=True)
