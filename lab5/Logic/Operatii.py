from Domain.Cheltuiala import *
import datetime

def citire_data():
    date_str=input("Dati data separate prin spatiu")
    data=date_str.split(" ")
    an=int(data[0])
    luna=int(data[1])
    zi=int(data[2])
    m=datetime.date(an,luna,zi)
    return m
def adunare_valoare_la_toate_cheltuielile(lista, dat, sum,lst_undo,lst_redo):
    '''

    :param lista:lista de cheltuieli
    :param dat:data care se introduce de la tastatura
    :param sum:suma care se adauga pentru fiecare cheltuiala care are data egala cu dat
    :return: o lista in care se adauga la cheltuielile cu data egala cu dat o suma , restul raman nemodificate
    '''
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lista)
        lst_redo.clear()
    lista_noua = []
    for cheltuiala in lista:
        data = get_data(cheltuiala)
        if data == dat:
            cheltuiala_nou = creare_cheltuiala(
                get_id(cheltuiala),
                get_nr_apartament(cheltuiala),
                get_suma(cheltuiala) + sum,
                get_data(cheltuiala),
                get_tipul(cheltuiala)

            )

            lista_noua.append(cheltuiala_nou)
        else:
            lista_noua.append(cheltuiala)

    return lista_noua
def max_cheltuiala_pentru_fiecare_tip(lista):
    '''
    :param lista: lista de cheltuieli
    :return: cheltuiala cu suma maxima pentru fiecare tip de cheltuiala
    '''
    tip_cheltuieli = {}
    for cheltuiala in lista:
        tipul = get_tipul(cheltuiala)
        suma = get_suma(cheltuiala)
        if tipul in tip_cheltuieli:
            if get_suma(tip_cheltuieli[tipul]) < suma:
               tip_cheltuieli[tipul] = cheltuiala
        else:
            tip_cheltuieli[tipul] = cheltuiala

    return tip_cheltuieli
def ordonare_cheltuieli_dupa_suma(lista,lst_undo,lst_redo):
    '''
    :param lista:lista de cheltuieli
    :return: lista ordonata crescator in functie de suma
    '''
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lista)
        lst_redo.clear()
    return sorted(lista, key=lambda x: get_suma(x))
def stergere_cheltuieli_pentru_un_apartament(lista,nr_apartament,lst_undo,lst_redo):
    '''

    :param lista:lista ch cheltuieli
    :param nr_apartament:nr apartamentului pentru care se face stergerea
    :return:o lista in care se sterge suma pentru ap mentionat
    '''
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lista)
        lst_redo.clear()
    lista_noua=[]
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala)==nr_apartament:
            cheltuiala_nou = creare_cheltuiala(
                get_id(cheltuiala),
                get_nr_apartament(cheltuiala),
                0,
                get_data(cheltuiala),
                get_tipul(cheltuiala)

            )

            lista_noua.append(cheltuiala_nou)
        else:
            lista_noua.append(cheltuiala)

        return lista_noua

def sume_lunare(lista):
    '''

    :param lista:lista cu cheltuieli
    :return:o lista cu sumele lunare pentru fiecare apartament
    '''
    result = {}
    for cheltuiala in lista:
        data=get_data(cheltuiala)
        luna = int(data.split('-')[1])
        if luna not in result:
            result[luna] = []
            result[luna].append(get_suma(cheltuiala))
        else:
            result[luna].append(get_suma(cheltuiala))
    return result
def undo(lista, lst_undo,lst_redo):
    """
    Face operatia de undo. Aduce lista la ultima stare inainte de orice operatie care modifica lista
    :param lst_rezervari: lista cu rezervari
    :param lst_undo: lista cu starile precedente
    :param lst_redo: lista cu starile inainte de undo
    :return: lista in starea in care se afla inainte de orice operatia care a modificat-o
    """
    if lst_undo:
        lst_redo.append(lista)
        return lst_undo.pop()

    return lista


def redo(lista,lst_undo,lst_redo):
    """
    Face operatia de redo. Readuce lista la ultima stare inainte de undo.
    :param lst_rezervari: lista cu rezervari
    :param lst_undo:lista cu starile precedente
    :param lst_redo:lista cu starile inainte de undo
    :return: lista in starea in care se afla inainte de undo
    """
    if lst_redo:
        lst_undo.append(lista)
        return lst_redo.pop()

    return lista