from Logic.Crud import *
from Domain.Cheltuiala import *


def arata_meniu():
    print("1.Adaugare cheltuiala")
    print("2.Stergere cheltuiala")
    print("3.Modificare cheltuiala")
    print("4.Afisare lista")
    print("0.Iesire")
def afisare_adaugare(lista):
    nr_apartament = int(input('Dati nr apartamentului : '))
    suma = float(input('Dati suma: '))
    data = int(input('Dati data: '))
    tipul = input('Dati tipul: ')
    return adaugare_cheltuiala(lista,nr_apartament,suma,data,tipul)
def afisare_stergere(lista):
    nr_apartament = int(input("Dati nr apartamentului care va fi sters"))
    print("Cheltuiala a fost stersa")
    return stergere_cheltuiala(nr_apartament,lista)
def afisare_modificare(lista):
    nr_apartament =int(input('Dati nr apartamentului de modificat: '))
    suma = float(input('Dati suma: '))
    data = int(input('Dati data: '))
    tipul = input('Dati tipul: ')
    return modificare_cheltuiala(lista,creare_cheltuiala(nr_apartament,suma,data,tipul))

def afisare_lista(lista):
    for cheltuiala in lista:
        print(to_string(cheltuiala))

def interfata(lista):
    while True:
        arata_meniu()
        op=int(input("Alegeti optiunea"))
        if op == 1:
            lista=afisare_adaugare(lista)
        if op==2:
            lista=afisare_stergere(lista)
        if op==3:
            lista=afisare_modificare(lista)
        if op == 4:
            afisare_lista(lista)
        if op == 0:
          break
    else:
        print("Invalid")


