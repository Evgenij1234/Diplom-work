import scrapy


class CatchingMaterialsItem(scrapy.Item):
    category =  scrapy.Field()
    name = scrapy.Field()  # 1.1 Название*
    link = scrapy.Field()  # 1.2 Ссылка*
    price = scrapy.Field()  # 1.3 Цена*
    unit = scrapy.Field()  # 1.3 ед.изм*
    characteristics = scrapy.Field()  # 1.4 Характеристики (список объектов)
