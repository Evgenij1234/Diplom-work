# parser
# parser

./dockerRun.sh - остановк, удаление старого, создание нового образа, запуск, подключение к консоле
scrapy crawl spider_main - запуск паука из файла

Проверка доступности сайта из скрапи по домену:
scrapy shell 'https://www.xn--24-6kce4bvjpfdl.xn--p1ai/'
Попробовать открыть в браузере:
 view(response)

С параметрами:
./dockerRun.sh 

cd catching_materials
scrapy crawl spider_main \
    -a user='user1234' \
    -a start_url='https://baza.124bt.ru' \
    -a allowed_domains='baza.124bt.ru' \
    -a product_path='/product/' \
    -a category_selector="p em a" \
    -a name_selector='[itemprop="name"]' \
    -a price_selector='.price.nowrap' \
    -a unit_selector='.ruble' \
    -a block_selector='//table[@id="product-features"]' \
    -a key_selector='.//td[@class="name"]' \
    -a value_selector='.//td[@class="value"]'

Межсетевой пример:
curl -X POST http://localhost:5000/start-scrapy \
     -H "Content-Type: application/json" \
     -d '{
           "user_id": "user123", 
           "start_url": "https://baza.124bt.ru",
           "allowed_domains": "baza.124bt.ru",
           "product_path": "/product/",
           "category_selector": "p em a",
           "name_selector": "[itemprop=\"name\"]",
           "price_selector": ".price.nowrap",
           "unit_selector": ".ruble",
           "block_selector": "//table[@id=\"product-features\"]",
           "key_selector": ".//td[@class=\"name\"]",
           "value_selector": ".//td[@class=\"value\"]"
         }'


Останвока:
curl -X POST http://localhost:5000/stop-scrapy \
     -H "Content-Type: application/json" \
     -d '{
           "user_id": "user123"
         }'
Запрос данных:
curl "http://localhost:5000/get-data?user_id=user123"

Запрос логов: 
curl "http://localhost:5000/get-log?user_id=user123"

Правила ввода идентификаторов сайта, параметры start_url, allowed_domains, product_path:
1. start_url - Ссылка на головную страницу сайта имеет вид https://domain.com
2. allowed_domains - ограничение на домен, имеет вид domain.com
3. product_path - определяет целевую страницу для сбора данных, имеет вид /product/

Правила для параметров category_selector, name_selector, price_selector, unit_selector:
1. tag - Найти все теги <tag>
2. #id - Найти элемент с id="id"
3. .class - Найти элементы с классом class
4. tag.class - Найти <tag> с классом class
5. tag[attr="value"] - Найти <tag> с атрибутом attr="value"
6. tag:nth-child(n) - Получить значение из элемента n по порядку, который вложен в tag.
7. tag1 tag2 - тег2 вложеный в тег 1 - вложеные теги
8. .class1 .class2 класс2 вложеный в класс 1 0 вложеные классы
9. tag1, tag2 - несколько тегов
10. class1, class2- несколько классов
11. .class1.class2 - один элемент имеет несколько классов



Правила для параметров block_selector, key_selector, value_selector:
1. //tag - Найти все теги <tag> на странице
2. //*[@id='id'] - Найти элемент с id="id"
3. //*[contains(@class, 'class')] - Найти элементы с классом class
4. //tag[contains(@class, 'class')] - Найти <tag> с классом class
5. //tag[@attr='value'] - Найти <tag> с атрибутом attr="value"
6. (//tag)[n] - Получить n-ый элемент внутри tag
7. //tag1//tag2 - Найти tag2, вложенный в tag1
8. //*[contains(@class, 'class1')]//*[contains(@class, 'class2')] - Найти class2, вложенный в class1
9. //tag1 | //tag2 - Найти несколько тегов tag1, tag2
10. //*[contains(@class, 'class1')] | //*[contains(@class, 'class2')] - Найти несколько классов .class1, .class2
11. //*[contains(@class, 'class1') and contains(@class, 'class2')] - Найти элемент с несколькими классами .class1.class2

./dockerRun.sh 


1. https://baza.124bt.ru
2. https://obi.ru
3. https://s-stroy.ru
4. https://m-delivery.ru


Запросы:

1. cd catching_materials
scrapy crawl spider_main \
    -a start_url='https://baza.124bt.ru' \
    -a allowed_domains='baza.124bt.ru' \
    -a product_path='/product/' \
    -a category_selector="p em a" \
    -a name_selector='[itemprop="name"]' \
    -a price_selector='.price.nowrap' \
    -a unit_selector='.ruble' \
    -a block_selector='//table[@id="product-features"]' \
    -a key_selector='.//td[@class="name"]' \
    -a value_selector='.//td[@class="value"]'


2. cd catching_materials
scrapy crawl spider_main \
    -a start_url='https://obi.ru' \
    -a allowed_domains='obi.ru' \
    -a product_path='/products/' \
    -a category_selector='ul.dPLk0 > li:nth-child(4) > a > span[itemprop="name"]' \
    -a name_selector='._3LdDm' \
    -a price_selector='._3IeOW' \
    -a unit_selector='._3SDdj' \
    -a block_selector='//div[@class="_1qc6Q"]' \
    -a key_selector='.//dt[@class="ImGAo"]' \
    -a value_selector='.//dd[@class="_gJlB"]'


3. cd catching_materials
scrapy crawl spider_main \
    -a start_url='https://s-stroy.ru' \
    -a allowed_domains='s-stroy.ru' \
    -a product_path='/product/' \
    -a category_selector='div.styles_list__bel0I > div.styles_item__ogzkm:nth-last-child(2) a.styles_textLink__wrap__zShba div.styles_text--primary__UjU_1' \
    -a name_selector='.styles_title__hhoA4' \
    -a price_selector='.styles_rubleBase__EaZAE.styles_price__rubleBase__xRBqZ' \
    -a unit_selector='.styles_centBase__8oK0Y.styles_currency__DUTSc.styles_price__centBase__qmEpj' \
    -a block_selector='//div[@class="styles_column__ro9aH"]' \
    -a key_selector='.//div[@class="styles_labelWrap__ByWFg"]' \
    -a value_selector='.//div[ contains(@class, "styles_text--default__yYra8") and contains(@class, "styles_text--regular__mUH83") and contains(@class, "styles_value__Ojowr")]'


4. cd catching_materials
scrapy crawl spider_main \
    -a start_url='https://m-delivery.ru' \
    -a allowed_domains='m-delivery.ru' \
    -a product_path='/product/' \
    -a category_selector='.way_to_page > *:nth-child(11)' \
    -a name_selector='h1.no_underline' \
    -a price_selector='.product-price__new span:nth-of-type(2)' \
    -a unit_selector='.product-price__new span:nth-of-type(1)' \
    -a block_selector='//div[@class="column"]' \
    -a key_selector='.//div[@class="first"]' \
    -a value_selector='.//div[@class="item"]/p[not(parent::div[@class="first"])]'


# Список маршрутов
