import streamlit as st
import pandas as pd

#configurações do streamlit para pagina ocupar a tela toda
st.set_page_config(
    layout="wide",
    page_title="spotify songs"

)

#leitura dos dados
df = pd.read_csv('01 Spotify.csv')

#setando index
df.set_index("Track", inplace=True)


artists = df["Artist"].value_counts().index #pega valores únicos da coluna Artist
artist = st.selectbox("Artista", artists)   #salva na variável um objeto selectbox('nome do select', dados da seleção)
df_filtered = df[df["Artist"] == artist]    #faz uma filtragem no df baseado na seleção do checkbox anterior


albuns = df_filtered["Album"].value_counts().index
album = st.selectbox("Album", albuns)

df_filtered2 = df[df["Album"] == album]
display = st.checkbox('Display')
if display:
    st.bar_chart(df_filtered2["Stream"])

st.bar_chart(df_filtered["Stream"])


display = st.checkbox('Exibir qtd de streams por musicas do artista')



