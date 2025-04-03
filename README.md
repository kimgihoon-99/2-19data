메가커피 메뉴 크롤링 및 시각화 분석
이 프로젝트는 국내 커피 프랜차이즈 '메가커피(Mega Coffee)' 웹사이트에서 메뉴 데이터를 수집하고, 이를 다양한 방식으로 시각화한 Python 기반 프로젝트입니다.

📌 프로젝트 개요
🕸 웹 크롤링: 메가커피 공식 홈페이지에서 메뉴 이름, 가격, 카테고리 등의 정보를 자동 수집

📊 시각화 분석:

평균 가격/카테고리별 비교

버블 차트, 지도 시각화, 컬러맵 등 다양한 시각적 표현

💡 HTML로 시각화 결과 저장: 브라우저에서 바로 결과 확인 가능

🧪 분석 예시
카테고리별 메뉴 수 및 평균 가격 시각화

인기 카테고리별 버블차트 (starbucks_bubble.html)

사업체 수/인구 수 기반 지역별 색상지도 (cholopleth)

매장 분포 지도 시각화 (starbucks_map.html)

💡 활용 기술
크롤링: requests, BeautifulSoup, selenium

데이터 처리: pandas

시각화: plotly, folium, matplotlib
