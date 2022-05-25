#importar librerias
import streamlit as st
import pickle
import pandas as pd
from PIL import Image
def main():
    #titulo
    st.title('prueba')
    #titulo de sidebar
    st.sidebar.header('Menu')

    #funcion para poner los parametrso en el sidebar
    def user_input_parameters():
        a = st.sidebar.slider('aux1', 0.0, 0.5, 1.0)
        b = st.sidebar.slider('aux2', 0.0, 0.5, 1.0)
        c = st.sidebar.slider('aux3', 0.0, 0.5, 1.0)
        d = st.sidebar.slider('aux4', 0.0, 0.5, 1.0)
        data = {'a': a,
                'b': b,
                'c': c,
                'd': d,
                }
        features = pd.DataFrame(data, index=[0])
        return features

    df = user_input_parameters()

    #escoger el modelo preferido
    option = ['si', 'también', 'a que va a ser que si...']
    model = st.sidebar.selectbox('tu eres tonto?', option)

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

    st.image(image, caption='Sunrise by the mountains')

if __name__ == '__main__':
    main()
    
