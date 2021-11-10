from Domain.Cheltuiala import *
from Logic.Crud import *


def test_domain():
    c1= creare_cheltuiala(1,2,4,1212-2-2,"canal")
    assert get_nr_apartament(c1)==2
    assert get_suma(c1)==4
    assert get_data(c1)==1212-2-2
    assert get_tipul(c1)=="canal"
def test_stergere_cheltuiala():
    c1=creare_cheltuiala(1,1,6,1234-12-12,"canal")
    lista=[c1]
    c2=creare_cheltuiala(2,2,3,2111-2-13,"canal")
    lista=[c1,c2]
    lst_undo=[]
    lst_redo=[]
    assert stergere_cheltuiala(2,lista,lst_undo,lst_redo)==[c1]
def test_modificare_cheltuiala():
    c1 = creare_cheltuiala(1,1, 6, 2222-2-23, "canal")
    c2 = creare_cheltuiala(2,2, 3, 1888-9-12, "canal")
    lista=[c1,c2]
    lst_undo = []
    lst_redo = []
    new_id=1
    new_nr_apartament=get_nr_apartament(c2)
    new_suma=4
    new_data=1222-2-2
    new_tipul="canal"
    new_c=creare_cheltuiala(1,2,4,1222-2-2,"canal")
    assert modificare_cheltuiala(lista , new_id,get_nr_apartament(new_c),new_suma,new_data,new_tipul,lst_undo,lst_undo)
    assert get_suma(new_c)==new_suma
    assert get_data(new_c) == new_data
    assert get_tipul(new_c) == new_tipul
def test_call():
    test_domain()
    test_stergere_cheltuiala()
    test_modificare_cheltuiala()







