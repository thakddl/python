import pymysql
class DaoStock:
    def __init__(self):
        host = 'localhost'
        port = 3305
        database = 'python'
        username = 'root'
        password = 'python'
        
        self.conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
        
    def insertStock(self,s_code,s_name,price,time):
        sql=f"""
            INSERT INTO STOCK
            VALUES
            (
                '{s_code}'
                ,'{s_name}'
                ,{price}
                ,'{time}'
            )
        """
        cnt = self.curs.execute(sql)
        self.conn.commit()
        return cnt
    
    def __del__(self):
        self.curs.close()
        self.conn.close()