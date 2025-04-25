from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Account(Base):
    __tablename__ = 'account'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(String)
    adapterType = Column(String)
    serviceType = Column(String)

    def __repr__(self):
        return "<Account(name='%s', adapterType='%s', serviceType='%s')>" % (
            self.name, self.adapterType, self.serviceType)

trader1_account = Account(name="Trader1", active='Y', adapterType="IB", serviceType="Exchange")


from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo=True)
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

