from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Staff(Base):
    __tablename__ = 'staff'

    StaffId = Column(Integer, primary_key=True)
    Role = Column(Integer)
    UserName = Column(String)
    Password = Column(String)
    phone = Column(String)  # Assuming phone numbers can include non-numeric characters
    Salary = Column(Float)
    Daysoff = Column(String)
    JoinedDate = Column(DateTime)
    # Define relationships if needed, e.g., One-to-Many
    # orders = relationship("Order", back_populates="staff")
    # bills = relationship("Bill", back_populates="staff")

# Configure MySQL connection
db_url = 'mysql+mysqlconnector://username:password@localhost/database_name'
engine = create_engine(db_url)

# Create tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Example usage:
# staff_member = Staff(StaffId=1, Role=2, UserName="JohnDoe", Password="password123",
#                     phone="123-456-7890", Salary=2500.00, Daysoff="Saturday, Sunday",
#                     JoinedDate=datetime(2022, 1, 15))
# session.add(staff_member)
# session.commit()
