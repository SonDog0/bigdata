
# forge 데이터셋 - KNN 분류 : 0 ,1 등으로 분류
import mglearn
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor

# X , y = mglearn.datasets.make_forge()
# mglearn.discrete_scatter(X[:,0] , X[:,1] , y )
# plt.show()
#
# # wave 데이터셋 - KNN 회귀 : 실제값을 예측
# # 즉 이웃을 사용해서 그것이 평균의 예측값이 됨
#
# X , y = mglearn.datasets.make_wave(n_samples = 40)
# plt.plot(X,y,'o')
# plt.show()
#
# mglearn.plots.plot_knn_classification(n_neighbors= 3)
# plt.show()
#
#
# mglearn.plots.plot_knn_regression(n_neighbors= 3)
# plt.show()

# 회귀분석 간단 예제

X = [[1],[2],[3],[4],[5]]
y = [0,0,1,1,1.5]

rgr = KNeighborsRegressor(n_neighbors =3 )
rgr.fit(X,y)

print('훈련 측정값 R ^2' ,rgr.score(X,y))

# 생성된 회귀모형을 검증
print(rgr.predict([[1.6] , [1.7], [2.3], [3.5]]))


