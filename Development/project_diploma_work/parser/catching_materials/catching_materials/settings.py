# Настройки Scrapy
BOT_NAME = "catching_materials"

SPIDER_MODULES = ["catching_materials.spiders"]
NEWSPIDER_MODULE = "catching_materials.spiders"

ITEM_PIPELINES = {
    'catching_materials.pipelines.CatchingMaterialsPipeline': 1,
}

# robots.txt
ROBOTSTXT_OBEY =  False

CONCURRENT_REQUESTS = 3

DOWNLOAD_DELAY = 3

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

DOWNLOADER_MIDDLEWARES = {
    "scrapy_playwright.middleware.PlaywrightMiddleware": 543,
}

# Настройки Playwright
PLAYWRIGHT_BROWSER_TYPE = "chromium"
PLAYWRIGHT_LAUNCH_OPTIONS = {
    "headless": True,
    "args": ["--no-sandbox", "--disable-setuid-sandbox"],
}

PLAYWRIGHT_DEFAULT_NAVIGATION_TIMEOUT = 30_000 

