from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DB_URL = 'mysql://root:password@localhost/kiki'
engine = create_engine(DB_URL)
Session = sessionmaker()
Session.configure(bind=engine)
