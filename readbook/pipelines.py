# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import urllib.request

# class ReadbookPipeline(object):
#     def open_spider(self,spider):
#         self.fp = open('bookinfo.json','w',encoding='utf-8')
#
#
#     def process_item(self, item, spider):
#         self.fp.write(str(item))
#         return item
#     def close_spider(self,spider):
#         self.fp.close()
class ReadbookedownloadPipeline(object):
    def process_item(self,item,spider):
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'),('Referer','https://www.dushu.com/')]
        urllib.request.install_opener(opener)
        urllib.request.urlretrieve(url=item['bookinfo'].get('url')[0],filename = '../images/'+item['bookinfo'].get('name')[0]+'.jpg')
        print(str(item['bookinfo'].get('url')))

