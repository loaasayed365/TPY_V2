from flask import Flask, redirect, render_template, request
from models.product import Product
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'

@app.route('/new')
def hello_world():
  return render_template('home.htm')


@app.route('/')
def listHtmlProduct():
  return render_template('product.htm', products=Product.listProducts())


@app.route('/addpro', methods=['GET', 'POST'])
def addHtmlProduct():
  uploaded_file = request.files['productImage']
  if uploaded_file.filename is not None:
    filename = secure_filename(uploaded_file.filename) 
    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],filename))
    product = Product(request.form['productName'],
      int(request.form['productPrice']), filename)
    product.addProduct()
  return redirect('/', 302)
  
  """
  if filename != '':
      file_ext = os.path.splitext(filename)[1]
      if file_ext not in app.config['UPLOAD_EXTENSIONS']:
          abort(400)
      uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
  f.save(os.path.join(app.config['UPLOAD_FOLDER'],fn))
  product = Product(request.form['productName'],
                    int(request.form['productPrice']),
                  if uploaded_file is not None:
      filename = secure_filename(uploaded_file.filename)      fn)
  product.addProduct()
  """
  



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
