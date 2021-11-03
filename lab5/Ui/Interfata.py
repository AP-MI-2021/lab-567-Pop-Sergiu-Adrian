from Logic.Crud import *
from Domain.Cheltuiala import *
from Logic.Operatii import *
import datetime


def arata_meniu():
    '''

    :return: optiunile din meniu
    '''
    print("1.Adaugare cheltuiala")
    print("2.Stergere cheltuiala")
    print("3.Modificare cheltuiala")
    print("4.Adaugre suma pentru toate cheltuielile dintr-o data citita de la tastatura")
    print("5.Afisarea cheltuielilor cu suma cea mai mare pentru fiecare tip")
    print("6.Ordonarea cheltuielilor crescator dupa suma")
    print("7.Afisare lista")
    print("0.Iesire")

def citire_data():
    date_str=input("Dati data separate prin spatiu")
    data=date_str.split(" ")
    an=int(data[0])
    luna=int(data[1])
    zi=int(data[2])
    return datetime.date(an,luna,zi)
def afisare_adaugare(lista):
    """

    :param lista: lista cu cheltuielei
    :return: se adauga cheltuiala creata in logic
    """
    try:
        id=int(input("Dati id :"))
        nr_apartament = int(input('Dati nr apartamentului : '))
        suma = float(input('Dati suma: '))
        data = citire_data()
        tipul = input('Dati tipul: ')
        return adaugare_cheltuiala(lista, id, nr_apartament, suma, data, tipul)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def afisare_stergere(lista):
    '''
    :param lista: o lista cu cheltuieli
    :return: se sterge o cheltuiala din lista
    '''
    try:
        nr_apartament = int(input("Dati nr apartamentului care va fi sters"))
        return stergere_cheltuiala(nr_apartament, lista)
    except ValueError as ve:
        print("Eroare",ve)
    return lista

def afisare_modificare(lista):
    '''
    :param lista:lista de cheltuieli
    :return: se modifica lista
    '''
    try:
        id=int(input("Dati id "))
        nr_apartament =int(input('Dati nr apartamentului de modificat: '))
        suma = float(input('Dati suma: '))
        data = citire_data()
        tipul = input('Dati tipul: ')
        return modificare_cheltuiala(lista,id, nr_apartament, suma, data, tipul)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def afisare_adaugare_valoare_la_toate_cheltuielile(lista):
    '''
    :param lista: lista de cheltuieli
    :return: se modifica lista cu cerintele din enunt
    '''
    dat= citire_data()
    sum = int(input("Dati suma:"))
    cheltuieli_lista = adunare_valoare_la_toate_cheltuielile(lista,dat,sum)
    return cheltuieli_lista
def afisare_maxim_cheltuieli_pentru_fiecare_tip(lista):
    tip_cheltuieli=max_cheltuiala_pentru_fiecare_tip(lista)
    for tipul,cheltuiala in tip_cheltuieli.items():
        print("{} : {}".format(tipul,cheltuiala))


def afisare_lista(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))

def interfata(lista):
    """meniulde comanda"""
    while True:
        arata_meniu()
        op=int(input("Alegeti optiunea"))
        if op == 1:
            lista=afisare_adaugare(lista)
        if op==2:
            lista=afisare_stergere(lista)
        if op==3:
            lista=afisare_modificare(lista)
        if op==4:
            lista=afisare_adaugare_valoare_la_toate_cheltuielile(lista)
        if op ==5:
            print(max_cheltuiala_pentru_fiecare_tip(lista))
        if op ==6:
            lista = ordonare_cheltuieli_dupa_suma(lista)
        if op == 7:
            afisare_lista(lista)
        if op == 0:
          break
    else:
        print("Invalid")


