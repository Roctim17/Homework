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


#4-3
from scipy.stats import norm 
p1=norm. pdf (40, loc=50, scale=10)
p2=norm. pdf (40, 50, 10) - norm. cdf (30, 50, 10)
p3=norm.cdf (2.5, Loc=0, scale=1)
p4=norm. cdf (2) -norm.cdf (-1.5)
q=norm.ppf (0.025, loc=0, scale=1)
print ('p(x<=48) = ',round (p1,6), 'n"p(30<=x<=40) =', round (p2,6), '\n"p(z<=2.5)=',round(p3,6), '\np(-1.5<=z<=2) =', round (p4,6), '\nq(2.5) = ', round (q, 6))


#4-4
from scipy.stats import chi2
p1=chi2.cdf (10, df=15)
p2=1-chi2. cdf (15, df=25) 
q=chi2.ppf (0.95, df=10)
print ('p(10, 15)=', round (p1, 6), '\np(15, 25)=', round(p2,6), '\nq(0.95,10)=', round (q,6))

#4-5
from scipy.stats import t
p1=t.cdf (-2, df=10)
p2=1-t.cdf (3, df=15)
q=t. ppf (0.975, df=25)
print ('(p<=-2, df=10) =', round(p1,6), '/n''p(x>3, df=15)=', round (p2,6), '\n''q(p=0.975, df=25) = ', round (q,6))