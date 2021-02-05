import scrapy
from mosoteachSpider.items import MosoteachspiderItem
from mosoteachSpider.custom_widget import Warning


class MosoteachSpider(scrapy.Spider):
    name = 'mosoteachAll'
    allowed_domains = ['www.mosoteach.cn']
    cin=open('course.txt','r')
    start_urls = [cin.readline().strip('\n')]
    
    def start_requests(self):
        # 登录之后用 chrome 的 debug 工具从请求中获取的 cookies
        try:
            data=open('cookie.txt','r')
        except FileNotFoundError:
            Warning(['请先填写Cookie!'],1,True)
            print('NOCOOKIE')
        else:
            cookiesstr=""
            while True:
                p=data.readline().strip('\n')
                if not p:
                    break
                else:
                    cookiesstr+=p
                    cookiesstr+='='
                    p=data.readline().strip('\n')
                    cookiesstr+=p
                    cookiesstr+=';'
            cookiesstr=cookiesstr.rstrip(';')
            cookies = {i.split("=")[0]:i.split("=")[1] for i in cookiesstr.split(";")}
    
            # 携带 cookies 的 Request 请求
            yield scrapy.Request(
                self.start_urls[0],
                callback=self.parse,
                cookies=cookies
            )

    def parse(self, response):
        item = MosoteachspiderItem()
        link = response.xpath('//div[@class="res-row-open-enable res-row preview " or @class="res-row-open-enable res-row preview-file "]/@data-href').extract()
        item['link'] = link
        name = response.xpath('//div[@class="res-row-open-enable res-row preview " or @class="res-row-open-enable res-row preview-file "]//span[@class="res-name"]//text()').extract()
        item['name'] = name
        size=response.xpath('//div[@class="res-row-open-enable res-row preview " or @class="res-row-open-enable res-row preview-file "]//div[@class="create-box manual-order-hide-part"]//span[1]//text()').extract()
        item['size']=size
        return item
