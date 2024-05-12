# importando tkinder
from tkinter import *
from tkinter import font
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from views import *
from tkinter import messagebox
import csv


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
#-------------------------------------------------------#



def view(selected_columns):
    filtered_data = []

    with open('data.csv', 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        
        # Ignora a primeira linha (cabeçalhos das colunas)
        next(reader)
        
        # Itera sobre as linhas do arquivo CSV
        for row in reader:
            # Verifica se a coluna correspondente à categoria "mensalista" é igual a "MENSALISTA"
            if row[12].strip().upper() == "MENSALISTA":
                selected_row = [row[column] for column in selected_columns if column < len(row)]
                filtered_data.append(selected_row)               

    return filtered_data

selected_columns = [0,  1, 2 , 6, 11 ,12]
data = view(selected_columns)
print(data)

[0,  1, 2 , 6, 11 ,12]

#---------------------separa---------------------------#
global tree

###Funcao Inserir####
#functions
def show():

    global tree

    listheader = ['nome', 'sobrenome', 'telefone', 'placa', 'controle', 'mensalista']

    #data = view()
    
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
    tree.heading(3, text= 'placa', anchor=NW)    
    tree.heading(4, text= 'controle', anchor=NW)    
    tree.heading(5, text= 'mensalista', anchor=NW)    

   
    # tree  columns
    tree.column(0, width=100, anchor='nw')
    tree.column(1, width=100, anchor='nw')
    tree.column(2, width=100, anchor='nw')
    tree.column(3, width=100, anchor='nw')    
    tree.column(4, width=100, anchor='nw')
    tree.column(5, width=100, anchor='nw')
    #tree.column(6, width=50, anchor='nw')   
    

    # Defina as tags com diferentes estilos de texto
    tree.tag_configure('oddrow', foreground='red')

    # Iterate through the rows and apply tags based on the row index
    for i, item in enumerate(data):
        if i % 2 == 0:
            tree.insert('', 'end', values=item, tags=('oddrow',))
        else:
            tree.insert('', 'end', values=item, tags=('oddrow',))

'''
    for item in demo_list:
        tree.insert('', 'end', values=item)
'''
show()
'''
def to_update():
    try:
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        Name = str(tree_list[0])
        Gender = str(tree_list[1])
        Telephone = str(tree_list[2])
        Email = str(tree_list[3])

        e_nome.insert(0, Name)
        e_email.insert(0, Gender)
        e_tel.insert(0, Telephone)
        e_obs.insert(0, Email)

        def confirm():
            new_name = e_nome.get()
            new_gender = e_email.get()
            new_telephone = e_tel.get()
            new_email = e_obs.get()

            data = [new_telephone, new_name, new_gender, new_telephone, new_email]

            update(data)

            messagebox.showinfo('Success', 'data updated successfully')

            e_nome.delete(0, 'end')
            e_email.delete(0, 'end')
            e_tel.delete(0, 'end')
            e_obs.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            b_confirm.destroy()


            show()
            
        b_confirm =  Button(frame_baixo, text="Confirm", width=10, height=1, bg=co2, fg = co0, font=('Ivy 8 bold'), command=confirm)
        b_confirm.place(x = 290, y = 110)

    except IndexError:
        messagebox.showerror('Error', 'Select one of them from the table')
'''


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

#pesquisa
b_pesquisa = Button(frame_baixo, command=to_search, text='PESQUISAR', width=10, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_pesquisa.place(x=10, y=55)
#---------------------------------------------------------##

#bota_fechamento
b_cadastro = Button(frame_baixo, command='', text='FATURA', width=15, font=('Ivy 14 bold'),  bg=co5, fg=co1, relief='raised', overrelief='ridge')
b_cadastro.place(x=30, y=200)


#--------------------##
#atualizar banco
b_view = Button(frame_baixo, text="BANCO", width=10, height=1, bg=co2, fg = co0,font=('Ivy 8 bold'), command = show)
b_view.place(x=100, y=55)
#----------------------##

janela.mainloop()

