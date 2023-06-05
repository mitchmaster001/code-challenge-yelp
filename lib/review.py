from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# creating the engine
engine = create_engine('sqlite:///restaurant.db')

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()


# Creating the table
Base = declarative_base()

class Review(Base):
    __tabelname__ = "review"

    review_id = Column(Integer, primary_key=True)
    customer_id = Column(Integer, ForeignKey("customer_id"))
    restaurant_id = Column(Integer, ForeignKey("restaurant_id"))
    rating = Column(Integer)

    # Establishing relationships
    customer = relationship('Customer')
    restaurant = relationship('Restaurant')


    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating

    # getter for customer rating
    @property
    def rating(self):
        return self._rating

    # getter for customer()
    @property
    def customer(self):
        return self._customer

    # getter for restaurant()
    @property
    def restaurant(self):
        return self._restaurant

    # returns all of the reviews
    @classmethod
    def all(cls):
        return session.query(cls).all()