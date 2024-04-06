<h1 align="center">Fechamento de Ações</h1>
</br>

<div align="center">
<img src="https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/image.png" alt="Digital Whiteboard">
</div>
</br>
</br>


## Visão Geral
<p>
 Este projeto é uma aplicação web desenvolvida em Python utilizando o framework Streamlit. A aplicação permite que os usuários visualizem o fechamento de ações de uma empresa específica, analisem variações de preço ao longo do tempo e examinem a distribuição dos dividendos.
<p/>

### Tecnologias usada:
[Python](https://docs.python.org/3/)<br/>
﻿[yfinance](https://pypi.org/project/yfinance/)<br/>
[streamlit](https://docs.streamlit.io/)<br/>
[plotly](https://plotly.com/python/)<br/>

## Estrutura do Projeto
<p>
O projeto está dividido em vários scripts para melhor organização e modularidade.
<p/>
<br/>

1. [main.py](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/main.py): O ponto de entrada da aplicação que importa e utiliza os módulos e scripts necessários.
2. [page.py](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/modulos/page.py): Contém a função `page()` que personaliza o layout da página usando `st.set_page_config`.
3. [style.py](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/modulos/style.py): Define estilos e formatação CSS para melhorar a estética da aplicação.
4. [data.py](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/modulos/data.py): Contém a função `dataFrame()` que exibe um DataFrame filtrado com base nos anos selecionados.
5. [graphic](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/modulos/graphic.py).py: Contém funções para gerar gráficos interativos, como `line()` e `bar()`.
6. [right_bar](https://github.com/SidneyTeodoroJr/Bolsa_de_Valores/blob/main/src/modulos/right_bar.py).py: Define uma barra lateral direita com informações pessoais e links sociais do desenvolvedor.

## Instruções de Execução
1. Instale as dependências necessárias usando:
    ```shell
    pip install -r requirements.txt
2. Execute o aplicativo Streamlit com o comando streamlit:
   ```shell
   streamlit run src/main.py
3. Acesse a aplicação no navegador.
   
## Personalizações
1. O título da página, o ícone e a disposição inicial da barra lateral podem ser ajustados no arquivo `page.py`.
2. Estilos visuais podem ser customizados no arquivo `style.py`.

### Referência:
   [YouTube ](https://youtu.be/u7Whb4QbXJs)
<br/>

## Contribuições
<p>
Contribuições são bem-vindas! Se quiser melhorar o projeto, adicionar novas funcionalidades ou corrigir problemas, fique à vontade.
</p>
<hr>
</br>

<div align="center">
<a href="https://www.facebook.com/profile.php?id=100091086461235"><img src="https://img.shields.io/badge/-Facebook-%230077B5?style=for-the-badge&logo=facebook&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
<a href="https://www.instagram.com/sidneyteodoroaraujo" target="_blank"><img src="https://img.shields.io/badge/-Instagram-%23E4405F?style=for-the-badge&logo=instagram&logoColor=white" /></a>
<a href="https://www.linkedin.com/in/sidney-teodoro-4a4a8119b?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3B%2FevuTOiSSJS2hWGCZgtZiQ%3D%3D" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" style="border-radius: 30px" target="_blank" /></a>
</div>
