import streamlit as st
import pandas as pd

# Link da planilha original (mantendo o formato simples que ele conseguiu ler)
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    return pd.read_csv(url)

try:
    df = load_data()
    
    # Ele enxergou a coluna 'Mês de Referência'. Vamos usar ela!
    st.write("Colunas encontradas:", df.columns.tolist())
    
    # Se você quiser filtrar por mês, usamos a coluna que ele já vê
    mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês de Referência'].unique())
    
    st.write(f"Você selecionou o mês: {mes_escolhido}")
    st.success("O app está lendo a sua planilha agora!")

except Exception as e:
    st.error(f"Erro: {e}")
