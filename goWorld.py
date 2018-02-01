#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import json
import logging
import os
from PIL import Image, ImageFont, ImageDraw
import urllib
from logging.config import fileConfig
from urllib import request
import random
import re
from control.py_mail import send_html

'''配置日志'''
fileConfig('./log/logging.conf')
logger=logging.getLogger('infoLogger')
'''
爬取旅游信息模块
'''

class CrawlOptAnalysis(object):
    def __init__(self, search_word="北京"):
        self.search_word = search_word
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            'Host': 'so.ly.com',
            # 'Referer': 'http://www.toutiao.com/search/?keyword={0}'.format(urllib.parse.quote(self.search_word)),
            # 'Referer': 'http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word={0}'.format(urllib.parse.quote(self.search_word)),
            'Referer': 'https://so.ly.com/hot?q={0}'.format(urllib.parse.quote(self.search_word)),
            'Accept': 'application/json, text/javascript',
        }

    def _crawl_data(self):
        # url = 'http://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&queryWord={1}&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&word={1}&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&fr=&pn=30&rn=30&gsm=1e&1517294333179='.format(offset, urllib.parse.quote(self.search_word))
        url = 'https://so.ly.com/commonAjax/AjaxHandler/GetSearchResult?sourceType=pc&searchType=1000&callback=jQuery183042507453937925077_1517375011708&keyword={0}&startCityId=321&projectType=0&selectType=&selectSourceType=0&sort=0&isStat=1&from=1&to=20&cityname=%E4%B8%8A%E6%B5%B7&fchannel=&fpagetype=&_=1517375012012'.format(urllib.parse.quote(self.search_word))
        print(url)
        try:
            with request.urlopen(url, timeout=10,) as response:
                content = response.read()
        except Exception as e:
            content = None
            print('crawl data exception.'+str(e))
        return content

    def _parse_data(self, content):
        '''
        解析每次上拉加载更多爬取的 item 数据及每个 item 点进去详情页所有大图下载链接
        [
            {'article_title':XXX, 'article_image_detail':['url1', 'url2', 'url3']},
            {'article_title':XXX, 'article_image_detail':['url1', 'url2', 'url3']}
        ]
        '''
        if content is None:
            return None
        try:
            # stra = str(content.decode('utf8')).split('(')[1].split(')')[0]
            deal_str = str(content.decode('utf8').lstrip('jQuery183042507453937925077_1517375011708(').strip(')'))
            data_list = json.loads(deal_str)
            print(data_list)
            result_list = list()
            data_list = data_list.get('ReturnValue').get('Records')
            for item in data_list:
                result_dict = {'article_title': item['Title'],'image_url': item['Picture'],'feature':item['SubTitle']}
                result_list.append(result_dict)
        except Exception as e:
            print('parse data exception.'+str(e))
            site = destination()
            print(site)
            CrawlOptAnalysis(site).go()
        return result_list

    def _save_picture(self, page_title, url):
        '''
        把爬取的所有大图下载下来
        下载目录为./output/search_word/page_title/image_file
        '''
        if url is None or page_title is None:
            print('save picture params is None!')
            return
        reg_str = r"[\/\\\:\*\?\"\<\>\|]"  #For Windows File filter: '/\:*?"<>|'
        page_title = re.sub(reg_str, "", page_title)
        # save_dir = './output/{0}/{1}/'.format(self.search_word, page_title)
        save_dir = './resource/download/'
        if os.path.exists(save_dir) is False:
            os.makedirs(save_dir)
        save_file = save_dir + url.split("/")[-1]
        url = 'http:'+url                   #字符串拼接
        if os.path.exists(save_file):
            return
        try:
            with request.urlopen(url, timeout=30) as response, open(save_file, 'wb') as f_save:
                f_save.write(response.read())
            print('Image is saved! search_word={0}, page_title={1}, save_file={2}'.format(self.search_word, page_title, save_file))
            name = jointImage(save_file)
            return name
        except Exception as e:
            print('save picture exception.'+str(e))

    def go(self):
        page_list = self._parse_data(self._crawl_data())

        try:
            random_num = random.randint(0, len(page_list)-1)
            where = self.search_word
            events = page_list[random_num]['article_title']
            url = page_list[random_num]['image_url']
            info = page_list[random_num]['feature']
            name = self._save_picture(events,url)#发送的同时保存图片，后续将处理图片
            print(page_list[random_num])
            send_html('Tour', name, where+';'+events+';'+info,url)
        except Exception as e:
            print(e)

#随机生成目的地
def destination():
    # try:
    #     with request.urlopen('http://travel.qunar.com/place/?from=header', timeout=10) as response:
    #         content = response.read().decode('utf8')
    #         selector = etree.HTML(content)
    #         continent_list = selector.xpath('//*[@id="js_destination_recommend"]/div[2]/div[2]/div[2]/dl')
    #         r_num = random.randint(0, len(continent_list) - 1)
    #         continent_name = continent_list[r_num].xpath('dt')[0].text
    #         country_list = continent_list[r_num].xpath('dd/ul/li/a')
    #         r_county = random.randint(0, len(country_list) - 1)
    #         country_name = continent_list[r_num].xpath('dd/ul/li/a')[r_county].text
    # except Exception as e:
    #     logging.error('获取地名错误：' + e)
    with open('./resource/json/dest.json', 'r', encoding='utf-8') as f:
        dest_json = json.loads(f.read())
        dest_list = dest_json.get('group').get('dest').get('common')
        r_num = random.randint(0, len(dest_list) - 1)
        dest_desc = dest_list[r_num].get('cities')[0].get('parent')
        dest_list = dest_list[r_num].get('cities')[0].get('children')
        r_dest = random.randint(0, len(dest_list) - 1)
        dest_name = dest_list[r_dest]
    return dest_name

def jointImage(image):
    img1 = Image.open(image)
    img1 = img1.convert('RGBA')
    x,y=img1.size
    img2 = Image.open("./resource/img/point.png")
    img2 = img2.convert('RGBA')

    r, g, b, alpha = img2.split()
    alpha = alpha.point(lambda i: i > 0 and 204)

    img1.paste(img2, (x-200, y-160),alpha)
    # img = Image.composite(img2, img1, alpha)
    # img1.show()
    image_name = image.split('.jpg')[0] + '.png'
    img1.save(image_name)

    return image_name

if __name__ == '__main__':
    site = destination()
    print(site)
    CrawlOptAnalysis(site).go()