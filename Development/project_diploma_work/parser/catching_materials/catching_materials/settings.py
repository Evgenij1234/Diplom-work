# Scrapy
BOT_NAME = "catching_materials"
SPIDER_MODULES = ["catching_materials.spiders"]
NEWSPIDER_MODULE = "catching_materials.spiders"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
PLAYWRIGHT_LAUNCH_OPTIONS = {'headless': True}
COOKIES_ENABLED = True
# Базовые настройки логирования
LOG_LEVEL = 'DEBUG'
LOG_FORMAT = '%(asctime)s [%(levelname)s] %(message)s'
LOG_DATEFORMAT = '%H:%M:%S'


ITEM_PIPELINES = {
    'catching_materials.pipelines.CatchingMaterialsPipeline': 1,
}
ROBOTSTXT_OBEY =  False
CONCURRENT_REQUESTS = 1
DOWNLOAD_DELAY = 1
FEED_EXPORT_ENCODING = "utf-8"

# playwright
DOWNLOAD_HANDLERS = {
    "http": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
    "https": "scrapy_playwright.handler.ScrapyPlaywrightDownloadHandler",
}
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Referer': 'https://www.google.com/',
}
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    'headless': True,
}
PLAYWRIGHT_BROWSER_TYPE = "chromium"