from mongo import read_data

def check_author(query, coll):
    '''
    Check that the Quote/Author to be included is not already in our database

    Receive:
        - query: the phrase or Author to include in the database
        - coll (string): the collection where we want to check
    Returns:
        True or False depending on whether the conditions are met
    '''
    exist = read_data(query, {}, coll)

    if len(exist) > 0:
        return True
    else:
        return False


def check_parameters(kwargs, mandatory, at_least_one = None):
    '''
    Check that the parameters we introduce to delete or introduce
    information from our collections are met

    Receive: 
        - kwargs (dictionary) is the new info that we will enter.
        - mandatory (list) is the documents that are mandatory to upload or remove
            API information
    Returns:
        True or False depending on whether the conditions are met  
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

