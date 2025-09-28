print ("Hello World")
a = [1,2,3,4,5]
print(a)
b = ["Roctim"]
print(b)
d = list(range(10))
print(d)
e = list(range(100,200,20))
print(e)
a.append(6)
print(a)
b.insert(2,"Rt17")
print(b)
ab = a+b
print(ab)
f = [2,3,4,5,2,8]
f.sort()
print(f)
g = ["roctim","roc","Rt","Rt17","Roc"]
print(g)
print("Hello World",a,b,d,e,ab,f,g,e)



# Home Work 


# dcl = {'rfg':68,'jdfhj':85,'kdhfjk':74,'jghfj':88,'fg':63}
# print(dcl)

dc1={"刘文時":68,"王于期":85,"田思雨":74,"徐丽娜":88,"丁文能":63}
#5名学生考试分数的字典
print (dc1)

# 用 dict 函数创建字典
dc2=dict(刘文涛=68,王宇翔=85,田思雨=74,徐丽娜 =88,丁文彬 =63)
#5名学生考试分数的字典
print (dc2)
#以列表的形式返回字典 dc1 中的键
dc1.keys ()
# 以列表的形式返回字典 dc1 中的值
dc1.values ()

#以列表的形式返回字典 dc1 中的键值对
dc1.items ( )

#返回（查询）字典 dc1 中键k上的值dc1［'徐丽娜'］
# 返回徐丽娜（键）的分数
88
# 删除字典 dc1 中的某个键值对
dc1['徐丽娜']

del dc1['田思雨']
print(dc1)

# end of page 13 
# ＃使用 set 函数創建集合
set1= set ([2,2,2,1,8,3,3,5,5])
set1
# 11, 2,3,5,8) print
# 使用大括号｛｝创建集合
set2 = {2,2,2,1,4,3,3,5,6,6}
set2
# (1, 2, 3,4,5,6) print
# 两个集合的并集（两个集合中不同元素的集合）
set1|set2
# ＃ 或写成 set1.union （set2）
# {1, 2,3, 4,5,6,8} print
#两个集合的交集（两个集合中同时包含的元素）
set1&set2
# 或写成 setl.intersection （set2）
# (1, 2,3,5} print

# end of page 14 


import numpy as np
a1=np.array([5,4,1,2,3])
a2=np.arange(10)
a3=np.arange(2,6,0.5)

print('a1:',a1)
print('a2:',a2)
print('a3:',a3)