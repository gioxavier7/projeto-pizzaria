import customtkinter as ctk
from tkinter import *
from tkinter import messagebox, PhotoImage
import utils
from utils import carregar_dados, salvar_dados, salvar_perfil, validar_login
from cardapio import adicionar_pizza, remover_pizza, verificar_cardapio
from receitas import verificar_receitas, adicionar_receita
import ingredientes 
from estoque import adicionar_pedido, atualizar_perfil
import perfil_loja
from pedidos import adicionar_pedido, obter_pedidos

# Carregar dados iniciais
pizzaria = carregar_dados()

# Criando a interface gráfica
tela_login = ctk.CTk()

class Aplication():
    def __init__(self):
       self.tela_login = tela_login
       self.tela()
       self.img_login()
       tela_login.mainloop()

    def tela(self):
        #criando tela de login
        tela_login.geometry('700x400')
        tela_login.title('Login')
        tela_login.resizable(False, False)

    def tela_home(self):
        # Criação da janela principal
        tela_home = ctk.CTkToplevel()
        tela_home.title('Home')
        tela_home.geometry('700x400')
        tela_home.resizable(False, False)

        #função para criar a tela cardápio
        def tela_cardapio():
            tela_cardapio = ctk.CTkToplevel()
            tela_cardapio.title('Cardápio')
            tela_cardapio.geometry('850x500')
            tela_cardapio.resizable(False, False)

            #frame para criação do menu cardápio
            cardapio_frame = ctk.CTkFrame(tela_cardapio, height=60)
            cardapio_frame.pack(fill='x')

            # Configuração do layout do grid
            for i in range(3):
                cardapio_frame.grid_columnconfigure(i, weight=1, uniform="equal")

            #botao menu principal - Verificar Cardápio
            button_menu_verificar_cardapio = ctk.CTkButton(cardapio_frame, text='Verificar Cardápio',
                                                font=('Poppins', 10), fg_color= '#CA2521', hover_color='#9F1F1B',
                                                width=100, height=30,
                                                command=verificar_cardapio)
            button_menu_verificar_cardapio.grid(row=0, column=0, padx=10, pady=10, sticky='ew')           

            #botao menu principal - Adicionar Pizza
            button_menu_adicionar_pizza = ctk.CTkButton(cardapio_frame, text='Adicionar Pizza',
                                                font=('Poppins', 10), fg_color= '#CA2521', hover_color='#9F1F1B',
                                                width=100, height=30,
                                                command=adicionar_pizza)
            button_menu_adicionar_pizza.grid(row=0, column=1, padx=10, pady=10, sticky='ew')

            #botao menu principal - Remover Pizza
            button_menu_remover_pizza = ctk.CTkButton(cardapio_frame, text='Remover Pizza',
                                                font=('Poppins', 10), fg_color= '#CA2521', hover_color='#9F1F1B',
                                                width=100, height=30,
                                                command=remover_pizza)
            button_menu_remover_pizza.grid(row=0, column=2, padx=10, pady=10, sticky='ew')

        #função para criar tela receitas
        def tela_receitas():
            tela_receitas = ctk.CTkToplevel()
            tela_receitas.title('Receitas')
            tela_receitas.geometry('700x400')
            tela_receitas.resizable(False, False)
            
            receita_img = PhotoImage(file='images/receita.png')
            label_img = ctk.CTkLabel(master=tela_receitas, image=receita_img, text=None).place(x=50, y=65)

            #frame de receitas
            receita_frame = ctk.CTkFrame(master=tela_receitas, width=350, height=396)
            receita_frame.pack(side=ctk.RIGHT)

            #frame receita widgets
            receita_label = ctk.CTkLabel(master=receita_frame, text='Veja as receitas.', font=('Poppins', 20, 'bold'), text_color=('white')).place(x=25, y=105)

            #campo preenchemento nome da pizza para procurar a receita
            nome_pizza_entry = ctk.CTkEntry(master=receita_frame, placeholder_text='Nome da Pizza', 
                                    width=300, font=('Poppins', 20)).place(x=25, y=145)
            nome_pizza_label = ctk.CTkLabel(master=receita_frame, text='*Preenchemento obrigatório', text_color='#CA2521', 
                                        font=('Poppins', 8)).place(x=25, y=185)
            
            #botão para buscar receitas
            button_verificar_receitas = ctk.CTkButton(master=receita_frame, text='BUSCAR', width=300, 
                                        fg_color='#CA2521', hover_color='#9F1F1B', command=verificar_receitas).place(x=25, y=285)
            
            #redirecionamento para adicionar receita
            adicionar_pizza_span = ctk.CTkLabel(master=receita_frame, text='Se não tem uma receita').place(x=25, y=325)

            def tela_adicionar_receita():
                #remover frame de receitas
                receita_frame.pack_forget()

                #criando a tela de adicionar receitas
                adicionar_receitas_frame = ctk.CTkFrame(master=tela_receitas, width=350, height=396)
                adicionar_receitas_frame.pack(side=ctk.RIGHT)

                #frame cadastro receitas widgets
                adicionar_receita_label = ctk.CTkLabel(master=adicionar_receitas_frame, text='Adicione uma receita.', font=('Poppins', 20, 'bold'), 
                text_color=('white')).place(x=25, y=105)

                #campo de preenchimento para adicionar receita
                entry_nome_pizza = ctk.CTkEntry(master=adicionar_receitas_frame, placeholder_text='Nome da Pizza', 
                                        width=300, font=('Poppins', 14))
                entry_nome_pizza.place(x=25, y=145)
                
                entry_ingredientes_pizza = ctk.CTkEntry(master=adicionar_receitas_frame, placeholder_text='Ingredientes', 
                                        width=300, font=('Poppins', 14))
                entry_ingredientes_pizza.place(x=25, y=185)
                
                #função para o botão "voltar"
                def voltar_tela_receita():
                    adicionar_receitas_frame.pack_forget()
                    receita_frame.pack(side=ctk.RIGHT)

                #botao voltar
                button_voltar = ctk.CTkButton(master=adicionar_receitas_frame, text='VOLTAR', width=145, 
                                                fg_color='#CA2521', hover_color='#9F1F1B', 
                                                command=voltar_tela_receita)
                button_voltar.place(x=25, y=265)
                
                def salvar_receita():
                    nome_pizza = entry_nome_pizza.get()
                    ingredientes = entry_ingredientes_pizza.get()

                    if not nome_pizza or not ingredientes:
                        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                        return

                    # Carregar os dados do arquivo
                    pizzaria = carregar_dados()

                    # Verificar se a pizza existe no cardápio
                    pizza_existente = False
                    for pizza in pizzaria['cardapio']:
                        if pizza['nome'] == nome_pizza:
                            pizza_existente = True
                            pizza['receita'] = ingredientes
                            break
                    
                    if not pizza_existente:
                        messagebox.showerror("Erro", "A pizza não existe no cardápio.")
                        return

                    # Salvar os dados atualizados no arquivo
                    salvar_dados(pizzaria)

                    messagebox.showinfo(title='Receita criada!', message='Veja a receita adicionada na tela anterior')

                #botao para salvar receita
                button_salvar = ctk.CTkButton(master=adicionar_receitas_frame, text='ADICIONAR', width=145, 
                                                fg_color='#CA2521', hover_color='#9F1F1B', command=salvar_receita)
                button_salvar.place(x=180, y=265)

            button_adicionar_receita = ctk.CTkButton(master=receita_frame, text='Adicione uma receita', width=150, 
                                            fg_color='#ECA442', hover_color='#DD993E', 
                                            command=tela_adicionar_receita)
            button_adicionar_receita.place(x=175, y=325)

        #função para criar a tela ingredientes
        def tela_ingredientes():
            tela_ingredientes = ctk.CTkToplevel()
            tela_ingredientes.title('Ingredientes')
            tela_ingredientes.geometry('700x400')
            tela_ingredientes.resizable(False, False)
            
            ingrediente_img = PhotoImage(file='images/ingredientes.png')
            label_img = ctk.CTkLabel(master=tela_ingredientes, image=ingrediente_img, text=None).place(x=50, y=65)

            #frame de ingredientes
            ingrediente_frame = ctk.CTkFrame(master=tela_ingredientes, width=350, height=396)
            ingrediente_frame.pack(side=ctk.RIGHT)

            #frame ingrediente widgets
            ingrediente_label = ctk.CTkLabel(master=ingrediente_frame, text='Veja os ingredientes.', font=('Poppins', 20, 'bold'), text_color=('white')).place(x=25, y=105)

            #campo preenchemento nome do ingrediente para procurar
            nome_ingrediente_entry = ctk.CTkEntry(master=ingrediente_frame, placeholder_text='Nome do Ingrediente', 
                                    width=300, font=('Poppins', 20)).place(x=25, y=145)
            nome_ingrediente_label = ctk.CTkLabel(master=ingrediente_frame, text='*Preenchemento obrigatório', text_color='#CA2521', 
                                            font=('Poppins', 8)).place(x=25, y=185)
            
            #botão para buscar ingredientes
            button_verificar_ingredientes = ctk.CTkButton(master=ingrediente_frame, text='BUSCAR', width=300, 
                                            fg_color='#CA2521', hover_color='#9F1F1B', command=ingredientes.listar_ingredientes).place(x=25, y=285)
            
            #redirecionamento para adicionar ingrediente
            adicionar_ingrediente_span = ctk.CTkLabel(master=ingrediente_frame, text='Se não tem ingredientes').place(x=25, y=325)

            def tela_adicionar_ingrediente():
                #remover frame de ingredientes
                ingrediente_frame.pack_forget()

                #criando a tela de adicionar ingredientes
                adicionar_ingredientes_frame = ctk.CTkFrame(master=tela_ingredientes, width=350, height=396)
                adicionar_ingredientes_frame.pack(side=ctk.RIGHT)

                #frame cadastro widgets
                adicionar_ingrediente_label = ctk.CTkLabel(master=adicionar_ingredientes_frame, text='Adicione um ingrediente', font=('Poppins', 20, 'bold'), 
                text_color=('white')).place(x=25, y=60)

                #frame cadastro ingredientes widgets
                adicionar_ingrediente_label = ctk.CTkLabel(master=adicionar_ingredientes_frame, text='Adicione ingredientes', font=('Poppins', 20, 'bold'), 
                text_color=('white')).place(x=25, y=60)

                #campo de preenchimento para adicionar ingrediente
                entry_nome_ingrediente = ctk.CTkEntry(master=adicionar_ingredientes_frame, placeholder_text='Nome do ingrediente', 
                                        width=300, font=('Poppins', 14))
                entry_nome_ingrediente.place(x=25, y=105)
                
                entry_quantidade = ctk.CTkEntry(master=adicionar_ingredientes_frame, placeholder_text='Quantidade', 
                                        width=300, font=('Poppins', 14))
                entry_quantidade.place(x=25, y=145)                 
                
                entry_validade = ctk.CTkEntry(master=adicionar_ingredientes_frame, placeholder_text='Validade', 
                                        width=300, font=('Poppins', 14))
                entry_validade.place(x=25, y=185)
                
                #função para o botão "voltar"
                def voltar_tela_ingrediente():
                    adicionar_ingredientes_frame.pack_forget()
                    ingrediente_frame.pack(side=ctk.RIGHT)

                #botao voltar
                button_voltar = ctk.CTkButton(master=adicionar_ingredientes_frame, text='VOLTAR', width=145, 
                                                fg_color='#CA2521', hover_color='#9F1F1B', 
                                                command=voltar_tela_ingrediente)
                button_voltar.place(x=25, y=265)
                
            # Função para salvar o ingrediente
                def salvar_ingrediente():
                    nome_ingrediente = entry_nome_ingrediente.get()
                    quantidade = entry_quantidade.get()
                    validade = entry_validade.get()

                    if not nome_ingrediente or not quantidade or not validade:
                        messagebox.showerror("Erro", "Todos os campos devem ser preenchidos.")
                        return

                    # Carregar os dados do arquivo
                    pizzaria = carregar_dados()

                    # Adicionar o novo ingrediente ao estoque
                    if 'estoque' not in pizzaria:
                        pizzaria['estoque'] = {}

                    pizzaria['estoque'][nome_ingrediente] = {
                        'quantidade': quantidade,
                        'validade': validade
                    }

                    # Salvar os dados atualizados no arquivo
                    salvar_dados(pizzaria)

                    messagebox.showinfo(title='Ingrediente adicionado!', message='O ingrediente foi adicionado com sucesso!')
                    # Salvar os dados atualizados no arquivo
                    salvar_dados(pizzaria)

                # Botão para salvar o ingrediente
                button_salvar_ingrediente = ctk.CTkButton(master=adicionar_ingredientes_frame, text='ADICIONAR', width=145, 
                                                fg_color='#CA2521', hover_color='#9F1F1B', command=salvar_ingrediente)
                button_salvar_ingrediente.place(x=180, y=265)

            button_adicionar_ingrediente = ctk.CTkButton(master=ingrediente_frame, text='Adicione ingredientes', width=150, 
                                            fg_color='#ECA442', hover_color='#DD993E', 
                                            command=tela_adicionar_ingrediente)
            button_adicionar_ingrediente.place(x=175, y=325)

        #função para criar a tela pedidos
        def criar_tela_pedidos():
            tela_pedidos = ctk.CTkToplevel()
            tela_pedidos.title('Pedidos')
            tela_pedidos.geometry('700x400')
            tela_pedidos.resizable(False, False)

            img_pedidos = PhotoImage(file='images/pedidos.png')
            label_img = ctk.CTkLabel(master=criar_tela_pedidos, image=img_pedidos, text=None)
            label_img.place(x=50, y=65)

            # Frame de pedidos
            pedidos_frame = ctk.CTkFrame(master=tela_pedidos, width=350, height=396)
            pedidos_frame.pack(side=RIGHT)

            pedidos_label = ctk.CTkLabel(master=pedidos_frame, text='Pedidos Existentes', font=('Poppins', 20, 'bold'), text_color=('white'))
            pedidos_label.pack(pady=10)

            pedidos_text = ctk.CTkTextbox(master=pedidos_frame, width=300, height=250)
            pedidos_text.pack(pady=10)

            pedidos_text.insert(ctk.END, "Pedidos:\n")
            pedidos = obter_pedidos()
            for pedido in pedidos:
                pedidos_text.insert(ctk.END, f"Pizza: {pedido['nome_pizza']}, Quantidade: {pedido['quantidade']}, Endereço: {pedido['endereco_entrega']}\n")

            def tela_adicionar_pedido():
                adicionar_pedido_janela = ctk.CTkToplevel()
                adicionar_pedido_janela.title("Adicionar Pedido")
                adicionar_pedido_janela.geometry("400x300")

                # Nome da Pizza
                nome_label = ctk.CTkLabel(adicionar_pedido_janela, text="Nome da Pizza:")
                nome_label.pack(pady=5)
                nome_entry = ctk.CTkEntry(adicionar_pedido_janela)
                nome_entry.pack(pady=5)

                # Quantidade
                quantidade_label = ctk.CTkLabel(adicionar_pedido_janela, text="Quantidade:")
                quantidade_label.pack(pady=5)
                quantidade_entry = ctk.CTkEntry(adicionar_pedido_janela)
                quantidade_entry.pack(pady=5)

                # Endereço de Entrega
                endereco_label = ctk.CTkLabel(adicionar_pedido_janela, text="Endereço de Entrega:")
                endereco_label.pack(pady=5)
                endereco_entry = ctk.CTkEntry(adicionar_pedido_janela)
                endereco_entry.pack(pady=5)

                def salvar_pedido():
                    nome_pizza = nome_entry.get()
                    quantidade = quantidade_entry.get()
                    endereco = endereco_entry.get()

                    sucesso, mensagem = adicionar_pedido(nome_pizza, quantidade, endereco)
                    if sucesso:
                        messagebox.showinfo("Sucesso", mensagem)
                        adicionar_pedido_janela.destroy()
                        tela_pedidos.destroy()
                        criar_tela_pedidos()  # Atualiza a lista de pedidos
                    else:
                        messagebox.showerror("Erro", mensagem)

                # Botão para adicionar pedido
                adicionar_button = ctk.CTkButton(adicionar_pedido_janela, text="Adicionar Pedido", command=salvar_pedido)
                adicionar_button.pack(pady=10)

                # Botão para redirecionar para adicionar pedido
            button_adicionar_pedido = ctk.CTkButton(master=pedidos_frame, text="Adicionar Pedido", command=tela_adicionar_pedido)
            button_adicionar_pedido.pack(pady=10, side=ctk.BOTTOM, anchor=ctk.S)

        #função para criar a tela perfil
        def tela_perfil_loja():
            tela_perfil_loja = ctk.CTkToplevel()
            tela_perfil_loja.title('Perfil')
            tela_perfil_loja.geometry('850x500')
            tela_perfil_loja.resizable(False, False)

            img_perfil_lojas = PhotoImage(file='images/perfil_lojas.png')
            label_img = ctk.CTkLabel(master=tela_perfil_loja, image=img_perfil_lojas, text=None)
            label_img.place(x=50, y=65)

            # frame
            perfil_loja_frame = ctk.CTkFrame(master=tela_perfil_loja, width=350, height=396)
            perfil_loja_frame.pack(side=RIGHT)

            # frame login widgets
            perfil_loja_label = ctk.CTkLabel(master=perfil_loja_frame, text='Perfil da Loja!', font=('Poppins', 20, 'bold'), text_color=('white'))
            perfil_loja_label.place(x=25, y=50)


            #campo de preenchimento
            entry_nome_estabelecimento = ctk.CTkEntry(master=perfil_loja_frame, placeholder_text='Nome do Estabelecimento', width=300, font=('Poppins', 14))
            entry_nome_estabelecimento.place(x=25, y=105)

            entry_telefone_loja = ctk.CTkEntry(master=perfil_loja_frame, placeholder_text='Telefone da loja', width=300, font=('Poppins', 14))
            entry_telefone_loja.place(x=25, y=145)

            entry_horario_atendimento = ctk.CTkEntry(master=perfil_loja_frame, placeholder_text='Horário de Atendimento', width=300, font=('Poppins', 14))
            entry_horario_atendimento.place(x=25, y=185)

            entry_endereco = ctk.CTkEntry(master=perfil_loja_frame, placeholder_text='Endereço do estabelecimento', width=300, font=('Poppins', 14))
            entry_endereco.place(x=25, y=225)

            def validar_perfil_loja():
                nome_estabelecimento = entry_nome_estabelecimento.get()
                telefone_loja = entry_telefone_loja.get()
                horario_atendimento = horario_atendimento.get()
                endereco = entry_endereco.get()

                if nome_estabelecimento == '' or telefone_loja == '' or horario_atendimento == '' or endereco == '':
                    messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
                    return

                if not telefone_loja.isdigit() or len(telefone_loja) != 11:
                    messagebox.showerror('Erro', 'Telefone deve conter apenas números e ter 11 dígitos.')
                    return
                
                # Se todos os dados são válidos, salve os dados
                perfil_loja = {
                    'nome_estabelecimento': nome_estabelecimento,
                    'telefone_loja': telefone_loja,
                    'horário_atendimento': horario_atendimento,
                    'endereco': endereco
                }
                utils.salvar_perfil(perfil_loja)

                # Mostrar mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Perfil da loja salvo com sucesso!')

            # botao para salvar cadastro
            button_salvar = ctk.CTkButton(master=perfil_loja_frame, text='SALVAR', width=300, fg_color='#CA2521', hover_color='#9F1F1B', command=validar_perfil_loja)
            button_salvar.place(x=25, y=285)

        # Criação do frame de menu principal
        # Adicionando imagem ao lado esquerdo
        img = PhotoImage(file='images/pizza.png')
        label_img = ctk.CTkLabel(master=tela_home, image=img, text=None)
        label_img.place(x=50, y=65)

        # frame
        central_frame = ctk.CTkFrame(master=tela_home, width=350, height=396)
        central_frame.pack(side=RIGHT)

        button_cardapio = ctk.CTkButton(master=central_frame, text='Cardápio', 
                                            font=('Poppins', 10), fg_color='#CA2521', hover_color='#9F1F1B', 
                                            width=150, height=40, command=tela_cardapio)
        button_cardapio.place(x=100, y=50)

        button_receitas = ctk.CTkButton(master=central_frame, text='Receitas', 
                                            font=('Poppins', 10), fg_color='#CA2521', hover_color='#9F1F1B', 
                                            width=150, height=40, command=tela_receitas)
        button_receitas.place(x=100, y=120)

        button_ingredientes = ctk.CTkButton(master=central_frame, text='Ingredientes', 
                                                font=('Poppins', 10), fg_color='#CA2521', hover_color='#9F1F1B', 
                                                width=150, height=40, command=tela_ingredientes)
        button_ingredientes.place(x=100, y=190)

        button_pedidos = ctk.CTkButton(master=central_frame, text='Pedidos', 
                                        font=('Poppins', 10), fg_color='#CA2521', hover_color='#9F1F1B', 
                                        width=150, height=40, command=criar_tela_pedidos)
        button_pedidos.place(x=100, y=260)

        button_perfil = ctk.CTkButton(master=central_frame, text='Perfil', 
                                        font=('Poppins', 10), fg_color='#CA2521', hover_color='#9F1F1B', 
                                        width=150, height=40, command=tela_perfil_loja)
        button_perfil.place(x=100, y=330)

    # Criando a tela de login e adicionando a imagem
    def img_login(self):
        img = PhotoImage(file='images/pizza.png')
        label_img = ctk.CTkLabel(master=tela_login, image=img, text=None)
        label_img.place(x=50, y=65)

        # frame
        login_frame = ctk.CTkFrame(master=tela_login, width=350, height=396)
        login_frame.pack(side=RIGHT)

        # frame login widgets
        login_label = ctk.CTkLabel(master=login_frame, text='Faça login!', font=('Poppins', 20, 'bold'), text_color=('white'))
        login_label.place(x=25, y=50)

        # campo preenchimento username
        username_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Nome Completo', width=300, font=('Poppins', 20))
        username_entry.place(x=25, y=105)
        username_label = ctk.CTkLabel(master=login_frame, text='*Preenchimento obrigatório', text_color='#CA2521', font=('Poppins', 8))
        username_label.place(x=25, y=135)

        # campo preenchimento senha
        senha_entry = ctk.CTkEntry(master=login_frame, placeholder_text='Senha', width=300, font=('Poppins', 14), show='*')
        senha_entry.place(x=25, y=175)
        senha_label = ctk.CTkLabel(master=login_frame, text='*Preenchimento obrigatório', text_color='#CA2521', font=('Poppins', 8))
        senha_label.place(x=25, y=205)

        def validar_login():
                username = username_entry.get()
                senha = senha_entry.get()

                if username == '' or senha == '':
                    messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
                    return

                if utils.validar_login(username, senha):
                    self.tela_home()
                else:
                    messagebox.showerror('Erro', 'Credenciais inválidas. Por favor, tente novamente.')

        # botão para login
        button_login = ctk.CTkButton(master=login_frame, text='LOGIN', width=300, fg_color='#CA2521', hover_color='#9F1F1B', command=validar_login)
        button_login.place(x=25, y=285)

        # redirecionamento para cadastro
        cadastro_span = ctk.CTkLabel(master=login_frame, text='Se não tem uma conta')
        cadastro_span.place(x=25, y=325)

        def tela_cadastro():
            # remover frame de login
            login_frame.pack_forget()

            # criando a tela de cadastro
            cadastro_frame = ctk.CTkFrame(master=tela_login, width=350, height=396)
            cadastro_frame.pack(side=RIGHT)

            # frame cadastro widgets
            cadastro_label = ctk.CTkLabel(master=cadastro_frame, text='Faça seu cadastro!', font=('Poppins', 20, 'bold'), text_color=('white'))
            cadastro_label.place(x=25, y=50)

            # campo de preenchimento
            entry_nome = ctk.CTkEntry(master=cadastro_frame, placeholder_text='Nome Completo', width=300, font=('Poppins', 14))
            entry_nome.place(x=25, y=105)
            entry_email = ctk.CTkEntry(master=cadastro_frame, placeholder_text='E-mail', width=300, font=('Poppins', 14))
            entry_email.place(x=25, y=145)
            entry_senha = ctk.CTkEntry(master=cadastro_frame, placeholder_text='Senha', width=300, font=('Poppins', 14), show='*')
            entry_senha.place(x=25, y=185)
            entry_telefone = ctk.CTkEntry(master=cadastro_frame, placeholder_text='Telefone', width=300, font=('Poppins', 14))
            entry_telefone.place(x=25, y=225)
            entry_cpf = ctk.CTkEntry(master=cadastro_frame, placeholder_text='CPF', width=300, font=('Poppins', 14))
            entry_cpf.place(x=25, y=265)

            # função para o botão "voltar"
            def voltar_login():
                cadastro_frame.pack_forget()
                login_frame.pack(side=RIGHT)

            def validar_cadastro():
                nome = entry_nome.get()
                email = entry_email.get()
                senha = entry_senha.get()
                telefone = entry_telefone.get()
                cpf = entry_cpf.get()

                if nome == '' or email == '' or senha == '' or telefone == '' or cpf == '':
                    messagebox.showerror('Erro', 'Todos os campos devem ser preenchidos.')
                    return

                if not cpf.isdigit() or len(cpf) != 11:
                    messagebox.showerror('Erro', 'CPF deve conter apenas números e ter 11 dígitos.')
                    return

                if not telefone.isdigit() or len(telefone) != 11:
                    messagebox.showerror('Erro', 'Telefone deve conter apenas números e ter 11 dígitos.')
                    return

                # Se todos os dados são válidos, salve os dados
                perfil = {
                    'nome': nome,
                    'email': email,
                    'senha': senha,
                    'telefone': telefone,
                    'cpf': cpf
                }
                utils.salvar_perfil(perfil)

                # Mostrar mensagem de sucesso
                messagebox.showinfo('Sucesso', 'Cadastro realizado com sucesso!')

                # Retornar para a tela de login
                voltar_login()

            # botao voltar
            button_voltar = ctk.CTkButton(master=cadastro_frame, text='VOLTAR', width=145, fg_color='#CA2521', hover_color='#9F1F1B', command=voltar_login)
            button_voltar.place(x=25, y=305)

            # botao para salvar cadastro
            button_salvar = ctk.CTkButton(master=cadastro_frame, text='CADASTRAR', width=145, fg_color='#CA2521', hover_color='#9F1F1B', command=validar_cadastro)
            button_salvar.place(x=180, y=305)

        button_cadastro = ctk.CTkButton(master=login_frame, text='Cadastre-se', width=150, fg_color='#ECA442', hover_color='#DD993E', command=tela_cadastro)
        button_cadastro.place(x=175, y=325)
Aplication()