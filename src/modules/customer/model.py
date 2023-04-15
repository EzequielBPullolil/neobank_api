from src.database import Base, engine
from sqlalchemy import String, Column


class Customer(Base):
    __tablename__ = 'Customers'
    id = Column(String, primary_key=True)
    email = Column(String, nullable=False, unique=True)
    dni = Column(String, nullable=False, unique=True)
    cvu_identifier = Column(String(22), nullable=False, unique=True)
    alias = Column(String)

    def __init__(self, id, email, dni, alias, cvu) -> None:
        super().__init__()
        self.id = id
        self.email = email
        self.dni = dni
        self.alias = alias
        self.cvu_identifier = cvu

    def __repr__(self) -> str:
        return f"Customer(id={self.id!r}, email={self.email!r}, dni={self.dni!r},  alias={self.alias!r}))"


Base.metadata.create_all(engine)
