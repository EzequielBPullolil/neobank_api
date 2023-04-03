from src.modules.customer.db_utils import EmailManager, DniManager


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
