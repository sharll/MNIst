import numpy as np
a = [1, 2, 3, 4]
b = np.array(a)
size = b.size
shape = b.shape
print(shape)
print("\n")

ndi = b.ndim
type = b.dtype
array_one = np.ones([10,10]) 
array_two = np.zeros([4,5])
print(array_one)
print(array_two)
print("\n")
arr = np.random.normal(1.75, 0.1, (4,5))
print(arr)
after_arr = arr[1:3, 2:4]
print(after_arr)

print("reshape函数的使用：")
one_20 = np.ones([20])
one_4_5 = one_20.reshape([4, 5])
print("---》4行5列《-----")
print(one_4_5)
print("\n")

#条件计算
#比较运算，重要！！！
stus_score = np.array([[80,88], [90,91], [92,93],[75,83], [71,72]])
print(stus_score > 80)#重要！！！
print("\n")
print(np.where(stus_score<80, 0, 90))

stus_score = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
# 求每一列的最大值(0表示列)
print("每一列的最大值为:")
result = np.amax(stus_score, axis=0)
print(result)
print("每一行的最大值为:")
result = np.amax(stus_score, axis=1)
print(result)

print("每一列的平均值:")
result = np.mean(stus_score, axis=0)
print(result)

stus_score[:, 0] =stus_score[:, 0]+5
print("加分后")
print(stus_score)




#矩阵运算np.dot（重点）
#矩阵相乘 (M行, N列) * (N行, Z列) = (M行, Z列)
stus_scores = np.array([[80, 88], [82, 81], [84, 75], [86, 83], [75, 81]])
print(stus_score.shape)
q = np.array([[0.4], [0.6]])
result = np.dot(stus_scores, q)
print("最终结果为：")
print(result)
#读取数据文件！！！重要
result = np.genfromtxt("student_score.csv", delimiter= ",")
print(result)