# 대여소를 클러스터로 분류하고, folium 라이브러리를 사용하여 지도에 표시

import pandas as pd
pd.set_option('display.expand_frame_repr', False)

# 데이터 생성
l_office_info = pd.read_csv('l_office_info.csv')

# print(l_office_info.head())
#    l_office_no l_office_name gu_name  r_holder_no  x_value  y_value
# 0         2315   봉은사역 5번출구 옆     강남구           10  37.5142  127.061
# 1         2365       K+ 타워 앞     강남구           15  37.5233  127.038
# 2         2313        금원빌딩 앞     강남구           10  37.5251  127.052
# 3         2347       두산건설 본사     강남구           15  37.5186  127.035
# 4         2362   신사동 가로수길 입구     강남구           10  37.5176  127.022


id_clu = pd.read_csv('id_clu.csv')
# print(id_clu.head())
#    l_office_no  avg_dist  count cluster
# 0         1001      4333  14314       f
# 1         1002      4990   7309       h
# 2         1003      3881   6924       e
# 3         1004      5307   7688       h
# 4         1006      4415   6046       e

l_office_info_fin = pd.merge(l_office_info, id_clu.iloc[:,[0,3]] , on = 'l_office_no')

# df1
# print(id_clu.iloc[:,[0,3]].head())
#   l_office_no cluster
# 0        1001       f
# 1        1002       h
# 2        1003       e
# 3        1004       h
# 4        1006       e

# df2
# print(l_office_info)
#    l_office_no l_office_name gu_name  r_holder_no  x_value  y_value
# 0         2315   봉은사역 5번출구 옆     강남구           10  37.5142  127.061
# 1         2365       K+ 타워 앞     강남구           15  37.5233  127.038
# 2         2313        금원빌딩 앞     강남구           10  37.5251  127.052
# 3         2347       두산건설 본사     강남구           15  37.5186  127.035
# 4         2362   신사동 가로수길 입구     강남구           10  37.5176  127.022

# df1 left join df2 on l_office_no

# print(l_office_info_fin.head())
#   l_office_no l_office_name gu_name  r_holder_no  x_value  y_value cluster
# 0        2315   봉은사역 5번출구 옆     강남구           10  37.5142  127.061       i
# 1        2365       K+ 타워 앞     강남구           15  37.5233  127.038       h
# 2        2313        금원빌딩 앞     강남구           10  37.5251  127.052       h
# 3        2347       두산건설 본사     강남구           15  37.5186  127.035       g
# 4        2362   신사동 가로수길 입구     강남구           10  37.5176  127.022       h


# 색상 테이블 선언
color_df = pd.DataFrame({'cluster':['a','b','c','d','e','f','g','h','i'],
                         'color':['#fc0000','#fc8f01','#f7fc00','#045e7a','#32baff','#17047a','#004ffc','#a800fc','#fc00ef']})


l_office_info_fin = pd.merge(l_office_info_fin, color_df , on= 'cluster')
# print(l_office_info_fin.head())
#    l_office_no             l_office_name gu_name  r_holder_no  x_value  y_value cluster    color
# 0         2315               봉은사역 5번출구 옆     강남구           10  37.5142  127.061       i  #fc00ef
# 1         2302  교보타워 버스정류장(신논현역 3번출구 후면)     강남구           10  37.5056  127.024       i  #fc00ef
# 2         2307             압구정 한양 3차 아파트     강남구           10  37.5286  127.039       i  #fc00ef
# 3         2340        삼호물산버스정류장(23370) 옆     강남구           15  37.4775  127.045       i  #fc00ef
# 4         2355            삼성역 5~6번 출구 사이     강남구           20  37.5091  127.062       i  #fc00ef



import folium

# Map
# Parameters:
# location (tuple or list, default None) – Latitude and Longitude of Map (Northing, Easting).
# width (pixel int or percentage string (default: '100%')) – Width of the map.
# height (pixel int or percentage string (default: '100%')) – Height of the map.
# tiles (str, default 'OpenStreetMap') – Map tileset to use. Can choose from a list of built-in tiles, pass a custom URL or pass None to create a map without tiles.
# API_key (str, default None) – API key for Cloudmade or Mapbox tiles.
# min_zoom (int, default 0) – Minimum allowed zoom level for the tile layer that is created.
# max_zoom (int, default 18) – Maximum allowed zoom level for the tile layer that is created.
# max_native_zoom (int, default None) – The highest zoom level at which the tile server can provide tiles. If provided you can zoom in past this level. Else tiles will turn grey.
# zoom_start (int, default 10) – Initial zoom level for the map.
# attr (string, default None) – Map tile attribution; only required if passing custom tile URL.
# detect_retina (bool, default False) – If true and user is on a retina display, it will request four tiles of half the specified size and a bigger zoom level in place of one to utilize the high resolution.
# crs (str, default 'EPSG3857') – Defines coordinate reference systems for projecting geographical points into pixel (screen) coordinates and back. You can use Leaflet’s values : * EPSG3857 : The most common CRS for online maps, used by almost all free and commercial tile providers. Uses Spherical Mercator projection. Set in by default in Map’s crs option. * EPSG4326 : A common CRS among GIS enthusiasts. Uses simple Equirectangular projection. * EPSG3395 : Rarely used by some commercial tile providers. Uses Elliptical Mercator projection. * Simple : A simple CRS that maps longitude and latitude into x and y directly. May be used for maps of flat surfaces (e.g. game maps). Note that the y axis should still be inverted (going from bottom to top).
# control_scale (bool, default False) – Whether to add a control scale on the map.
# prefer_canvas (bool, default False) – Forces Leaflet to use the Canvas back-end (if available) for vector layers instead of SVG. This can increase performance considerably in some cases (e.g. many thousands of circle markers on the map).
# no_touch (bool, default False) – Forces Leaflet to not use touch events even if it detects them.
# disable_3d (bool, default False) – Forces Leaflet to not use hardware-accelerated CSS 3D transforms for positioning (which may cause glitches in some rare environments) even if they’re supported.
# zoom_control (bool, default True) – Display zoom controls on the map.
# Returns:
# Return type:
# Folium Map Object


# 지도 설정
map = folium.Map(location=[l_office_info_fin['x_value'].mean(), l_office_info_fin['y_value'].mean()], zoom_start=12, tiles='OpenStreetMap')

# map = folium.Map(location=[l_office_info_temp['x_value'].mean(), l_office_info_temp['y_value'].mean()], zoom_start=12, tiles='Stamen Terrain')
# map = folium.Map(location=[l_office_info_temp['x_value'].mean(), l_office_info_temp['y_value'].mean()], zoom_start=12, tiles='Stamen Toner')



for n in l_office_info_fin.index:
    popup_name = l_office_info_fin['gu_name'][n] + ' - ' + l_office_info_fin['l_office_name'][n]

    # 지도 내용 설정
    # CircleMarker
    # Parameters:
    # locations (list of points (latitude, longitude)) – Latitude and Longitude of line (Northing, Easting)
    # popup (string or folium.Popup, default None) – Input text or visualization for object displayed when clicking.
    # radius (float) – Radius of the circle, in meters.

    folium.CircleMarker(
        location=[l_office_info_fin['x_value'][n], l_office_info_fin['y_value'][n]],
        radius=4,
        popup=popup_name,
        color=l_office_info_fin['color'][n]
    ).add_to(map)

map.save('foilum_cluster.html')

