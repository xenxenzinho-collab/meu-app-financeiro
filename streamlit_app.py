import streamlit as st
import pandas as pd

# Link da sua planilha
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    # Vamos tentar ler o CSV geral
    return pd.read_csv(url)

try:
    df = load_data()
    st.write("Colunas detectadas:", df.columns.tolist())
    st.write("Primeiras 5 linhas da planilha:")
    st.write(df.head())
    
    # Se você vir a coluna de Valor aqui, copia o nome EXATO que aparecer
    # e substitua onde está escrito 'Valor' abaixo:
    total = df['Valor'].sum() 
    st.write(f"Total: {total}")
    
except Exception as e:
    st.error(f"Erro ao ler os dados: {e}")
