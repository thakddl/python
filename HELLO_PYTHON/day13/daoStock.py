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
    
    def mySelect(self,s_name):
        sql = f"""
                SELECT 
                    s_code
                    ,s_name
                    ,price
                    ,ymd_hm
                FROM stock
                WHERE
                s_name = '{s_name}'
              """
        self.curs.execute(sql)
        myList = self.curs.fetchall()
        return myList 
    
    def myNames(self):
        sql = f"""
                SELECT 
                    s_name
                FROM stock
                GROUP BY s_name
              """
        self.curs.execute(sql)
        myList = self.curs.fetchall()
        return myList 
    
    def myPrice(self,s_name):
        ret = []
        sql = f"""
                SELECT 
                    s_name
                    ,price
                FROM stock
                where 
                    s_name ='{s_name}'
              """
        self.curs.execute(sql)
        myList = self.curs.fetchall()
        for p in myList:
            ret.append(p['price'])
        
        return ret 
    
    def __del__(self):
        self.curs.close()
        self.conn.close()


    