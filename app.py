from flask import Flask, render_template, jsonify
from database import loadJobs
app = Flask(__name__)
JOBS = loadJobs()




@app.route('/')
def hello_world():  
  return render_template('home.htm', jobs=JOBS, company_name='AlaaTest')


@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
