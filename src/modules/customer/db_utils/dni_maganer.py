from src.modules.customer.exceptions import DuplicatedDNI
from src.modules.customer.helpers.encrypt_dni import encrypt_dni
from sqlalchemy import select
from src.database import session
from src.modules.customer.model import Customer


class DniManager:

    def check_dni_availability(self, dni):
        '''
            Check if exist the parsed dni 
            is availability in database
        '''
        hashed_dni = encrypt_dni(dni)
        query = select(Customer).where(Customer.dni == hashed_dni)
        result = session.execute(query).fetchone()
        if (result != None):
            raise DuplicatedDNI()
