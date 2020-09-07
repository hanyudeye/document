# -*- coding: utf-8 -*-
import scrapy

# 引入类
from mySpider.items import MyspiderItem as ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    # start_urls = ['http://itcast.cn/']
    start_urls = ("http://www.itcast.cn/channel/teacher.shtml#ajavaee", )

    def parse(self, response):
        # filename = "teacher.html"
        # open(filename, 'wb').write(response.body)

        # 获取网站标题
        # context = response.xpath('/html/head/title/text()')

        # 提取网站标题
        # title = context.extract_first()
        # print(title)
        # pass

        # 存放老师信息的集合
        items = []

        for each in response.xpath("//div[@class='li_txt']"):
            # 将我们得到的数据封装到一个 `ItcastItem` 对象
            item = ItcastItem()

            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()
            
            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]
            
            items.append(item)

        # 直接返回最后数据
        return items
