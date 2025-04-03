import scrapy
from catching_materials.items import CatchingMaterialsItem
from .normalize_date import clean_items

class MySpider(scrapy.Spider):
    name = "spider_main"
    allowed_domains = []
    custom_settings = {
        'CONCURRENT_REQUESTS': 30, #в продакшене увеличить до 30
        'DOWNLOAD_DELAY': 1.0,
    }

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.visited_urls = set() # Словарь уже пройденных ссылок
        
        # Параметры скрапинга
        self.start_url = kwargs.get('start_url', '') #Стартовая ссылка
        if 'allowed_domains' in kwargs:
            self.allowed_domains = [kwargs['allowed_domains']] #Ограничение на домен
        self.product_path = kwargs.get('product_path', '') #Ограничение на путь

        #Параметры селекторов
        self.category_selector = kwargs.get('category_selector', '') #Категория
        self.name_selector = kwargs.get('name_selector', '') #Название
        self.price_selector = kwargs.get('price_selector', '') #Цена
        self.unit_selector = kwargs.get('unit_selector', '') #Еденица измерения

        # Параметры селекторов характеристик
        self.block_selector = kwargs.get('block_selector', '') #Селектор блока характеристик
        self.key_selector = kwargs.get('key_selector', '') #Селектор ключа характеристик
        self.value_selector = kwargs.get('value_selector', '') #Селектор значения характеристик
        
        #Пуск скрапинга
    def start_requests(self):
        if not self.start_url:
            raise ValueError("start_url не указан!")
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    # Обход всех ссылок на целевом сайте
    def parse(self, response):
        product_links = response.css("a::attr(href)").getall()
        for link in product_links:
            full_url = response.urljoin(link)
            if full_url not in self.visited_urls:
                self.visited_urls.add(full_url)
                yield response.follow(full_url, self.parse_product)
    #Сбор данных о стройматериалах с целевой страницы
    def parse_product(self, response):
        if self.product_path in response.url:
            item = CatchingMaterialsItem()
            item["category"] = response.css(self.category_selector + '::text').get(default="").strip()
            item["name"] = response.css(self.name_selector  + '::text').get(default="").strip()
            item["price"] = response.css(self.price_selector  + '::text').get(default="").strip()
            item["unit"] = response.css(self.unit_selector  + '::text').get(default="уч.ед.").strip()

            characteristics_dict = {}
            table = response.xpath(self.block_selector)
        
            if table:
                # Извлекаем ВСЕ ключи и значения из таблицы
                keys = clean_items(table.xpath(self.key_selector + '//text()[normalize-space()]').getall())
                values = clean_items(table.xpath(self.value_selector + '//text()[normalize-space()]').getall())

                #Логи
                self.logger.info(f"Ключи: {keys}")
                self.logger.info(f"Очищенные ключи: {[key.strip() for key in keys]}")
                self.logger.info(f"значения {values}")
                self.logger.info(f"Очищенные значения {[value.strip() for value in values]}")
                # Сопоставляем их попарно
                for key, value in zip(keys, values):
                    key = key.strip()
                    value = value.strip()
                    if key and value:
                        characteristics_dict[key] = value
            else:
                self.logger.warning(f"Таблица характеристик не найдена по селектору: {self.block_selector}")

            item["characteristics"] = characteristics_dict or {"Нет данных": ""}
            item["link"] = response.url
            yield item
        else:
            self.logger.info(f"Страница не содержит данных: {response.url} (не содержит {self.product_path})")
            yield response.follow(response.url, self.parse, dont_filter=True)
