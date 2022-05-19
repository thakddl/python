from flask import Flask
from flask.templating import render_template
from day13.daoStock import DaoStock
from boto.gs.acl import ENTRY

app = Flask(__name__, static_url_path='', static_folder='static')
ds = DaoStock()
 
@app.route('/stock')
def stock():
    return render_template('stock.html')

@app.route('/jqplot')
def jqplot():
    data=[]
    de = DaoStock()
    mylist = de.myNames()
    for n in mylist:
        s_name = n['s_name']
        prices = de.myPrice(s_name)
        dataEntry= [s_name, prices]
        data.append(dataEntry)
    print(data)
    return render_template('jqplot.html', data=data)

if __name__ == "__main__": 
    app.run(host='0.0.0.0', port=80, debug=True)