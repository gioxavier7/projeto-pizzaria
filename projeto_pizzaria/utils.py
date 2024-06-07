import json
import os
from tkinter import messagebox

# Verifica se o arquivo pizzaria.json existe e cria um novo se não existir
if not os.path.exists('data/pizzaria.json'):
    with open('data/pizzaria.json', 'w') as file:
        json.dump({}, file)

def carregar_dados():
    # Abre o arquivo pizzaria.json e verifica se está vazio
    if os.path.getsize('data/pizzaria.json') == 0:
        return {
            'nome': '',
            'endereco': '',
            'horario_atendimento': '',
            'telefone': '',
            'cardapio': [],  # Lista para armazenar pizzas
            'estoque': {}
        }
    else:
        with open('data/pizzaria.json', 'r') as file:
            return json.load(file)

def salvar_dados(dados):
    with open('data/pizzaria.json', 'w') as file:
        json.dump(dados, file, indent=4)

# Função específica para salvar perfil
def salvar_perfil(perfil):
    dados = carregar_dados()
    dados['perfil'] = perfil
    salvar_dados(dados)

# Função específica para validar o login
def validar_login(username, senha):
    dados = carregar_dados()
    perfil = dados.get('perfil', {})
    return perfil.get('nome') == username and perfil.get('senha') == senha

# Função específica para salvar ingredientes adicionados
def adicionar_ingrediente(nome, quantidade, validade):
    dados = carregar_dados()
    if nome in dados['ingredientes']:
        messagebox.showerror('Erro', 'Ingrediente já existe.')
        return False
    dados['ingredientes'][nome] = {
        'quantidade': quantidade,
        'validade': validade
    }
    salvar_dados(dados)
    return True


# Função específica para salvar dados do perfil da loja
def salvar_perfil_loja(nome_estabelecimento, telefone, horario_funcionamento, endereco):
    # Carregar os dados do arquivo
    pizzaria = carregar_dados()

    # Adicionar os dados do perfil da loja
    pizzaria['perfil_loja'] = {
        'nome_estabelecimento': nome_estabelecimento,
        'telefone': telefone,
        'horario_funcionamento': horario_funcionamento,
        'endereco': endereco
    }

    # Salvar os dados atualizados no arquivo
    salvar_dados(pizzaria)


# Dados iniciais da pizzaria
pizzaria = carregar_dados()
