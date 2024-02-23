# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import pandas as pd
print("*****纯小白的学习python，高手绕行*****")
print("*****欢迎收藏点赞*****")
print("\n")
print("本文内容使用pandas和matplotlib画出一个销量统计曲线的简单示例")

# 基本思路：
# 1.使用pandas从xiaoliang.csv读取数据
# 2.数据处理，赋给year,all_xiaoliang等变量，供下一步绘图用
# 3.使用matplotlib设置图的各种配置，主要包括坐标轴，画线 图例
# 4.使用matplotlib把图片保存下来

# 导入matplotlib和pandas

# 读取数据，使用pandas的read_csv函数来读取数据
# 读数据，会创建一个实例pandas.core.frame.DataFrame
data = pd.read_csv("result.csv", header=None)
# readcsv的参数很多，这里实在写不下，就算了
# 这里的设置是从当前py的目录下的xiaoliang.csv读取数据，选取文件的第一行为列名，从第0列为索引
# 我的xialiang.csv如下，可以按如下去建立自己的xiaolaing.csv
# index	年份	总计	华南	华北	华东	华西	华中
# 0	2000	1607	440	123	445	233	366
# 1	2001	1601	500	345	44	35	677
# 2	2002	2175	233	599	455	333	555
# 3	2003	1366	554	100	556	112	44
# 4	2004	1889	334	666	222	334	333
# 5	2005	1588	100	222	675	256	335
# 6	2006	1978	90	223	444	777	444
# 7	2007	1720	400	700	40	245	335
# 8	2008	1476	234	499	355	133	255
# 9	2009	1538	120	262	575	246	335
# 10	2010	2175	233	599	455	333	555
# 11	2011	1499	554	344	445	112	44
# 12	2012	2096	334	666	222	334	540
# 13	2013	1254	100	222	334	256	342
# 14	2014	1808	233	445	455	333	342
# 15	2015	1210	554	100	322	112	122
# 16	2016	1720	334	666	333	334	53
# 17	2017	945	    100	222	334	256	33
# 18	2018	1056	90	23	444	455	44
# 19	2019	1407	400	700	40	245	22
# 20	2020	1232	234	499	355	133	11

print(data.iloc[0])  # 可以打印出来看看
acc0 = data.iloc[0]
acc1 = data.iloc[1]
acc2 = data.iloc[2]
# 数据已经一股脑读到data中了，下面要开始处理
# 首先处理年份

# DataFrame有类似字典的操作，可以按列名，把某一列的数据都读出来,生成numpy.ndarray的实例，打印出来如下的样子
# [2000 2001 2002 2003 2004 2005 2006 2007 2008 2009 2010 2011 2012 2013 2014 2015 2016 2017 2018 2019 2020]

# 依次把各种销量读出来并复制给各个变量，下面绘图要用
# 不想读表的，也可以类似下面方式直接赋值，就是一个数字列表的事
# all_xiaoliang = [1607,2301,2175,1466,1889,1588,2790,2014,1476,1538,2175,1897,2096,1254,1808,1210,1820,1245,1453,1968,1333]

# 下面开始画图
plt.figure(1, figsize=(7, 5), facecolor='w',
           edgecolor='w', dpi=100, frameon=True)
# 画图的第一件事，就是用figure设置画布，后续画图就是在这块画布上涂涂抹抹
# figure的参数大概如下
# figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, frameon=True)
# num： 图像编号或名称，数字为编号 ，字符串为名称。本例设不设无所谓，随便设了1。
# figsize： 指定figure的宽和高，单位为英寸。
# dpi：参数指定绘图对象的分辨率。
# facecolor：背景颜色。默认为白色
# edgecolor：边框颜色。默认为白色
# frameon：是否显示边框（图形框架） 不太好解释，把这个参数改成false看一下就知道了
# 颜色color:常见的颜色标识符 b 蓝色，g 绿色，r 红色，c 青绿色，m 洋红，y 黄色，k 黑色，w 白色

plt.rcParams['font.sans-serif'] = ['KaiTi']  # 显示中文楷体
# 因为有中文，所以改一下字体为中文楷体。如果你的机器没有中文楷体，就显示方格，可以试着改成"微软雅黑"等等
# rcParams这个对象，是一个类似于字典的变量，用于存储matplotlib的一些运行设置
# 利用rcParams可以控制Matplotlib中的几乎所有属性
# 包括但不限于：图像大小(figure size), DPI(Dots Per Inch,表示分辨率), 线宽(line width), 颜色color and 风格style
# 以及axes, axis 和 grid等的属性，文本text和字体font的属性等等等等
# print(plt.rcParams) #可以打印一下，能看到N多属性
# print(plt.rcParams)
plt.rcParams["axes.linewidth"] = 1  # 默认线宽0.8，我们可以改粗一点
# 下面包括设置网格线等等，其实也可以利用类似方法修改，只是太不方便，也记不住

plt.grid(which="both", linestyle=":", linewidth=1, color='y', alpha=1)
plt.title("l2p self-training oot")
# 设置网格线
# grid(b=None, which='major', axis='both', **kwargs）
# visible可选参数，布尔值；缩写为b。是否显示网格线，若设置了网格线的关键字参数，则表明要设置网格线且可见；若设置visible=None且没有设置关键字参数， 则网格线不可见
# which	可选参数，要操作的网格线类型：‘major’, ‘minor’, ‘both’, 默认值：major，绘制主要刻度网格线
# axis	可选参数，要操作哪个轴的网格线：‘x’, ‘y’, ‘both’,默认值：both ，同时绘制x轴和y轴网格线
# alpha	网格线透明度
# color	网格线颜色
# linestyle	缩写ls 网格线线条类型 常用的有：- 实线、-- 破折线、-. 点划线、: 虚线、无线条（符号就是空格）
# linewidth	缩写lw 网格线线条粗细

# 下面设置x轴
plt.xlabel("task", fontsize=18, labelpad=0, horizontalalignment='right', x=0.5)
# 设置X轴标签文字，和字体大小
# xlabel(xlabel, fontdict=None, labelpad=None, **kwargs) 设置x轴
# xlabel:此参数是标签文本，并包含字符串值。
# labelpad:此参数用于与轴边界框的点间距，包括刻度和刻度标签，其默认值为“无”。
# **kwargs:此参数是文本属性，用于控制标签的外观。其实一般情况下用默认的都可以。我是故意设了几个值以便调整感受效果。
# horizontalalignment='right'，表示左对齐
# x=1.04,  #调整x轴标签的左右位置,0.3表示画布从左往右50%的位置，注意不是坐标轴50%的位置，得考虑两边框架
# 还有rotation,position=(0,-29)等许多乱七八糟的参数，可以看https://blog.csdn.net/m0_56102834/article/details/127817911

plt.xticks(fontsize=12)
# 设置X坐标轴字体大小，注意xlabel设置的是标签文字，也即那个“年份”，这里是设2000那些年份的数字
# ticks:此参数是xtick位置的列表。和一个可选参数。如果将一个空列表作为参数传递，则它将删除所有xticks
# labels:此参数包含放置在给定刻度线位置的标签。它是一个可选参数。
# **kwargs:此参数是文本属性，用于控制标签的外观，和xlabel类似，不多说了

plt.xticks(color="y")  # 设x轴文字颜色为黄色
plt.xticks(range(1, 11))  # 设置X轴显示哪些值，分开设好读
plt.xlim([0, 11])  # 设置x轴从2000开始到2020结束

# xlim(*args, **kwargs)
# 用于获取或设置x轴的最左和最右限制
# 参数left:用于将xlim设置为最左值。
# right:此参数用于将xlim设置为最右值。
# **kwargs:此参数是文本属性，用于控制标签的外观。
# 返回值：left, right:返回新的x轴限制的元组。

# 下面设置y轴，同样套路
plt.ylabel("acc@1", fontsize=18)
plt.yticks(fontsize=12)
plt.yticks(range(0, 110, 10))  # 其实许多时候可以先看看默认的情况，不合适再改
plt.ylim([0, 100])  # 设置y轴从0显示到2400
# plt.yscale('log') 设置y轴为对数坐标，有时有用，但本例用不到，因此注掉

# 开始画中间的线了，使用#matplotlib.pyplot
# 这是一个有命令风格的函数集合
# 每一个pyplot函数都使一副图像做出些许改变，例如创建一幅图，在图中创建一个绘图区域，在绘图区域中添加一条线等等。
# plot(X_ln,Y_ln, marker, color, linestyle,linewidth, markersize)
# X_ln,Y_ln，表示X Y坐标，可以为点，也可以为列表
# 线性linestyle ：- 实线、-- 破折线、-. 点划线、: 虚线、无线条（符号就是空格）
# 点型marker常见的点形状标识符有：. 点标记、D 菱形标记、d 窄菱形标记、, 像素标记、o 实心圈标记，
# marker还有：v 倒三角标记、^ 上三角标记、> 右三角标记、< 左三角标记、1 下花三角标记、2 上花三角标记
# marker还有：3 左花三角标记、4 右花三角标记、s 实心方形标记、p 实心五角标记、* 星型标记、h 六边形标记，
# marker还有：H 另一种六边形标记、+ 加号标记、x x标记、| 竖线标记、_ 横线标记
# 颜色color: b 蓝色，g 绿色，r 红色，c 青绿色，m 洋红，y 黄色，k 黑色，w 白色
# linewidth，线宽
# markersize，点标记的大小。

# 依次类推，画各个区域的线
# 以年份为x坐标，总销量为y坐标，画线， 线型为实线 颜色为红色 点型为上三角 线宽和点大小为默认
plt.plot(range(1, 11), acc0, 'r-^')
plt.plot(range(1, 11), acc1, 'b-v')
plt.plot(range(1, 11), acc2, 'g-x')

# 下面设置图例
plt.legend(["previous oot data", "future oot data", "no oot data"],
           fontsize=14, bbox_to_anchor=(0.5, 0.5), prop={'size': 13}, ncol=1)
# 参数同样有一大堆，只写了几个最常用的，方便修改看效果
# 第一个参数就是字符串列表，不解释了
# fontsize 是文字自豪
# bbox_to_anchor表示在画布的位置，同样是比例
# prop是整个图例的大小
# ncol 表示每列显示2个，默认是1，即竖着一溜下来
# 其实这些参数默认值都还可以，一般情况下没必要调

# 画的差不多了，最后保存一张png图出来
plt.show()

# 代码没多少，注释写到手软，就冲这还不给点解赞吗
