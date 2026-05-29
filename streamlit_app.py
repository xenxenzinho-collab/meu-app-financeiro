import streamlit as st
import pandas as pd

# Link da sua planilha
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    return pd.read_csv(url)

df = load_data()

# DICA: Vamos ver quais colunas existem na tua planilha para não errar
st.write("Colunas encontradas na planilha:", df.columns.tolist())

# Filtro por mês
mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês de Referência'].unique())

# Filtro e Soma (Certifica-te que o nome abaixo é igual a um dos nomes da lista que aparecerá acima)
gastos_do_mes = df[df['Mês de Referência'] == mes_escolhido]
total = gastos_do_mes['Valor'].sum()

# Exibição
st.metric(label=f"Total de Gastos - {mes_escolhido}", value=f"R$ {total:,.2f}")
st.table(gastos_do_mes)
