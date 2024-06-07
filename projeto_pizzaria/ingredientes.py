import customtkinter as ctk
from tkinter import messagebox
from utils import carregar_dados, salvar_dados

def adicionar_ingrediente():
    pizzaria = carregar_dados()
    
    # Criar janela para inserção de dados do ingrediente
    ingrediente_window = ctk.CTkToplevel()
    ingrediente_window.title("Adicionar Ingrediente")
    
    # Adicionar entrada de texto para cada informação do ingrediente
    nome_label = ctk.CTkLabel(ingrediente_window, text="Digite o nome do ingrediente:")
    nome_label.pack(pady=5)
    nome_entry = ctk.CTkEntry(ingrediente_window)
    nome_entry.pack(pady=5)

    quantidade_label = ctk.CTkLabel(ingrediente_window, text="Digite a quantidade:")
    quantidade_label.pack(pady=5)
    quantidade_entry = ctk.CTkEntry(ingrediente_window)
    quantidade_entry.pack(pady=5)

    validade_label = ctk.CTkLabel(ingrediente_window, text="Digite a validade:")
    validade_label.pack(pady=5)
    validade_entry = ctk.CTkEntry(ingrediente_window)
    validade_entry.pack(pady=5)
    
    # Função para adicionar o ingrediente
    def adicionar():
        nome_ingrediente = nome_entry.get()
        quantidade = quantidade_entry.get()
        validade = validade_entry.get()

        if not nome_ingrediente or not quantidade or not validade:
            messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
            return

        # Adicionar ingrediente
        pizzaria['estoque'][nome_ingrediente] = {'quantidade': quantidade, 'validade': validade}
        
        # Salvar dados
        salvar_dados(pizzaria)
        
        # Exibir mensagem de sucesso
        messagebox.showinfo("Sucesso", "Ingrediente adicionado!")
        ingrediente_window.destroy()

    # Botão para adicionar ingrediente
    adicionar_button = ctk.CTkButton(ingrediente_window, text="Adicionar", command=adicionar)
    adicionar_button.pack(pady=10)

def listar_ingredientes():
    pizzaria = carregar_dados()
    
    # Verificar se há ingredientes no estoque
    if not pizzaria['estoque']:
        messagebox.showinfo("Aviso", "Não há ingredientes no estoque.")
        return
    
    # Construir uma string com as informações dos ingredientes
    info_ingredientes = ""
    for ingrediente, info in pizzaria['estoque'].items():
        info_ingredientes += f"Nome: {ingrediente}, Quantidade: {info['quantidade']}, Validade: {info['validade']}\n"
    
    # Exibir informações dos ingredientes em uma caixa de diálogo
    messagebox.showinfo("Estoque de Ingredientes", info_ingredientes)

