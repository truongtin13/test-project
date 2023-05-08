import streamlit as st
import numpy as np
from scipy.spatial.distance import cosine
from df_change import df_change

def nhandien():
  dfmid = df_change()
  tab1, tab2 = st.tabs(['Đăng ký khuôn mặt','Nhận diện khuôn mặt'])
    
  with tab1:
    name = st.text_input('Nhập đầy đủ họ tên:')
    known_image = st.camera_input("Chụp một bức ảnh để đăng ký:")
        
    if known_image is not None:
      if name == '':
        st.error('Xin hãy nhập họ tên.')
            
      else:
        st.success('Bạn đã đăng ký xong tên và khuôn mặt.')
        
        if 'names' not in st.session_state:
          st.session_state['names'] = []
        st.session_state['names'].append(name)
        names = st.session_state['names']
        st.write(names)
        
        if 'images' not in st.session_state:
          st.session_state['images'] = []
        st.session_state['images'].append(known_image)
        images = st.session_state['images']
        st.write(images)
        
  with tab2:
    unknown_image = st.camera_input("Chụp một bức ảnh để nhận diện:")
    
    
    
nhandien()
