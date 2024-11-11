# 분류 모델 웹앱 만들기

import streamlit as st

# 1. 기계학습 모델 파일 로드
import joblib
model = joblib.load('logistic_regression_model.pkl') 

# 2. 모델 설명
 st.title('하루 게시물 수에 따른 팔로워수 증가 예측 모델')

# 3. 데이터시각화
with col2:
      st.subheader('')
      st.image('' )   # 이미지 불러오기
with col3:
      st.subheader('')
      st.image('')    # 이미지 불러오기

# 4. 모델 활용

