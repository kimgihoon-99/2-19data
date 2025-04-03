# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 16:56:56 2025

@author: Admin
"""

# 데이터 모으기 
from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()
url = 'https://www.mega-mgccoffee.com/store/find/'
driver.get(url)

seoul_btn = 'body > div.wrap > div.cont_wrap.find_wrap > div > div.cont_box.find01 > div.map_search_wrap > div > div.cont_text_wrap.map_search_tab_wrap > div > ul > li:nth-child(2)'
driver.find_element('css selector', seoul_btn).click()

all_btn = '#store_area_search_list > li:nth-child(1)'

driver.find_element('css selector', all_btn).click()

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

mgc_coffee_soup_list = soup.select('#store_area_search_list_result')
print(len(mgc_coffee_soup_list))


mgc_coffee_soup_list[0]

mgc_coffee_store = mgc_coffee_soup_list[0]

# report 파일 정리

import pandas as pd
sgg_pop_df = pd.read_csv('./starbucks_location/files/report.txt', sep= '\t', header=2)

columns = {
    '기간': 'GIGAN',
    '자치구': 'JACHIGU',
    '계': 'GYE_1',
    '계.1': 'GYE_2',
    '계.2': 'GYE_3',
    '남자': 'NAMJA_1',
    '남자.1': 'NAMJA_2',
    '남자.2': 'NAMJA_3',
    '여자': 'YEOJA_1',
    '여자.1': 'YEOJA_2',
    '여자.2': 'YEOJA_3',
    '세대': 'SEDAE',
    '세대당인구': 'SEDAEDANGINGU',
    '65세이상고령자': 'N_65SEISANGGORYEONGJA'}

sgg_pop_df.rename(columns = columns, inplace = True)

sgg_pop_df.info()

condition = sgg_pop_df['JACHIGU'] != '합계'
sgg_pop_df_selected = sgg_pop_df[condition]

columns = ['NAMJA_1', 'YEOJA_2']
sgg_pop_df_final = sgg_pop_df_selected['columns']

sgg_pop_df_final.to_excel('./starbucks_location/files/report.xlsx', index=False)

sgg_biz_df = pd.read_csv('./starbucks_location/files/report2.txt', sep= '\t', header=2)

condition = sgg_biz_df['외국인'] == '국적'
sgg_biz_df_selected = sgg_biz_df[condition]

columns = ['자치구', '계', '사업체수']
sgg_biz_df_final = sgg_biz_df_selected[columns]
sgg_biz_df_final.columns = ['시군구명', '종사자수', '사업체수']

sgg_biz_df_final = sgg_biz_df_final.reset_index(drop=True)

sgg_biz_df_final.to_excel('./starbucks_location/files/mgc_sex.xlsx', index=False)


# 메가 커피 매장 데이터 불러오기

seoul_sgg = pd.read_excel('./starbucks_location/files/seoul_mgc_list.xlsx')

mgc_coffee = pd.read_excel('./starbucks_location/files/seoul_mgc_list.xlsx')


starbuck_sgg_count = mgc_coffee.pivot_table(index = '시군구명',
                                                 values='매장명',
                                                 aggfunc='count') \
                        .rename(columns={'매장명': '메가커피_매장수'})
































