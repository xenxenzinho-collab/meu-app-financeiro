import streamlit as st
import pandas as pd

# Link da planilha
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    # Lê a planilha, tratando a linha 0 como cabeçalho
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip() # Remove espaços extras dos nomes
    # Remove linhas que possam ter repetido o cabeçalho
    df = df[df['Data'] != 'Data'] 
    # Converte 'Valor' para número forçadamente, ignorando erros
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    return df

try:
    df = load_data()
    
    # Filtro de Mês
    mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês'].dropna().unique())
    
    # Filtra os dados
    gastos_filtrados = df[df['Mês'] == mes_escolhido]
    
    # Exibe a tabela
    st.write(f"Gastos de {mes_escolhido}:")
    st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])
    
    # Soma o total (com segurança)
    total = gastos_filtrados['Valor'].sum()
    st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")

except Exception as e:
    st.error(f"Erro: {e}")
    st.write("Verifica se na tua planilha a coluna de valores se chama 'Valor' e a de mês 'Mês'.")
