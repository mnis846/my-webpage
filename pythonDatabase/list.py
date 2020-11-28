import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session

engine = create_engine(os.getenv( "postgresql://postgres:Tandan@localhost/postgres" ))
db = scoped_session(sessionmaker(bind=engine))

def main():
    Flights =db.execute("SELECT origin, destination, duration FROM Flights" ).fetchall()
    for flight in Flights:
        print(f"{flight.origin} to {flight.destination}, {flight.duration} minutes. ")


if __name__ == "__main__":
    main()