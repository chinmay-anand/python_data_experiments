from typing import Optional

from sqlmodel import Field, SQLModel, Session, create_engine, select

class Hero(SQLModel, table=True):
    # "table=True" makes the clsass "Hero" regitered in the SQLModel.metadata attribute
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None

connection_string = "sqlite:///database.db";
# connection_string = 'mysql+mysqlconnector://test:test@localhost:3306/'+'testdb'; # MySQL connection string


def add_data_to_table(p_engine):
    # prepare data to insert
    hero_1 = Hero(name="Deadpond", secret_name="Dive Wilson")
    hero_2 = Hero(name="Spider-Boy", secret_name="Pedro Parqueador")
    hero_3 = Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)
    # Add above records to table using session
    with Session(p_engine) as session:
        session.add(hero_1)
        session.add(hero_2)
        session.add(hero_3)
        session.commit()



if __name__=="__main__":
    engine = create_engine(connection_string, echo=True); # True enables sql tracing

    # The next call creates the database and also the tables if not existing -  for all the tables registered with SQLModel.metadata object.
    # SQLModel.metadata.create_all(engine);
    
    # add sample data to table
    # add_data_to_table(engine);