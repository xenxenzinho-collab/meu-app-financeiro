import streamlit as st
import pandas as pd

# Link da sua planilha publicada como CSV
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vShEgA7UKO1hJ3-DeZgcsMMgEQEJhzgO-D6YGaKyj3o_wZPmYykeR0dgxhwvNbwKFJbTq6N3Ll3QrqO/pub?gid=1165293891&single=true&output=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    # Remove espaços extras nos nomes das colunas e garante que tudo seja lido corretamente
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    
    # Verifica se a coluna 'Mes' existe na planilha
    if 'Mes' in df.columns:
        # Filtro de Mês
        meses_disponiveis = df['Mes'].dropna().unique()
        mes_escolhido = st.selectbox("Selecione o Mês:", meses_disponiveis)
        
        # Filtra os dados pelo mês escolhido
        gastos_filtrados = df[df['Mes'] == mes_escolhido]
        
        st.write(f"### Gastos de {mes_escolhido}")
        st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])
        
        # Converte 'Valor' para numérico para somar corretamente
        gastos_filtrados['Valor'] = pd.to_numeric(gastos_filtrados['Valor'], errors='coerce')
        total = gastos_filtrados['Valor'].sum()
        
        st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
    else:
        st.error("A coluna 'Mes' não foi encontrada. Verifique se o cabeçalho na planilha está escrito exatamente como 'Mes'.")
        st.write("Colunas detectadas:", df.columns.tolist())

except Exception as e:
    st.error(f"Erro ao carregar os dados: {e}")
