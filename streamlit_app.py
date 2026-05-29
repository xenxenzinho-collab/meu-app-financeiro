import streamlit as st
import pandas as pd

# Link da planilha
SHEET_ID = '10_Zgkv0QjBUTC_xvzy1JV4Y9rawbmdfhs-9kJBJBCg8'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip() # Remove espaços extras dos nomes
    return df

try:
    df = load_data()
    
    # Filtro
    if 'Mês de Referência' in df.columns:
        mes_escolhido = st.selectbox("Selecione o Mês:", df['Mês de Referência'].dropna().unique())
        
        # Filtra os dados
        gastos_filtrados = df[df['Mês de Referência'] == mes_escolhido]
        
        # Exibe a tabela
        st.write(f"Gastos de {mes_escolhido}:")
        st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])
        
        # Soma o total
        total = gastos_filtrados['Valor'].sum()
        st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
    else:
        st.error("A coluna 'Mês de Referência' não foi encontrada. Verifique o cabeçalho da aba 'Meses'.")

except Exception as e:
    st.error(f"Erro ao carregar: {e}")
