from Domain.Cheltuiala import *
def adaugare_cheltuiala(lista, nr_apartament,suma,data,tipul):

    cheltuiala = creare_cheltuiala(nr_apartament,suma,data,tipul)
    rezultat = lista + [cheltuiala]
    return rezultat
def stergere_cheltuiala(nr_apartament,lista):
    new_cheltuieli=[]
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala)!=nr_apartament:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli

def modificare_cheltuiala(lista,new_cheltuiala):
    lista_modificata=[]
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) != get_nr_apartament(new_cheltuiala):

            lista_modificata.append(cheltuiala)
        else:
            lista_modificata.append(new_cheltuiala)

    return lista_modificata
