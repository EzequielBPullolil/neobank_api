from src.modules.customer.helpers import EmailManager


class SingUpCustomerService():
    emailManager = EmailManager()

    def register_user(self, email):
        '''
            Check if email are avaible and persist 
            customer
        '''
        self.emailManager.check_email_availability(email)
