# -*- coding: utf-8 -*-
import scrapy
from mySpider.items import MyspiderItem 


class HxwkSpider(scrapy.Spider):
    name = 'hxwk'
    allowed_domains = ['hxwk.org']
    start_urls = [
        # 'http://hxwk.org/',
                  # 首页
                  'http://pang-jing.hxwk.org/page/2/',
                  # 'http://a-w.hxwk.org/'
                  ]

    def parse(self, response):
        # item= MyspiderItem()
        # item['title']=response.xpath("/html/head/title/text()")
        # print(item['title'])

        url=self.start_urls[0]
        # print("hello")
        # print(url)
        # pass
        # scrapy.Request(url,self.parseList)
        # open(filename, 'wb').write(response.body)

        # 获取网站标题
        # context = response.xpath('/html/head/title/text()')
        # print(response.body)
        self.parseList(response)




    def parseList(self,response):
        # urls = response.xpath("//a/@href").extract()
        urls = response.xpath("//td/ul/li/a/@href").extract()
        counts = response.xpath("//td/ul/li/span/text()").extract()
        # print(response.xpath('/html/head/title/text()'))
        # print(urls[0])
        u="http://baidu.com"
        # scrapy.Request(urls[0],self.parseNews)
        scrapy.Request(u,self.parseNews)

		# for url in urls:
		# 	yield scrapy.Request(url,self.parseNews)

    def parseNews(self,response):
        # data = response.xpath("//div[@class='post_content_main']")
        # item = NewsSpiderItem()
        # timee = data.xpath("//div[@class='post_time_source']/text()").extract()
        # title = data.xpath("//h1/text()").extract()
        # content = data.xpath("//div[@class='post_text']/p/text()").extract()
        # pass
        pageurls=response.xpath("//h2[@class='entry-title']/a/@href").extract()
        titles=response.xpath("//h2[@class='entry-title']/a/text()").extract()
        print('afa')
        print(pageurls)
        print(titles)



