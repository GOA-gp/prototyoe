import streamlit as st
import joblib

# 1. 기계학습 모델 파일 로드
model = joblib.load('linear_regression_model (1).pkl') 

# 2. 모델 설명
st.title('하루 게시물 수에 따른 팔로워수 증가 예측 모델')

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
        st.error('게시물 수는 0 이상이어야 합니다.')
    else:
        try:
            # 모델을 사용하여 예측
            prediction = model.predict([[a]])  # 입력값을 2차원 배열로 변환
            st.success(f'예상 팔로워 수 증가: {prediction[0]:,.0f}명')
        except Exception as e:
            # 예측 중 에러 발생 시 처리
            st.error('예측할 수 없습니다.')
            st.write('하루 게시물 수와 팔로워 증가수는 상관관계가 없답니다^^')
           



