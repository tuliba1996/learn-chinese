import scrapy
from scrapy import Spider, Selector


class CrawlerItem(scrapy.Item):

    User = scrapy.Field()
    Comment = scrapy.Field()
    Time = scrapy.Field()
#


class Word(Spider):
    name = 'crawler'
    allowed_domains = ['chineseconverter.com']
    convert_url = 'https://www.chineseconverter.com/en/convert/chinese-to-pinyin'
    start_urls = ['https://www.chineseconverter.com/en/convert/chinese-to-pinyin']

    def parse(self, response):
        token = response.css('input[name="_csrf-frontend"]::attr(value)').extract_first()
        print('token', token)
        data = {
            '_csrf-frontend': token,
            'ChineseToPinyin[input]': '我',
            'ChineseToPinyin[type]': 'pinyin'
        }
        yield scrapy.FormRequest(url=self.convert_url, formdata=data, callback=self.parse_quote)

    def parse_quote(self, response):
        d = response.css('div.form-group > div.result-html::text').extract_first()
        print('result', d)



# class CrawlerSpider(Spider):
#     name = "crawler"
#     allowed_domains = ["thegioididong.com"]
#     start_urls = [
#         "https://www.thegioididong.com/dtdd/samsung-galaxy-a50",
#     ]
#
#     def parse(self, response):
#         questions = Selector(response).xpath('//ul[@class="listcomment"]/li')
#         print('afsdf', response)
#         for question in questions:
#             item = CrawlerItem()
#
#             item['User'] = question.xpath(
#                 'div[@class="rowuser"]/a/strong/text()').extract_first()
#             item['Comment'] = question.xpath(
#                 'div[@class="question"]/text()').extract_first()
#             item['Time'] = question.xpath(
#                 'div[@class="actionuser"]/a[@class="time"]/text()').extract_first()
#
#             yield item
