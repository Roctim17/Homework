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