from Domain.Cheltuiala import *
def adaugare_cheltuiala(lista,id, nr_apartament,suma,data,tipul):
    '''
    Adaugam o prajitura in lista
    :param lista:lista cu cheltuieli
    :param nr_apartament: nr apartamentului acestei cheltuieli
    :param suma: suma cheltuieli
    :param data: data in care se produce cheltuiala
    :param tipul: tipul de cheltuiala
    :return: o lista cu cheltuieli
    '''
    cheltuiala = creare_cheltuiala(id,nr_apartament,suma,data,tipul)
    rezultat = lista + [cheltuiala]
    return rezultat
def stergere_cheltuiala(nr_apartament,lista):
    '''
    Se sterge o cheltuiala cu nr de apartament care se da
    :param nr_apartament: nr apartamentului care se sterge
    :param lista: lista cu cheltuieli
    :return: lista dupa stergere
    '''
    new_cheltuieli=[]
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala)!=nr_apartament:
            new_cheltuieli.append(cheltuiala)
    return new_cheltuieli

def modificare_cheltuiala(lista,new_cheltuiala):
    '''

    :param lista:o lista cu cheltuieli
    :param new_cheltuiala: o lista cu noua cheltuiala
    :return: lista dupa modificare
    '''
    lista_modificata=[]
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala) != get_nr_apartament(new_cheltuiala):

            lista_modificata.append(cheltuiala)
        else:
            lista_modificata.append(new_cheltuiala)

    return lista_modificata
