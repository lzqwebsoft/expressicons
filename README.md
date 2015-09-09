# 快递100图标及编码爬虫
爬取[快递100](http://m.kuaidi100.com/all/)快递图标及编码，Python Scrapy示例。  
### 结构说明
<pre>  
expressicons  
|__resources 已爬取的编码及图标资源目录  
|__expressicons Scrapy代码  
<pre>  

***注：*** 由于快递100的图标是PNG格式，而Scrapy的图片管道类`ImagesPipeline`默认将图片转化为JPEG格式，且对图片进行了压缩，因此在这里使用文件管道类`FilesPipeline`下载图片（切换`ImagesPipeline`与`FilesPipeline`毫无违合感，用法相同）。

参见：[http://scrapy-chs.readthedocs.org/zh_CN/latest/topics/images.html](http://scrapy-chs.readthedocs.org/zh_CN/latest/topics/images.html)
