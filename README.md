# MetaSpider

> MetaSpider是一款基于Tika的网络富文本元信息爬虫，实现网络富文本（Doc，PDF，PPT，JPG，PNG，...）文件的爬取和元信息抽取。

![](https://img.shields.io/badge/Python-v2.7-blue.svg) ![](https://img.shields.io/badge/Scrapy-v1.5-green.svg)

## Usage:

> requirements
> jnius==1.1.0
> scrapy==1.5.0
> pymongo==3.6.1

## Intrduction

通过jnius实现Python对Tika的调用，解析爬虫获取的富文本资源，将元数据存入Mongo数据库。

其他操作与Scrapy编程方式相同

数据库配置以及图片缓存文件夹在settings中设置，分别位于META_SROTE和MONGO_CONF中。

pipelines中需要指定tika-app所在路径和java_home路径。

Tika-app-xx.jar请至Tika官网下载：

[http://tika.apache.org/download.html](http://tika.apache.org/download.html)


注意：以上路径选择推荐使用绝对路径。





>（ps：案例中的spider仅供参考，大家不要一直爬我博客；另外请遵守爬虫道德规范~~）









