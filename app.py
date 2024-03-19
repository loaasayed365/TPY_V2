from flask import Flask, render_template, jsonify
from database import loadJobs,loadJob
app = Flask(__name__)




@app.route('/')
def hello_world():  
  return render_template('home.htm', jobs=JOBS, company_name='AlaaTest')


@app.route('/api/jobs')
def list_jobs():
  JOBS = loadJobs()
  return jsonify(JOBS)

@app.route('/job/<id>')
def list_job(id):
  job = loadJob(id)
  return jsonify(job)
  
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
