import numpy as np
import pandas as pd


# pandas 입출력
pd.set_option('display.expand_frame_repr', False)
df = pd.read_csv('tbl_seoul_final.csv',
                    encoding='euc-kr')

print(df)
