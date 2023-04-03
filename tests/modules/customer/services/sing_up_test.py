from src.modules.customer.exceptions import DuplicatedEmail, DuplicatedDNI
from src.modules.customer.services.sing_up import SingUpCustomerService
import pytest


class TestSingUpCustomerServices:
    sing_up_customer = SingUpCustomerService()

    def test_correct_sing_up_user(self):
        '''
            Sings an user
        '''
        self.sing_up_customer.register_user(
            email='abcdf@mail.com', dni='44160102')

    def test_already_singed_email_raise_exception(self, singed_customer):
        '''
            Check if parse an singed_email to SingUpCustomer 
        '''
        registered_email = singed_customer['email']
        with pytest.raises(DuplicatedEmail) as e_info:
            self.sing_up_customer.register_user(
                registered_email, dni='11234234')
            assert f"The email '{registered_email}' is already in use" in str(
                e_info.value)

    def test_already_singed_dni_raise_exception(self, singed_customer):
        '''
            Check if parse an registered dni raise exception
        '''
        registered_dni = singed_customer['dni']
        with pytest.raises(DuplicatedDNI) as e_info:
            self.sing_up_customer.register_user(
                email='dniraise@email.com',
                dni=registered_dni
            )
            assert f"The dni '{registered_dni}' is already in use" in str(
                e_info.value)
