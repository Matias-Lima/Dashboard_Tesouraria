import streamlit as st
import pandas as pd
import numpy as np
import streamlit_option_menu
from streamlit_option_menu import option_menu
import matplotlib.pyplot as plt
import altair as alt



# Funções ------------------------
def load_data():
    # Carregue seus dados aqui, substitua 'seu_dataframe.csv' pelo nome do arquivo CSV que contém seus dados
    data = pd.read_excel("Dados.xlsx")
    data = data.drop(['BASE PERSON ID', 'SERVER ID', 'Nome dizimista e ofertante'], axis=1)

    return data

# Função para calcular o saldo final por departamento
def calcular_saldo_final(data):

    saldo_final = data.groupby('Nome do Departamento')['Valor'].sum()

    return saldo_final

def plot_soma_acumulada(data, departamento):
    
    ministerio = pd.DataFrame(data)
    # Selecionando os dados para o departamento especificado
    ministerio = data.loc[data['Nome do Departamento'] == departamento]

    ministerio = pd.DataFrame(ministerio)

    ministerio.index = pd.to_datetime(ministerio['Data do Movimento'], format='%d/%m/%Y')

    ministerio = ministerio[ministerio.index.year > 2022]


    # Ordenando o DataFrame pelo índice (data)
    ministerio = ministerio.sort_index()

    # Calculando a soma acumulada do valor ao longo do tempo
    ministerio["soma_acumulada"] = ministerio['Valor'].cumsum()

    return ministerio["soma_acumulada"]
   


# --------------------------------


# Defina o layout da barra lateral para começar na parte superior
st.set_page_config(layout="wide", initial_sidebar_state="expanded", page_title="Igreja Adventista de Pinheiros", page_icon=":church:")

imagem_url = "fotos/Igreja_Adventista_Dia.svg.png"
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
   chart_data, x="col1", y=["col2", "col3"]  # Optional
        )  

  st.divider()

  #Tutorial Video
  st.header('Distribuição dos recursos')
  st.image('fotos/recursos.jpg', caption='Como os recursos são distribuídos', use_column_width=True)



# ------------- Departamentos ---------------

if selected == "Departamentos":
  st.title(f"Informações sobre a situação dos departamentos")
  st.divider()
  #Use Cases
  with st.container():
      
      col1, col2 = st.columns([10, 3])

      with col1:
            data = load_data()
            departamento = st.selectbox('Selecione o Departamento', data['Nome do Departamento'].unique())
            dados = plot_soma_acumulada(data, departamento)

            st.line_chart(dados)

      with col2:
          st.subheader('Informações')
      

  st.divider()

  with st.container():
        
       st.subheader('Histograma')
       data = load_data()
       # Calculando o saldo final por departamento
       saldo_final_por_departamento = calcular_saldo_final(data)

        # Transpondo o DataFrame
       saldo_final_por_departamento_df = saldo_final_por_departamento.to_frame(name='Saldo Final')

        # Ordenando por Saldo Final em ordem decrescente
       saldo_final_por_departamento = saldo_final_por_departamento_df.sort_values(by='Saldo Final', ascending=False)

       st.bar_chart(saldo_final_por_departamento, use_container_width=True)
       saldo_final_por_departamento

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
          st.image('fotos/_7me.png', caption='Aplicativo 7me da igreja Adventista')

  st.divider()
  #Tutorial Video
  st.header('Tutorial Video')
  video_file = open('7me um aplicativo completo.mp4', 'rb')
  video_bytes = video_file.read()
  st.video(video_bytes)


  st.divider()
  st.header('Nossa Equipe')

  # Definindo as colunas para 4 membros por linha
  col1, col2, col3, col4 = st.columns(4)

  # Adicionando imagens e legendas para cada membro da equipe
  with col1:
      st.image('fotos/tesouraria_diretor.jpeg', caption='Rodrigo Abreu: Tesoureiro')

  with col2:
      st.image('fotos/rose.jpg', caption='Rosiele: Assistente de Tesouraria')

  with col3:
      st.image('fotos/trevisan.png', caption='Trevisan: Assistente de Tesouraria')

  with col4:
      st.image('fotos/ana_paula.png', caption='Ana Paula: Assistente de Tesouraria')

  # Adicionando mais 4 membros da equipe
  col5, col6, col7, col8 = st.columns(4)

  with col5:
      st.image('fotos/carol.png', caption='Nome: Cargo')

  with col6:
      st.image('fotos/Paulo.png', caption='Nome: Cargo')

  with col7:
      st.image('fotos/lucas.png', caption='Nome: Cargo')

  with col8:
      st.image('fotos/carol_2.png', caption='Nome: Cargo')

  # Adicionando mais 4 membros da equipe
  col9, col10, col11, col12 = st.columns(4)

  with col9:
      st.image('fotos/calebe.png', caption='Nome: Cargo')

  with col10:
      st.image('fotos/felipe.png', caption='Nome: Cargo')

  with col11:
      st.image('fotos/marcio.png', caption='Nome: Cargo')

  with col12:
      st.image('fotos/ana_paula.png', caption='Nome: Cargo')