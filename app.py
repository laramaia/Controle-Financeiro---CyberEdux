import streamlit as st
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt

if "rendimentos" not in st.session_state:
    st.session_state["rendimentos"] = []
if "despesas" not in st.session_state:
    st.session_state["despesas"] = []
if "impostos" not in st.session_state:
    st.session_state["impostos"] = []

def formatar_data_brasil(data):
    meses = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
    return f"{data.day:02d}/{data.month:02d}/{data.year} ({meses[data.month - 1]})"


def formatar_valor_brasil(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def cadastro_rendimentos():
    st.subheader("Cadastro de Rendimentos")
    data = st.date_input("Data do Rendimento", value=datetime.now(), format="DD/MM/YYYY")
    data_formatada = formatar_data_brasil(data)
    valor = st.number_input("Valor do Rendimento", min_value=0.0)
    if valor == 0.0:
        st.error("O campo 'Valor' não pode estar vazio.")
    valor_formatado = formatar_valor_brasil(valor)
    st.text(f"Valor formatado: {valor_formatado}")
    origem = st.text_input("Origem do Rendimento")
    if not origem.strip():
        st.error("O campo 'Origem' não pode estar vazio.")
    if st.button("Adicionar Rendimento"):
        novo_rendimento = {"data": data_formatada, "valor": valor, "origem": origem}
        st.session_state["rendimentos"].append(novo_rendimento)
        st.success(f'Rendimento de {valor_formatado} adicionado com sucesso para {data_formatada}')


def cadastro_despesas():
    st.subheader("Cadastro de Despesas")
    data = st.date_input("Data da Despesa", value=datetime.now(), format="DD/MM/YYYY")
    data_formatada = formatar_data_brasil(data)
    valor = st.number_input("Valor da Despesa", min_value=0.0)
    if valor == 0.0:
        st.error("O campo 'Valor' não pode estar vazio.")
    valor_formatado = formatar_valor_brasil(valor)
    st.text(f"Valor formatado: {valor_formatado}")
    origem = st.text_input("Categoria da Despesa")
    if not origem.strip():
        st.error("O campo 'Origem' não pode estar vazio.")
    if st.button("Adicionar Despesa"):
        nova_despesa = {"data": data_formatada, "valor": valor, "origem": origem}
        st.session_state["despesas"].append(nova_despesa)
        st.success(f'Despesa de {valor_formatado} adicionada com sucesso para {data_formatada}')


def cadastro_impostos():
    st.subheader("Cadastro de Impostos")
    nome = st.text_input("Nome do imposto")
    if not nome.strip():
        st.error("O campo 'Nome' não pode estar vazio.")
    data = st.date_input("Data de pagamento", value=datetime.now(), format="DD/MM/YYYY")
    data_formatada = formatar_data_brasil(data)
    valor = st.number_input("Valor do Imposto", min_value=0.0)
    if valor == 0.0:
        st.error("O campo 'Valor' não pode estar vazio.")
    valor_formatado = formatar_valor_brasil(valor)
    st.text(f"Valor formatado: {valor_formatado}")
    vencimento = st.text_input("Data de vencimento do imposto")
    if not vencimento.strip():
        st.error("O campo 'Vencimento' não pode estar vazio.")
    if st.button("Adicionar Rendimento"):
        novo_imposto = {"nome": nome, "data": data_formatada, "valor": valor, "vencimento": vencimento, }
        st.session_state["impostos"].append(novo_imposto)
        st.success(f'Imposto de {valor_formatado} adicionado com sucesso para {data_formatada}')


def visualizar_ou_excluir_rendimentos():
    st.subheader("Seus Rendimentos")
    for i, rendimento in enumerate(st.session_state["rendimentos"]):
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
        with col1:
            st.write(f"**Valor:** {rendimento['valor']}")
        with col2:
            st.write(f"**Data:** {rendimento['data']}")
        with col3:
            st.write(f"**Origem:** {rendimento['origem']}")
        with col4:
            if st.button("Excluir", key=f'delete_rend_{i}'):
                st.session_state["rendimentos"].pop(i)
                #st.experimental_rerun()


def visualizar_ou_excluir_despesas():
    st.subheader("Suas Despesas")
    for i, despesa in enumerate(st.session_state["despesas"]):
        col1, col2, col3, col4 = st.columns([2, 2, 2, 1])
        with col1:
            st.write(f"**Valor:** {despesa['valor']}")
        with col2:
            st.write(f"**Data:** {despesa['data']}")
        with col3:
            st.write(f"**Origem:** {despesa['origem']}")
        with col4:
            if st.button("Excluir", key=f'delete_desp_{i}'):
                st.session_state["despesas"].pop(i)
                #st.experimental_rerun()


def visualizar_ou_excluir_impostos():
    st.subheader("Seus Impostos")
    for i, imposto in enumerate(st.session_state["impostos"]):
        col1, col2, col3, col4, col5 = st.columns([2, 2, 2, 2, 1])
        with col1:
            st.write(f"**Valor:** {imposto['valor']}")
        with col2:
            st.write(f"**Data:** {imposto['data']}")
        with col3:
            st.write(f"**Vencimento:** {imposto['vencimento']}")
        with col4:
            st.write(f"**Nome:** {imposto['nome']}")
        with col5:
            if st.button("Excluir", key=f'delete_rend_{i}'):
                st.session_state["impostos"].pop(i)
                #st.experimental_rerun()


def visualizar_gráfico_rendimento():
    st.subheader("Rendimentos semanais")
    if not st.session_state["rendimentos"]:
        st.warning("Nenhum rendimento cadastrado")
        return 0.0
    
    rendimentos = st.session_state["rendimentos"]
    # Ordena rendimentos pela data
    rendimentos.sort(key=lambda rendimento: rendimento["data"])

    semanas = {}
    primeira_data = rendimentos[0]["data"]

    for rendimento in rendimentos:
        data = rendimento["data"]
        # Retorna semana ao subtrair data atual da mais antiga e dividir por 7 (semana inicia com 1)
        semana = ((data - primeira_data).days // 7) + 1 
        # Se semana atual não estiver no dicionário, inicializa chave com valor 0
        if semana not in semanas:
            semanas[semana] = 0
        semanas[semana] += rendimento["valor"]  

    for semana in sorted(semanas.keys()):
        # Mostra respectivamente a chave (índice) da semana e o valor do dicionário
        plt.bar(f"Semana {semana}", semanas[semana]) 

    plt.title("Rendimentos semanais")
    plt.xlabel("Semanas")
    plt.ylabel("Valores (R$)")

    st.pyplot(plt)
    

st.title("Você no Comando - Controle Financeiro para Autônomos")
menu = st.sidebar.selectbox("Selecione uma opção", ["Cadastrar Rendimento", "Cadastrar Despesa", "Cadastrar Imposto", "Visualizar Dados"])

if menu == "Cadastrar Rendimento":
    cadastro_rendimentos()
elif menu == "Cadastrar Despesa":
    cadastro_despesas()
elif menu == "Cadastrar Imposto":
    cadastro_impostos()
elif menu == "Visualizar Dados":
    visualizar_ou_excluir_rendimentos()
    visualizar_ou_excluir_despesas()
    visualizar_ou_excluir_impostos()
    visualizar_gráfico_rendimento()
