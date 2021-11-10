from Domain.Cheltuiala import *
from Logic.Crud import *
from Logic.Operatii import *
from Ui.Interfata import *

def test_stergere_cheltuieli_nr_apartament():
    c1 = creare_cheltuiala(1, 1, 6, 2222 - 2 - 23, "canal")
    c2 = creare_cheltuiala(2, 2, 3, 1888 - 9 - 12, "canal")
    lista = [c1, c2]
    lst_undo=[]
    lst_redo=[]
    stergere_cheltuieli_pentru_un_apartament(lista,1,lst_undo,lst_redo)
    assert get_suma(c1) ==6
def test_adunare_valoare_la_toate_cheltuielile():
    #test pentru adunare unei valoare la toate cheltuielile care au o data introdusa de utilizator
    c1 = creare_cheltuiala(1,1,23,1233-2-2,"intretinere")
    c2 = creare_cheltuiala(2,3,2,1333-2-2,"canal")
    c3 = creare_cheltuiala(3,5,2,1233-2-2,"alte cheltuieli")
    lista = [c1,c2,c3]
    lst_undo = []
    lst_redo = []
    lista = adunare_valoare_la_toate_cheltuielile(lista,1233-2-2,23,lst_undo,lst_redo)
    assert get_suma(get_by_id(1,lista)) ==46
    assert get_suma(get_by_id(2,lista)) == 2
def test_max_cheltuiala_pentru_fiecare_tip():
    #test pentru cea mai mare cheltuiala pentru fiecare tip
    c1 = creare_cheltuiala(1, 1, 23, 1233-2-2, "intretinere")
    c2 = creare_cheltuiala(2, 3, 234, 1233-2-2, "canal")
    c3 = creare_cheltuiala(3, 5, 2, 1233-2-2, "alte cheltuieli")
    lista = [c1, c2, c3]
    rezultat= max_cheltuiala_pentru_fiecare_tip(lista)
    assert rezultat["intretinere"]==c1
    assert rezultat["canal"]==c2
    assert rezultat["alte cheltuieli"]==c3
def test_ordonare_cheltuieli_dupa_suma():
    #test pentru ordonare cheltuielilor in functie de suma
    c1 = creare_cheltuiala(1, 1, 23,1233-2-2, "intretinere")
    c2 = creare_cheltuiala(2, 3, 234,1233-2-2, "canal")
    c3 = creare_cheltuiala(3, 5, 2,1233-2-2, "alte cheltuieli")
    lista=[c1,c2,c3]
    lst_undo = []
    lst_redo = []
    rezultat=ordonare_cheltuieli_dupa_suma(lista,lst_undo,lst_redo)
    assert rezultat[0]==c3
    assert rezultat[1]==c1
    assert rezultat[2]==c2
def test_sume_lunare():
    c1 = creare_cheltuiala(1, 1, 23, "1233-2-2", "intretinere")
    c2 = creare_cheltuiala(2, 3, 234, "1233-2-2", "canal")
    c3 = creare_cheltuiala(3, 5, 2, "1233-4-2", "alte cheltuieli")
    lista=[c1,c2,c3]
    result_sume = sume_lunare(lista)
    result = {}
    result[2] = [23,234]
    result[4] = [2]
    assert len(result) == len(result_sume)
    assert result_sume == result
    assert (result_sume == result) == True
def test_undo_redo():
    lst_test = []
    lst_undo_test = []
    lst_redo_test = []
    lst_test =adaugare_cheltuiala(lst_test, 1, 1, 12, 1-2-3, 'canal', lst_undo_test, lst_redo_test)
    lst_test =adaugare_cheltuiala(lst_test, 2, 2, 13, 12-3-4, 'alte cheltuieli', lst_undo_test, lst_redo_test)
    lst_test =adaugare_cheltuiala(lst_test, 3, 3, 14, 123-3-4, 'intretinere', lst_undo_test, lst_redo_test)
    lst_test = undo(lst_test,lst_undo_test,lst_redo_test)
    assert len(lst_test) == 2
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 1
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 0
    #assert undo(lst_test,lst_undo_test,lst_redo_test) is None
    assert len(lst_test) == 0
    lst_test = adaugare_cheltuiala(lst_test, 1, 1, 12, 1 - 2 - 3, 'canal', lst_undo_test, lst_redo_test)
    lst_test = adaugare_cheltuiala(lst_test, 2, 2, 13, 12 - 3 - 4, 'alte cheltuieli', lst_undo_test, lst_redo_test)
    lst_test = adaugare_cheltuiala(lst_test, 3, 3, 14, 123 - 3 - 4, 'intretinere', lst_undo_test, lst_redo_test)
    #assert redo(lst_test,lst_undo_test,lst_redo_test) is None
    assert len(lst_test) == 3
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 1
    lst_test =redo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 2
    lst_test = redo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 3
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 1
    lst_test = adaugare_cheltuiala(lst_test, 5, 3, 12, 1 - 2 - 3, 'canal', lst_undo_test, lst_redo_test)
    #assert redo(lst_test,lst_undo_test,lst_redo_test) is None
    assert len(lst_test) == 2
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 1
    lst_test = undo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 0
    lst_test = redo(lst_test, lst_undo_test, lst_redo_test)
    lst_test = redo(lst_test, lst_undo_test, lst_redo_test)
    assert len(lst_test) == 2
    #assert redo(lst_test, lst_undo_test, lst_redo_test) is None
    assert len(lst_test) == 2

