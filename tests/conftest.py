import pytest
from sqlalchemy import text
from src.database import session
from src.modules.customer.model import Customer
from src.app import create_app
import uuid
from src.modules.customer.helpers.hash_dni import hash_dni
from src.modules.customer.helpers.generate_cvu import generate_cvu

email = 'test@mail.com'
id = str(uuid.uuid4())
dni = '44170104'


def pytest_configure():
    '''

       Reset database deleting all rows from TEST database
    '''
    global id, email, dni
    session.execute(
        text('DELETE FROM "Customers"')
    )
    print('DATABASE RESET')
    alias = 'neobank_ezequiel'
    cvu = generate_cvu()
    encripted_dni = hash_dni(dni)
    customer = Customer(id, email, encripted_dni, alias, cvu)
    session.add(customer)
    session.commit()


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def singed_customer():

    global id, email, dni
    return {
        'id': id,
        'email': email,
        'dni': dni
    }
