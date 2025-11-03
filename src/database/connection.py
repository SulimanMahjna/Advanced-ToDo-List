from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://postgres:HATM@123@localhost/mydatabase")
metadata.bind(engine)