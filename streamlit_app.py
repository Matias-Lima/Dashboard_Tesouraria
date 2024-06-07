import streamlit as st
import pandas as pd
import numpy as np
import streamlit_option_menu
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import altair as alt



# Funções ------------------------

@st.cache_data
def load_data():
    # Carregue seus dados aqui, substitua 'seu_dataframe.csv' pelo nome do arquivo CSV que contém seus dados
    data = pd.read_excel("Dados.xlsx")
    data = data.drop(['BASE PERSON ID', 'SERVER ID', 'Nome dizimista e ofertante'], axis=1)

    return data

# Função para calcular o saldo final por departamento
def calcular_saldo_final(data):

    saldo_final_por_departamento = data.groupby('Nome do Departamento')['Valor'].sum()
    return saldo_final_por_departamento

# Função para plotar o gráfico
def plotar_grafico(saldo_final_por_departamento):
    
    st.bar_chart(saldo_final_por_departamento)
    st.pyplot()

def plot_soma_acumulada(data, departamento):
    # Selecionando os dados para o departamento especificado
    dados_do_departamento = data.loc[data['Nome do Departamento'] == departamento]
    # Garantir que a coluna 'Data do Movimento' é do tipo datetime
    dados_do_departamento['Data do Evento'] = pd.to_datetime(dados_do_departamento['Data do Evento'], errors='coerce')
    # Configurando a data como índice e ordenando
    dados_do_departamento = dados_do_departamento.set_index('Data do Evento')
# Filtrar dados a partir de 2021
    dados_do_departamento = dados_do_departamento[dados_do_departamento.index >= '2021-01-01']

    dados_do_departamento = dados_do_departamento.sort_index()

    # Calculando a soma acumulada do valor ao longo do tempo
    valores = dados_do_departamento['Valor'].cumsum()

    st.line_chart(valores)



# --------------------------------


# Defina o layout da barra lateral para começar na parte superior
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Igreja Adventista de Pinheiros", page_icon=":church:")

imagem_url = "Igreja_Adventista_Dia.svg.png"
# Adicione a imagem à barra lateral
st.sidebar.image(imagem_url, caption='Igreja Adventista de Pinheiros')

with st.sidebar:
  selected = option_menu(
    menu_title = "Menu",
    options = ["Home","Departamentos","Fluxos","Informações"],
    icons = ["house","book","envelope", "list-task", 'gear'],
    menu_icon = "intersect",
    default_index = 0,
    styles={ 
         "container": {"margin":"0px"},
          "nav-link": {"font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "rgba(255, 255, 255, 0.5)"},     
      }
  )


if selected == "Home":
  st.title(f"Informações Gerais Sobre a situação financeira de Pinheiros")
  st.markdown('**A prática da prestação de contas de forma recorrente e sistemática fortalece nosso compromisso com a transparência, além de permitir que nossa comunidade se mantenha informadae engajada nos desafios de nosso planejamento financeiro.**')
  st.divider()
  #Use Cases
  with st.container():
        
       st.subheader('*7me App da Igreja Adventista*')
       chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["col1", "col2", "col3"])
       st.line_chart(
   chart_data, x="col1", y=["col2", "col3"], color=["#FF0000", "#0000FF"]  # Optional
        )  

  st.divider()

  #Tutorial Video
  st.header('Tutorial Video')
  video_file = open('Similo_Tutorial3_compressed.mp4', 'rb')
  video_bytes = video_file.read()
  st.video(video_bytes)


# ------------- Departamentos ---------------

if selected == "Departamentos":
  st.title(f"Informações sobre a situação dos departamentos")
  st.divider()
  #Use Cases
  with st.container():
      
      col1, col2 = st.columns([4, 1])
      with col1:
            data = load_data()
            departamento = st.selectbox('Selecione o Departamento', data['Nome do Departamento'].unique())
            plot_soma_acumulada(data, departamento)

      with col2:
          st.subheader('*Informações *')

  st.divider()

  with st.container():
        
       st.subheader('Histograma')
       data = load_data()
       # Calculando o saldo final por departamento
       saldo_final_por_departamento = calcular_saldo_final(data)
        # Plotando o gráfico
       plotar_grafico(saldo_final_por_departamento)

  st.divider()

# -------------------------- Informações --------------------------------------

if selected == "Informações":
  st.title(f"Informações Gerais e Avisos")
  st.subheader('*Nova ferramenta do ministério da Tesouraria.*')
  
  st.divider()

  #Use Cases
  with st.container():
      
      col1, col2 = st.columns([2, 5])
      with col1:
          st.header('Como usar o 7me App')
          st.markdown(
              """
              - _Baixe e instale o aplicativo:_
              - _Crie uma conta:_
              - _Explore recursos adicionais: ...._
              - _Faça um pedido de Oração_
              """
              )
      with col2:
          st.image('7me.png', caption='Aplicativo 7me da igreja Adventista')

  st.divider()
  #Tutorial Video
  st.header('Tutorial Video')
  video_file = open('7me um aplicativo completo.mp4', 'rb')
  video_bytes = video_file.read()
  st.video(video_bytes)


  st.divider()
  st.header('Nossa Equipe')

  col1, col2, col3, col4 = st.columns([3, 3, 3, 3])
  with col1:
    st.image('tesouraria_diretor.jpeg', caption='Rodrigo Abreu: Tesoureiro')
  with col2:
    st.image('rose.jpg', caption='Rosiele: Assistente de Tesouraria')
  with col3:
    st.image('trevisan.png', caption='Trevisan: Assistente de Tesouraria')
  with col4:
    st.image('ana_paula.png', caption='Ana Paula: Assistente de Tesouraria')
  