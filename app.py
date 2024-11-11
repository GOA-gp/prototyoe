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
a = st.number_input('하루 게시물수를 입력하세요 (게시물 수는 0이상이여야 합니다)', value=0)  

# 버튼 생성 및 동작
if st.button('팔로워가 몇명이나 증가할까?'):
    if a < 0:
        st.write('0 이상의 값을 입력해 주세요')
    else:
        # 예측 모델을 통해 결과를 얻기
        predicted_followers = model.predict([[a]])
        st.write(f'예상되는 팔로워 증가 수는 {predicted_followers[0]}명 입니다.')


