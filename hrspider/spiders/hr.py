import scrapy


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['careers.tencent.com/search.html']
    start_urls = ['http://careers.tencent.com/search.html/']

    def parse(self, response):
        pass
