import customtkinter as ctk
from tkinter import messagebox
from utils import carregar_dados, salvar_dados

def adicionar_pizza():
    pizzaria = carregar_dados()
    
    # Criar janela para inserção de dados da pizza
    pizza_window = ctk.CTkToplevel()
    pizza_window.title("Adicionar Pizza")
    
    # Adicionar entrada de texto para cada informação da pizza
    nome_label = ctk.CTkLabel(pizza_window, text="Digite o nome da pizza:")
    nome_label.pack()
    nome_entry = ctk.CTkEntry(pizza_window)
    nome_entry.pack()

    descricao_label = ctk.CTkLabel(pizza_window, text="Digite a descrição da pizza (salgada ou doce):")
    descricao_label.pack()
    descricao_entry = ctk.CTkEntry(pizza_window)
    descricao_entry.pack()

    preco_label = ctk.CTkLabel(pizza_window, text="Digite o preço da pizza:")
    preco_label.pack()
    preco_entry = ctk.CTkEntry(pizza_window)
    preco_entry.pack()
    
    # Função para adicionar a pizza ao cardápio
    def adicionar():
        preco = preco_entry.get()
        descricao = descricao_entry.get()
        nome_pizza = nome_entry.get()

        if not nome_pizza or not descricao or not preco:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Verificação se a descrição é válida (doce ou salgada)
        if descricao.lower() not in ['doce', 'salgada']:
            messagebox.showerror("Erro", "A descrição deve ser 'doce' ou 'salgada'.")
            return

        # Criar dicionário representando a pizza
        pizza = {"nome": nome_pizza, "descricao": descricao, "preco": preco}
        
        # Adicionar pizza ao cardápio
        pizzaria['cardapio'].append(pizza)
        
        # Salvar dados
        salvar_dados(pizzaria)
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Pizza adicionada ao cardápio!")
        pizza_window.destroy()

    # Botão para adicionar pizza
    adicionar_button = ctk.CTkButton(pizza_window, text="Adicionar", command=adicionar)
    adicionar_button.pack()

def remover_pizza():
    pizzaria = carregar_dados()
    
    # Criar janela para inserção do nome da pizza a ser removida
    remover_window = ctk.CTkToplevel()
    remover_window.title("Remover Pizza")
    
    # Adicionar entrada de texto para inserir o nome da pizza
    nome_label = ctk.CTkLabel(remover_window, text="Digite o nome da pizza a ser removida:")
    nome_label.pack()
    nome_entry = ctk.CTkEntry(remover_window)
    nome_entry.pack()
    
    # Função para remover a pizza do cardápio
    def remover():
        nome_pizza = nome_entry.get()

        if not nome_pizza:
            messagebox.showerror("Erro", "Digite o nome da pizza a ser removida.")
            return
        
        # Remover pizza do cardápio
        pizzaria['cardapio'] = [pizza for pizza in pizzaria['cardapio'] if pizza['nome'] != nome_pizza]
        
        # Salvar dados
        salvar_dados(pizzaria)
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Pizza removida do cardápio!")
        remover_window.destroy()

    # Botão para remover pizza
    remover_button = ctk.CTkButton(remover_window, text="Remover", command=remover)
    remover_button.pack()

def verificar_cardapio():
    pizzaria = carregar_dados()
    
    # Construir uma string com as informações das pizzas
    info_pizzas = ""
    for pizza in pizzaria['cardapio']:
        info_pizzas += f"Nome: {pizza['nome']}, Descrição: {pizza['descricao']}, Preço: {pizza['preco']}\n"
    
    # Exibir informações das pizzas em uma caixa de diálogo
    messagebox.showinfo("Cardápio", info_pizzas)