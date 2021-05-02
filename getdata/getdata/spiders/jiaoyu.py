from getdata.items import GetdataItem
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class MyJiao(CrawlSpider):
    name = "jiaoyu"
    allowed_domains = ['www.moe.gov.cn']
    start_urls = [
        'http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/'
    ]

    for i in range(1, 10):
        url = "http://www.moe.gov.cn/jyb_xwfb/gzdt_gzdt/index_" + str(i) + ".html"
        start_urls.append(url)

    rules = [
        Rule(LinkExtractor(allow='/moe'), callback='parse_item'),
        Rule(LinkExtractor(allow='jyb_xwfb/gzdt_gzdt/s'), callback='parse_item')
    ]

    def parse_item(self, response):
        title = response.xpath('//*[@id="moe-detail-box"]/h1/text()').extract()
        add_time = response.xpath('//*[@id="moe-detail-box"]/div[1]/text()').extract()
        content = response.xpath('//*[@id="moe-detail-box"]/div[2]/p').extract()
        editor = response.xpath('//*[@id="detail-editor"]/text()').extract()

        item = GetdataItem()
        item['title'] = title
        item['add_time'] = add_time
        item['content'] = content
        item['editor'] = editor

        yield item
