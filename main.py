# importando tkinder
from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from views import *
from tkinter import messagebox


###cores###
co0 = "#f0f3f5" #BRANCO
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d"
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#ef5350"
co8 = "#263238"
co9 = "#e9edf5"

#para chamar outra janela fazer este def e depois para nao dar conflito a janela do menu nao pode ser igual a janela de cadastro ou etc
def cadastro1():
    import cadastro

def atualizar():
    import update

def fatura():
    import faturamento

def fechamento():
    import fechar

   

####criando janela####
janela = Tk()
janela.title("")
janela.geometry("1043x453")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

##DIVIDINDO A JANELA####
frame_cima = Frame(janela, width=310, height=50, bg=co6, relief='flat')
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=403, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief="flat")
frame_direita.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

##LABEL EM CIMA####
app_nome = Label(frame_cima, text='MENU', anchor=NW, font=('Ivy 18 bold'),  bg=co6, fg=co1, relief='flat')
app_nome.place(x=110, y=10)


global tree

###Funcao Inserir####
#functions
def show():
    
    global tree

    listheader = ['nome', 'sobrenome', 'telefone', 'email', 'obs', 'modelo', 'placa', 'data_entra', 'hora_entra', 'data_sai', 'hora_sai', 'cor', 'manobrista', 'controle', 'mensalista', 'parada_rap', 'esta', 'veiculo']

    demo_list = view()
    
    tree = ttk.Treeview(frame_direita, selectmode="extended", columns=listheader, show="headings")

    vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    tree.bind('<Configure>', lambda e: tree.columnconfigure(0, minsize=e.width))
    #tree head
    tree.heading(0, text= 'nome', anchor=NW)
    tree.heading(1, text= 'sobrenome', anchor=NW)
    tree.heading(2, text= 'telefone', anchor=NW)
    tree.heading(3, text= 'email', anchor=NW)    
    tree.heading(4, text= 'obs', anchor=NW)
    tree.heading(5, text= 'modelo', anchor=NW)
    tree.heading(6, text= 'placa', anchor=NW)
    tree.heading(7, text= 'data_entra', anchor=NW)
    tree.heading(8, text= 'hora_entra', anchor=NW)
    tree.heading(9, text= 'cor', anchor=NW)
    tree.heading(10, text= 'manobrista', anchor=NW)
    tree.heading(11, text= 'controle', anchor=NW)
    tree.heading(12, text= 'hora_entrada', anchor=NW)
    tree.heading(13, text= 'hora_saida', anchor=NW)
    tree.heading(14, text= 'mensalista', anchor=NW)
    tree.heading(15, text= 'parada_rap', anchor=NW)
    tree.heading(16, text= 'esta', anchor=NW)
    tree.heading(17, text= 'User type', anchor=NW)
    #tree.heading(18, text= 'carro_pequeno', anchor=NW)
    #tree.heading(19, text= 'carro_grande', anchor=NW)
   
    # tree  columns
    tree.column(0, width=50, anchor='nw')
    tree.column(1, width=50, anchor='nw')
    tree.column(2, width=50, anchor='nw')
    tree.column(3, width=50, anchor='nw')    
    tree.column(4, width=50, anchor='nw')
    tree.column(5, width=50, anchor='nw')
    tree.column(6, width=50, anchor='nw')
    tree.column(7, width=50, anchor='nw')
    tree.column(8, width=50, anchor='nw')
    tree.column(9, width=50, anchor='nw')
    tree.column(10, width=50, anchor='nw')
    tree.column(11, width=50, anchor='nw')
    tree.column(12, width=50, anchor='nw')
    tree.column(13, width=50, anchor='nw')
    tree.column(14, width=50, anchor='nw')
    #tree.column(15, width=50, anchor='nw')
    #tree.column(16, width=50, anchor='nw')
   
  

    for item in demo_list:
        tree.insert('', 'end', values=item)

show()
'''
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

            for widget in janela.winfo_children():
                widget.destroy()

            b_confirm.destroy()
            show()

            for widget in frame_direita.winfo_children():
                widget.destroy()

            b_confirm.destroy()


            show()
            
        b_confirm =  Button(frame_baixo, text="Confirm", width=10, height=1, bg=co2, fg = co0, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x = 290, y = 110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

def to_remove():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']
        tree_telephone = str(tree_list[2])

        remove(tree_telephone)  # Certifique-se de que a função remove esteja definida

        messagebox.showinfo('Sucesso', 'Deletado')

        for widget in frame_direita.winfo_children():
            widget.destroy()
    
    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')

        show()
'''

def to_search():
    telefone = e_search.get()

    data = search(telefone)

    def delete_command():
        tree.delete(*tree.get_children())

    delete_command()

    for item in data:
        tree.insert('', 'end', values = item)
        
    e_search.delete(0, 'end')


### CONFIGURANDO FRAME BAIXO ###

l_search = Label(frame_baixo, text='Pesquisa *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_search.place(x=10, y=10)
e_search = Entry(frame_baixo, width=45, justify='left',   relief='solid')
e_search.place(x=10, y=30)


#botão atualizar
b_cadastro1 = Button(frame_baixo, command=atualizar, text='ATUALIZAR', width=15, font=('Ivy 14 bold'),  bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_cadastro1.place(x=30, y=150)

#bota_cadastro
b_cadastro = Button(frame_baixo, command=cadastro1, text='CADASTRO', width=15, font=('Ivy 14 bold'),  bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_cadastro.place(x=30, y=100)

#bota_fechamento
b_cadastro = Button(frame_baixo, command=fatura, text='FATURA', width=15, font=('Ivy 14 bold'),  bg=co5, fg=co1, relief='raised', overrelief='ridge')
b_cadastro.place(x=30, y=200)

#bota_fechamento
b_fechar = Button(frame_baixo, command=fechamento, text='FECHAR', width=15, font=('Ivy 14 bold'),  bg=co3, fg=co1, relief='raised', overrelief='ridge')
b_fechar.place(x=30, y=250)

#pesquisa
b_pesquisa = Button(frame_baixo, command=to_search, text='PESQUISAR', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_pesquisa.place(x=10, y=55)

#atualizar banco
b_view = Button(frame_baixo, text="BANCO", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command = show)
b_view.place(x=100, y=55)


janela.mainloop()


