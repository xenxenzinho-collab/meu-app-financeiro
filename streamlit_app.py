import streamlit as st
import pandas as pd

# Link da sua planilha (o mesmo que você me passou)
url = 'https://docs.google.com/spreadsheets/d/e/2PACX-1vShEgA7UKO1hJ3-DeZgcsMMgEQEJhzgO-D6YGaKyj3o_wZPmYykeR0dgxhwvNbwKFJbTq6N3Ll3QrqO/pub?gid=1165293891&single=true&output=csv'

st.title("💰 Controle Financeiro")

@st.cache_data
def load_data():
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    return df

try:
    df = load_data()
    
    # Verifica se a coluna 'Mes' existe
    if 'Mes' in df.columns:
        # Pega os meses únicos e remove os que estiverem vazios (NaN)
        meses_unicos = df['Mes'].dropna().unique()
        
        if len(meses_unicos) > 0:
            mes_escolhido = st.selectbox("Selecione o Mês:", meses_unicos)
            
            # Filtra os dados
            gastos_filtrados = df[df['Mes'] == mes_escolhido]
            
            st.write(f"### Gastos de {mes_escolhido}")
            st.table(gastos_filtrados[['Data', 'Estabelecimento', 'Valor']])
            
            # Converte Valor para numérico e soma
            gastos_filtrados['Valor'] = pd.to_numeric(gastos_filtrados['Valor'], errors='coerce')
            total = gastos_filtrados['Valor'].sum()
            st.metric(label="Total do Mês", value=f"R$ {total:,.2f}")
        else:
            st.warning("A coluna 'Mes' está vazia na sua planilha. Preencha os meses nas linhas!")
    else:
        st.error(f"Coluna 'Mes' não encontrada. Colunas atuais: {df.columns.tolist()}")

except Exception as e:
    st.error(f"Erro ao carregar: {e}")
