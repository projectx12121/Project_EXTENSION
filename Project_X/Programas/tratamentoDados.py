from ProcessingData1 import dadosBrutos
from ProcessingData1 import dadosTratados

def main():

    dados = "Database/dadosBrutos.csv"

    # Metodos
    dadosBrutos.main(dados)
    dadosTratados.main(dados)

if __name__ == '__main__':
    main()