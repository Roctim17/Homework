#4-1 page114
import pandas as pd
import numpy as np
example4_1 = pd.read_csv('C:\Projects\Python\data\data\chap04\example4_1.csv',encoding='gbk')
mymean=sum(example4_1['不合格品效']*example4_1['概率'])
myvar=sum((example4_1['']-mymean)**2*example4_1['率'])
mystd=np.sqrt(myvar)
print('期望值:',round(mymean,4),'方差:',round(myvar,4),'标准差:',round(mystd,4))

#4-2
from scipy.stats import binom 
p0=binom.pmf(0,5,0.06) 
p1=binom.pmf(1,5,0.06) 
p3=binom.pmf(3,5,0.06)
print('p(x=0)=',round(p1,6),'\n p(x<=3)=',round(p3,6))