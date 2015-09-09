# -*- coding: utf-8 -*-

# Scrapy settings for expressicons project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'expressicons'

SPIDER_MODULES = ['expressicons.spiders']
NEWSPIDER_MODULE = 'expressicons.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0'

ITEM_PIPELINES = {
   'expressicons.pipelines.ExpressiconsImagePipeline': 100,
   'expressicons.pipelines.ExpressiconsPipeline': 200
}
FILES_STORE = '/root/Images/Expressicons_temp'
EXPRESS_ICONS_STORE = '/root/Images/Expressicons'
