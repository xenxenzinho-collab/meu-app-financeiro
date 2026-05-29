import streamlit as st
import pandas as pd

# Link da planilha
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

# Filtro
mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês de Referência'].unique())

# Exibe os gastos do mês selecionado
gastos_filtrados = df[df['Mês de Referência'] == mes_escolhido]
st.write(f"Gastos de {mes_escolhido}:")
st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])

# Soma o total
total = gastos_filtrados['Valor'].sum()
st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
