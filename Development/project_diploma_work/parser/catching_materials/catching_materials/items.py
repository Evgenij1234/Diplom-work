import scrapy


class CatchingMaterialsItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()
    description = scrapy.Field()
    pass

