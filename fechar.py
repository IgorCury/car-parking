# importando tkinder
from tkinter import *
from tkinter import font, ttk, messagebox
from tkcalendar import Calendar, DateEntry
from time import strftime, sleep
from views import add, update
from main import show, view, tree
from datetime import datetime
from csv import DictWriter
from tkinter import Tk, Button, Label, Entry, Text, END
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os


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
#--------------------------------#
####criando janela####
janela3 = Tk()
janela3.title("")
janela3.geometry("800x500")
janela3.configure(background=co9)
janela3.resizable(width=FALSE, height=FALSE)

#--------------------------------------------------------------#

#criando funções#
def insert():

    nome = e_nome.get()
    sobre = e_sobrenome.get()
    telefone = e_tel.get()
    email = e_email.get()
    obs = e_obs.get()
    data_entra = e_data.get()
    hora_entra = e_hora.cget('text')
    controle = e_controle.get()
    marca = e_marca.get()
    placa = e_placa.get()
    cor = e_cor.get()
    mano = e_mano.get()
    usertype = e_veiculo.get()


    data = [nome, sobre, telefone, email, obs, data_entra, hora_entra, controle, marca, placa, cor, mano, usertype]

    if nome == '' or sobre == '' or telefone == '' or email == '' or obs == '' or data_entra == '' or hora_entra == '' or controle == '' or marca == '' or placa == '' or cor == '' or mano == '' or usertype == '':
        messagebox.showwarning('data', 'O Campo nao pode se vazio')
    else:
        add(data)
        messagebox.showinfo('data', 'addicionado')

        e_nome.delete(0, 'end')
        e_sobrenome.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')
        e_obs.delete(0, 'end')
        e_data.delete(0, 'end')
        e_controle.delete(0, 'end')
        e_hora.config(text='')
        e_marca.delete(0, 'end')
        e_placa.delete(0, 'end')
        e_cor.delete(0, 'end')
        e_mano.delete(0, 'end')
        e_veiculo.delete(0, 'end')


#tree
def show():
    
    global tree

    listheader = ['nome', 'sobrenome', 'telefone', 'email', 'obs', 'controle', 'hora_entra', 'data_entra', 'modelo', 'placa', 'cor', 'mano', 'usertype']

    demo_list = view()

    tree = ttk.Treeview(janela3, selectmode="extended", columns=listheader, show="headings")
    
    for item in demo_list:
        tree.insert('', 'end', values=item)


def to_update():
    global label12, label13 

    try: 
        tree_data = tree.focus()
        tree_dictionary = tree.item(tree_data)
        tree_list = tree_dictionary['values']

        # Extrair os valores relevantes
        nome = str(tree_list[0])
        sobre = str(tree_list[1])
        telefone = str(tree_list[2])
        email = str(tree_list[3])
        obs = str(tree_list[4])
        controle = str(tree_list[11])
        
        mano = str(tree_list[10])
        placa = str(tree_list[6])
        cor = str(tree_list[9])
        marca = str(tree_list[5])
        data_entrada = str(tree_list[8])
        hora_entrada = str(tree_list[7])
        usertype = str(tree_list[13])

        e_nome.insert(0, nome)
        e_sobrenome.insert(0, sobre)
        e_tel.insert(0, telefone)
        e_email.insert(0, email)
        e_obs.insert(0, obs)
        e_controle.insert(0, controle)
        e_mano.insert(0, mano)
        e_placa.insert(0, placa)
        e_cor.insert(0, cor)
        e_marca.insert(0, marca)
        e_hora.insert(0, data_entrada)
        e_data.insert(0, hora_entrada)
        e_veiculo.insert(0, usertype)


        data_entrada = tree_list[7]  # Assuming the date of entry is at index 7
        hora_entrada = tree_list[8]
        usertype = tree_list[13]  # As  # Assuming the user type is at index 13
        
        # Calcular o valor a pagar com base no tipo de veículo
        if usertype == "MOTO":
            taxa = 20
        elif usertype == "CARRO PEQUENO":
            taxa = 30
        elif usertype == "CARRO GRANDE":
            taxa = 40
        else:
            # Exibir uma mensagem de erro se o tipo de veículo não for reconhecido
            messagebox.showerror('Erro', 'Tipo de veículo não reconhecido')

        # Convert date and time of entry into datetime objects
        entrada_completa = f"{data_entrada} {hora_entrada}"
        entrada_formatada = datetime.strptime(entrada_completa, '%d/%m/%Y %H:%M:%S')

        # Calcular o tempo decorrido em horas
        hora_atual = datetime.now()
        diferenca_tempo = hora_atual - entrada_formatada
        horas_decorridas = diferenca_tempo.total_seconds() / 3600  # Usar total_seconds() para considerar dias completos

        # Calcular o valor a pagar
        valor = horas_decorridas * taxa

        # Arredondar o valor calculado para duas casas decimais
        valor_arredondado = round(valor, 2)
        hora_arredondada = round(horas_decorridas)

        # Criar o texto para exibir no Label
        texto_label = f'Valor a pagar R$ {valor_arredondado}'
        texto_label1 = f'Hora Estacionada {hora_arredondada}'

        # Criar e colocar o Label
        label12 = Label(janela3, text=texto_label, font=('Ivy 9 bold'))
        label12.place(x=110, y=460)
        
        label13 = Label(janela3, text=texto_label1, font=('Ivy 9 bold'))
        label13.place(x=470, y=460)

    except IndexError:
        messagebox.showerror('Erro', 'Selecione um item da tabela')



   
##DIVIDINDO A JANELA####
frame_cima1 = Frame(janela3, width=1043, height=50, bg=co2, relief='flat')
frame_cima1.grid(row=0, column=0)

frame_baixo1 = Frame(janela3, width=310, height=403, bg=co1, relief="flat")
frame_baixo1.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita1 = Frame(janela3, width=588, height=403, bg=co1, relief="flat")
frame_direita1.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

##LABEL EM CIMA####
app_nome = Label(janela3, text='FINALIZAR', anchor=NW, font=('Ivy 20 bold'),  bg=co2, fg=co1, relief='flat')
app_nome.place(x=360, y=10)

def time():
    string = strftime('%H:%M')
    #e_estado.config(text=string)
    #e_estado.after(1000, time)


### CONFIGURANDO FRAME BAIXO ###
#nome
l_nome = Label(janela3, text='Nome *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=70)
e_nome = Entry(janela3, width=45, justify='left',   relief='solid')
e_nome.place(x=15, y=100)

#sobrenome
l_sobrenome = Label(janela3, text='Sobrenome *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_sobrenome.place(x=400, y=70)
e_sobrenome = Entry(janela3, width=45, justify='left',   relief='solid')
e_sobrenome.place(x=400, y=100)

#email
l_email = Label(janela3, text='Email *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=140)
e_email = Entry(janela3, width=45, justify='left',   relief='solid')
e_email.place(x=15, y=160)

#marca
l_marca = Label(janela3, text='Marca *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_marca.place(x=400, y=140)
e_marca = Entry(janela3, width=45, justify='left',   relief='solid')
e_marca.place(x=400, y=160)

#Telefone
l_tel = Label(janela3, text='Telefone *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_tel.place(x=10, y=200)
e_tel = Entry(janela3, width=45, justify='left',   relief='solid')
e_tel.place(x=15, y=220)


#Placa
l_placa = Label(janela3, text='placa *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_placa.place(x=400, y=200)
e_placa = Entry(janela3, width=45, justify='left',   relief='solid')
e_placa.place(x=400, y=220)

l_veiculo = Label(janela3, text='Veiculo *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_veiculo.place(x=400, y=400)
e_veiculo = Entry(janela3, width=45, justify='left', relief='solid')
e_veiculo.place(x=400, y=420)


#horas e datas
l_hora = Label(janela3, text='Data Entrada *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_hora.place(x=600, y=350)
e_hora = Entry(janela3, width=15, justify='left',   relief='solid')
e_hora.place(x=600, y=370)

l_data = Label(janela3, text='Hora Entrada *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_data.place(x=400, y=350)
e_data = Entry(janela3, width=15, justify='left',   relief='solid')
e_data.place(x=400, y=370)




#Cor
l_cor = Label(janela3, text='Cor *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_cor.place(x=400, y=250)
e_cor = Entry(janela3, width=45, justify='left',   relief='solid')
e_cor.place(x=400, y=270)

time() 

#Sobre
l_obs = Label(janela3, text='Obs *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_obs.place(x=15, y=300)
e_obs = Entry(janela3, width=45, justify='left',   relief='solid')
e_obs.place(x=15, y=320)

#manobrista
l_mano = Label(janela3, text='Manobrista *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_mano.place(x=400, y=300)
e_mano = Entry(janela3, width=45, justify='left',   relief='solid')
e_mano.place(x=400, y=320)


l_controle = Label(janela3, text='Controle *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_controle.place(x=15, y=250)
e_controle = Entry(janela3, width=45, justify='left', relief='solid')
e_controle.place(x=15, y=270)

#---------------cadastro tempo------------------#
Valor = Label(janela3, text="TOTAL", font=('Ivy 18 bold'), background=co1)
Valor.place(x=15, y=470)
#-------------------------------------------------#

#cadastrar
b_validar = Button(janela3, command=to_update, text='VALIDAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_validar.place(x=15, y=350)



#cadastrar
b_pdf = Button(janela3, text='VALIDAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_pdf.place(x=15, y=400)


####-------------------------PDF_____________________----------#



janela3.mainloop()

