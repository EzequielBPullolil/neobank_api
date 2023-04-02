from src.app import db


class Customer(db.Model):
    id = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)

    def __init__(self, id, email) -> None:
        super().__init__()
        self.id = id
        self.email = email
