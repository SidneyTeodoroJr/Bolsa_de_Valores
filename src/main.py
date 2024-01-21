# Rodar o app: streamlit run app\main.py
# Acessar a aplicação no navegador: http://localhost:8501

# Importando as dependências
import yfinance as yf
import streamlit as st
import plotly.express as px

# Importando os módulos
from modulos.style import css # Estilo
from modulos.data import dataFame # Data frame
from modulos.graphic import line, bar # Gráficos
from modulos.right_bar import right_bar # Barra lateral esquerda

st.markdown("<h1>Fechamento das ações 💹</h1>", unsafe_allow_html=True)
st.markdown("---")

ticker = st.text_input("Digite a sua ação", "POMO4")
empresa = yf.Ticker(f"{ticker}.SA") 

# Data frame
tickerDF = empresa.history(period="id", start="2020-01-01", end="2024-01-20")

# Filtrando dados para os anos de 2020 até 2024
tickerDF_filtered = tickerDF[(tickerDF.index.year >= 2020) & (tickerDF.index.year <= 2024)]

# Agrupando os dados por ano
tickerDF_grouped = tickerDF_filtered.groupby(tickerDF_filtered.index.year).sum()

# Dividindo as colunas
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    st.write(f"**Empresa:** {empresa.info['longName']}")  # Nome da empresa
with col2:
    st.write(f"**Mercado:** {empresa.info['industryDisp']}")  # Industria / Mercado
with col3:
    st.write(f"**Preço Atual:** {empresa.info['currentPrice']}**BRL**")  # Valor da ação


# Plotagem do data frame
st.markdown("---")
st.markdown("<h2>Data Frame 📋</h2>", unsafe_allow_html=True)
dataFame(tickerDF_filtered)

st.markdown("---")
# Plotagem dos gráficos
line(tickerDF) # Linha
bar(tickerDF)  # Barra

# Gráfico de Pizza (Pie Chart)
def pie():
    st.markdown("<h2>Fechamento Anual </h2>", unsafe_allow_html=True)

    st.markdown(f'<p>O gráfico abaixo mostra os fechamentos anuais da empresa: <span class="verde">{ticker}</span></p>', unsafe_allow_html=True)

    # Configurando as cores do gráfico
    colors = ['#004200', '#67a258', '#21187a', '#900000', '#ed3b20']
    fig_pie = px.pie(tickerDF_grouped, values='Close', names=tickerDF_grouped.index, color_discrete_sequence=colors)
    st.plotly_chart(fig_pie)

pie()

# Barra lateral
right_bar()

# Estilo do projeto
css()