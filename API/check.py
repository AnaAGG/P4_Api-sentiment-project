from mongoConnections import read_data

def check_author(query, coll):
    '''
    descripcion
    '''
    exist = read_data(query, {}, coll)

    if len(exist) > 0:
        return True
    else:
        return False


def check_parameters(kwargs, mandatory, at_least_one = None):
    '''
    kwargs es la nueva info que meteremos, por lo tanto es un diccionario que tiene
    key and values. mandatory es los documentos que son obligatorios para subir o quitar
    informacion de la API(esto será una lista)

    '''
    for i in mandatory:
        if i not in kwargs.keys():
            return False
    if at_least_one:
        contains = 0
        for param in at_least_one:
            if param in kwargs.keys():
                contains +=1
        if contains == 0:
            return False
    return True

