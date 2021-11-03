from Ui.Interfata import *
from Tests.Teste_crud import *
from Tests.Teste_operatii import *
def meniu():
    test_call()
    test_adunare_valoare_la_toate_cheltuielile()
    test_max_cheltuiala_pentru_fiecare_tip()
    test_ordonare_cheltuieli_dupa_suma()
    lista=[]
    interfata(lista)
meniu()
