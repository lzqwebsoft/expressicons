# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import scrapy
import os
import shutil
import expressicons.settings
from scrapy.contrib.pipeline.files import FilesPipeline
from scrapy.exceptions import DropItem

class ExpressiconsImagePipeline(FilesPipeline):
    idx = 0

    def get_media_requests(self, item, info):
        for idx,company in enumerate(item['companies']):
            self.idx = idx
            yield scrapy.Request(company['image'])

    def item_completed(self, results, item, info):
        for status, data in results:
            if status:
                current = 0
                for idx, c in enumerate(item['companies']):
                    if(c['image'] == data['url']):
                        current = idx
                        break
                item['companies'][current]["image"] = data['path']
        return item

class ExpressiconsPipeline(object):
    def open_spider(self, spider):
       self.f = open("express_list.xml", "w+")
       self.f.write('<?xml version="1.0" encoding="UTF-8"?>\r\n')
       self.f.write('<companies>')

    def process_item(self, item, spider):
        self.f.write("\r\n    <!-- " + item['type'].encode('UTF-8')  + "  -->\r\n")
        for company in item['companies']:
           self.f.write(('    <company code="'+ company['code'] +'">' + company['name'] + '</company>\r\n').encode('UTF-8'))
           # 重命名快递公司的图标文件
           old_file = os.path.join(expressicons.settings.FILES_STORE, company['image'])
           filename, file_extension = os.path.splitext(old_file)
           new_file = os.path.join(expressicons.settings.EXPRESS_ICONS_STORE, company['code'] + file_extension)
           if(os.path.exists(old_file)):
              shutil.copy2(old_file, new_file)
        return item

    def close_spider(self, spider):
        self.f.write('</companies>')
        self.f.close()
