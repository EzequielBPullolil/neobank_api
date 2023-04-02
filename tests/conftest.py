import pytest
from src.modules.customer.model import Customer
from src.app import create_app, db
import uuid


@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture()
def singed_customer(app):

    with app.app_context():
        id = str(uuid.uuid4())
        email = 'email@test.com'
        customer = Customer(id=id, email=email)
        db.session.add(customer)
        db.session.commit()
    return {
        'id': id,
        'email': email
    }
