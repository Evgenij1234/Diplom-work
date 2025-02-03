BOT_NAME = "catching_materials"

SPIDER_MODULES = ["catching_materials.spiders"]
NEWSPIDER_MODULE = "catching_materials.spiders"

ITEM_PIPELINES = {
    'catching_materials.pipelines.JsonWriterPipeline': 300,
}

# Obey robots.txt rules
ROBOTSTXT_OBEY =  False

CONCURRENT_REQUESTS = 3

DOWNLOAD_DELAY = 3

TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
