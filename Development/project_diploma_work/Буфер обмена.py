import scrapy
from catching_materials.items import CatchingMaterialsItem

class MySpider(scrapy.Spider):
    name = "spider_main"
    allowed_domains = ["baza.124bt.ru"]
    custom_settings = {
        'CONCURRENT_REQUESTS': 30,  # Максимум 30 одновременных запросов
        'DOWNLOAD_DELAY': 1,  # Задержка 1 секунда между запросами
    }

    # Параметры сбора (используем значения из аргументов командной строки)
    def __init__(self, category=None, name=None, price=None, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.category = category
        self.name = name
        self.price = price

    def start_requests(self):
        yield scrapy.Request(
            url="https://baza.124bt.ru/",
            callback=self.parse,
        )

    def parse(self, response):
        # Извлекаем ссылки
        product_links = response.css("a::attr(href)").getall()
    
        for link in product_links:
            if link not in self.visited_urls:
                self.visited_urls.add(link)  
                yield response.follow(link, self.parse_product)

    def parse_product(self, response):
        if '/product/' in response.url:
            item = CatchingMaterialsItem()
            item["category"] = self.category or response.css('p.em a::text').get(default="").strip() or ""
            item["name"] = self.name or response.css('[itemprop="name"]::text').get(default="").strip() or ""
            item["price"] = self.price or response.css('.price.nowrap::text').get(default="").strip() or ""
            item["unit"] = response.css('.ruble::text').get(default="шт").strip() or "шт"
            item["characteristics"] = " ".join(response.css('.features *::text').getall()).strip() or "Нет описания"
            self.logger.info(f"Собран товар: {item['name']} - {item['price']}")
            yield item
        else:
            self.logger.info(f"Нет товара на странице: {response.url}")
            yield response.follow(response.url, self.parse, dont_filter=True)
