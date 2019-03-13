# 파이썬에서 이미지 다루기
# opencv ( computer vision library)
# 이미지 데이터 관련 작업(이미지 선명화, 픽셀화 등등)을
# 기계적으로 수행할 수 있도록 도와주는 라이브러리
# 주로 이미지를 통한 얼굴인식, 장애물 인식, 객체 인식에 사용
# 딥러닝을 통한 이미지 인식에 널리 사용되고 있음
# 심지어 영상처리를 이용한 객체 인식(차량 번호판)에도 사용 됨


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
from pandasql import sqldf
import cv2
from PIL import Image     # Pillow 를 설치하면 됨

pd.set_option('display.expand_frame_repr', False)



# # 그레이 스케일greyscale로 이미지 출력하기
# # imread(그림파일, 읽어올방식)
# img = cv2.imread('c:/Java/data/IU4.jpg',
#                  cv2.IMREAD_GRAYSCALE)  # 흑백으로 읽어옴
#
# print(type(img))  # 이미지 객체의 유형 확인
# print(img)   # 이미지의 픽셀값 확인
# print(img.shape)   # 이미지의 크기 확인
# print(img[0,0])   # 이미지의 첫번째 픽셀값 확인( 0 ~ 255 )
#
#
# plt.imshow(img, cmap='gray')
# plt.axis('off')
# plt.show()
#
#
# # 칼라패턴rgb로 이미지 출력하기
# img = cv2.imread('c:/Java/data/IU4.jpg',
#                  cv2.IMREAD_COLOR)  # 칼라로 읽어옮
#
# print(img)         # IMREAD_COLOR로 이미지를 읽으면
#                     # 기본적으로 BGR 형식으로 픽셀 저장
# print(img[0,0])
#
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# plt.imshow(img)
# plt.axis('off')
# plt.show()


# 파이썬에서 이미지 다루기 2 - PIL
# 또 다른 이미지 관련 패키지로 Pillow가 있는데
# 여러가지 이미지 형식을 다룰 수 있게 해주고
# 이미지 내부 데이터 접근, 다양한 이미지 처리 기능
# (이미지 생성, 변환, 필터링)을 지원하고 있음

# 이미지 픽셀화 예제
img = Image.open('c:/Java/data/tower.jpg')
pixels = img.getdata()

# print(img.size)
# print(np.array(pixels))     # 픽셀을 numpy 배열로 변환


plt.imshow(img)
plt.axis('off')
# plt.show()




# 그레이 스케일로 변환
gsimg = img.convert('L')
pixels = gsimg.getdata()

# gsimg.show()

print(np.array(pixels))



# 이미지를 31x31 크기의 배열로 만든 후 출력
# 이미지 흑백 전환은 average hash 기법을 사용함
# 즉, 각 픽셀값들의 평균값을 기준으로
# 평균보다 작으면 0, 평균보다 크면 1로 설정

imgsize = 31
gsimg = gsimg.resize((imgsize, imgsize), Image.ANTIALIAS)
#                   => 이미지 크기 재조정 및 부드럽게 처리

pixel_data = gsimg.getdata()
pixel_data = np.array(pixel_data)
pixels = pixel_data.reshape(imgsize, imgsize)
# 픽셀크기를 31x31 크기로 재조정

plt.imshow(pixels)
plt.axis('off')
plt.show()


avg = pixels.mean()        # 픽셀들의 평균값 계산
diff = 1*(pixels > avg)    # 평균보다 크면 1 아니면 0

print(diff)