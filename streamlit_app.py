import streamlit as st
import pandas as pd

# Link da sua planilha publicada (CSV)
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vShEgA7UKO1hJ3-DeZgcsMMgEQEJhzgO-D6YGaKyj3o_wZPmYykeR0dgxhwvNbwKFJbTq6N3Ll3QrqO/pub?gid=1165293891&single=true&output=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    # Limpa possíveis espaços extras nos nomes das colunas
    df.columns = df.columns.str.strip()
    # Garante que a coluna Valor seja numérica
    df['Valor'] = pd.to_numeric(df['Valor'], errors='coerce')
    return df

try:
    df = load_data()
    
    # Filtro de Mês
    if 'Mes' in df.columns:
        mes_escolhido = st.selectbox("Selecione o Mês:", df['Mes'].dropna().unique())
        
        # Filtra e exibe os dados
        gastos_filtrados = df[df['Mes'] == mes_escolhido]
        st.write(f"### Gastos de {mes_escolhido}")
        st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])
        
        # Exibe o total
        total = gastos_filtrados['Valor'].sum()
        st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
    else:
        st.error("A coluna 'Mes' não foi encontrada na planilha. Verifique o cabeçalho.")

except Exception as e:
    st.error(f"Erro ao carregar: {e}")
