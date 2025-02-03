import scrapy

class MySpider(scrapy.Spider):
    name = "spider_new"  # Имя паука
    allowed_domains = ["xn--24-6kce4bvjpfdl.xn--p1ai"]  # Ограничение на домен
    start_urls = ["https://www.xn--24-6kce4bvjpfdl.xn--p1ai/catalog"]  # Начальные URL-адреса

    def parse(self, response):
        # Извлечение данных с добавлением проверки наличия элементов
        yield {
            "title": response.css("title::text").get(default="No title"),
            "url": response.url,
            "description": response.css('meta[name="description"]::attr(content)').get(default="No description"),
            "keywords": response.css('meta[name="keywords"]::attr(content)').get(default="No keywords"),
        }

        # Извлечение и фильтрация ссылок
        for next_page in response.css("a::attr(href)").getall():
            if next_page:
                # Проверяем, что ссылка относится к указанному домену и является относительной/абсолютной
                next_page = response.urljoin(next_page)
                if self.allowed_domains[0] in next_page:
                    yield response.follow(next_page, callback=self.parse)
