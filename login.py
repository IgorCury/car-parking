from tkinter import *
from tkinter import messagebox
#--- cores
co0 = "#f0f3f5"  # black
co1 = "#feffff"  # white
co2 = "#3fb5a3"  # green
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra

# Função principal
def main():
    import main

# Função para exibir a janela de login
def exibir_janela_login():
    # criandoJanela --------------------
    janela = Tk()
    janela.title('')
    janela.geometry('310x300')
    janela.configure(background=co1)
    janela.resizable(width=False, height=False)

    # Divindo janela------------------------------
    frame_cima = Frame(janela, width=310, height=50, bg=co1, relief='flat')
    frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

    frame_baixo = Frame(janela, width=310, height=250, bg=co1, relief='flat')
    frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)


    # ConfigurandoFrame---------------------------------
    l_nome = Label(frame_cima, text='LOGIN', anchor=NE, font=('Ivy 25'), bg=co1, fg=co4)
    l_nome.place(x=5, y=5)

    l_linha = Label(frame_cima, text='', width=275, anchor=NW, font=('Ivy 1'), bg=co2, fg=co4)
    l_linha.place(x=10, y=45)

    # credenciais---------------------------------
    crend = ['igor', '123456789']

    def verifica_senha():
        nome = e_nome.get()
        senha = e_pass.get()

        if nome == 'admin' and senha == 'admin':
            messagebox.showinfo('Login', 'Seja bem-vindo Admin!')
            janela.destroy()
            main()  # Chamar a função main após fechar a janela
        elif crend[0] == nome and crend[1] == senha:
            messagebox.showinfo('Login', f'Seja bem-vindo de volta, {crend[0]}!')
            janela.destroy()
            main()  # Chamar a função main após fechar a janela
        else:
            messagebox.showwarning('Erro', 'Verifique o nome de usuário ou senha.')

    # ConfigurandoFrameBaixo---------------------------------
    l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_nome.place(x=10, y=20)
    e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 15), highlightthickness=1, relief='solid')
    e_nome.place(x=14, y=50)

    l_pass = Label(frame_baixo, text='Senha *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
    l_pass.place(x=10, y=95)
    e_pass = Entry(frame_baixo, width=25, justify='left', show='*', font=('', 15), highlightthickness=1, relief='solid')
    e_pass.place(x=14, y=130)

    b_confir = Button(frame_baixo, command=verifica_senha, text='ENTRAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
    b_confir.place(x=15, y=180)

    janela.mainloop()

exibir_janela_login()
