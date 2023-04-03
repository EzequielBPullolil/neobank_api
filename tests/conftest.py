import pytest
from sqlalchemy import text
from src.database import session
from src.modules.customer.model import Customer
from src.app import create_app
import uuid
from modules.customer.helpers.hash_dni import hash_dni


def pytest_configure():
    '''
       Reset database deleting all rows from TEST database
    '''
    session.execute(
        text('DELETE FROM "Customers"')
    )
    session.commit()
    print('DATABASE RESET')


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def singed_customer():
    id = str(uuid.uuid4())
    email = 'test@mail.com'
    dni = '44170104'
    encripted_dni = hash_dni(dni)
    customer = Customer(id, email, encripted_dni)
    session.add(customer)
    session.commit()

    return {
        'id': id,
        'email': email,
        'dni': dni
    }
