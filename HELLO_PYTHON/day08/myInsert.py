import pymysql

host = 'localhost'
port = 3305
database = 'python'
username = 'root'
password = 'python'

conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
cursor = conn.cursor()

e_id = 6
e_name = 6
sex = 6
age = 6
sql = f"""INSERT INTO emp 
          VALUES ('{e_id}','{e_name}','{sex}','{age}')"""
cnt = cursor.execute(sql) 
print("cnt",cnt)
conn.commit()
conn.close()
