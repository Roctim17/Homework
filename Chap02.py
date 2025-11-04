import pandas as pd 
import matplotlib.pyplot as plt 
df = pd.read_csv('C:\Projects\Python\data\data\chap01\example1_1.csv', encoding = 'gbk')
plt.rcParams['font.sans-serif'] = ['SimHei']

t4=pd.crosstab (df. 性别,df.态度)
t4.plot (kind='bar')
plt.title('(a) 垂直并列条形图')
t4.plot (kind='barh')
plt.title('(b) 水平并列条形图')
# 堆叠条形图
t5=pd.crosstab (df. 社区,df. 态度)
t5. plot (kind='bar', stacked=True)
plt.title ('(c) 垂直堆叠条形图')
t6=pd.crosstab(df. 态度,df. 社区)
t6. plot (kind='barh', stacked=True)
plt.title ('(d) 水平堆叠条形')
plt.show()
# print(plt.show())

#2-3
import pandas as pd 
import matplotlib.pyplot as plt
df=pd. read_csv(r'C:\Projects\Python\data\data\chap01\example2_2.csv', encoding= 'gbk')
plt.rcParams['font.sans-serif'] = ['SimHei']
plt. subplots(1,2, figsize=(10,6))
plt.subplot(121)
P1 = plt.pie(df ['北京'],labels=df ['支出项目'],
autopct='%1.2f%%')
plt.title('(a)普通饼图')
plt.subplot(122)
p2=plt.pie (df ['北京'],labels=df ['支出项目'],
           autopct="%1.2f%%",
shadow=True,
explode = (0.2,0,0.1,0,0,0,0,0))
plt.title(' (b) 3DDt|4')
plt.show()
print(plt.show())