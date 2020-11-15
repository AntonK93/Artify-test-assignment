from sqlalchemy.ext.declarative import declarative_base

# create Base lei
Base = declarative_base()

class Config:

    # Connection data to your mysql database
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PWD = ''
    DB_NAME = 'artify'

    # Connection data to your redis database
    REDIS_HOST = 'localhost'
    REDIS_PORT = 6379
    REDIS_DB = 0

    # Time to keep session, in miliseconds
    SESSION_TIME = 600

    # Host of your client application
    CLIENT_APP = 'http://localhost:8080'