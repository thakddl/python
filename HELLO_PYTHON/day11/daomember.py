import pymysql

class DaoMember:
    def __init__(self):
        host = 'localhost'
        port = 3305
        database = 'python'
        username = 'root'
        password = 'python'
        
        self.conn = pymysql.connect(host=host, user=username, passwd=password, db=database, port=port, charset='utf8')
        self.curs = self.conn.cursor(pymysql.cursors.DictCursor)
    
    def mySelect(self):
        sql="""
                select
                    m_id,
                    m_name,
                    tel,
                    addr
                from
                    member
            """
        self.curs.execute(sql)
        myList = self.curs.fetchall()
        return myList
    
    def myInsert(self):
        pass