from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

# creating the engine
engine = create_engine('sqlite:///restaurant.db')

# Creating the session
Session = sessionmaker(bind=engine)
session = Session()


# Creating the table
Base = declarative_base()

class Restaurant(Base):
    __tabelname__ = "restaurants"

    restaurant_id = Column(Integer, primary_key=True)
    name = Column(String)

    # Establishing relationships
    reviews = relationship('Review', back_populates='restaurants')
    customers = relationship('Customer', secondary='reviews', back_populates='restaurants')

    def __init__(self, name):
        self._name = name

    # getter for Restaurant name()
    @property
    def name(self):
        return self._name

    # getter for reviews()
    @property
    def reviews(self):
        return self.reviews
    
    # Returns a **unique** list of all customers who have reviewed a particular restaurant.
    def customers(self):
        unique_customer_rev = set()
        for review in self.reviews:
            unique_customer_rev.add(review.customer)
        return list(unique_customer_rev)

    # returns the average star rating for a restaurant based on its reviews
    def average_star_rating(self):
        total_ratings = sum(review.rating for review in self.reviews)
        num_reviews = len(self.reviews)
        if num_reviews > 0:
            return total_ratings / num_reviews
        else:
            return 0.0