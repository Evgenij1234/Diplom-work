# Scrapy
BOT_NAME = "catching_materials"
SPIDER_MODULES = ["catching_materials.spiders"]
NEWSPIDER_MODULE = "catching_materials.spiders"
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
PLAYWRIGHT_LAUNCH_OPTIONS = {'headless': True}
LOG_LEVEL = 'DEBUG'
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
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    'headless': True,
}
PLAYWRIGHT_BROWSER_TYPE = "chromium"
