# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface


class MosoteachspiderPipeline:
    def process_item(self, item, spider):
        if spider.name=='mosoteachVideo':
            count=len(item['name'])
            with open('linksVideo.txt', 'w+') as fp:
                for i in range(count):
                    fp.write(item['name'][i]+'\n'+item['size'][i]+'\n'+item['duration'][i]+'\n'+item['link'][i]+'\n')
            fp.close()
        elif spider.name=='mosoteachFile':
            count=len(item['name'])
            with open('linksFile.txt', 'w+') as fp:
                for i in range(count):
                    fp.write(item['name'][i]+'\n'+item['size'][i]+'\n'+item['link'][i]+'\n')
            fp.close()
        elif spider.name=='mosoteachAll':
            count=len(item['name'])
            with open('linksAll.txt', 'w+') as fp:
                for i in range(count):
                    fp.write(item['name'][i]+'\n'+item['size'][i]+'\n'+item['link'][i]+'\n')
            fp.close()