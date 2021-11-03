from Domain.Cheltuiala import *
def adunare_valoare_la_toate_cheltuielile(lista, dat, sum):
    '''

    :param lista:lista de cheltuieli
    :param dat:data care se introduce de la tastatura
    :param sum:suma care se adauga pentru fiecare cheltuiala care are data egala cu dat
    :return: o lista in care se adauga la cheltuielile cu data egala cu dat o suma , restul raman nemodificate
    '''
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
def ordonare_cheltuieli_dupa_suma(lista):
    '''
    :param lista:lista de cheltuieli
    :return: lista ordonata crescator in functie de suma
    '''
    return sorted(lista, key=lambda x: get_suma(x))