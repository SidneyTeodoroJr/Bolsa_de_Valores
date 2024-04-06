import streamlit as st

# Estilo do projeto
def css():
    st.markdown("""
                <style>
                @import url('https://fonts.googleapis.com/css2?family=Open+Sans:ital,wght@0,700;1,300&family=Poppins:wght@200&family=Roboto+Serif:ital,opsz,wght@1,8..144,200&display=swap');

                body {
                    padding: 0;
                    margin: 0;
                    background-color: #eb4f4f;
                }
                /*Removendo o botão de menu padrão*/
                .stDeployButton {
                    visibility: hidden;
                } 
                /*Estilizando os títulos e texto*/
                h1 {
                    font-size: 3em;
                    font-family: 'Open Sans', sans-serif;
                }
                h2 {
                    font-size: 2em;
                    font-family: 'Poppins', sans-serif;
                    margin-bottom: 0.5em;
                }
                p {
                    text-align: center;
                    font-size: 1.1em;
                    font-family: 'Roboto Serif', serif;
                }
                #link {
                    color: #a0a3a1;
                }
                h1, h2 {
                    text-align: center;
                }
                /*Imagem da sidebar*/
                img {
                    border-radius: 50%;
                    box-shadow: rgb(38, 57, 77) 0px 20px 30px -10px;
                } 
                #docs {
                    border-radius: 5%;
                    box-shadow: none;
                    width: 70%;
                }      
                </style>
    """, unsafe_allow_html=True)