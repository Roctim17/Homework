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