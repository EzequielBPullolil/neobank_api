from src.database import Base, engine
from sqlalchemy import String, Column


class Customer(Base):
    __tablename__ = 'Customers'
    id = Column(String, primary_key=True)
    email = Column(String)

    def __init__(self, id, email) -> None:
        super().__init__()
        self.id = id
        self.email = email

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, email={self.email!r}))"


Base.metadata.create_all(engine)
