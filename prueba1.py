#importar librerias
import streamlit as st
from streamlit_option_menu import option_menu
#import pickle
import pandas as pd
from PIL import Image
def main():
    #titulo
    st.title('prueba')
    #titulo de sidebar
#    st.sidebar.header('Menu')

    # 1. as sidebar menu
    with st.sidebar:
        selected = option_menu("Main Menu", ["Home", 'Settings'], 
            icons=['house', 'gear'], menu_icon="cast", default_index=1)
        selected

    # 2. horizontal menu
    selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal")
    selected2

    # 3. CSS style definitions
    selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    
#    option = ['si', 'también', 'a que va a ser que si...']
#    model = st.sidebar.selectbox('tu eres tonto?', option)

    # st.subheader('User Input Parameters')
    # st.subheader(model)
    # st.write(df)

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
    
