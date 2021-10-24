from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, sql

from configparser import ConfigParser
import mysql.connector as mc

class DB:
	# TODO: db_name as attribute

	def reflect(self,db_name):
		# connect to Mysql/MariaDB:
		engine = create_engine(f"mysql+pymysql://root:1234@localhost/{db_name}")


		# Create a MetaData instance
		metadata = MetaData()
		print(metadata.tables)

		# reflect db schema to MetaData
		metadata.reflect(bind=engine)
		return metadata.tables