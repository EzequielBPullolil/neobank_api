import pytest
from src.modules.customer.exceptions import DuplicatedEmail, DuplicatedDNI
from src.modules.customer.services.sign_up import SignUpCustomerService
from src.modules.customer.model import Customer
from src.database import session
from sqlalchemy import select


class TestSingUpCustomerServices:
    sing_up_customer = SignUpCustomerService()

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
                email=registered_email, dni='11234234')
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

    def test_register_user_generate_random_alias(self):
        '''
            Check if persisted user of register_user have an random alias
        '''
        email = 'aliastest@singup.com'
        self.sing_up_customer.register_user(
            email=email, dni='44160123')

        result = session.execute(
            select(Customer.alias).where(Customer.email == email)
        ).fetchone()[0]

        assert result != None
        assert 'neobank' in result

    def test_register_user_generate_random_cvu_identifier(self):
        '''
            Check if the customer persisted by SingUpCustomerService
            generate random CBU 
        '''
        email = 'cbutest@singup.com'
        self.sing_up_customer.register_user(
            email=email, dni='11111111')

        result = session.execute(
            select(Customer.cvu_identifier).where(Customer.email == email)
        ).fetchone()[0]

        assert result != None
        assert len(result) == 22
