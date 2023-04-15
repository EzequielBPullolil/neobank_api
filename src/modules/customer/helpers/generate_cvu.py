import random


def generate_cvu() -> str:
    '''
        Generates a 22-digit INT and returns
        it if it is not registered in the Customer table
    '''
    cvu = random.randint(10**21, 10**22-1)

    return str(cvu)
