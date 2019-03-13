import numpy as np
import pandas as pd
pd.set_option('display.expand_frame_repr', False)
company = pd.read_csv('c:/java/ddrdata/company_utf.csv')
name = company.iloc[:,6]
print(type(name))
print(name[:5])

cnt = 0

for i in range(0,len(company)):
    if(company.iloc[i,6] ) == 'nan':
        cnt+=1

print(cnt)
