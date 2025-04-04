./dockerRun.sh 

cd catching_materials
scrapy crawl spider_main \
    -a start_url='https://krasnoyarsk.lemanapro.ru/' \
    -a allowed_domains='krasnoyarsk.lemanapro.ru' \
    -a product_path='/product/' \
    -a category_selector=".jSdescdudT_pdp:nth-child(5)" \
    -a name_selector='.t12nw7s2_pdp' \
    -a price_selector='.price.nowrap' \
    -a unit_selector='.ruble' \
    -a block_selector='//table[@id="product-features"]' \
    -a key_selector='.//td[@class="name"]' \
    -a value_selector='.//td[@class="value"]'