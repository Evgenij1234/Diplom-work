# parser

./dockerRun.sh - остановк, удаление старого, создание нового образа, запуск, подключение к консоле

# Полезные ссылки
scrapy shell 'url' - парсинг из ссылки
cd catching_materials
scrapy crawl spider_main - запуск паука из файла


С параметрами:

./dockerRun.sh 
cd catching_materials
scrapy crawl spider_main \
    -a start_url='https://baza.124bt.ru' \
    -a allowed_domains='baza.124bt.ru' \
    -a product_path='/product/' \
    -a category_selector="p em a::text" \
    -a name_selector='[itemprop="name"]::text' \
    -a price_selector='.price.nowrap::text' \
    -a unit_selector='.ruble::text' \
    -a block_selector='//table[@id="product-features"]' \
    -a key_selector='.//td[@class="name"]' \
    -a value_selector='.//td[@class="value"]'




# Правила парсинга

1. Селекторы начинаются с .
2. Теги без .
3. Вложенность через пробел
4. Не типовые атрибуты например прописываются в формате[itemprop="name"]
5. Получить все что внутри тега и вложенных тегов в него можно в формате [itemprop="name"] ::text
6. ПОлучить текст из только этого тега но не вложенных [itemprop="name"]::text