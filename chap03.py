# page 89
import pandas as pd 
example3_1 = pd.read_csv('C:\Projects\Python\data\data\chap03\example3_1.CSV',encoding='gbk')
pd.DataFrame.mean(example3_1)

# page 90
import pandas as pd 
import numpy as np
example3_2 = pd.read_csv("C:\Projects\Python\data\data\chap03\example3_2.CSV",encoding='gbk')
m=example3_1['']
f=example3_2['']
print(':',np.average(a=m,weights=f))

#page 90
import pandas as pd
example3_1[''].median()

#page 91
import pandas as pd 
pd.DataFrame.quantile(example3_1,q=[0.25,0.75],interpolation='linear')

#page 93
import pandas as pd
pd.DataFrame.quantile(example3_1,q=[0.1,0.25,0.5,0.75,0.9],interpolation='linear')

# page 94
import pandas as pd
R=example3_1[''].max()- example3_1[''].min()
print(':',R)

import numpy as np
IQR = np.quantile(example3_1['',q=0.25])-np.quantile(example3_1[''],q=0.25)
print('IQR =',IQR)

#Page 95
import pandas as pd 
var = example3_1[''].var(ddof=1)
print(':',var)

sd=example3_1[''].std()
print(':'round(sd,2))

#page 96
import pandas as pd
import numpy as np
example2_3 = pd.read_csv('C:\Projects\Python\data\data\chap03\example2_3.CSV', encoding='gbk')
s_mean = example2_3.mean()
s_sd = example2_3.std()
s_cv = s_sd / s_mean
df = pd.DataFrame