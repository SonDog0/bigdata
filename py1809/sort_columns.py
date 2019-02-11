# 원래 데이터 불러서
import pandas as pd

son = pd.read_csv('c:/Java/data/lpoint_ppomppu.txt' , sep = '\t' , header = None)

# 파악 하고
print(son.describe())


# 중복행 제거
unique_son =son.drop_duplicates()

# 중복행 제거 파악
print(unique_son.describe())

# 정제 된 파일로 재생성

unique_son.to_csv('lpoint_ppomppu_sort.txt',sep= '\t' , index = False)