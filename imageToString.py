#!/usr/bin/env python
#encoding: utf-8
#Author: guoxudong
import argparse             #argparse模块用于命令行参数控制
from PIL import Image

parser=argparse.ArgumentParser()
parser.add_argument('file')     #增加参数file
parser.add_argument('-O','--output')    #参数--output
parser.add_argument('--width',type=int,default=150)  #参数--width
parser.add_argument('--height',type=int,default=45) #参数--height
args=parser.parse_args()        #获取命令行参数

IMG=args.file
# IMG='./image/welcome.jpg'
WIDTH=args.width
HEIGHT=args.height
OUTPUT=args.output
# OUTPUT='./txtResource/welcome.txt'


ascii_char=list("abc@#$%^&*o. ")      #字符串列表

def get_char(r,g,b,alpha=256):  #将像素转换为字符函数
    if alpha==0:
        return ' '
    length=len(ascii_char)
    gray=int(0.2126*r+0.7152*g+0.0722*b)  #RGB转换为灰度

    unit=(256.0+1)/length      #
    return ascii_char[int(gray/unit)]    #获取该灰度在字符串列表中所对应的字符

if __name__=='__main__':
    im=Image.open(IMG)      #打开图片args.file，返回Image对象
    im=im.resize((WIDTH,HEIGHT),Image.NEAREST)   #重置尺寸

    txt="<br>\n"
    for i in range(HEIGHT):      #HEIGHT，WIDTH默认是80像素
        for j in range(WIDTH):
            txt+=get_char(*im.getpixel((j,i)))  #获取像素，计算对应字符，保存到txt中，获取像素点这里用的是getpixel（(i,j))函数
        txt+='<br>\n'       #每到行尾换行
    print (txt+'<br>')     #输出

    if OUTPUT:
        with open(OUTPUT,'w') as f:
            f.write(txt)     #保存到文本中
    else:
        with open("output.txt",'w') as f:
            f.write(txt)

