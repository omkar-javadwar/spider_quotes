import scrapy


class Quotes(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://mohsinweb.herokuapp.com/quotes/'
    ]

    def parse(self, response):
        for quote in response.css('div.quotes'):
            yield {
                'quote': quote.css('p.aquote::text').extract(),
                'author': quote.css('p.author::text').extract_first(),
            }
