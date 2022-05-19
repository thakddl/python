import pymysql

host = 'localhost'
port = 3305
database = 'python'
username = 'root'
password = 'python'

conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
cursor = conn.cursor()

e_id = 6
e_name = 7
sex = 7
age = 7
sql = f"""UPDATE emp 
             SET 
                 e_name='{e_name}', 
                 sex='{sex}', 
                 age='{age}'
           WHERE e_id='{e_id}'"""
cnt = cursor.execute(sql) 
print("cnt",cnt)
conn.commit()
conn.close()
