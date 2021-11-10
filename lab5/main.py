from Ui.Interfata import *
from Tests.Teste_crud import *
from Tests.Teste_operatii import *
from Ui.Interfata_linie import *
def meniu():
    test_call()
    test_stergere_cheltuieli_nr_apartament()
    test_adunare_valoare_la_toate_cheltuielile()
    test_max_cheltuiala_pentru_fiecare_tip()
    test_ordonare_cheltuieli_dupa_suma()
    test_sume_lunare()
    test_undo_redo()
    lista=[]
    lst_undo=[]
    lst_redo=[]
    #interfata_menu(lista)
    interfata(lista,lst_undo,lst_redo)
meniu()
