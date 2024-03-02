from flask import Flask, render_template, jsonify
app = Flask(__name__);
JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Bengaluru, India',
    'salary': 'Rs. 10,00,000'
  },
  {
    'id': 2,
    'title': 'Data Scientist',
    'location': 'Delhi, India',
    'salary': 'Rs. 15,00,000'
  },
{
  'id': 3,
  'title': 'Frontend',
  'location': 'Remote',
  'salary': 'Rs. 12,00,000'
},
  {
    'id': 4,
    'title': 'Backend',
    'location': 'Romania',
    'salary': '$15,00,000'
  }
]
@app.route('/')
def hello_world():
    return render_template('home.htm',jobs=JOBS,company_name='AlaaTest')

@app.route('/api/jobs')
def list_jobs():
  return jsonify(JOBS) 
if __name__ == '__main__':  
    app.run(host='0.0.0.0', port=8080)
