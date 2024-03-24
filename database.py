import sqlalchemy
from sqlalchemy import create_engine, text, MetaData, Table, Column, Integer, String, ForeignKey, DateTime, Row
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


def loadJob(id):
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs where id = :valh"),
                          {'valh': id})
    jobs = []
    for row in result.all():
      jobs.append(row._asdict())

    print(jobs)
  return jobs


"""
result_all = result.all() 
print(type(result_all))
result_dic = dict(result_all[0]._mapping)
print(type(result_dic))
print(result_dic)
"""


def addDbPorduct(productName, price, image):
  with engine.connect() as conn:
    query = text(
        "INSERT INTO tbl_product (productName,price,image) VALUES (:productName, :price, :image)"
    )
    conn.execute(query, {
        'productName': productName,
        'price': price,
        'image': image
    })
    conn.commit()


def getDbProducts():
  with engine.connect() as conn:
    result = conn.execute(text("select * from tbl_product"))
    products = []
    for row in result.all():
      products.append(row._asdict())
    return products


def getDbProduct(id):
  with engine.connect() as conn:
    result = conn.execute(
        text("select * from tbl_product where productId = :valh"),
        {'valh': id})
    products = []
    for row in result.all():
      products.append(row._asdict())
    return products
