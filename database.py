import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, DateTime,Row
import os



engine = create_engine(os.environ['DB_CONN_STRING'])
#print(sqlalchemy.__version__)

#  DB VARIABLES

def loadJobs():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())
  return jobs
  
"""
result_all = result.all() 
print(type(result_all))
result_dic = dict(result_all[0]._mapping)
print(type(result_dic))
print(result_dic)
"""
