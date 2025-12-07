import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="Dashboard de Anúncios de Carros", layout="wide")

CAR_DATA_PATH = 'vehicles.csv'
try:
    car_data = pd.read_csv(CAR_DATA_PATH)
except FileNotFoundError:
    st.error(
        f"Erro: O arquivo de dados '{CAR_DATA_PATH}' não foi encontrado. Verifique se ele está na pasta raiz do projeto.")
    st.stop()

st.title('🚗 Análise de Anúncios de Vendas de Carros')
st.header('Visualizações Exploratórias com Streamlit e Plotly')
st.markdown(
    "Selecione os gráficos abaixo para visualizar as distribuições e relações nos dados.")

st.subheader('Selecione os Gráficos a Gerar:')
build_histogram = st.checkbox('Mostrar Histograma de Preços')
build_scatter = st.checkbox(
    'Mostrar Gráfico de Dispersão (Preço vs. Quilometragem)')

if build_histogram:
    st.subheader('Distribuição de Preços dos Veículos')
    st.write(
        'Este histograma mostra a frequência de anúncios em diferentes faixas de preço.')

    fig_hist = px.histogram(
        car_data,
        x="price",
        nbins=100,
        title='Histograma de Preços'
    )

    st.plotly_chart(fig_hist, use_container_width=True)

if build_scatter:
    st.subheader('Relação entre Preço e Quilometragem')
    st.write('Este gráfico de dispersão mostra como o preço varia em função da quilometragem (odometer).')

    fig_scatter = px.scatter(
        car_data,
        x="odometer",
        y="price",
        color="condition",
        hover_data=['model', 'year'],
        title='Preço (Y) versus Quilometragem (X)'
    )

    st.plotly_chart(fig_scatter, use_container_width=True)

st.caption("Fim do Dashboard. Desenvolvido com Streamlit.")
