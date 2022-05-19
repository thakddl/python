from flask import Flask
from flask import request
from flask.templating import render_template

app = Flask(__name__)
 
@app.route('/')
def index():
    return render_template('post.html')

@app.route('/view')
def view():
    name = 'Hope'
    list = ['a','b','c']
    c = {'e_id':1, 'e_name':1, 'sex':1, 'age':1}
    d = [
            {'e_id':2, 'e_name':2, 'sex':2, 'age':2},
            {'e_id':3, 'e_name':3, 'sex':3, 'age':3}        
        ]
    return render_template('view.html', name=name, list=list, c=c, d=d)

@app.route('/para', methods=['POST', 'GET'])
def para():
    #a = request.args['a']
    #aa = request.args.get("aa")
    a = request.form.get('a')
    return f'a = {a}'

if __name__ == "__main__": 
    app.run(host='localhost', port=80)