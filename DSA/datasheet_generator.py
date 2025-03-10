from faker import Faker
import random
import csv

# Configuração do Faker
fake = Faker('pt_BR')

# Lista de profissões para sortear
profissoes = [
    "Engenheiro de Software",
    "Professor",
    "Médico",
    "Designer Gráfico",
    "Advogado",
    "Analista de Dados",
    "Contador",
    "Arquiteto",
    "Enfermeiro",
    "Gestor de Projetos",
    "Desenvolvedor Web",
    "Vendedor",
    "Cientista de Dados",
    "Técnico de TI",
    "Marketing Digital",
    "Consultor",
    "Psicólogo",
    "Gerente de Recursos Humanos",
    "Farmacêutico",
    "Administrador"
]

# Função para gerar um salário aleatório
def gerar_salario():
    return round(random.uniform(2000, 15000), 2)

# Gerar os dados
num_registros = 50
dados = []

for _ in range(num_registros):
    nome = fake.name()
    profissao = random.choice(profissoes)
    salario = gerar_salario()
    aniversario = fake.date_of_birth(minimum_age=18, maximum_age=65)
    cpf = fake.cpf()
    idade = fake.year()
    dados.append({
        "Idade": idade,
        "CPF": cpf,
        "Nome": nome,
        "Profissao": profissao,
        "Salario": salario,
        "Aniversario": aniversario
    })

# Salvar em um arquivo CSV
nome_arquivo = "datasheet.csv"

with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo_csv:
    writer = csv.DictWriter(arquivo_csv, fieldnames=["Nome", "Profissao", "Salario", "Aniversario", "CPF", "Idade"])
    writer.writeheader()
    writer.writerows(dados)

print(f"Datasheet com {num_registros} registros gerado no arquivo '{nome_arquivo}'.")

