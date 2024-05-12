import sys
import csv
import re


def add(i):
    
    with open('data.csv', 'a+', newline='') as file:
        write = csv.writer(file)
        write.writerow(i)
    


def view():
    data = []
    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    print(data)
    return data 


#view()

def remove(i):

    def save(j):
        with open('data.csv', 'w', newline='') as file:
             writer = csv.writer(file) 
             writer.writerows(j)

    new_list = []
    telefone = i

    with open('data.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)

            for element in row:
                if element == telefone:
                    new_list.remove(row)
    save(new_list)

#remove('54231')
#view()
def update(i):
    def update_newlist(j):
        with open('data.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(j)

    new_list = []
    telefone = i[3]  # Definindo o telefone antes de usá-lo
    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            new_list.append(row)
            for element in row:
                if element == telefone:
                    nome = i[1]
                    telefone = i[2]
                    email = i[3]
                    obs = i[4]
                    
                    data = [nome, telefone, email, obs]
                    index = new_list.index(row)
                    new_list[index] = data

    update_newlist(new_list)

#sample = ['123', 'girlcoder', 'F', '123', 'girl123@gmail.com']
#update(sample)

def search(i):
    data = []
    telefone = i

    with open('data.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for element in row:
                if element == telefone:
                    data.append(row)
    print(data)
    return data
search('123')
