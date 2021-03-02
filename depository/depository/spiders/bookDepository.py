import scrapy
from ..items import DepositoryItem

class BookdepositorySpider(scrapy.Spider):
    name = 'bookDepository'
    start_urls = [
        'https://www.bookdepository.com/category/1541/Physics/'
    ]

    def parse(self, response):
        items = DepositoryItem()

        product_name = response.css('.title a::text').extract()
        product_author = response.css('.author span::text').extract()
        product_price = response.css('.price::text').extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price

        yield items