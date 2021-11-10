from Domain.Cheltuiala import *

def get_by_id(id, lista):
    '''
    gaseste cheltuiala cu id-ul dat
    :param id: numar intreg
    :param lista: lista de cheltuieli
    :return: un obiect cheltuiala daca exista o cheltuiala cu id-ul dat sau None in caz contrar
    '''
    for cheltuiala in lista:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None
def adaugare_cheltuiala(lista,id, nr_apartament,suma,data,tipul,lst_undo,lst_redo):
    '''
    Adaugam o prajitura in lista
    :param lista:lista cu cheltuieli
    :param nr_apartament: nr apartamentului acestei cheltuieli
    :param suma: suma cheltuieli
    :param data: data in care se produce cheltuiala
    :param tipul: tipul de cheltuiala
    :return: o lista cu cheltuieli
    '''
    erori=[]
    if id < 0 :
        erori.append("Id ul trebuie sa fie intreg pozitiv")
    if get_by_id(id,lista) is not None:
        erori.append("Exista deja o cheltuiala cu acest id")
    if nr_apartament <0 :
        erori.append("Nr apartamentului trebuie sa fie intreg pozitiv")
    if suma<0:
        erori.append("Suma trebuie sa fie pozitiva")
    if tipul!="canal"and tipul!="intretinere" and tipul!="alte cheltuieli":
        erori.append('Tipul trebuie sa fie unul dintre canal,intretinere sau alte cheltuieli')
    if erori!=[]:
        raise ValueError(erori)
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lista)
        lst_redo.clear()
    cheltuiala = creare_cheltuiala(id,nr_apartament,suma,data,tipul)
    return lista + [cheltuiala]

def stergere_cheltuiala(nr_apartament,lista,lst_undo,lst_redo):
    '''
    Se sterge o cheltuiala cu nr de apartament care se da
    :param nr_apartament: nr apartamentului care se sterge
    :param lista: lista cu cheltuieli
    :return: lista dupa stergere
    '''
    if get_by_id(nr_apartament,lista) is None:
        raise ValueError("Nu exista cheltuiala cu aceest nr de apartament")
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lista)
        lst_redo.clear()
    new_cheltuieli=[]
    for cheltuiala in lista:
        if get_nr_apartament(cheltuiala)!=nr_apartament:
            new_cheltuieli.append(cheltuiala)
            print("Cheltuiala a fost stearsa!")
    return new_cheltuieli

def modificare_cheltuiala(lista,id,nr_apartament,suma,data,tipul,lst_undo,lst_redo):
    '''

    :param lista:o lista cu cheltuieli
    :param new_cheltuiala: o lista cu noua cheltuiala
    :return: lista dupa modificare
    '''
    erori = []
    if id < 0:
        erori.append("Id ul trebuie sa fie intreg pozitiv")
    if get_by_id(nr_apartament, lista) is  None:
        erori.append("Nu exista nici o cheltuiala cu acest nr de apartament")
    if nr_apartament < 0:
        erori.append("Nr apartamentului trebuie sa fie intreg pozitiv")
    if suma < 0:
        erori.append("Suma trebuie sa fie pozitiva")
    if tipul != "canal" and tipul != "intretinere" and tipul != "alte cheltuieli":
        erori.append('Tipul trebuie sa fie unul dintre canal,intretinere sau alte cheltuieli')
    if erori != []:
        raise ValueError(erori)
    lista_modificata=[]
    if (lst_undo is not None) & (lst_redo is not None):
        lst_undo.append(lista)
        lst_redo.clear()
    for cheltuiala in lista:
        new_cheltuiala=creare_cheltuiala(id,nr_apartament,suma,data,tipul)
        if get_nr_apartament(cheltuiala) != get_nr_apartament(new_cheltuiala):

            lista_modificata.append(cheltuiala)
        else:
            lista_modificata.append(new_cheltuiala)

    return lista_modificata
