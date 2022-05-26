#importar librerias
import streamlit as st
#rom streamlit_option_menu import option_menu
#import pickle
import pandas as pd
from PIL import Image
def main():
    #titulo
    st.title('prueba')
    #titulo de sidebar
    st.sidebar.header('Menu')
    
    option = ['si', 'también', 'a que va a ser que si...']
    model = st.sidebar.selectbox('tu eres tonto?', option)

    st.subheader('User Input Parameters')
    st.subheader(model)
    st.write(df)

    # if st.button('RUN'):
    #     if model == 'modelo a':
    #         st.success(classify(m_a(df)))
    #     elif model == 'modelo b':
    #         st.success(classify(m_b(df)))
    #     else:
    #         st.success(classify(m_c(df)))
    image = Image.open('mapa_medidas.png')
    st.image(image, caption='mapatas')
    
    imageq = Image.open('test.gif')
    st.image(imageq, caption='Medidas de locos')
      
if __name__ == '__main__':
    main()
    
