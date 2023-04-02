from src.modules.customer.exceptions import DuplicatedEmail
from sqlalchemy import select
from src.database import session, engine
from src.modules.customer.model import Customer


class EmailManager:
    def check_email_availability(self, email):
        '''
            If finds Customer with same email
            raise exception
        '''
        query = select(Customer).where(Customer.email == email)
        result = session.execute(query).fetchone()

        if(len(result) > 0):
            raise DuplicatedEmail(email)
