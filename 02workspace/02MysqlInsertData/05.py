# 用 python MySQL-connector 插入数据
import mysql.connector

cnx = mysql.connector.connect(
    host='192.168.0.23',       # 数据库主机地址
    user='user',    # 数据库用户名
    password='vatopaoi=',   # 数据库密码
    port='3306',
    database='vt_aoi'
)

cursor = cnx.cursor()
# query = ("UPDATE rep_result SET GUID='genByPy' WHERE GUID='AAAABBBBCCCCDDDD03'")
query = ("UPDATE rep_frame SET GUID='genByPy' WHERE GUID='AAAABBBBCCCCDDDD03'")

cursor.execute(query)
cnx.commit() #* 记得加入此行 确保数据有提交到数据库中

# print(cnx) # 输出 <mysql.connector.connection_cext.CMySQLConnection object at 0x7ff200815c88>
cnx.close()