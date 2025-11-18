#4-1 page114
import pandas as pd
import numpy as np
example4_1 = pd.read_csv('',encoding='gbk')
mymean=sum(example4_1['']*example4_1[''])
myvar=sum((example4_1['']-mymean)**2*example4_1[''])
mystd=np.sqrt(myvar)
print(':',round(mymean,4),':',round(myvar,4),':',round(mystd,4))
