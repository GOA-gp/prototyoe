import streamlit as st
import joblib

# 1. 기계학습 모델 파일 로드
model = joblib.load('linear_regression_model (1).pkl') 

# 2. 모델 설명
st.title('하루 게시물 수에 따른 팔로워수 증가 예측 모델')
st.write('사용데이터: 1000건')
st.write('훈련데이터: 700건')
st.write('테스트데이터: 300건')
st.write('사용한기계학습모델: 선형회귀')
st.write('데이터 출처: kaggle')

# 3. 데이터 시각화
# 컬럼을 생성합니다.
col2, col3, col4 = st.columns(3)

with col2:
    st.subheader('데이터 시각화1')
    st.image('시각화1 (1).png')   # 이미지 불러오기
with col3:
    st.subheader('데이터 시각화2')
    st.image('시각화2.png')       # 이미지 불러오기
with col4:
    st.subheader('데이터 시각화3')
    st.image('시각화3.png')       # 이미지 불러오기
    
    
st.subheader('이 모델의 모델평가 정확도는 -0.00 입니다')

# 4. 모델 활용

# 사용자의 입력을 받아서 a에 저장하기 (초기값은 0)
a = st.number_input(
    '하루 게시물수를 입력하세요 (게시물 수는 0이상이여야 합니다)', 
    value=0, 
    key='post_input'  # 고유 키를 설정하여 중복 방지
)  

# 버튼 생성 및 동작
if st.button('팔로워가 몇명이나 증가할까?'):
    if a < 0:
        st.error('게시물 수는 0 이상의 정수여야 합니다.')
    else:
        try:
            # 모델을 사용하여 예측
            prediction = model.predict([[a]])  # 입력값을 2차원 배열로 변환
            st.success(f'예상 팔로워 수 증가: {prediction[0]:,.0f}명')
        except Exception as e:
            # 예측 중 에러 발생 시 처리
            st.error('예측할 수 없습니다.')
            st.write('개인마다 올리는 게시물의 종류와 질이 다르고 게시물에 노출되는 사람들도 모두 다르다보니 단순한 게시물수만 가지고는 예측 할 수가 없습니다 ')




st.subheader('하루 게시물당 팔로워 수 증가 수 예측 모델이 유발할 수 있는 윤리적 문제')
st.subheader('표본편향')
st.write('특정 계층, 지역, 플랫폼 사용자들로만 구성된 데이터를 사용할 경우 예측 모델이 특정 그룹에만 적합하고, 다른 그룹에 대해 부정확하거나 차별적인 결과를 낼 가능성이 있습니다')

st.subheader('팔로워 수 예측에 대한 고정관념 강화')
st.write('특정 유형의 사용자(예: 콘텐츠 제작 빈도가 높은 사용자)가 항상 더 많은 팔로워를 가져야 한다는 편견을 강화할 수 있습니다.')
           



