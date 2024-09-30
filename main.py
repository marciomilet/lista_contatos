import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

connection_string = os.getenv('connection')
client = MongoClient(connection_string)
db_connection = client['test']
collection = db_connection.get_collection('contatos')

def inserir_contatos():
    while True:
        nome = input("Digite o nome do contato: ")
        email = input("Digite o e-mail do contato: ")
        celular = input("Digite o número do celular (ex: +55 XX XXXXX-XXXX): ")

        # Criando o documento do contato
        contato = {
            "nome": nome,
            "email": email,
            "celular": celular
        }

        # Inserindo o contato no banco de dados
        collection.insert_one(contato)
        print(f"Contato {nome} inserido com sucesso.")

        # Perguntar se o usuário deseja adicionar mais contatos
        continuar = input("Deseja adicionar outro contato? (s/n): ")
        if continuar != 's':
            break


def consultar_por_nome(nome):
    contato = collection.find_one({"nome": nome})
    if contato:
        print(f"Contato encontrado: {contato}")
    else:
        print("Contato não encontrado.")

# Função para consultar contato por e-mail
def consultar_por_email(email):
    contato = collection.find_one({"email": email})
    if contato:
        print(f"Contato encontrado: {contato}")
    else:
        print("Contato não encontrado.")

# Função para listar todos os contatos
def listar_todos_contatos():
    contatos = collection.find()
    for contato in contatos:
        print(contato)
    while True:
        continuar = input("voltar pro menu? (s/n)")
        if continuar == 's':
            break
        

    

# Função principal para o menu de opções
def menu():
    while True:
        print("\nMenu de opções:")
        print("1. Inserir contatos")
        print("2. Consultar contato por nome")
        print("3. Consultar contato por e-mail")
        print("4. Listar todos os contatos")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            inserir_contatos()
        elif opcao == '2':
            nome = input("Digite o nome para consulta: ")
            consultar_por_nome(nome)
        elif opcao == '3':
            email = input("Digite o e-mail para consulta: ")
            consultar_por_email(email)
        elif opcao == '4':
            listar_todos_contatos()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()