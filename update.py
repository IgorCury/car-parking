# importando tkinder
from tkinter import *
from tkinter import font, ttk, messagebox
from tkcalendar import Calendar, DateEntry
from time import strftime, sleep
from views import add, update
from main import show, view, tree

###cores###
co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#ef5350"
co8 = "#263238"
co9 = "#e9edf5"


####criando janela####
janela2 = Tk()
janela2.title("")
janela2.geometry("1043x453")
janela2.configure(background=co9)
janela2.resizable(width=FALSE, height=FALSE)

#criando funções#

def insert():
    nome = e_nome.get()
    telefone = e_tel.get()
    email = e_email.get()
    obs = e_obs.get()

    data = [nome,  telefone, email, obs]

    if nome == '' or telefone == '' or email == '' or obs == '':
        messagebox.showwarning('data', 'O Campo nao pode se vazio')
    else:
        add(data)
        messagebox.showinfo('data', 'addicionado')

        e_nome.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')
        e_obs.delete(0, 'end')
#tree
def show():
    
    global tree

    listheader = ['nome', 'telefone', 'email', 'obs']

    demo_list = view()

    tree = ttk.Treeview(janela2, selectmode="extended", columns=listheader, show="headings")
    
    for item in demo_list:
        tree.insert('', 'end', values=item)

def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        nome = str(tree_list[0])
        telefone = str(tree_list[1])
        email = str(tree_list[2])
        obs = str(tree_list[3])

        e_nome.insert(0, nome)
        e_tel.insert(0, telefone)
        e_email.insert(0, email)
        e_obs.insert(0, obs)

        def confirm():
            new_nome = e_nome.get()
            new_telefone = e_tel.get()
            new_email = e_email.get()
            new_obs = e_obs.get()

            data = [new_telefone, new_nome, new_telefone, new_email, new_obs]

            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_obs.delete(0, 'end')

            for widget in janela2.winfo_children():
                widget.destroy()

            b_confirm.destroy()
            show()

        b_confirm = Button(janela2, text="Confirm", width=10, height=1, bg=co2, fg = co0, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x = 10, y = 10)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')





##DIVIDINDO A JANELA####
frame_cima1 = Frame(janela2, width=1043, height=50, bg=co2, relief='flat')
frame_cima1.grid(row=0, column=0)

frame_baixo1 = Frame(janela2, width=310, height=403, bg=co1, relief="flat")
frame_baixo1.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita1 = Frame(janela2, width=588, height=403, bg=co1, relief="flat")
frame_direita1.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

##LABEL EM CIMA####
app_nome = Label(janela2, text='ATUALIZAR', anchor=NW, font=('Ivy 20 bold'),  bg=co2, fg=co1, relief='flat')
app_nome.place(x=521, y=10)

def time():
    string = strftime('%H:%M')
    e_estado.config(text=string)
    e_estado.after(1000, time)


def temporizador():
    t = 5
    total_a_pagar = ''

    escolha = var.get()    
    if escolha == 1:  # Moto
        total_a_pagar = 'R$ 10,00'
    elif escolha == 2:  # Carro Pequeno
        total_a_pagar = 'R$ 20,00'
    elif escolha == 3:  # Carro Grande
        total_a_pagar = 'R$ 30,00'
    
    while t >= 0:        
        janela2.update()  # Supondo que 'janela' seja uma variável definida em outro lugar
        sleep(1)
        t -= 1
        
    messagebox.showinfo('Tempo', f'O tempo acabou. Total a pagar: {total_a_pagar}')



### CONFIGURANDO FRAME BAIXO ###
#nome
l_nome = Label(janela2, text='Nome *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=70)
e_nome = Entry(janela2, width=45, justify='left',   relief='solid')
e_nome.place(x=15, y=100)

#sobrenome
l_sobrenome = Label(janela2, text='Sobrenome *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_sobrenome.place(x=400, y=70)
e_sobrenome = Entry(janela2, width=45, justify='left',   relief='solid')
e_sobrenome.place(x=400, y=100)

#email
l_email = Label(janela2, text='Email *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=140)
e_email = Entry(janela2, width=45, justify='left',   relief='solid')
e_email.place(x=15, y=160)

#marca
l_marca = Label(janela2, text='Marca *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_marca.place(x=400, y=140)
e_marca = Entry(janela2, width=45, justify='left',   relief='solid')
e_marca.place(x=400, y=160)

#Telefone
l_tel = Label(janela2, text='Telefone *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_tel.place(x=10, y=200)
e_tel = Entry(janela2, width=45, justify='left',   relief='solid')
e_tel.place(x=15, y=220)


#Placa
l_placa = Label(janela2, text='placa *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_placa.place(x=400, y=200)
e_placa = Entry(janela2, width=45, justify='left',   relief='solid')
e_placa.place(x=400, y=220)

#Data da entrada
l_data = Label(janela2, text='Data entrada *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_data.place(x=10, y=250)
e_data = DateEntry(janela2, width=12, background='darkblue', foreground='white', borderwidth=2, locale='pt_br', year=2024)
e_data.place(x=20, y=270)

#Horario da enntrada
e_estado = Label(janela2, text='Horario da entrada *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
e_estado.place(x=150, y=250)
e_estado = Label(janela2, font=('Ivy', 15, 'bold'), background=co1, foreground='black') 
e_estado.place(x=190, y=270)

time()

#Cor
l_placa = Label(janela2, text='Cor *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_placa.place(x=400, y=250)
e_placa = Entry(janela2, width=45, justify='left',   relief='solid')
e_placa.place(x=400, y=270)



#Sobre
l_obs = Label(janela2, text='Obs *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_obs.place(x=15, y=300)
e_obs = Entry(janela2, width=45, justify='left',   relief='solid')
e_obs.place(x=15, y=320)

#manobrista
l_obs = Label(janela2, text='Manobrista *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_obs.place(x=400, y=300)
e_obs = Entry(janela2, width=45, justify='left',   relief='solid')
e_obs.place(x=400, y=320)


l_controle = Label(janela2, text='Controle *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_controle.place(x=750, y=300)
e_controle = Entry(janela2, width=45, justify='left', relief='solid')
e_controle.place(x=750, y=320)


#-----------carro---------------------#
label = Label(janela2, text="Veiculo", font=('Ivy 18 bold'), background=co1)
label.place(x=900, y=50)

var = IntVar()
R1 = Radiobutton(janela2, text="Moto", variable=var, value=1, font=('Ivy 12 bold '), background=co1)
R1.place(x=850, y=100)
R2 = Radiobutton(janela2, text="Carro Pequeno", variable=var, font=('Ivy 12 bold'), value=2,  background=co1)
R2.place(x=850, y=150)
R3 = Radiobutton(janela2, text="Carro Grande", variable=var, font=('Ivy 12 bold '), value=3,  background=co1)
R3.place(x=850, y=200)

#---------------cadastro tempo------------------#
label = Label(janela2, text="Tempo", font=('Ivy 18 bold'), background=co1)
label.place(x=521, y=350)

escolha = IntVar()
R4 = Radiobutton(janela2, text="Mensalista", variable=escolha, value=4, font=('Ivy 12 bold '), background=co1)
R4.place(x=350, y=400)
R5 = Radiobutton(janela2, text="Parada Rápida", variable=escolha, font=('Ivy 12 bold'), value=5, background=co1, command=temporizador)
R5.place(x=521, y=400)
R6 = Radiobutton(janela2, text="Estacionar", variable=escolha, font=('Ivy 12 bold '), value=6,  background=co1)
R6.place(x=710, y=400)

#cadastrar
b_confir = Button(frame_baixo1, command=to_update, text='ATUALIZAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confir.place(x=15, y=320)



