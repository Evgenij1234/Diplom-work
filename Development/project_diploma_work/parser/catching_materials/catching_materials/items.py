import scrapy


class CatchingMaterialsItem(scrapy.Item):
    user = scrapy.Field() # Пользователь
    category =  scrapy.Field() # Категория*
    name = scrapy.Field()  # Название*
    price = scrapy.Field()  # Цена*
    unit = scrapy.Field()  # ед.изм*
    characteristics = scrapy.Field()  # Характеристики
    link = scrapy.Field()  # Ссылка*
    resource = scrapy.Field() # Ресурс, с которого полуаем
    date_time = scrapy.Field() # Дата и время начала сбора
