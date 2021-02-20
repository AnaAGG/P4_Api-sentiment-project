from mongoConnections import read_data

def check_author(query, coll):
    '''
    descripcion
    '''
    exist = read_data(query, coll)

    if len(exist) > 0:
        return True
    else:
        return False

'''
def check_parameters(coll, kwargs, mandatory, database = db): #kwargs es la nueva info que meteremos, por lo tanto es un diccionario que tiene key and values. mandatory es los documentos que son obligatorios para subir o quitar informacion de la API(esto será una lista)
    
    for i in mandatory:
        if i in kwargs.keys():
            pass
    '''
