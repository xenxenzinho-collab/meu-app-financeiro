import streamlit as st
import pandas as pd
import urllib.parse

# ID da planilha
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'

# Definimos que vamos ler a aba 'Gastos'
nome_da_aba = 'Gastos' 
aba_encoded = urllib.parse.quote(nome_da_aba)
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={aba_encoded}'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    return pd.read_csv(url)

try:
    df = load_data()
    
    # Exibe as colunas para conferência
    st.write("Colunas encontradas:", df.columns.tolist())
    
    # Filtro de mês (a coluna na aba Gastos chama-se 'Mês')
    mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês'].unique())

    # Soma os valores da coluna 'Valor'
    gastos_do_mes = df[df['Mês'] == mes_escolhido]
    total = gastos_do_mes['Valor'].sum()

    st.metric(label=f"Total de Gastos - {mes_escolhido}", value=f"R$ {total:,.2f}")
    st.table(gastos_do_mes[['Gastos Cartão', 'Estabelecimento', 'Valor']])

except Exception as e:
    st.error(f"Erro: {e}")
