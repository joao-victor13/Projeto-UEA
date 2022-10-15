from tkinter import *
from tkinter import messagebox

class Aplication:
        def __init__(self, master=None):
            
            # Frames -----------------

            self.frame_cima = Frame(janela, width=310, height=50, bg=cor1, relief='flat' )
            self.frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)
            self.frame_baixo = Frame(janela, width=310, height=300, bg=cor1, relief='flat')
            self.frame_baixo.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)


            # configurando frame_cima

            self.l_name = Label(self.frame_cima, text='LOGIN', height=1, anchor=NE, font=('Ivy 25 '), bg=cor1, fg=cor4)
            self.l_name.place(x=5, y=5)

            self.l_line = Label(self.frame_cima, width=275, text='', height=1, anchor=NW, font=('Ivy 1 '), bg=cor2)
            self.l_line.place(x=10, y=45)



            # configurando frame_baixo

            self.l_name = Label(self.frame_baixo, text='Nome *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
            self.l_name.place(x=10, y=20)
            self.e_name = Entry(self.frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', textvariable=nome)
            self.e_name.place(x=14, y=50)

            self.l_pass = Label(self.frame_baixo, text='Password *', height=1, anchor=NW, font=('Ivy 10 bold'), bg=cor1, fg=cor4)
            self.l_pass.place(x=10, y=95)
            self.e_pass = Entry(self.frame_baixo, show='*', width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid', textvariable=senha)
            self.e_pass.place(x=15, y=130)

            self.button_confirm = Button(self.frame_baixo, text='ENTRAR', width=39, height=2, bg=cor2, fg=cor1, font=('Ivy 8 bold'), relief=RAISED, overrelief=RIDGE)
            self.button_confirm["command"] = self.verificar_senha
            self.button_confirm.place(x=15, y=180)

        
        def nova_janela(self, nome, senha):

            l_name = Label(self.frame_baixo, text='Seja bem vindo ' + nome, height=1, anchor=NE, font=('Ivy 15'), bg=cor1, fg=cor4)
            l_name.place(x=50, y=25)


        def verificar_senha(self):
            nomeInput = nome.get()
            senhaInput = senha.get()

            if nomeInput == 'admin' and senhaInput == 'admin':
                for widget in self.frame_baixo.winfo_children():
                    widget.destroy()
                    self.nova_janela(nomeInput, senhaInput)
                    

            else:
                messagebox.showerror("Erro", "Verifique o nome de usuário ou a senha");


# cores --------------------
 
cor0 = '#f0f3f5' # Preta
cor1 = '#feffff' # Branca
cor2 = '#3fb5a3' # Verde
cor3 = '#38576b' # Valor 
cor4 = '#403d3d' # letra

# criando janela -----------

janela = Tk ()
janela.title ('Tela de Login')
janela.geometry('310x250')
janela.resizable(width=False, height=False)
janela.configure(background = cor1)

nome = StringVar()
senha = StringVar()


Aplication(janela)
janela.mainloop()