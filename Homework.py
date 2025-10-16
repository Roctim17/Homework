

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

a4 = np.array ([[1,2],[3,4],[5,6]])
print(a4)

import numpy as np
a5=np.array(12)
a6=a5.reshape(3,4)
a6
print(a6,'a6')

a6.ndim
a6.shape
a6.dtype
a6.astype(float)
a6[2]
a3[5]
a1.sort()


# end of page 15 


import pandas as pd
s1 = pd.Series ([2,3,4,5])
print(s1)

s2 = pd.Series ([5,8,7,6], index=['a','b','c','d'])
print(s2)

s3 = pd.Series ([5,8,7<6], index =['fd',25,True])
print(s3)

s4 =pd.Series ({'a':1,'b':'boy','c':3})
print(s4)


import numpy as np
a5 = np.arange (12)
a6 = a5.reshape (3,4)
print (a6)

a6.ndim
a6.shape
a6.dtype
a6.astype (float)
a6[2]
a3[5]
a1.sort()
# End of page 18
s1 = pd.Series([2,3,4,5])
print(s1)
s2 = pd.Series([5,8,7,6], index = ['a','b','c','d'])
print(s2)
s3 = pd.Series([60,80,50], index=['fu',25,True])
print(s3)
s4 = pd.Series({'a':1,'b':'boy','c':3})
print(s4)
s5 = pd. Series ( range (5))
print (s5)


import pandas as pa
s6 = pd.Series ([5, 8, 7, 6], index= ['a','b','c','d'])
# print（'索引：',s6.index)
# print（'数据：',s6.values)
# print（'类型：',s6.dtype)
s6.name ='我是一个 pandas 的 Series'
s6.index.name= ''
print(s6)
s6 = s6.astype(float)
print(s6)

s6[[1,3]]=[2,8]
print(s6)
s7=pd.Seriee([1,2,3],index=['a','c','e'],dtype=float)
print(s6+s7)
s8=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'], dtype=float)
c=s8.cumsum ()
s=s8.sum()
m=s8.mean()
print()

import pandas as pd
d = {"姓名":["刘文涛","王宇翔","田思雨","徐丽娜","丁文彬"],

"统计学":[68, 85, 74, 88, 63],

"数学":[85, 91, 74, 100, 82],

"经济学":[84, 63, 61, 49, 89]}
table1_1 = pd.DataFrame (d)
print(table1_1)

import pandas as pd
df = pd.read_csv("C:\Projects\Python\data\data\chap01\table1_1.csv",encoding='gbk')
df[['数学']]
print(df,'this')
df[['数学','经济学']]
df.loc[2]
df.loc[[2,4]]
df.loc[2:4]
df['经济学']=[88,75,92,67,78]
df
print(df)
df.insert(2,'经济学',[88,75,92,67,78])
df
print(df)
df.drop(['经济学'],axis=1,inplace=True)
df
print(df)
df.drop(index=2,inplace=True)
df
print(df)
df.rename(colume={'经济学':'ROC','数学':'Rt17'})
df.iloc[2,1]=85
df
print(df)
df.loc[:,]