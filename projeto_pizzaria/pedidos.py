import json
from utils import carregar_dados, salvar_dados

def validar_pedido(nome_pizza, quantidade, endereco):
    pizzaria = carregar_dados()
    
    # Verificar se a pizza está no cardápio
    pizza_existente = False
    for pizza in pizzaria['cardapio']:
        if pizza['nome'] == nome_pizza:
            pizza_existente = True
            break

    if not pizza_existente:
        return False, "A pizza não existe no cardápio."

    # Verificar se a quantidade contém apenas números
    if not quantidade.isdigit():
        return False, "A quantidade deve conter apenas números."

    # Verificar se o endereço foi preenchido
    if not endereco:
        return False, "O endereço de entrega deve ser preenchido."

    return True, None

def adicionar_pedido(nome_pizza, quantidade, endereco):
    valido, mensagem_erro = validar_pedido(nome_pizza, quantidade, endereco)

    if not valido:
        return False, mensagem_erro
    
    pizzaria = carregar_dados()
    
    # Adicionar o pedido
    novo_pedido = {
        'nome_pizza': nome_pizza,
        'quantidade': int(quantidade),
        'endereco_entrega': endereco
    }
    pizzaria['pedidos'].append(novo_pedido)
    
    # Salvar os dados atualizados no arquivo
    salvar_dados(pizzaria)
    
    return True, "Pedido adicionado com sucesso!"

def obter_pedidos():
    pizzaria = carregar_dados()
    return pizzaria['pedidos']
