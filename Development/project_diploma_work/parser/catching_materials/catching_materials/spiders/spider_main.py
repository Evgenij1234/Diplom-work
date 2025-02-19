import scrapy
import asyncio
from catching_materials.items import CatchingMaterialsItem
from scrapy_playwright.page import PageMethod

class MySpider(scrapy.Spider):
    name = "spider_main"
    allowed_domains = ["baza.124bt.ru"]
    
    def start_requests(self):
        yield scrapy.Request(
            url="https://baza.124bt.ru/",
            callback=self.parse,
            meta={"playwright": True, "playwright_include_page": True},
        )

    async def parse(self, response):
        page = response.meta.get("playwright_page")
        if page:
            try:
                await page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                await asyncio.wait_for(page.wait_for_timeout(3000), timeout=6)
            except asyncio.TimeoutError:
                self.logger.warning(f"Timeout при загрузке страницы: {response.url}")

        product_links = response.css("a::attr(href)").getall()
        #product_links = [link for link in product_links if '/product/' in link]
        for link in product_links:
            yield response.follow(link, self.parse_product, meta={"playwright": True})
            
            next_page = response.css(".pagination-next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, self.parse, meta={"playwright": True})

    async def parse_product(self, response):
        page = response.meta.get("playwright_page")
        if page:
            try:
                await asyncio.wait_for(page.wait_for_timeout(3000), timeout=6)
            except asyncio.TimeoutError:
                self.logger.warning(f"Timeout при загрузке товара: {response.url}")
        item = CatchingMaterialsItem()
        item["category"] = response.css('p em a::text').get(default="").strip() or ""
        item["name"] = response.css('[itemprop="name"]::text').get(default="").strip() or ""
        item["link"] = response.url
        item["price"] = response.css('.price.nowrap::text').get(default="").strip() or ""
        item["unit"] = response.css(".ruble::text").get(default="шт").strip() or "шт"
        item["characteristics"] = "".join(response.css(".features ::text").getall()).strip() or "Нет описания"
        self.logger.info(f"Собран товар: {item['name']} - {item['price']}")
        yield item