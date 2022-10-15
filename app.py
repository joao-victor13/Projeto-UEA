from tkinter import *
from tkinter import messagebox
import requests

class Aplication:
        def __init__(self, master=None):
            
            # Frames -----------------

            self.frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat' )
            self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
            self.frame_baixo = Frame(janela, width=310, height=250, bg=cor1, relief='flat')
            self.frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


            # configurando frame_cima

            self.l_name = Label(self.frame_cima, text='LOGIN', height=1, anchor=NE, font=('SegoeUI 25 bold italic'), bg=cor1, fg=cor4)
            self.l_name.place(x=5, y=5)

            self.l_line = Label(self.frame_cima, width=275, text='', height=1, anchor=NW, font=('Ivy 1 '), bg=cor2)
            self.l_line.place(x=10, y=45)

            # configurando frame_baixo

            self.l_name = Label(self.frame_baixo, text='Usuário:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
            self.l_name.place(x=10, y=20)
            self.e_name = Entry(self.frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', textvariable=nome)
            self.e_name.place(x=14, y=50)

            self.l_pass = Label(self.frame_baixo, text='Senha:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
            self.l_pass.place(x=10, y=95)
            self.e_pass = Entry(self.frame_baixo, show='*', width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', textvariable=senha)
            self.e_pass.place(x=15, y=130)

            self.without_login = Label(self.frame_baixo, text="Ainda não tem cadastro? Criar uma conta", height=1, anchor=NE, font=('Ivy 10'), bg=cor1, fg=cor5)
            self.without_login.bind("<Button-1>", self.goto_register)
            self.without_login.place(x=14, y=170)

            self.button_confirm = Button(self.frame_baixo, text='ENTRAR', width=39, height=2, bg=cor2, fg=cor1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
            self.button_confirm["command"] = self.verificar_senha
            self.button_confirm.place(x=15, y=200)


        def register(self):
            nomeInput = new_nome.get()
            senhaInput = new_senha.get()

            api_url = "http://127.0.0.1:5000/usuario/cadastrar"
            data = {
                "usuario": nomeInput,
                "senha": senhaInput
            }

            request = requests.post(url=api_url, json=data)

            
            if request.status_code == 201:
                messagebox.showinfo("Sucesso", "Usuário foi cadastrado com sucesso")

            elif request.status_code == 409:
                messagebox.showerror("Erro", "Usuário já cadastrado")

            else:
                messagebox.showerror("Erro", "Erro ao cadastrar usuário")
                

        def register_page(self):

            self.l_name = Label(self.frame_cima, text='REGISTRE-SE', height=1, anchor=NE, font=('SegoeUI 25 bold italic'), bg=cor1, fg=cor4)
            self.l_name.place(x=5, y=5)

            self.l_line = Label(self.frame_cima, width=275, text='', height=1, anchor=NW, font=('Ivy 1'), bg=cor2)
            self.l_line.place(x=10, y=45)
            
            self.l_name = Label(self.frame_baixo, text='Crie um nome de usuário:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
            self.l_name.place(x=10, y=20)
            self.e_name = Entry(self.frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', textvariable=new_nome)
            self.e_name.place(x=14, y=50)

            self.l_pass = Label(self.frame_baixo, text='Crie uma senha:', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
            self.l_pass.place(x=10, y=95)
            self.e_pass = Entry(self.frame_baixo, show='*', width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', textvariable=new_senha)
            self.e_pass.place(x=15, y=130)

            self.button_confirm = Button(self.frame_baixo, text='REGISTRAR', width=39, height=2, bg=cor2, fg=cor1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
            self.button_confirm["command"] = self.register
            self.button_confirm.place(x=15, y=180)

        def goto_register(self, event):
            for widget in self.frame_cima.winfo_children():
                widget.destroy()

            for widget in self.frame_baixo.winfo_children():
                widget.destroy()
                self.register_page()

        def nova_janela(self, nome):

            l_name = Label(self.frame_baixo, text='Seja bem vindo,', height=1, anchor=NE, font=('SegoeUI 15 bold italic'), bg=cor1, fg=cor4)
            l_name_user = Label(self.frame_baixo, text=nome, height=1, anchor=NE, font=('SegoeUI 15 bold italic'), bg=cor1, fg=cor4)
            
            l_name.place(x=75, y=75)
            l_name_user.place(x=75, y=100)


        def verificar_senha(self):
            nomeInput = nome.get()
            senhaInput = senha.get()

            api_url = "http://127.0.0.1:5000/usuario/autenticar"
            data = {
                "usuario": nomeInput,
                "senha": senhaInput
            }

            request = requests.post(url=api_url, json=data)

            if request.status_code == 200:
                for widget in self.frame_cima.winfo_children():
                    widget.destroy()

                for widget in self.frame_baixo.winfo_children():
                    widget.destroy()
                    self.nova_janela(nomeInput)

            else:
                messagebox.showerror("Erro", "Verifique o nome de usuário ou a senha")


# cores --------------------
 
cor0 = '#f0f3f5' # Preta
cor1 = '#feffff' # Branca
cor2 = '#3fb5a3' # Verde
cor3 = '#38576b' # Valor 
cor4 = '#403d3d' # letra
cor5 = '#00008b' # criar-conta

# criando janela -----------

janela = Tk ()
janela.title ('Tela de Login')
janela.geometry('310x300')
janela.resizable(width=False, height=False)
janela.configure(background = cor1)

nome = StringVar()
senha = StringVar()

new_nome = StringVar()
new_senha = StringVar()

Aplication(janela)
janela.mainloop()