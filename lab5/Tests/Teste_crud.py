from Domain.Cheltuiala import *
from Logic.Crud import *


def test_domain():
    c1= creare_cheltuiala(1,2,4,23,"apa")
    assert get_nr_apartament(c1)==2
    assert get_suma(c1)==4
    assert get_data(c1)==23
    assert get_tipul(c1)=="apa"
def test_stergere_cheltuiala():
    c1=creare_cheltuiala(1,1,6,3,"altele")
    lista=[c1]
    c2=creare_cheltuiala(2,2,3,6,"apa")
    lista=[c1,c2]
    assert stergere_cheltuiala(2,lista)==[c1]
def test_modificare_cheltuiala():
    c1 = creare_cheltuiala(1,1, 6, 3, "altele")
    c2 = creare_cheltuiala(2,2, 3, 6, "apa")
    lista=[c1,c2]
    new_id=1
    new_nr_apartament=get_nr_apartament(c2)
    new_suma=4
    new_data=5
    new_tipul="gaz"
    new_c=creare_cheltuiala(1,2,4,5,"gaz")
    assert modificare_cheltuiala(lista,new_c)
    assert get_suma(new_c)==new_suma
    assert get_data(new_c) == new_data
    assert get_tipul(new_c) == new_tipul
def test_call():
    test_domain()
    test_stergere_cheltuiala()
    test_modificare_cheltuiala()







