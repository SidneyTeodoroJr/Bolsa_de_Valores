import streamlit as st

def right_bar():
    # Foto pessal
    st.sidebar.image("https://avatars.githubusercontent.com/u/91035485?v=4")

    st.sidebar.markdown("<h1>Sidney T. A. Junior</h1>", unsafe_allow_html=True)
    st.sidebar.markdown("<h2>Desenvolvedor de automação e aplicações web</h2>", unsafe_allow_html=True)
    st.sidebar.markdown('<p>Contribuições são bem-vindas!<br/> Se quiser melhorar o projeto, adicionar novas funcionalidades ou corrigir problemas, fique à vontade. <br/><a href="https://sidney-personal-portifolio.netlify.app/"><img src="https://img.shields.io/badge/Portfolio-FF5722?style=for-the-badge&logo=todoist&logoColor=white" style="border-radius: 30px; width: 35%; margin-top: 10%;" /></a></p>', unsafe_allow_html=True)

# Dividindo em duas colunas
    with st.sidebar:
        col1,col2 = st.columns(2)
        with col1: # Primeira coluna
            # linkedin
            st.markdown('<a href="https://www.linkedin.com/in/sidney-teodoro-4a4a8119b?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2FevuTOiSSJS2hWGCZgtZiQ%3D%3D"><img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px;" /></a>', unsafe_allow_html=True)

        with col2: # Segunda coluna
            # Instagram
            st.markdown('<a href="https://www.instagram.com/sidneyteodoroaraujo"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" style="border-radius: 30px;"/></a>', unsafe_allow_html=True)
