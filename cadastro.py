# importando tkinder
import tkinter as tk 
from tkinter import *
from tkinter import font, ttk, messagebox
from tkcalendar import Calendar, DateEntry
from csv import DictWriter
from time import strftime, sleep
import random
from views import add
import os
from datetime import datetime, timedelta





aleatorio = random.randint(100000, 999999)

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
janela1 = Tk()
janela1.title("")
janela1.geometry("1043x453")
janela1.configure(background=co9)
janela1.resizable(width=FALSE, height=FALSE)
style = ttk.Style(janela1)
style.configure('Custom.TRadiobutton', background=co1, font=('Ivy 15 bold'))


##DIVIDINDO A JANELA####
frame_cima1 = Frame(janela1, width=1043, height=50, bg=co2, relief='flat')
frame_cima1.grid(row=0, column=0)

frame_baixo1 = Frame(janela1, width=310, height=403, bg=co1, relief="flat")
frame_baixo1.grid(row=1, column=0, sticky=NSEW, padx=0, pady=1)

frame_direita1 = Frame(janela1, width=588, height=403, bg=co1, relief="flat")
frame_direita1.grid(row=0, column=1, rowspan=2, padx=1, pady=0, sticky=NSEW)

##LABEL EM CIMA####
app_nome = Label(janela1, text='CADASTRO', anchor=NW, font=('Ivy 20 bold'),  bg=co2, fg=co1, relief='flat')
app_nome.place(x=521, y=10)

def time():
    string = strftime('%H:%M:%S')
    e_entrada.config(text=string)
    e_entrada.after(1000, time)
    
def data():
    data_hora_atual = datetime.now()
    data_atual = data_hora_atual.strftime("%d/%m/%Y")
   



def temporizador():
    t = 2
    total_a_pagar = ''

    tempoo = user_type.get()    
    if tempoo == 'MOTO':  # Moto
        total_a_pagar = 'R$ 10,00'
    elif tempoo == 'CARRO PEQUENO':  # Carro Pequeno
        total_a_pagar = 'R$ 20,00'
    elif tempoo == 'CARRO GRANDE':  # Carro Grande
        total_a_pagar = 'R$ 30,00'
    
    while t >= 0:        
        janela1.update()  # Supondo que 'janela' seja uma variável definida em outro lugar
        sleep(1)
        t -= 1
        
    messagebox.showinfo('Tempo', f'O tempo acabou. Total a pagar: {total_a_pagar}')
    
 

### CONFIGURANDO FRAME BAIXO ###
#nome
l_nome = Label(janela1, text='Nome *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=70)
e_nome = Entry(janela1, width=45, justify='left',   relief='solid')
e_nome.place(x=15, y=100)

#sobrenome
l_sobrenome = Label(janela1, text='Sobrenome *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_sobrenome.place(x=400, y=70)
e_sobrenome = Entry(janela1, width=45, justify='left',   relief='solid')
e_sobrenome.place(x=400, y=100)

#email
l_email = Label(janela1, text='Email *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_email.place(x=10, y=140)
e_email = Entry(janela1, width=45, justify='left',   relief='solid')
e_email.place(x=15, y=160)

#marca
l_modelo= Label(janela1, text='Modelo *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_modelo.place(x=400, y=140)
e_modelo = Entry(janela1, width=45, justify='left',   relief='solid')
e_modelo.place(x=400, y=160)

#Telefone
l_tel = Label(janela1, text='Telefone *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_tel.place(x=10, y=200)
e_tel = Entry(janela1, width=45, justify='left',   relief='solid')
e_tel.place(x=15, y=220)


#Placa
l_placa = Label(janela1, text='placa *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_placa.place(x=400, y=200)
e_placa = Entry(janela1, width=45, justify='left',   relief='solid')
e_placa.place(x=400, y=220)

#Data da entrada
l_data = Label(janela1, text='Data entrada *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_data.place(x=10, y=250)
e_data = DateEntry(janela1, width=12, background='darkblue', foreground='white', borderwidth=2, locale='pt_br', year=2024)
e_data.place(x=20, y=270)

#Horario da enntrada
l_entrada = Label(janela1, text='Horario da entrada *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_entrada.place(x=150, y=250)
e_entrada = Label(janela1, font=('Ivy', 15, 'bold'), background=co1, foreground='black') 
e_entrada.place(x=190, y=270)
time() 


#Cor
l_cor = Label(janela1, text='Cor *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_cor.place(x=400, y=250)
e_cor = Entry(janela1, width=45, justify='left',   relief='solid')
e_cor.place(x=400, y=270)



#Sobre
l_obs = Label(janela1, text='Obs *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_obs.place(x=15, y=300)
e_obs = Entry(janela1, width=45, justify='left',   relief='solid')
e_obs.place(x=15, y=320)

#manobrista
l_manobrista = Label(janela1, text='Manobrista *', anchor=NW, font=('Ivy 10 bold'),  bg=co1, fg=co4, relief='flat')
l_manobrista.place(x=400, y=300)
e_manobrista = Entry(janela1, width=45, justify='left',   relief='solid')
e_manobrista.place(x=400, y=320)


l_controle = Label(janela1, text='Controle *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_controle.place(x=750, y=300)
e_controle = Entry(janela1, width=45, justify='left', relief='solid')
e_controle.place(x=750, y=320)
e_controle.insert(0, str(aleatorio))

#-----------carro---------------------#
label = Label(janela1, text="Veiculo", font=('Ivy 18 bold'), background=co1)
label.place(x=900, y=50)

user_type = tk.StringVar()
radiobtn1 = ttk.Radiobutton(janela1, text = 'MOTO', value='MOTO', variable = user_type, style='Custom.TRadiobutton')
radiobtn1.place(x=830, y=100)

radiobtn2 = ttk.Radiobutton(janela1, text = 'CARRO PEQUENO', value='CARRO PEQUENO', variable = user_type, style='Custom.TRadiobutton')
radiobtn2.place(x=830, y=150)

radiobtn3 = ttk.Radiobutton(janela1, text = 'CARRO GRANDE', value='CARRO GRANDE', variable = user_type, style='Custom.TRadiobutton')
radiobtn3.place(x=830, y=200)


#---------------cadastro tempo------------------#
label = Label(janela1, text="Tempo", font=('Ivy 18 bold'), background=co1)
label.place(x=521, y=350)

tempoo = tk.StringVar()
radiobtn4 = ttk.Radiobutton(janela1, text = 'MENSALISTA', value='MENSALISTA', variable = tempoo, style='Custom.TRadiobutton', command=temporizador)
radiobtn4.place(x=350, y=400)

radiobtn5 = ttk.Radiobutton(janela1, text = 'PARADA RAPIDA', value='PARADA RAPIDA', variable = tempoo, style='Custom.TRadiobutton')
radiobtn5.place(x=521, y=400)

radiobtn5 = ttk.Radiobutton(janela1, text = 'ESTACIONAR', value='ESTACIONAR', variable = tempoo, style='Custom.TRadiobutton')
radiobtn5.place(x=710, y=400)

#cadastrar
b_confir = Button(frame_baixo1,  command=lambda: [insert(), 'temporizador()'], text='CADASTRAR', width=39, height=2, font=('Ivy 8 bold'), bg=co2, fg=co1, relief=RAISED, overrelief=RIDGE)
b_confir.place(x=15, y=320)

'''
#criando funções#
def insert():
    nome = e_nome.get()
    sobrenome = e_sobrenome.get()
    telefone = e_tel.get()
    email = e_email.get()
    obs = e_obs.get()
    modelo = e_modelo.get()
    placa = e_placa.get()
    data_entra = e_data.get()
    hora_entra = e_entrada.cget('text')
    cor = e_cor.get()
    manobrista = e_manobrista.get()
    controle = e_controle.get()
    tempo = tempoo.get()
    usertype = user_type.get()
    

    data = [nome, sobrenome, telefone, email, obs, modelo, placa, data_entra, hora_entra, cor, manobrista, controle, usertype, tempo]
    if nome == '' or sobrenome == '' or telefone == '' or email == '' or obs == '' or modelo == '' or placa == '' or data_entra == '' or hora_entra == '' or cor == '' or manobrista == '' or controle == '':
        messagebox.showwarning('data', 'O Campo nao pode ser vazio')
    
    else:
        add(data) 
        messagebox.showinfo('data', 'addicionado')

        e_nome.delete(0, 'end')
        e_sobrenome.delete(0, 'end')
        e_tel.delete(0, 'end')
        e_email.delete(0, 'end')
        e_obs.delete(0, 'end')
        e_modelo.delete(0, 'end')
        e_placa.delete(0, 'end')
        e_data.delete(0, 'end')
        e_entrada.config(text='')
        e_cor.delete(0, 'end')
        e_manobrista.delete(0, 'end')
        e_controle.delete(0, 'end')
        
'''



def insert():
    nome = e_nome.get()
    sobrenome = e_sobrenome.get()
    telefone = e_tel.get()
    email = e_email.get()
    obs = e_obs.get()
    modelo = e_modelo.get()
    placa = e_placa.get()
    data_entra = e_data.get()
    hora_entra = e_entrada.cget('text')
    cor = e_cor.get()
    manobrista = e_manobrista.get()
    controle = e_controle.get()
    tempo = tempoo.get()
    usertype = user_type.get()

    #write to csv file code here
    with open('data.csv', 'a', newline = '') as f:
        dict_writer = DictWriter(f, fieldnames=['nome', 'sobrenome', 'telefone','email','obs','modelo','placa','data_entra','hora_entra','cor','manobrista','controle', 'Tempo', 'User Type'])
        if os.stat('data.csv').st_size == 0:        #if file is not empty than header write else not
            dict_writer.writeheader()
 
       
        dict_writer.writerow({
            'nome' : nome,
            'sobrenome' :  sobrenome,
            'telefone' : telefone,
            'email' : email,
            'obs' : obs,
            'modelo' : modelo,
            'placa' : placa,
            'data_entra' : data_entra,
            'hora_entra' : hora_entra,
            'cor' : cor,
            'manobrista' : manobrista,
            'controle' : controle,
            'Tempo' : tempo,
            'User Type' : usertype,
            

        })

  
janela1.mainloop()


