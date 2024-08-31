import pandas as pd     # Importa a biblioteca Pandas para manipulação de dados.
import random           # Importa a biblioteca Random para gerar valores aleatórios.
import unidecode        # Importa Unidecode para remover acentuação dos caracteres.

# Dicionário de bairros e suas respectivas ruas no Rio de Janeiro.
bairros = {
    "Copacabana": ["Avenida Atlantica", "Rua Barata Ribeiro", "Rua Paula Freitas", "Rua Siqueira Campos"],
    "Ipanema": ["Avenida Vieira Souto", "Rua Visconde de Piraja", "Rua Garcia d'Avila", "Rua Farme de Amoedo"],
    "Leblon": ["Avenida Delfim Moreira", "Rua Bartolomeu Mitre", "Rua Ataulfo de Paiva", "Rua General Artigas"],
    "Botafogo": ["Praia de Botafogo", "Rua Sao Clemente", "Rua Voluntarios da Patria", "Rua Nelson Mandela"],
    "Tijuca": ["Rua Conde de Bonfim", "Rua Clarimundo de Melo", "Rua Jose Higino", "Rua Uruguai"],
    "Santa Teresa": ["Rua Almirante Alexandrino", "Rua Felipe Cardoso", "Rua Estrela", "Rua Monte Alegre"],
    "Lapa": ["Rua do Lavradio", "Rua dos Arcos", "Rua Mem de Sa", "Rua Visconde de Souza Franco"],
    "Centro": ["Avenida Rio Branco", "Rua Primeiro de Marco", "Rua do Ouvidor", "Rua da Assembleia"],
    "Flamengo": ["Rua Paissandu", "Rua Marques de Abrantes", "Rua Senador Dantas", "Rua do Catete"],
    "Gloria": ["Rua do Russel", "Rua da Gloria", "Rua do Ouvidor", "Rua Candido Mendes"],
    "Cascadura": ["Rua Casemiro de Abreu", "Rua Domingos Ferreira", "Rua Gal. Osorio", "Rua Plinio Casado"],
    "Barra da Tijuca": ["Avenida das Americas", "Rua do Anil", "Rua Ary Schiavo", "Avenida Ayrton Senna"],
    "Sao Conrado": ["Avenida Aquarela do Brasil", "Rua Professor Annes Dias", "Rua Miguel Lemos", "Rua Joao Lira"],
    "Recreio dos Bandeirantes": ["Avenida Glaucio Gil", "Rua do Dende", "Rua do Pepino", "Rua Joaquim Nabuco"],
    "Jardim Botanico": ["Rua Jardim Botanico", "Rua Pacheco Leao", "Rua Marquesa de Santos", "Rua Lopes Quintas"],
    "Vila Isabel": ["Rua 28 de Setembro", "Rua Heitor de Silva Costa", "Rua Buarque de Macedo", "Rua Joao Vicente"],
    "Catete": ["Rua do Catete", "Rua Silveira Martins", "Rua do Lavradio", "Rua Conde de Iraja"],
    "Rio Comprido": ["Rua do Bispo", "Rua General Glicerio", "Rua do Rio Comprido", "Rua Barao de Santa Marta"],
    "Humaita": ["Rua Humaita", "Rua Sao Clemente", "Rua Barao de Sao Francisco", "Rua Bento Lisboa"]
}

# Lista de raças de cachorros.
racas = [
    "Labrador", "Poodle", "Bulldog", "Beagle", "Chihuahua",
    "Dachshund", "Golden Retriever", "Yorkshire Terrier", "Shih Tzu", "Boxer",
    "Cocker Spaniel", "Schnauzer", "Pug", "Rottweiler", "Husky Siberiano",
    "Basset Hound", "Pit Bull", "Maltes", "Border Collie", "Shiba Inu"
]

# Lista de profissões diversas.
profissoes = [
    "Medico", "Engenheiro", "Advogado", "Professor", "Arquiteto",
    "Dentista", "Farmaceutico", "Psicologo", "Enfermeiro", "Designer",
    "Desenvolvedor", "Analista de Sistemas", "Gerente", "Administrador", "Economista",
    "Contador", "Jornalista", "Publicitario", "Biologo", "Quimico",
    "Veterinario", "Fisioterapeuta", "Historiador", "Antropologo", "Geografo",
    "Musico", "Ator", "Diretor", "Producao de Eventos", "Chef de Cozinha",
    "Personal Trainer", "Terapeuta Ocupacional", "Artesao", "Padeiro", "Lider de Projeto"
]

# Listas de nomes próprios femininos com sobrenomes.
nomes_femininos = [
    "Maria Luiza Silva", "Ana Beatriz Oliveira", "Juliana Costa", "Camila Pereira", "Fernanda Santos",
    "Tatiane Almeida", "Gabriela Rocha", "Isabela Martins", "Larissa Ferreira", "Mariana Lima",
    "Carla Rodrigues", "Amanda Carvalho", "Natália Pinto", "Luana Campos", "Patrícia Melo",
    "Daniele Souza", "Bruna Alves", "Viviane Mendes", "Roberta Moreira", "Michele Araújo"
]

# Listas de nomes próprios masculinos com sobrenomes.
nomes_masculinos = [
    "Diego Silva", "Lucas Ferreira", "Carlos Santos", "João Almeida", "Felipe Oliveira",
    "Rodrigo Costa", "Gabriel Rocha", "Ricardo Martins", "Marcelo Lima", "Eduardo Campos",
    "Pedro Pinto", "André Carvalho", "Rafael Melo", "Thiago Souza", "Leandro Rodrigues",
    "Bruno Alves", "Daniel Araújo", "Antonio Silva", "Gustavo Moreira", "Vinícius Santos"
]

# Função para gerar uma quantidade específica de registros de dados fictícios.
def gerar_dados(qtd_registros=100):

    dados = []

    for _ in range(qtd_registros):

        bairro = random.choice(list(bairros.keys()))         # Escolhe um bairro aleatório.
        rua = random.choice(bairros[bairro])                 # Escolhe uma rua aleatória dentro do bairro selecionado.
        numero_residencial = random.randint(1, 9999)    # Gera um número residencial aleatório.
        endereco = f"{rua}, {numero_residencial}"            # Formata o endereço completo.

        # Escolhe aleatoriamente entre nomes femininos e masculinos.
        if random.choice([True, False]):
            cliente = random.choice(nomes_femininos)
        else:
            cliente = random.choice(nomes_masculinos)

        cpf = f"{random.randint(10000000000, 99999999999)}"                                 # Gera um CPF fictício.
        salario = round(random.uniform(1350, 10000), 2)                                     # Gera um salário aleatório entre R$ 1.350 e R$ 10.000.
        raca = random.choice(racas)                                                              # Escolhe uma raça de cachorro aleatória.
        sexo = "Masculino" if cliente in nomes_masculinos else "Feminino"                        # Determina o sexo com base no nome escolhido.
        profissao = random.choice(profissoes)                                                    # Escolhe uma profissão aleatória.
        idade = random.randint(18, 72)                                                      # Gera uma idade aleatória entre 18 e 72 anos.
        celular = f"(21) {random.randint(90000, 99999)}-{random.randint(1000, 9999)}"  # Gera um número de celular fictício.

        # Remove acentuação dos caracteres para padronizar os dados.
        cliente = unidecode.unidecode(cliente)
        endereco = unidecode.unidecode(endereco)
        bairro = unidecode.unidecode(bairro)
        raca = unidecode.unidecode(raca)
        sexo = unidecode.unidecode(sexo)
        profissao = unidecode.unidecode(profissao)

        # Adiciona os dados gerados à lista.
        dados.append([cliente, endereco, cpf, bairro, salario, raca, sexo, profissao, idade, celular])

    # Define as colunas do DataFrame.
    colunas = ["Cliente", "Endereco", "CPF", "Bairro", "Salario", "Raca", "Sexo", "Profissao", "Idade", "Celular"]

    # Cria um DataFrame com os dados gerados.
    df = pd.DataFrame(dados, columns=colunas)

    # Retorna o DataFrame gerado.
    return df

# Gera registros e salva em um arquivo CSV.
df = gerar_dados(500)
file_path = "dadosBrutos.csv"           # Define o caminho para salvar o arquivo CSV.
df.to_csv(file_path, index=False, encoding='utf-8') # Salva o DataFrame como CSV sem o índice.
