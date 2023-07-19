import os
from datetime import datetime
import mysql.connector

# 创建连接对象
cnx = mysql.connector.connect(
    host='192.168.0.23',       # 数据库主机地址
    user='user',    # 数据库用户名
    password='vatopaoi=',   # 数据库密码
    port='3306',
    database='vt_aoi'
)

output_path = "./02workspace/04genSqlFromDb/output"
now_time = datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
create_new_folder_name = os.path.join(output_path, now_time)
os.makedirs(fr'{create_new_folder_name}')

# 获取数据库游标
cursor = cnx.cursor()

# 要导出的表的名称列表
table_names = ["rep_frame", "rep_lot", "rep_result", "rep_unit"]

# 循环导出每张表的表结构和数据
for table_name in table_names:
    # 导出表结构
    cursor.execute(f"SHOW CREATE TABLE {table_name}")
    create_table_sql = cursor.fetchall()[0][1]

    # 导出表数据
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()

    
    # 输出到文件
    with open(fr"{create_new_folder_name}/{table_name}.sql", "w", encoding="utf8") as sql_file:
        sql_file.write(create_table_sql + ";\n")

        for row in rows:
            values = '", "'.join([str(val) for val in row])
            sql_file.write(f'INSERT INTO {table_name} VALUES ("{values}");\n')

# 关闭数据库连接
cnx.close()