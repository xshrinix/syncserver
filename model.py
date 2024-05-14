import yaml
from dbconfig import Dssdb
import urllib
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

try:
    with open("config.yml", 'r') as ymlfile:
        conf = yaml.safe_load(ymlfile)
except Exception as ex:
    print(f"Error while reading the configuration file for driver usage reason: {ex}")
    exit(0)

if str(conf['main_setting']['database']).lower().strip() == 'mysql':
    use_driver = 'mysql+pymysql'
else:
    use_driver = 'mssql+pymssql'

database = create_engine("{driver}://{user}:{password}@{host}:{port}/{db}"
                         .format(driver=use_driver, user=str(Dssdb.username).strip(),
                                 password=urllib.parse.quote(str(Dssdb.password).strip()),
                                 host=str(Dssdb.host).strip(), port=Dssdb.port,
                                 db=str(Dssdb.db).strip()), pool_recycle=Dssdb.recycle, pool_pre_ping=True,
                         pool_size=Dssdb.pool_size)

sm = sessionmaker(bind=database)
Dbsession = scoped_session(sm)

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    