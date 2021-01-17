# -*- coding: utf-8 -*-

'''
@Time    : 2021/1/15 20:33
@Author  : Wanhao Zhang
@Contact : 1809721229@qq.com 
@FileName: biaobai.py
@Software: PyCharm
 
'''
from PIL import Image, ImageDraw, ImageFont
def draw(pic, draw_text):
    img = cv2.imread(pic)
    blank = Image.new("RGB", [img.shape[1],img.shape[0]], "white")
    drawObj = ImageDraw.Draw(blank)
    n = 10
    m = 9
    font = ImageFont.truetype(font_path, size = m)
    for i in range(0, img.shape[0], n):
        for j in range(0, img.shape[1], n):
            drawObj.text(
                [j, i],
                draw_text[int(j / n) % len(draw_text)],
                fill = (img[i][j][2], img[i][j][1],
                    img[i][j][0]),
                font = font
            )
    blank.save('img_' + pic)

draw('1.jpg', "我爱你")