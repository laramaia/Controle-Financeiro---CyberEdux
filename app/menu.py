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
if "metas" not in st.session_state:
    st.session_state["metas"] = []

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
        novo_rendimento = {"data": data, "valor": valor, "origem": origem}
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
    if st.button("Adicionar Imposto"):
        novo_imposto = {"nome": nome, "data": data_formatada, "valor": valor, "vencimento": vencimento, }
        st.session_state["impostos"].append(novo_imposto)
        st.success(f'Imposto de {valor_formatado} adicionado com sucesso para {data_formatada}')


def definir_meta():
    st.subheader("Defina uma meta de rendimento para melhor controle financeiro!")
    data_meta = st.date_input("Data da meta", value=datetime.now(), format="DD/MM/YYYY")
    data_meta_formatada = formatar_data_brasil(data_meta)
    valor_meta = st.number_input("Valor da Meta", min_value=0.0)
    if valor_meta == 0.0:
        st.error("O campo 'Valor' não pode estar vazio.")
    valor_meta_formatado = formatar_valor_brasil(valor_meta)
    st.text(f"Valor formatado: {valor_meta_formatado}")
    if st.button("Adicionar Meta"):
        nova_meta = {"data": data_meta_formatada, "valor": valor_meta_formatado}
        st.session_state["metas"].append(nova_meta)
        st.success(f'Meta adicionada com sucesso!')


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
            if st.button("Excluir", key=f'delete_impo_{i}'):
                st.session_state["impostos"].pop(i)
                #st.experimental_rerun()


def visualizar_grafico_rendimento():
    st.subheader("Rendimentos semanais")
    if not st.session_state["rendimentos"]:
        st.warning("Nenhum rendimento cadastrado")
        return 0.0
    
    rendimentos = st.session_state["rendimentos"]
    # Ordena rendimentos pela data
    rendimentos.sort(key=lambda rendimento: rendimento["data"])

    quinzenas = {}
    primeira_data = rendimentos[0]["data"]

    for rendimento in rendimentos:
        data = rendimento["data"]
        # Retorna quinzena ao subtrair data atual da mais antiga e dividir por 15 (inicia com 1)
        quinzena = ((data - primeira_data).days // 15) + 1 
        # Se quinzena atual não estiver no dicionário, inicializa chave com valor 0
        if quinzena not in quinzenas:
            quinzenas[quinzena] = 0
        quinzenas[quinzena] += rendimento["valor"]  
    
    # Organiza as quinzenas para exibir no gráfico
    for quinzena in sorted(quinzenas.keys()):
        # Mostra respectivamente a chave (índice) da quinzena e o valor do dicionário
        plt.bar(f"Quinzena {quinzena}", quinzenas[quinzena], color="blue") 
    
    # Adicionar títulos e rótulos ao gráfico
    plt.xlabel("Quinzenas")
    plt.ylabel("Valor (R$)")
    plt.title("Rendimentos Quinzenais")
    plt.xticks(rotation=45)
    
    st.pyplot(plt)
    plt.clf()


def visualizar_grafico_despesa():
    despesas = st.session_state["despesas"]

    if not despesas:
        st.warning("Nenhuma despesa cadastrada.")
        return 0.0
    
    # Dicionário que vai guardar a origem e seu respectivo gasto total
    analise_das_origens = {}

    for despesa in despesas:
        origem = despesa["origem"]
        valor = despesa["valor"]

        if origem in analise_das_origens:
            analise_das_origens[origem] += valor

        else:
            analise_das_origens[origem] = valor
    
    origens = list(analise_das_origens.keys())
    valores = list(analise_das_origens.values())

    plt.bar(origens, valores, color="blue")
    plt.title("Análise de despesas")
    plt.xlabel("Origem")
    plt.ylabel("Valor total (R$)")

    st.pyplot(plt)
    plt.clf()
    

def visualizar_grafico_meta_vs_rendimento():
    st.subheader("Comparação: Rendimento vs Meta por Quinzena")
    
    if not st.session_state["metas"]:
        st.warning("Nenhuma meta cadastrada.")
        return
    
    if not st.session_state["rendimentos"]:
        st.warning("Nenhum rendimento cadastrado.")
        return

    # Obter as metas
    metas = st.session_state["metas"]
    
    # Ordenar metas por data
    metas.sort(key=lambda meta: meta["data"])
    
    # Dicionário para armazenar os rendimentos por quinzena
    rendimentos_por_quinzena = {}
    for rendimento in st.session_state["rendimentos"]:
        data_rendimento = rendimento["data"]
        mes_ano = data_rendimento.strftime("%m/%Y")  # formato mês/ano
        if mes_ano in rendimentos_por_quinzena:
            rendimentos_por_quinzena[mes_ano] += rendimento["valor"]
        else:
            rendimentos_por_quinzena[mes_ano] = rendimento["valor"]
    
    # Dicionário para armazenar as metas por quinzena
    metas_por_quinzena = {}
    for meta in metas:
        data_meta = meta["data"]
        dia = data_meta.day
        mes_ano = data_meta.strftime("%m/%Y")
        if dia <= 15:
            quinzena = f"1ª Quinzena/{mes_ano}"
        else:
            quinzena = f"2ª Quinzena/{mes_ano}"
        
        metas_por_quinzena[quinzena] = meta["valor"]

    # Definir os meses que serão exibidos no gráfico
    quinzenas = sorted(set(rendimentos_por_quinzena.keys()).union(set(metas_por_quinzena.keys())))
    
    # Preparar as listas de valores para o gráfico
    valores_rendimento = [rendimentos_por_quinzena.get(quinzena, 0.0) for quinzena in quinzenas]
    valores_meta = [metas_por_quinzena.get(quinzena, 0.0) for quinzena in quinzenas]
    
    # Gerar o gráfico
    plt.figure(figsize=(10, 6))
    
    # Adicionar linha horizontal indicando que a meta foi atingida
    for i, quinzena in enumerate(quinzenas):
        plt.bar(quinzena, valores_meta[i], alpha=0.5, label="Meta" if i == 0 else "", color="blue")
        plt.bar(quinzena, valores_rendimento[i], alpha=0.7, label="Rendimento" if i == 0 else "", color="green")
        if valores_rendimento[i] >= valores_meta[i]:
            plt.text(quinzena, valores_rendimento[i] + 50, '✔️', ha='center', va='bottom', fontsize=12, color='green')
        else:
            plt.text(quinzena, valores_rendimento[i] + 50, '❌', ha='center', va='bottom', fontsize=12, color='red')
    
    plt.xlabel("Quinzenas")
    plt.ylabel("Valor (R$)")
    plt.title("Comparação entre Meta e Rendimento por Mês")
    plt.legend()

    st.pyplot(plt)


st.title("Você no Comando - Controle Financeiro para Autônomos")
menu = st.sidebar.selectbox("Selecione uma opção", ["Cadastrar Rendimento", "Cadastrar Despesa", "Cadastrar Imposto", "Cadastrar Meta", "Visualizar Dados", "Visualizar Gráficos"])

if menu == "Cadastrar Rendimento":
    cadastro_rendimentos()
elif menu == "Cadastrar Despesa":
    cadastro_despesas()
elif menu == "Cadastrar Imposto":
    cadastro_impostos()
elif menu == "Cadastrar Meta":
    definir_meta()
elif menu == "Visualizar Dados":
    visualizar_ou_excluir_rendimentos()
    visualizar_ou_excluir_despesas()
    visualizar_ou_excluir_impostos()
elif menu == "Visualizar Gráficos":
    visualizar_grafico_rendimento()
    visualizar_grafico_despesa()
    visualizar_grafico_meta_vs_rendimento()
