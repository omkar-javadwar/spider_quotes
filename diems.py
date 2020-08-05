import scrapy


class College(scrapy.Spider):
    name = 'diems'
    allowed_domains = ['dietms.org']
    start_urls = [
        'https://www.dietms.org'
    ]

    def parse(self, response):

        container = response.xpath('//*[@class= "wpb_text_column wpb_content_element  vc_custom_1577564478986"]')
        for quote in container:
            text = quote.xpath('.//*[@class = "wpb_wrapper"]/text()').extract_first()
            # author = quote.xpath('.//*[@class = "author"]/text()').extract_first()
            # keywords =  quote.xpath('.//*[@class = "keywords"]/@content').extract_first()

            print('-'*20)
            print(text)
        #   print(author)
        #   print(keywords)
            print('-'*20)