import pandas as pd
import plotly.express as px

def df(filepath):
    # Carregar o arquivo CSV em um DataFrame
    return pd.read_csv(filepath)

def bairro_salario_medio(df):
    # Calcular a média dos salários por bairro
    bairro_salario_medio = df.groupby('Bairro')['Salario'].mean().reset_index()

    # Criar gráfico de linhas para mostrar a tendência de salário médio por bairro
    fig = px.line(
        bairro_salario_medio,
        x='Bairro',  # Eixo X: Bairro
        y='Salario',  # Eixo Y: Salário Médio
        title='Tendência de Salário Médio por Bairro',  # Título do gráfico
        labels={'Salario': 'Salário Médio'}  # Rótulo do eixo Y
    )

    # Ajustar o layout do gráfico
    fig.update_layout(xaxis_title='Bairro', yaxis_title='Salário Médio')

    # Exibir o gráfico
    fig.show()

def distribuicao_salario(df):
    # Criar um histograma para mostrar a distribuição dos salários dos clientes
    fig = px.histogram(
        df,
        x='Salario',  # Eixo X: Salário
        title='Distribuição dos Salários dos Clientes',  # Título do gráfico
        labels={'Salario': 'Salário'},  # Rótulo do eixo X
        nbins=20  # Número de bins no histograma
    )

    # Ajustar o layout do gráfico
    fig.update_layout(xaxis_title='Salário', yaxis_title='Número de Clientes')

    # Exibir o gráfico
    fig.show()

def dispersao_salario_idade(df):
    # Criar um gráfico de dispersão 2D para mostrar a relação entre salário e idade por bairro
    fig = px.scatter(
        df,
        x="Salario",  # Eixo X: Salário
        y="Idade",  # Eixo Y: Idade
        color="Bairro",  # Cor dos pontos por bairro
        title="Distribuição de Salário e Idade por Bairro",  # Título do gráfico
        labels={"Salario": "Salário (R$)", "Idade": "Idade (anos)", "Bairro": "Bairro"},  # Rótulos dos eixos
        hover_data=["Cliente", "Endereco"]  # Dados adicionais ao passar o mouse
    )

    # Exibir o gráfico
    fig.show()

def dispersao_salario_idade_3d(df):
    # Criar um gráfico de dispersão 3D para mostrar a distribuição de salário e idade por bairro
    fig = px.scatter_3d(
        df,
        x='Salario',  # Eixo X: Salário
        y='Idade',  # Eixo Y: Idade
        z='Bairro',  # Eixo Z: Bairro
        color='Bairro',  # Cor dos pontos por bairro
        title='Distribuição de Salário e Idade por Bairro',  # Título do gráfico
        labels={'Salario': 'Salário', 'Idade': 'Idade'}  # Rótulos dos eixos
    )

    # Ajustar o layout do gráfico
    fig.update_layout(scene=dict(
        xaxis_title='Salário',
        yaxis_title='Idade',
        zaxis_title='Bairro'
    ))

    # Exibir o gráfico
    fig.show()

def bairro_raca_count(df):
    # Agrupar por bairro e raça e contar o número de registros
    bairro_raca_count = df.groupby(['Bairro', 'Raca']).size().reset_index(name='Quantidade')

    # Criar gráfico de barras empilhadas para mostrar a distribuição de raças de cachorro por bairro
    fig = px.bar(
        bairro_raca_count,
        x='Bairro',  # Eixo X: Bairro
        y='Quantidade',  # Eixo Y: Quantidade de cachorros
        color='Raca',  # Cor das barras por raça
        title='Distribuição de Raças de Cachorro por Bairro',  # Título do gráfico
        labels={'Quantidade': 'Número de Cachorros'},  # Rótulo do eixo Y
        barmode='stack'  # Modo empilhado das barras
    )

    # Ajustar o layout do gráfico
    fig.update_layout(xaxis_title='Bairro', yaxis_title='Quantidade')

    # Exibir o gráfico
    fig.show()

def bairro_profissao_count(df):
    # Agrupar por bairro e profissão e contar o número de registros
    bairro_profissao_count = df.groupby(['Bairro', 'Profissao']).size().reset_index(name='Quantidade')

    # Criar gráfico de barras empilhadas para mostrar a distribuição de profissões por bairro
    fig = px.bar(
        bairro_profissao_count,
        x='Bairro',  # Eixo X: Bairro
        y='Quantidade',  # Eixo Y: Quantidade de profissões
        color='Profissao',  # Cor das barras por profissão
        title='Distribuição de Profissões por Bairro',  # Título do gráfico
        labels={'Quantidade': 'Número de Profissões'},  # Rótulo do eixo Y
        barmode='stack'  # Modo empilhado das barras
    )

    # Ajustar o layout do gráfico
    fig.update_layout(xaxis_title='Bairro', yaxis_title='Quantidade')

    # Exibir o gráfico
    fig.show()

def bairro_counts(df):
    # Agrupar por bairro para contar o número de clientes
    bairro_counts = df.groupby("Bairro").size().reset_index(name='Contagem')

    # Merge para adicionar a contagem de clientes ao DataFrame original
    df = df.merge(bairro_counts, on="Bairro")

    # Criar gráfico de bolha para mostrar a distribuição de salário e idade com a quantidade de clientes por bairro
    fig = px.scatter(
        df,
        x="Salario",  # Eixo X: Salário
        y="Idade",  # Eixo Y: Idade
        size="Contagem",  # Tamanho das bolhas baseado na contagem de clientes
        color="Bairro",  # Cor das bolhas por bairro
        title="Distribuição de Salário e Idade com Quantidade de Clientes por Bairro",  # Título do gráfico
        labels={"Salario": "Salário (R$)", "Idade": "Idade (anos)", "Contagem": "Número de Clientes", "Bairro": "Bairro"},  # Rótulos dos eixos
        hover_data=["Cliente", "Endereco"]  # Dados adicionais ao passar o mouse
    )

    # Exibir o gráfico
    fig.show()

def main(filepath):

    # Função principal para carregar dados e gerar gráficos
    frame = df(filepath)
    bairro_salario_medio(frame)
    distribuicao_salario(frame)
    dispersao_salario_idade_3d(frame)
    dispersao_salario_idade(frame)
    bairro_raca_count(frame)
    bairro_profissao_count(frame)
    bairro_counts(frame)

if __name__ == '__main__':
    # Executar a função principal com o caminho para o arquivo CSV
    main(filepath="")
