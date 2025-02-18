import scrapy
from catching_materials.items import CatchingMaterialsItem
from scrapy_playwright.page import PageMethod

class MySpider(scrapy.Spider):
    name = "spider_main"
    allowed_domains = ["baza.124bt.ru"]
    start_urls = ["https://baza.124bt.ru/"]
    custom_settings = {
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'PLAYWRIGHT_LAUNCH_OPTIONS': {'headless': True},  # Установите True для безголового режима
    }

    def start_requests(self):
        # Начинаем с первой страницы, прокрутка будет применяться ко всем страницам
        yield scrapy.Request(
            "https://baza.124bt.ru/", 
            callback=self.parse, 
            meta={"playwright": True}
        )

    def parse(self, response):
        # Прокрутка страницы, если это необходимо!!!!!!!!!!!!!!!!!!!!!!!!тут подумать, возможно логичнее будет скролить до определенного тега!
        if response.meta.get('playwright', False):
            yield from self.scroll_page(response)

        # Парсим все ссылки на страницы, содержащие товары
        product_links = response.css("a::attr(href)").getall()
        self.logger.info(f'Завершен парсинг страницы: {response.url}')
        
        # Фильтруем ссылки для страниц товаров
        product_links = [link for link in product_links if '/product/' in link]  # Проверяем на /product/
        
        # Для каждой ссылки на товар вызываем parse_product
        for link in product_links:
            yield response.follow(link, self.parse_product)

        # Если есть пагинация (следующие страницы каталога)
        next_page = response.css(".pagination-next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse)

    def scroll_page(self, response): #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!тут подумать, возможно логичнее будет скролить до определенного тега!
        """Метод для прокрутки страницы."""
        return scrapy.Request(
            response.url,  # Повторно загружаем текущую страницу
            callback=self.parse, 
            meta={
                "playwright": True,
                "playwright_page_methods": [
                    PageMethod('evaluate', 'window.scrollTo(0, document.body.scrollHeight)'),  # Прокрутка страницы до конца
                    PageMethod('evaluate', 'window.scrollBy(0, 1000)')  # Прокручиваем вниз на 1000px
                ]
            }
        )

    def parse_product(self, response):
        # Создаем объект CatchingMaterialsItem
        item = CatchingMaterialsItem()
        
        # Извлекаем категорию с самой страницы товара
        category_name = response.css('p em a::text').get(default="").strip() or ""
        item["category"] = category_name
        
        # Обработка названия товара
        item["name"] = response.css('[itemprop="name"]::text').get(default="").strip() or ""
        
        # Записываем ссылку на товар
        item["link"] = response.url

        # Обработка цены и единицы измерения
        item["price"] = response.css('.price.nowrap::text').get(default="").strip() or ""
        item["unit"] = response.css(".ruble::text").get(default="шт").strip() or "шт"
        
        # Обработка характеристик товара
        item["characteristics"] = "".join(response.css(".features ::text").getall()).strip() or "Нет описания"
        
        # Логируем информацию для отладки
        self.logger.info(f"Собран товар: {item['name']} - {item['price']}")

        # Отправляем item
        yield item
