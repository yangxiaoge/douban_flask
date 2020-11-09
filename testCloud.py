# -*- coding = utf-8 -*-
# @Time : 2020/11/7 15:12
# @Author : Bruce Yang
# @File : testCloud.py
# @Software : PyCharm
# @Description :

import sqlite3  # 数据库

import jieba  # 分词
import numpy as np  # 矩阵运算
from PIL import Image  # 图片处理
from matplotlib import pyplot as plt  # 绘图，数据可视化
from wordcloud import WordCloud  # 词云

# 准备词云所需要的的文字（词）
con = sqlite3.connect('豆瓣Top250.db')
cur = con.cursor()
sql = 'select info from douban'
data = cur.execute(sql)
text = ""
for item in data:
    text += item[0]
print(text)
cur.close()
con.close()

# 分词
cut = jieba.cut(text)
string = ' '.join(cut)
print(len(string))

#
img = Image.open(r'static/assets/img/test_tree.jpg')
img_array = np.array(img)  # 将图片转成数组
wc = WordCloud(
    background_color='white',
    mask=img_array,
    font_path='STXINGKA.TTF'  # 字体所在位置 C:\Windows\Fonts
)
wc.generate_from_text(string)

# 绘制图片
fig = plt.figure(1)
plt.imshow(wc)
plt.axis('off')  # 是否显示坐标轴
# plt.show()  # 显示生成的词云图片
plt.savefig(r'static/assets/img/word.jpg', dpi=500)
