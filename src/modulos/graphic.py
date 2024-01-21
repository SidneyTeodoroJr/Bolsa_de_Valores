import streamlit as st

import plotly.express as px

def line(tickerDF):
    st.markdown("<h2>Variação do Preço 📈</h2>", unsafe_allow_html=True)
    st.markdown("<p>Cada ponto no gráfico representa o preço de fechamento da ação em um determinado período, e a linha conecta esses pontos.</p>", unsafe_allow_html=True)
    
    # Configurando a cor do gráfico de linha
    fig = px.line(tickerDF, x=tickerDF.index, y='Close', line_shape="linear")
    fig.update_traces(line_color='#a10505')  # Escolha a cor desejada
    
    st.plotly_chart(fig, use_container_width=True)

def bar(tickerDF):
    st.markdown("<h2>Distribuição dos Dividendos 📊</h2>", unsafe_allow_html=True)
    st.markdown("<p'>Dividendos são pagamentos feitos por uma empresa aos seus acionistas como uma parcela dos lucros distribuídos.</p>", unsafe_allow_html=True)
    
    # Configurando a cor do gráfico de barras
    fig = px.bar(tickerDF, x=tickerDF.index, y='Dividends')
    fig.update_traces(marker_color='#048725')  # Escolha a cor desejada

    st.plotly_chart(fig, use_container_width=True)