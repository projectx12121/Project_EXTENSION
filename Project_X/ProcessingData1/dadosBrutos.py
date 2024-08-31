# Importa a biblioteca Pandas para manipulacao de dados
import pandas as pd

def df(filepath):

    # Le o arquivo CSV para um DataFrame
    return pd.read_csv(filepath)

def sistema(df):

    # Exibe informacoes do DataFrame, como contagem de entradas, tipos de dados e memoria ocupada
    print("\033[00;32m\n# Informacoes de sistema \033[00;00m")
    print(df.info())

def descricao(df):

    # Exibe o DataFrame original
    print(f"\033[00;32m\n# DataFrame - Dados originais \033[00;00m\n {df}")  # Mostra o conteudo completo do DataFrame

    # Gerando estatisticas descritivas apenas para colunas numericas
    descricao = df.describe()

    # Exibindo estatisticas descritivas para colunas numericas
    print("\033[00;32m\n# Estatisticas Descritivas - Colunas Numericas \033[00;00m")

    for coluna in descricao.columns:

        print(f"\n---------- {coluna} ----------\n")
        print(f"# Total de valores (count): {descricao[coluna]['count']:.0f}")
        print(f"# Media (mean): {descricao[coluna]['mean']:.2f}")
        print(f"# Desvio padrao (std): {descricao[coluna]['std']:.2f}")
        print(f"# 1º Quartil (25%): {descricao[coluna]['25%']:.2f}")
        print(f"# 3º Quartil (75%): {descricao[coluna]['75%']:.2f}")
        print(f"# Mediana (50%): {descricao[coluna]['50%']:.2f}")
        print(f"# Valor maximo (max): {descricao[coluna]['max']:.2f}")
        print(f"# Valor minimo (min): {descricao[coluna]['min']:.2f}")

    # Gerando estatisticas descritivas para colunas categoricas (nao numericas)
    descricao_categoricas = df.describe(include=['object'])

    # Exibindo estatisticas descritivas para colunas categoricas
    if not descricao_categoricas.empty:

        print("\033[00;32m\n# Estatisticas Descritivas para Colunas Categoricas \033[00;00m")

        for coluna in descricao_categoricas.columns:

            print(f"\n---------- {coluna} ----------\n")
            print(f"# Total de valores (count): {descricao_categoricas[coluna]['count']:.0f}")
            print(f"# Valor mais frequente (top): {descricao_categoricas[coluna]['top']}")
            print(f"# Frequencia do valor mais frequente (freq): {descricao_categoricas[coluna]['freq']:.0f}\n")

def main(filepath):

    print(f"\n\033[01;32m{'=-=' * 10} INFORMACOES DADOS BRUTOS {'=-=' * 10}\033[01;00m")
    sistema(df(filepath))                # Exibe informacoes sobre o DataFrame original
    relatorio = descricao(df(filepath))              # Exibe as estatisticas descritivas do DataFrame

# Verifica se o script esta sendo executado diretamente e, em caso afirmativo, chama a funcao principal
if __name__ == '__main__':
    main(filepath="")  # Executa a funcao principal com o caminho do arquivo CSV
