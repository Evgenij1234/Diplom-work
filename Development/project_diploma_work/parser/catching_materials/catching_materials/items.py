import scrapy


class CatchingMaterialsItem(scrapy.Item):
    category =  scrapy.Field() # Категория*
    name = scrapy.Field()  # Название*
    price = scrapy.Field()  # Цена*
    unit = scrapy.Field()  # ед.изм*
    characteristics = scrapy.Field()  # Характеристики
    link = scrapy.Field()  # Ссылка*
