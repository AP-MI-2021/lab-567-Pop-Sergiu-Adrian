def creare_cheltuiala(nr_apartament,suma,data,tipul):
    '''
    Se creaza o cheltuiala
    :param nr_apartament: un intreg pozitiv
    :param suma:float
    :param data:DD.MM.YYYY
    :param tipul: întreținere, canal, alte cheltuieli
    :return: o cheltuiala
    '''
    return {
        "nr_apartament":nr_apartament,
        "suma":suma,
        "data":data,
        "tipul":tipul
    }

#get
def get_nr_apartament(cheltuiala):
    return cheltuiala["nr_apartament"]
def get_suma(cheltuiala):
    return cheltuiala["suma"]
def get_data(cheltuiala):
    return cheltuiala["data"]
def get_tipul(cheltuiala):
    return cheltuiala["tipul"]
#set
def set_id(cheltuiala,nr_apartament):
    cheltuiala["nr_apartament"]=nr_apartament
def set_suma(cheltuiala,suma):
    cheltuiala["suma"]=suma
def set_data(cheltuiala,data):
    cheltuiala["data"]=data
def set_tipul(cheltuiala,tipul):
    cheltuiala["tipul"] = tipul

def to_string(cheltuiala):
    '''

    :param obiect: o cheltuiala
    :return: modul in care se afiseaza cheltuiala
    '''
    return "Nr apartament{},suma:{},data:{},tipul:{}".format(get_nr_apartament(cheltuiala),get_suma(cheltuiala),get_data(cheltuiala),get_tipul(cheltuiala))
