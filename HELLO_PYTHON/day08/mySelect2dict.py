import pymysql

host = 'localhost'
port = 3305
database = 'python'
username = 'root'
password = 'python'

conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
cursor = conn.cursor(pymysql.cursors.DictCursor)
sql = 'select * from emp'
cursor.execute(sql)
rows = cursor.fetchall()
print(rows)    
 
conn.close()
