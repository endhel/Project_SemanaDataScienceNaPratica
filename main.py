import streamlit as st
import pandas as pd

df = pd.read_csv('criminalidade_sp_2.csv')

st.title('Criminalidade em São Paulo')
st.markdown(
    '''
    A **criminalidade** é um problema recorrente no Brasil.
    Buscamos sempre formas de diminuir esses índices e usando técnicas de Ciência de Dados conseguimos entender melhor
    o que está acontecendo e gerar insights que direcionam ações capazes de diminuir índices de criminalidade.
   '''
)

st.sidebar.info(f'Foram carregadas {df.shape[0]} linhas.')

if st.sidebar.checkbox('Ver dados de entrada'):
    st.header('Dados de Entrada')
    st.write(df)

df.time = pd.to_datetime(df.time)
ano_selecionado = st.sidebar.slider('Selecione um ano', 2010, 2018, 2015)
df_selected = df[df.time.dt.year == ano_selecionado]

st.subheader('Mapa de Criminalidade')
st.map(df_selected)
