from Domain.Cheltuiala import *
from Logic.Crud import *
from Logic.Operatii import *

def test_adunare_valoare_la_toate_cheltuielile():
    #test pentru adunare unei valoare la toate cheltuielile care au o data introdusa de utilizator
    c1 = creare_cheltuiala(1,1,23,1233-2-2,"intretinere")
    c2 = creare_cheltuiala(2,3,2,1333-2-2,"canal")
    c3 = creare_cheltuiala(3,5,2,1233-2-2,"alte cheltuieli")
    lista = [c1,c2,c3]
    lista = adunare_valoare_la_toate_cheltuielile(lista,1233-2-2,23)
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
    rezultat=ordonare_cheltuieli_dupa_suma(lista)
    assert rezultat[0]==c3
    assert rezultat[1]==c1
    assert rezultat[2]==c2
