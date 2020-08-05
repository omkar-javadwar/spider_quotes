import scrapy


class Quotes(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = [
        'http://quotes.toscrape.com'
    ]

    def parse(self, response):

        container = response.xpath('//*[@class= "quote"]')
        for quote in container:
            text = quote.xpath('.//*[@class = "text"]/text()').extract_first()
            author = quote.xpath('.//*[@class = "author"]/text()').extract_first()
            keywords = quote.xpath('.//*[@class = "keywords"]/@content').extract_first()

            yield {
                'Text': text,
                'Author': author,
                'Key': keywords
            }

            next_url = response.xpath('//*[@class = "next"]/a/@href').extract_first()
            abs_next_url = response.urljoin(next_url)
            yield scrapy.Request(abs_next_url)