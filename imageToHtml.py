#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import os
from PIL import Image
from PIL import ImageFilter

'''
图片转化为html文件
'''

TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>{title}</title>
    <style>
        div {{
            line-height: 0.6em;
            letter-spacing: 0;
            font-size: 0.6rem;
            background: black;
            text-align: center;
            min-width: {size}em;
        }}
    </style>
</head>
<body>
    <div>{body}</div>
</body>
</html>
'''


class Converter(object):
    def __init__(self, word='田', size=200):
        self.word, self.size = word, size
        self.font = '<font color="{color}">{word}</font>'

    # 读取url内容
    # def __network(self, url):
    #     return request.urlopen(url).read()

    # 处理图片信息
    def __handle(self, binary):
        img = Image.open(binary)  # 打开制图片
        img.thumbnail((self.size, self.size))  # 压缩图片
        img.filter(ImageFilter.DETAIL)  # 图片增强
        return img

    # 分析图片像素
    def __analysis(self, img):
        body = ''
        piexls = img.load()
        width, height = img.size
        for y in range(height):
            for x in range(width):
                r, g, b = piexls[x, y]
                body += self.font.format(
                    color='#{:02x}{:02x}{:02x}'.format(r, g, b),
                    word=self.word[((y * width + x) % len(self.word))]
                )
            body += '\n<br />\n'
        return body

    # 写入文件内容
    def __writefile(self, file, str):
        fo = open(file, 'w')
        try:
            fo.write(str)
        except IOError:
            raise Exception
        finally:
            fo.close()

    # 生成html文档
    def buildDOC(self, url, output):
        try:
            # binary = self.__network(url)
            binary = url
            img = self.__handle(binary)
            html = TEMPLATE.format(
                title=self.word,
                body=self.__analysis(img),
                size=self.size
            )  # 向模板中填充数据
            self.__writefile(output, html)
        except Exception as err:
            print('Error:', err)
            return False
        else:
            print('Successful!')
            return True

# conv = Converter('dahia', 150)
# binary = './image/dahai.jpg'
# # url = 'http://www.sznews.com/ent/images/attachement/jpg/site3/20140215/001e4f9d7bf91469078115.jpg'
# out = './htmlTemplate/dahai.html'
#
# conv.buildDOC(binary, out)
'''
将image中的图片批量转化为html文件
'''

def listdir(path, list_name):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        elif os.path.splitext(file_path)[1] == '.jpg':
            list_name.append(file_path)
            file_name =file.split('.')[0]
            binary=file_path
            out = '.\\htmlTemplate\\'+file_name+'.html'
            conv = Converter(file_name, 100)
            conv.buildDOC(binary, out)
list = []
listdir('.\\image',list)
print(list)