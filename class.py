import pandas as pd
df = pd.read_excel(r"c:C:\Projects\Python\data\data\chap01\table_1.xlse")
df.to_csv(r"C:\Projects\Python\data\data\chap01\df1.csv",index=False,encoding='utf-8')
df.to_excel(r"C:\Projects\Python\data\data\chap01\df2.xlsx",index=False)

