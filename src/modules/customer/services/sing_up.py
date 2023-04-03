from src.modules.customer.db_utils import EmailManager, DniManager
from src.modules.customer.helpers.generate_alias import generate_alias
from src.database import session
from src.modules.customer.model import Customer
from uuid import uuid4
from src.modules.customer.helpers.hash_dni import hash_dni


class SingUpCustomerService():
    emailManager = EmailManager()
    dniManager = DniManager()

    def register_user(self, email, dni):
        '''
            Check if email are avaible and persist 
            customer
        '''
        self.emailManager.check_email_availability(email)
        self.dniManager.check_dni_availability(dni)
        hashed_dni =hash_dni(dni)
        alias = generate_alias('ezequiel')
        id = uuid4()
        customer = Customer(
            id,
            email,
            hashed_dni,
            alias
        )
        session.add(customer)

        session.commit()
