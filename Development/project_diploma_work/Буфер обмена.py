    def parse(self, response):
        product_links = response.css("a::attr(href)").getall()
        for link in product_links:
            # Добавленная проверка (единственное изменение)
            if link and link.startswith(('tel:', 'mailto:', 'javascript:', 'whatsapp:', 'callto:')):
                continue
                
            full_url = response.urljoin(link)
            if full_url not in self.visited_urls:
                self.visited_urls.add(full_url)
                yield response.follow(full_url, self.parse_product)