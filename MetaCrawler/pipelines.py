# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os

import pymongo as pymongo
import requests
from MetaCrawler.settings import META_SROTE, MONGO_CONF

os.environ['CLASSPATH'] = "tika-app-1.18.jar"
os.environ['JAVA_HOME'] = "jdk1.8.0_171"

from jnius import autoclass


Tika = autoclass('org.apache.tika.Tika')
Metadata = autoclass('org.apache.tika.metadata.Metadata')
FileInputStream = autoclass('java.io.FileInputStream')
# File = autoclass('java.io.File')
# Language = autoclass('org.apache.tika.language.LanguageIdentifier')
# Handler = autoclass('org.apache.tika.sax.BodyContentHandler')
# Parser = autoclass('org.apache.tika.parser.AutoDetectParser')
# ParseContext = autoclass('org.apache.tika.parser.ParseContext')
tika = Tika()
meta = Metadata()

def meta_parser(path):
    meta_dic = {}
    text = tika.parseToString(FileInputStream(path), meta)
    for key in meta.names():
        meta_dic[key] = meta.get(key)
    return meta_dic

def mongo_put(dic):
    client = pymongo.MongoClient(MONGO_CONF['url'])
    db = client[MONGO_CONF['database']]
    collection = db[MONGO_CONF['collection']]
    post = collection.insert_one(dic)
    client.close()


class MetacrawlerPipeline(object):
    def process_item(self, item, spider):
        dir_path = '{}'.format(META_SROTE)
        if not os.path.exists(dir_path) and len(item['src']) != 0:
            os.mkdir(dir_path)
        if len(item['src']) == 0:
            with open("check.txt", "a+") as fp:
                fp.write("".join(item['title']) + ":" + "".join(item['src']))
                fp.write("\n")

        for meta_url, name in zip(item['src'], item['title']):
            try:
                file_name = name
                with open('{}//{}'.format(dir_path, file_name), 'wb') as f:
                    req = requests.get(meta_url)
                    f.write(req.content)
                meta_dic = meta_parser('{}//{}'.format(dir_path, file_name))
                mongo_put(meta_dic)
                os.remove('{}//{}'.format(dir_path, file_name))
            except:
                pass
        return item
