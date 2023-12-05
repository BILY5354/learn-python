import mysql.connector

# 先是x轴 后是y
x_y = {
    -81: -49,
    -82: -49,
    -83: -49,
    -84: -48,
    -85: -48,
    -86: -47,
    -87: -47,
    -88: -46,
    -89: -46,
    -90: -45,
    -91: -44,
    -92: -44,
    -93: -43,
    -94: -43,
    -95: -42,
    -96: -41,
    -97: -41,
    -98: -40,
    -99: -39,
    -100: -39,
    -101: -37,
    -102: -36,
    -103: -35,
    -104: -35,
    -105: -33,
    -106: -31,
    -107: -29,
    -108: -27,
    -109: -25,
    -110: -22,
    -111: -22,
    -112: -19,
    -113: -16,
    -114: -13,
}


cnx = mysql.connector.connect(
    host='192.168.0.120',       # 数据库主机地址
    user='root',    # 数据库用户名
    password='123456',   # 数据库密码
    port='3306',
    database='vatop'
)

cursor = cnx.cursor()
add_info = ("INSERT INTO rep_unit (GUID, frameID, blockID, rowID, colID, unitStatus, resultID) VALUES (%s, %s, %s, %s, %s, %s, %s)")

for k, v in x_y.items():
    for i in range(v, -v):
        data_to_insert = ('00000000000000000000000000000000', 0, 0, k, i, 3, 0)
        cursor.execute(add_info, data_to_insert)
    

cnx.commit()  # * 记得加入此行 确保数据有提交到数据库中
cursor.close()
cnx.close()
