from Logic.Crud import *
from Ui.Interfata import afisare_lista
import datetime

def read_list():
    lista = []
    lst_str = input("Introduceti comanda respectand instructiunile date: ")
    lst_str_split = lst_str.split(',')
    for comanda in lst_str_split:
        lista.append(comanda)
    return lista
def afisare_adaugare(lista,comanda):
    """

    :param lista: lista cu cheltuielei
    :return: se adauga cheltuiala creata in logic
    """
    try:
        id=comanda[1]
        nr_apartament = comanda[2]
        suma = comanda[3]
        data = comanda[4]
        tipul = comanda[5]
        return adaugare_cheltuiala(lista, id, nr_apartament, suma, data, tipul)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def afisare_stergere(lista,comanda):
    '''
    :param lista: o lista cu cheltuieli
    :return: se sterge o cheltuiala din lista
    '''
    try:
        nr_apartament = comanda[1]
        return stergere_cheltuiala(nr_apartament, lista)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def afisare_modificare(lista,comanda):
    '''
    :param lista:lista de cheltuieli
    :return: se modifica lista
    '''
    try:
        id=comanda[1]
        nr_apartament =int(comanda[2])
        suma = float(comanda[3])
        data = int(comanda[4])
        tipul = input(comanda[5])
        return modificare_cheltuiala(lista,id, nr_apartament, suma, data, tipul)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def interfata_menu(lista):
    while True:
        print("Intr-o linie de comanda se vor scrie comenzile "
              "care se vor aplica listei, separate prin ',', elementele acestora fiind separate prin ","")
        print("Atentie ! Comanda se face scrie cu majuscula.")
        print("O comanda care nu se regaseste in lista de mai jos nu va duce la modificarea listei.")
        print("O comanda trebuie sa aiba toate campurile nenule \n ")

        print("1.Pentru adaugare cheltuiala in lista: Adaugare, id,nr_apartament,suma,data(AAAA.LL.ZZ),tipul(canal,intretinere sau alte cheltuieli ")
        print("2.Pentru stergerea unei cheltuieli: Sterge, nr_apartament")
        print("3.Pentru modificarea unei cheltuieli: Modificare, id,nr_apartament,suma,data(AAAA.LL.ZZ),tipul")
        print("4.Pentru afisarea tuturor cheltuielilor: Afisare")
        print("5. Pentru a iesire din meniu: Exit (la final)")
        lista = read_list()
        for comanda in lista:
            comanda_lista = comanda.split(',')
            if (comanda_lista[0] == 'Adaugare'):
                lista=afisare_adaugare(lista,comanda)
            elif (comanda_lista[0] == 'Sterge'):
                lista=afisare_stergere(lista,comanda)
            elif (comanda_lista[0] == 'Modificare'):
                lista=afisare_modificare(lista,comanda)
            elif (comanda_lista[0] == 'Afisare'):
                afisare_lista(lista)
        if 'Exit' in lista:
            break