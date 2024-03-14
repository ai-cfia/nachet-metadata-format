import os

def raise_error(message):
    raise Exception(message)

NACHET_SCHEMA = os.getenv("NACHET_SCHEMA") #or raise_error("NACHET_SCHEMA is not set")
NACHET_DB_URL = os.getenv("NACHET_DB_URL") #or raise_error("NACHET_DB_URL is not set")
