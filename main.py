from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

@app.route('/') #decorator
def  index():
  return render_template('index.html')


  
#외부 api 가져오기 

@app.route('/posts')
def show_post():
  response = requests.get('https://jsonplaceholder.typicode.com/posts')
  to_serve = response.json()
  
  return jsonify(to_serve)

@app.route('/todos')
def show_todos():
  return 'This is todos'

@app.route('/quote/<string:name>')
def show_quote(name):
  return 'This is quote {}'.format(name)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True) #프로젝트 첫 시작시 pip install flask
# shell에서 app 시작 : python main.py