# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 21:16:44 2018

@author: Lingyan_Xu
"""

import numpy as np
import xlrd
from numpy import *
from sklearn import preprocessing  
from smt.surrogate_models import KRG
import random
import matplotlib.pyplot as plt
#读取输入数据
data=xlrd.open_workbook('Input.xlsx') # 打开xls文件

x = []
table = data.sheet_by_index(0) # 打开第一张表
nrows = table.nrows # 获取表的行数  
for i in range(nrows): # 循环逐行打印
    x.append(table.row_values(i))
x = np.array(x)
# x[:,0] = x[:,0]/5
# x[:,1] = x[:,1]/20
# x[:,2] = (x[:,2]-0.5)/2
# x[:,3] = (x[:,3]-0.5)/2
# x[:,4] = (x[:,4]-0.5)/2

# print('input:',x)
# x = x[0:50]

#读取输出数据
data=xlrd.open_workbook('output2021-3.xlsx') # 打开xls文件

y=[]

table = data.sheet_by_index(0) # 打开第一张表
nrows = table.nrows # 获取表的行数  
for i in range(nrows): # 循环逐行打印
    y.append(table.row_values(i))
y = np.array(y)
y = y[:,0]
print(y)
# outputs = y[0:50]
# for i in range(len(y.T)):
#     y[:,i] = y[:,i] / max(y[:,i])
# print('output:',y)

the = [1e-2]

sm = KRG(theta0=the)
sm.set_training_values(x, y)
sm.train()
testdata = np.array([[0.83581406, 12.51206179, 0.924354149, 1.920193787, 1.561607967]])
y_pre_kri = sm.predict_values(testdata)
print('test_output',y_pre_kri)
#  x1(0,5)  X2(0,20) X3(0.5,2) X4(0.5,2) X5(0.5,2)
data_sample = []
for i in range(100):
    data_sample.append(random.uniform(0.5, 2))
print(data_sample)
# x1 = 2.5
x2 = 10
x3 = 1.75
x4 = 1.75
x5 = 1.75
data = []
for i in range(len(data_sample)):
    data.append([data_sample[i],x2,x3,x4,x5])
print(data)
data = np.array(data)
y_pre_kri = sm.predict_values(data)
print(y_pre_kri)
y = []
for i in range(len(y_pre_kri)):
    y.append(y_pre_kri[i][0])
# plt.plot(data_sample,y)
plt.legend()

plt.scatter(data_sample, y, s=20, c="#ff1212", marker='o')
plt.show()

import numpy as np
import pandas as pd

data = pd.DataFrame({'A':data_sample,'B':y})

print(data.corr()) # 计算pearson相关系数
    
    
    
    
    
    