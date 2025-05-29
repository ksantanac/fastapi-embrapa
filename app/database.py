import os

from dotenv import load_dotenv

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Carrega variáveis do .env
load_dotenv()

# URL de conexão com o banco MySQL
DATABASE_URL = os.getenv("DATABASE_URL")

# Cria a engine de conexão com o banco de dados, engine é o ponto central de conexão com o banco
engine = create_engine(DATABASE_URL)

# Cria uma fábrica de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Função geradora que fornece sessões de banco de dados
def get_db():
    # Cria uma nova sessão
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()