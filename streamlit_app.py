import streamlit as st
import pandas as pd

# Link da sua planilha (este link já aponta para a aba certa)
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vShEgA7UKO1hJ3-DeZgcsMMgEQEJhzgO-D6YGaKyj3o_wZPmYykeR0dgxhwvNbwKFJbTq6N3Ll3QrqO/pub?gid=1165293891&single=true&output=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    # Carrega os dados da aba que está no link
    df = pd.read_csv(url)
    # Remove espaços extras dos nomes das colunas
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    
    # Verifica se a coluna 'Mes' existe
    if 'Mes' in df.columns:
        # Seleciona o mês
        mes_escolhido = st.selectbox("Selecione o Mês:", df['Mes'].dropna().unique())
        
        # Filtra os dados
        gastos_filtrados = df[df['Mes'] == mes_escolhido]
        
        # Exibe a tabela
        st.write(f"### Gastos de {mes_escolhido}")
        st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])
        
        # Converte 'Valor' para número e soma
        gastos_filtrados['Valor'] = pd.to_numeric(gastos_filtrados['Valor'], errors='coerce')
        total = gastos_filtrados['Valor'].sum()
        
        st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
    else:
        st.error("Não encontrei a coluna 'Mes'. Verifique se o cabeçalho está exatamente assim.")
        st.write("Colunas encontradas:", df.columns.tolist())

except Exception as e:
    st.error(f"Erro ao carregar: {e}")
