from database import addDbPorduct, getDbProducts, getDbProduct


class Product:

  def __init__(self, productName='', price=0, image=''):
    self.productName = productName
    self.price = price
    self.image = image

  def getProductName(self):
    return self.productName

  def getPrice(self):
    return self.price

  def getImage(self):
    return self.image

  def setProdName(self, productName):
    self.productName = productName

  def setPrice(self, price):
    self.price = price

  def setImage(self, image):
    self.image = image

  def addProduct(self):
    addDbPorduct(self.productName, self.price, self.image)

  @staticmethod
  def listProducts():
    products = getDbProducts()
    return products

  @staticmethod
  def getProduct(id):
    products = getDbProduct(id)
    return products
