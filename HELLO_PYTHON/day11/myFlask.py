from flask import Flask
from flask.templating import render_template
from day11.daomember import DaoMember
from flask.globals import request
from flask.json import jsonify

app = Flask(__name__, static_url_path='', static_folder='static')
dm = DaoMember()

@app.route('/list')
def list():
    list = dm.mySelect()
    return render_template("memberlist.html", list=list)

@app.route('/myInsert')
def myInsert():
    data = request.get_json()
    m_name = data['m_name']
    tel = data['tel']
    addr = data['addr']
    cnt = dm.myInsert(m_name,tel,addr)
    result = "fail"
    if cnt==1:
        result="success"
    return jsonify(result=result)

@app.route('/myUpdate', methods=['POST'])
def myUpdate():
    data = request.get_json()
    m_id = data['m_id']
    m_name = data['m_name']
    tel = data['tel']
    addr = data['addr']
    cnt = dm.myUpdate(m_id,m_name,tel,addr)
    result = "fail"
    if cnt==1:
        result="success"
    return jsonify(result=result)

@app.route('/myDelete', methods=['POST'])
def myDelete():
    data = request.get_json()
    m_id = data['m_id']
    cnt = dm.myDelete(m_id)
    result = "fail"
    if cnt==1:
        result="success"
    return jsonify(result=result)

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=80)