from src.modules.customer.exceptions import DuplicatedEmail
from src.modules.customer.services.sing_up import SingUpCustomerService
import pytest


class TestSingUpCustomerServices:
    def test_already_singed_email_raise_exception(self, singed_customer):
        '''
            Check if parse an singed_email to SingUpCustomer 
        '''
        with pytest.raises(DuplicatedEmail) as e_info:
            SingUpCustomerService(email=singed_customer['email'])
            assert f"The email '{singed_customer['email']}' is already in use" in str(
                e_info.value)
