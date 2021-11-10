from Logic.Crud import *
from Logic.Operatii import *
import datetime


def arata_meniu():
    '''

    :return: optiunile din meniu
    '''
    print("1.Adaugare cheltuiala")
    print("2.Stergere cheltuiala")
    print("3.Modificare cheltuiala")
    print("4.Stergerea cheltuielilor pentru un nr de apartament")
    print("5.Adaugre suma pentru toate cheltuielile dintr-o data citita de la tastatura")
    print("6.Afisarea cheltuielilor cu suma cea mai mare pentru fiecare tip")
    print("7.Ordonarea cheltuielilor crescator dupa suma")
    print("8.Afisarea sumelor lunare pentru fiecare apartament")
    print("9.Afisare lista")
    print("10.Undo")
    print("11.Redo")
    print("0.Iesire")

def citire_data():
    date_str=input("Dati data separate prin spatiu")
    data=date_str.split(" ")
    an=int(data[0])
    luna=int(data[1])
    zi=int(data[2])
    return datetime.date(an,luna,zi)
def afisare_adaugare(lista,lst_undo,lst_redo):
    """

    :param lista: lista cu cheltuielei
    :return: se adauga cheltuiala creata in logic
    """
    try:
        id=int(input("Dati id :"))
        nr_apartament = int(input('Dati nr apartamentului : '))
        suma = float(input('Dati suma: '))
        data = input("Dati data separata prin - :")
        tipul = input("Dati tipul:")
        return adaugare_cheltuiala(lista, id, nr_apartament, suma, data, tipul,lst_undo,lst_redo)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def afisare_stergere(lista,lst_undo,lst_redo):
    '''
    :param lista: o lista cu cheltuieli
    :return: se sterge o cheltuiala din lista
    '''
    try:
        nr_apartament = int(input("Dati nr apartamentului care va fi sters"))
        return stergere_cheltuiala(nr_apartament, lista,lst_undo,lst_redo)
    except ValueError as ve:
        print("Eroare",ve)
    return lista

def afisare_modificare(lista,lst_undo,lst_redo):
    '''
    :param lista:lista de cheltuieli
    :return: se modifica lista
    '''
    try:
        id=int(input("Dati id "))
        nr_apartament =int(input('Dati nr apartamentului de modificat: '))
        suma = float(input('Dati suma: '))
        data = input("Dati data separata prin -:")
        tipul = input('Dati tipul: ')
        return modificare_cheltuiala(lista,id, nr_apartament, suma, data, tipul,lst_undo,lst_redo)
    except ValueError as ve:
        print("Eroare",ve)
    return lista
def afisare_stergere_cheltuiala_nr_apartament(lista,lst_undo,lst_redo):
    '''
    Se sterge ultima cheltuiala care are un nr de apartament dat
    :param lista: lista de cheltuieli
    :return: lista cu cheltuielile ramase
    '''
    nr_apartament=int(input("Introduceti nr de apartament:"))
    return stergere_cheltuieli_pentru_un_apartament(lista,nr_apartament,lst_undo,lst_redo)

def afisare_adaugare_valoare_la_toate_cheltuielile(lista,lst_redo,lst_undo):
    '''
    :param lista: lista de cheltuieli
    :return: se modifica lista cu cerintele din enunt
    '''
    dat= input("Dati data separata prin -:")
    sum = int(input("Dati suma:"))
    cheltuieli_lista = adunare_valoare_la_toate_cheltuielile(lista,dat,sum,lst_undo,lst_redo)
    return cheltuieli_lista
def afisare_maxim_cheltuieli_pentru_fiecare_tip(lista):
    tip_cheltuieli=max_cheltuiala_pentru_fiecare_tip(lista)
    for tipul,cheltuiala in tip_cheltuieli.items():
        print("{} : {}".format(tipul,cheltuiala))

def afisare_sume_lunare_cheltuieli(lista):
    result = sume_lunare(lista)
    for luna in result:
        print(f'Pentru Luna {luna} avem lista de sume: {result[luna]}')

def afisare_lista(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))

def afisare_undo(lista, lst_undo, lst_redo):
    undo_result = undo(lista, lst_undo, lst_redo)
    if undo_result is not None:
        return undo_result
    return lista


def afisare_redo(lista, lst_undo, lst_redo):
    redo_result = redo(lista, lst_undo, lst_redo)
    if redo_result is not None:
        return redo_result
    return lista


def interfata(lista,lst_undo,lst_redo):
    """meniulde comanda"""
    while True:
        arata_meniu()
        op=int(input("Alegeti optiunea"))
        if op == 1:
            lista=afisare_adaugare(lista,lst_undo,lst_redo)
        if op==2:
            lista=afisare_stergere(lista,lst_undo,lst_redo)
        if op==3:
            lista=afisare_modificare(lista,lst_undo,lst_redo)
        if op==4:
            lista=afisare_stergere_cheltuiala_nr_apartament(lista,lst_undo,lst_redo)
        if op==5:
            lista=afisare_adaugare_valoare_la_toate_cheltuielile(lista,lst_undo,lst_redo)
        if op ==6:
            print(max_cheltuiala_pentru_fiecare_tip(lista))
        if op ==7:
            lista = ordonare_cheltuieli_dupa_suma(lista,lst_undo,lst_redo)
        if op==8:
            afisare_sume_lunare_cheltuieli(lista)
        if op == 9:
            afisare_lista(lista)
        if op ==10:
            lista=afisare_undo(lista,lst_undo,lst_redo)
        if op==11:
            lista=afisare_redo(lista,lst_undo,lst_redo)
        if op == 0:
          break
    else:
        print("Invalid")


