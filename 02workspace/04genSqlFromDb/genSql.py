import mysql.connector

# 创建连接对象
cnx = mysql.connector.connect(
    host='192.168.0.23',       # 数据库主机地址
    user='user',    # 数据库用户名
    password='vatopaoi=',   # 数据库密码
    port='3306',
    database='vt_aoi'
)

# 获取所有表名
cur = cnx.cursor()
cur.execute('SHOW TABLES;')
tables = cur.fetchall()

# 生成所有 SQL 语句
sqls = []
for table in tables:
    cur.execute('SHOW CREATE TABLE ' + table[0] + ';')
    create_table = cur.fetchone()[1]
    sql = create_table + ';' + '\n'
    sqls.append(sql)

# print(sqls)

# 保存 SQL 脚本
with open('02workspace/04genSqlFromDb/database.sql', 'w', encoding='utf8') as f:
    f.writelines(sqls)
    
# 关闭连接
cur.close()
cnx.close()