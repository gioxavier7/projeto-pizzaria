from utils import carregar_dados, salvar_dados

def adicionar_pedido():
    pizzaria = carregar_dados()
    pedido = input("Digite o pedido: ")
    pizzaria['pedidos'].append(pedido)
    salvar_dados(pizzaria)
    print("Pedido adicionado!")

def atualizar_perfil():
    pizzaria = carregar_dados()
    nome = input("Digite o seu nome: ")
    email = input("Digite o seu email: ")
    pizzaria['perfil'] = {"nome": nome, "email": email}
    salvar_dados(pizzaria)
    print("Perfil atualizado!")
