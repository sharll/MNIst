#Pandas是基于Numpy开发出的,专门用于数据分析的开源Python库
import pandas as pd
import numpy as np
#pandas的series（一维数据，以键值对形式，键可以重复）
data_0=pd.Series(np.arange(4,10))
print(data_0)
data_1 =pd.Series([11,12,14],index=["北京","上海", "深圳"])
print(data_1)
# 创建一个3行4列的DataFrame类型数据（多数据特征，既有行索引，又有列索引）
data_3_4 = pd.DataFrame(np.arange(10, 22).reshape(3, 4))
# 打印数据
print(data_3_4)
# 打印第一行数据
print(data_3_4[:1])
# 打印第一列数据
print(data_3_4[:][0])
print(data_3_4[1:2][1])# https://blog.csdn.net/xpresslink/article/details/77727507列表切片理解

result = pd.read_csv("student_")