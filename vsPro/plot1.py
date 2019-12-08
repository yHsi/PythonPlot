#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@文件    :plot1.py
@说明    :
@时间    :2019/12/07 17:36:41
@作者    :YuXZhang
@版本    :1.0
'''

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# reading data
file_path = "../data/observable_NovAtel.txt"
f = open(file_path,"r")
arrA = []
lines = f.readlines()
for line in lines:
    arrA.append(line.replace("NaN","0").split())
f.close()
ar = np.array(arrA)

Color = ['orangered','dodgerblue','green','gold',
         'crimson','cornflowerblue','mediumseagreen','mediumaquamatine']

# plot 
lable = ar[:,0]
legend_ = ['f1P','f1L','f2P','f2L']
color_ = Color[0:len(legend_)]
print(legend_[0])
data = ar[:,1:5]
data = data.astype(np.float)
axis_x  = np.arange(len(lable))
print(axis_x)
width = 0.15
fig,f = plt.subplots()
for i in range(data.shape[1]):
    bar = plt.bar(axis_x+width * i,data[:,i],width,label = legend_[i],bottom = None,align = 'center',alpha=0.9,color = color_[i])
    #plt.legend(legend_[i],)

# 设置绘图区间
plt.axis([-0.5,5,0,109])
# 设置X坐标的具体位置
f.set_xticks(axis_x+width*(data.shape[1]-1)/2)
# 设置X的标签
f.set_xticklabels(lable)
# 设置x和y的坐标周名称
plt.ylabel("Percentage(%)",fontdict=None,labelpad=None,fontsize = "large"
           ,fontstyle = "normal",fontweight = "roman")
plt.xlabel("Systems",fontdict=None,labelpad=None,fontsize = "large"
           ,fontstyle = "normal",fontweight = "roman")

#生成图例
#patches = [mpatches.Patch(color = color_[i],label = "{:s}".format(legend_[i]))
 #        for i in range(len(color_))]
#ax = plt.gca()

#ax.legend(handles = patches,bbox_to_anchor = (0.9,0.1),ncol = 4)
plt.legend(bbox_to_anchor = (0.31,0.982),loc = "lower left",ncol = 4)
plt.show()



