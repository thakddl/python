import pymysql

host = 'localhost'
port = 3305
database = 'python'
username = 'root'
password = 'python'

conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
curs = conn.cursor()
sql = 'select * from emp'
curs.execute(sql)
rows = curs.fetchall()
print(rows)    
 
curs.close()
conn.close()