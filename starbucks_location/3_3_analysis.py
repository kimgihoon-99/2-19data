# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 04:24:08 2025

@author: tuesv
3-3 analysis.py
스타벅스 매장 수와 인구수 비교
"""

import pandas as pd
import folium
import json

# 서울시 시군별 통계테이터 불러오기
seoul_sgg_stat = pd.read_excel('./starbucks_location/files/seoul_sgg_stat.xlsx',
                               thousands= ',')

# 서울시 시군구 행정 경계 지도 파일
sgg_geojson_file_path = './starbucks_location/maps/seoul_sgg.geojson'
seoul_sgg_geo_2 = json.load(open(sgg_geojson_file_path, encoding='utf-8'))

# 서울시 시군구별 주민등록인구수 단계구분도 지도 시각화
starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                          tiles = 'CartoDB dark_matter',
                          zoom_start=11)


folium.Choropleth(geo_data=seoul_sgg_geo_2,
                  data=seoul_sgg_stat,
                  columns=['시군구명', '주민등록인구'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on='properties.SIG_KOR_NM').add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_cholopleth_pop.html')






# 서울시 시군구별 사업체수 단계구분도 지도 시각화
import pandas as pd
import folium
import json

seoul_sgg_stat = pd.read_excel('./starbucks_location/files/seoul_sgg_stat.xlsx',
                               thousands= ',')

sgg_geojson_file_path = './starbucks_location/maps/seoul_sgg.geojson'
seoul_sgg_geo_3 = json.load(open(sgg_geojson_file_path, encoding='utf-8'))

starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                          tiles = 'CartoDB dark_matter',
                          zoom_start=11)

folium.Choropleth(geo_data=seoul_sgg_geo_3,
                  data=seoul_sgg_stat,
                  columns=['시군구명', '사업체수_x'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on='properties.SIG_KOR_NM').add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_cholopleth_biz.html')


# 서울시 시군구별 종사자수 단계구분도 지도 시각화
import pandas as pd
import folium
import json

seoul_sgg_stat = pd.read_excel('./starbucks_location/files/seoul_sgg_stat.xlsx',
                               thousands= ',')

sgg_geojson_file_path = './starbucks_location/maps/seoul_sgg.geojson'
seoul_sgg_geo_4 = json.load(open(sgg_geojson_file_path, encoding='utf-8'))

starbucks_choropleth = folium.Map(location=[37.573050, 126.979189],
                          tiles = 'CartoDB dark_matter',
                          zoom_start=11)

folium.Choropleth(geo_data=seoul_sgg_geo_4,
                  data=seoul_sgg_stat,
                  columns=['시군구명', '종사자수_x'],
                  fill_color = 'YlGn',
                  fill_opacity=0.7,
                  line_opacity=0.5,
                  key_on='properties.SIG_KOR_NM').add_to(starbucks_choropleth)

starbucks_choropleth.save('starbucks_cholopleth_work.html')

# 인구 만 명당 스타벅스 매장 수 지도 시각화













































