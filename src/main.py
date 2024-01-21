# Rodar o app: streamlit run app\main.py
# Acessar a aplicação no navegador: http://localhost:8501

# Importando as dependências
import yfinance as yf
import streamlit as st
import plotly.express as px

# Importando os módulos
from modulos.page import page
from modulos.style import css # Estilo
from modulos.data import dataFrame # Data frame
from modulos.graphic import line, bar # Gráficos
from modulos.right_bar import right_bar # Barra lateral esquerda

page()

st.markdown("<h1>Fechamento das ações 💹</h1>", unsafe_allow_html=True)
st.markdown("---")

ticker = st.text_input("Digite a sua ação", "Bbdc3") # ITUB4
empresa = yf.Ticker(f"{ticker}.SA") 

# Data frame
tickerDF = empresa.history(period="id", start="2020-01-01", end="2024-01-20")
# Filtrando dados para os anos de 2020 até 2024
tickerDF_filtered = tickerDF[(tickerDF.index.year >= 2020) & (tickerDF.index.year <= 2024)]
# Agrupando os dados por ano
tickerDF_grouped = tickerDF_filtered.groupby(tickerDF_filtered.index.year).sum()

col_empresa,col_preço = st.columns(2) # Colunas
with col_empresa:
    st.write(f"**Empresa:** {empresa.info['longName']}")  # Nome da empresa
with col_preço:
    st.write(f"**Preço Atual:** {empresa.info['currentPrice']}**BRL**")  # Valor da ação
    
st.write(f"**Mercado:** {empresa.info['industryDisp']}")  # Industria / Mercado

# Plotagem do data frame
with st.expander("Tabela"):
    st.markdown("<h2>Data Frame 📋</h2>", unsafe_allow_html=True)
    dataFrame(tickerDF_filtered)

st.markdown("---")
# Plotagem dos gráficos
tab1, tab2 = st.tabs(["Gráfico de Linha", "Gráfico Barras"])

with tab1:
    line(tickerDF) # Linha

with tab2:
    bar(tickerDF)  # Barra

# Gráfico de Pizza (Pie Chart)
def pie():
    colors = ['#004200', '#67a258', '#21187a', '#900000', '#ed3b20'] # Configurando as cores
    fig_pie = px.pie(tickerDF_grouped, values='Close',
                      color_discrete_sequence=colors,
                      title=f"O gráfico abaixo mostra os fechamentos anuais da empresa: {ticker}", # Descrição
                      names=tickerDF_grouped.index
                    )

    st.plotly_chart(fig_pie)

with st.expander("Fechamento Anual 💰"):
    pie()

right_bar() # Barra lateral
css() # Estilo do projeto