import customtkinter as ctk
from tkinter import messagebox
from utils import carregar_dados, salvar_dados

def adicionar_receita():
    pizzaria = carregar_dados()
    
    # Criar janela para inserção de dados da receita
    receita_window = ctk.CTkToplevel()
    receita_window.title("Adicionar Receita")
    
    # Adicionar entrada de texto para cada informação da receita
    nome_label = ctk.CTkLabel(receita_window, text="Digite o nome da pizza para adicionar a receita:")
    nome_label.pack(pady=5)
    nome_entry = ctk.CTkEntry(receita_window)
    nome_entry.pack(pady=5)

    ingredientes_label = ctk.CTkLabel(receita_window, text="Digite os ingredientes da receita:")
    ingredientes_label.pack(pady=5)
    ingredientes_entry = ctk.CTkEntry(receita_window)
    ingredientes_entry.pack(pady=5)
    
    # Função para adicionar a receita à pizza
    def adicionar():
        nome_pizza = nome_entry.get()
        ingredientes = ingredientes_entry.get()

        if not nome_pizza or not ingredientes:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Verificar se a pizza existe no cardápio
        pizza_existente = False
        for pizza in pizzaria['cardapio']:
            if pizza['nome'] == nome_pizza:
                pizza_existente = True
                break
        
        if not pizza_existente:
            messagebox.showerror("Erro", "A pizza não existe no cardápio.")
            return
        
        # Adicionar receita à pizza
        for pizza in pizzaria['cardapio']:
            if pizza['nome'] == nome_pizza:
                pizza['receita'] = ingredientes
                break
        
        # Salvar dados
        salvar_dados(pizzaria)
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Receita adicionada à pizza!")
        receita_window.destroy()

    # Botão para adicionar receita
    adicionar_button = ctk.CTkButton(receita_window, text="Adicionar", command=adicionar)
    adicionar_button.pack(pady=10)

def verificar_receitas():
    pizzaria = carregar_dados()
    
    # Verificar se há receitas no cardápio
    if not pizzaria['cardapio']:
        messagebox.showinfo("Aviso", "Não há receitas no cardápio.")
        return
    
    # Construir uma string com as informações das pizzas
    info_pizzas = ""
    for pizza in pizzaria['cardapio']:
        if 'receita' in pizza:
            info_pizzas += f"Nome: {pizza['nome']}, Receita: {pizza['receita']}\n"
        else:
            info_pizzas += f"Nome: {pizza['nome']}, Sem receita\n"
    
    # Exibir informações das receitas em uma caixa de diálogo
    messagebox.showinfo("Receitas", info_pizzas)
