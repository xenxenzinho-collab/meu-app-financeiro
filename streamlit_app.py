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

# Remove espaços extras dos nomes das colunas para evitar erros
df.columns = df.columns.str.strip()

st.write("Colunas encontradas agora:", df.columns.tolist())

# Filtro
if 'Mês de Referência' in df.columns:
    mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês de Referência'].unique())
    
    # Exibe os gastos
    gastos_filtrados = df[df['Mês de Referência'] == mes_escolhido]
    
    # Verifica quais colunas existem para exibir na tabela
    colunas_para_exibir = [col for col in ['Data', 'Estabelecimento', 'Valor'] if col in df.columns]
    
    if colunas_para_exibir:
        st.table(gastos_filtrados[colunas_para_exibir])
    else:
        st.warning("As colunas 'Data', 'Estabelecimento' ou 'Valor' não foram encontradas na planilha.")
        
    # Soma o total se a coluna Valor existir
    if 'Valor' in df.columns:
        total = gastos_filtrados['Valor'].sum()
        st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
else:
    st.error("A coluna 'Mês de Referência' não foi encontrada.")
