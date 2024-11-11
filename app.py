# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('linear_regression_model (1).pkl') 

# 2. 모델 설명
 st.title('하루 게시물 수에 따른 팔로워수 증가 예측 모델')

# 3. 데이터시각화
with col2:
      st.subheader('데이터 시각화1')
      st.image('시각화1 (1).png' )   # 이미지 불러오기
with col3:
      st.subheader('데이터 시각화2')
      st.image('시각화2.png')    # 이미지 불러오기
 with col4:
      st.subheader('데이터 시각화3')
      st.image('시각화3.png')    # 이미지 불러오기

# 4. 모델 활용

# 사용자의 입력을 받아서 a에 저장하기(초기값은 0)
a = st.number_input('하루 게시물수를 입력하세요 (게시물 수는 0이상이여야 합니다)', value= 0)  

# 버튼 생성 및 동작
if st.button('팔로워가 몇명이나 증가할까?'):
       if a > 0:
              st.write('예측할수 없습니다. 현생을 사시는걸 축하드려요^^')
       elif a < 0:
              st.write('0 이상의 값을 입력해 주세요')
       else:
              st.write('예측할수 없습니다. 현생을 사시는걸 축하드려요^^')
