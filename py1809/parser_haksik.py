# 서울 버스 홈페이지에서 1164번 2115번 버스 도착 예정시간 (서경대본관 , 08372)
# 'http://210.96.13.82:8099/api/rest/stationinfo/getStationByUid?arsId=08372'

import requests
from bs4 import BeautifulSoup


first_arrive=[]
two_arrive= []

url ='http://210.96.13.82:8099/api/rest/stationinfo/getStationByUid?arsId=08372'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'}

res = requests.get(url,headers=headers)

html = BeautifulSoup(res.text,'lxml')

print(html)

for arr in html.select('msgbody arrmsg1'):
    first_arrive.append(arr.text)

for arr in html.select('msgbody arrmsg2'):
    two_arrive.append(arr.text)



for i in range(0,len(first_arrive)):
    print(first_arrive[i])


def bus_1164_arr1():
    return first_arrive[0]

def bus_1164_arr2():
    return two_arrive[0]


def bus_2115_arr1():
    return first_arrive[1]

def bus_2115_arr2():
    return two_arrive[1]




