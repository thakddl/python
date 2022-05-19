import pymysql

class DaoEmp:
    def __init__(self):
        host = 'localhost'
        port = 3305
        database = 'python'
        username = 'root'
        password = 'python'
        
        self.conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
        self.curs = self.conn.cursor()
        
        
    def mySelect(self):
        sql = """
                select
                    e_id,
                    e_name,
                    sex,
                    age
                from 
                    emp"""
        self.curs.execute(sql)
        myList = self.curs.fetchall()
        return myList 
    
    def myInsert(self,e_name,sex,age):
        sql = f"""
                INSERT INTO EMP
                VALUES
                (
                    0,
                    '{e_name}',
                    '{sex}',
                    {age}
                )"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt 
    
    def myUpdate(self,e_id,e_name,sex,age):
        sql = f"""
                UPDATE EMP
                SET
                    e_name = '{e_name}',
                    sex = '{sex}',
                    age = {age}
                WHERE
                    e_id = '{e_id}'"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt 
    
    def myDelete(self,e_id):
        sql = f"""
                DELETE FROM EMP
                WHERE
                    e_id = '{e_id}'"""
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt 
    
    def __del__(self):
        self.curs.close()
        self.conn.close()

if __name__ == '__main__':
    de = DaoEmp()
    myList = de.mySelect()
    #cnt = de.myInsert(9,9,9)
    #cnt = de.myUpdate(13,9,3,9)
    cnt = de.myDelete(14)
    print(cnt)