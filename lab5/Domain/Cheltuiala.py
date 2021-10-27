def creare_cheltuiala(id,nr_apartament,suma,data,tipul):
    '''
    Se creaza un dictionar in care se aduna mia multe cheltuieli
    :param id :id
    :param nr_apartament: un intreg pozitiv
    :param suma:float
    :param data:DD.MM.YYYY
    :param tipul: întreținere, canal, alte cheltuieli
    :return: o cheltuiala
    '''
    return {
        "id":id,
        "nr_apartament":nr_apartament,
        "suma":suma,
        "data":data,
        "tipul":tipul
    }

#get
def get_id(cheltuiala):
    '''
    getter pentru id
    :param cheltuiala: cheltuiala
    :return: id pentru cheltuiala
    '''
    return cheltuiala["id"]

def get_nr_apartament(cheltuiala):
    '''
    Getter pentru nr apartament
    :param cheltuiala: cheltuiala
    :return:nr apartamentului cheltuieli
    '''
    return cheltuiala["nr_apartament"]
def get_suma(cheltuiala):
    '''
    getter pentru suma
    :param cheltuiala: cheltuiala
    :return: suma cheltuieli
    '''
    return cheltuiala["suma"]
def get_data(cheltuiala):
    '''
    getter pentru data
    :param cheltuiala:cheltuiala
    :return: data cheltuieli
    '''
    return cheltuiala["data"]
def get_tipul(cheltuiala):
    '''
    getter pentru tip
    :param cheltuiala: cheltuiala
    :return: tipul cheltuieli
    '''
    return cheltuiala["tipul"]
#set
def set_id(cheltuiala,id):
    cheltuiala["id"]=id
def set_nr_apartement(cheltuiala,nr_apartament):
    '''
    setter pentru nr_apartament
    :param cheltuiala: cheltuiala
    :param nr_apartament: nr apartamentului
    :return: se seteaza nr apartamentului
    '''
    cheltuiala["nr_apartament"]=nr_apartament
def set_suma(cheltuiala,suma):
    '''

    :param cheltuiala:
    :param suma:
    :return:
    '''
    cheltuiala["suma"]=suma
def set_data(cheltuiala,data):
    '''

    :param cheltuiala:
    :param data:
    :return:
    '''
    cheltuiala["data"]=data
def set_tipul(cheltuiala,tipul):
    '''

    :param cheltuiala:
    :param tipul:
    :return:
    '''
    cheltuiala["tipul"] = tipul

def to_string(cheltuiala):
    '''

    :param obiect: o cheltuiala
    :return: modul in care se afiseaza cheltuiala
    '''
    return "{}. Nr apartament{},suma:{},data:{},tipul:{}".format(get_id(cheltuiala),get_nr_apartament(cheltuiala),get_suma(cheltuiala),get_data(cheltuiala),get_tipul(cheltuiala))
