from utils import salvar_perfil_loja

def validar_dados_perfil_loja(nome, telefone, horario, endereco):
    # Verificar se todos os campos foram preenchidos
    if not nome or not telefone or not horario or not endereco:
        return False, "Todos os campos devem ser preenchidos."

    # Verificar se o telefone contém apenas números
    if not telefone.isdigit():
        return False, "O telefone deve conter apenas números."

    return True, None

def atualizar_perfil_loja(nome, telefone, horario, endereco):
    # Validar os dados do perfil da loja
    valido, mensagem_erro = validar_dados_perfil_loja(nome, telefone, horario, endereco)

    if not valido:
        return False, mensagem_erro
    
    # Salvar os dados do perfil da loja
    salvar_perfil_loja(nome, telefone, horario, endereco)
    return True, "Perfil da loja atualizado com sucesso!"
