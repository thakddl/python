from flask import Flask
from flask.templating import render_template
from day10.daoemp import DaoEmp
from flask.globals import request
from flask.json import jsonify

app = Flask(__name__, static_url_path='', static_folder='static')
de = DaoEmp()
 
@app.route('/emplist')
def emplist():
    emplist = de.mySelect()
    return render_template('emplist.html', list=emplist )

@app.route('/myInsert', methods=['POST'])
def myInsert():
    data = request.get_json()
    e_name = data['e_name']
    sex = data['sex']
    age = data['age']
    cnt = de.myInsert(e_name,sex,age)
    result = "fail"
    if cnt==1:
        result="success"
    return jsonify(result=result)

@app.route('/myUpdate', methods=['POST'])
def myUpdate():
    data = request.get_json()
    e_id = data['e_id']
    e_name = data['e_name']
    sex = data['sex']
    age = data['age']
    cnt = de.myUpdate(e_id,e_name,sex,age)
    result = "fail"
    if cnt==1:
        result="success"
    return jsonify(result=result)

@app.route('/myDelete', methods=['POST'])
def myDelete():
    data = request.get_json()
    e_id = data['e_id']
    cnt = de.myDelete(e_id)
    result = "fail"
    if cnt==1:
        result="success"
    return jsonify(result=result)


if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=80)