import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import ReadbookItem


class ReadSpider(CrawlSpider):
    name = 'read'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/book/1107_1.html']

    rules = (

                #< a href="/book/1107_2.html" > 2 < / a >
        Rule(LinkExtractor(allow=r'/book/1107_\d+.html'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        src_list = response.xpath('//div[@class="book-info"]//img')

        for src in src_list:
            url = src.xpath('./@data-original').extract()
            name = src.xpath('./@alt').extract()
            bookinfo = {}
            bookinfo['name'] = name
            bookinfo['url'] = url

            book = ReadbookItem(bookinfo=bookinfo)
            yield book
