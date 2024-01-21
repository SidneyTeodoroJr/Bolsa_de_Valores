import streamlit as st

def dataFrame(tickerDF_filtered):
    # Adiciona um controle deslizante para os anos
    selected_years = st.slider("Filtrar os anos", min_value=int(tickerDF_filtered.index.year.min()), max_value=int(tickerDF_filtered.index.year.max()), value=(int(tickerDF_filtered.index.year.min()), int(tickerDF_filtered.index.year.max())))

    # Aplica o filtro de anos
    filtered_df = tickerDF_filtered[(tickerDF_filtered.index.year >= selected_years[0]) & (tickerDF_filtered.index.year <= selected_years[1])]

    # Plotando o data frame
    st.dataframe(filtered_df, height=400)