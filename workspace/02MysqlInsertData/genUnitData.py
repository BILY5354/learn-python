# 生成 rep_unit 表数据
from datetime import datetime, timedelta
import mysql.connector
""" #todo
GUID AAAABBBBCCCCDDDD03
framID 托盘数:3
posBlock 固定为1
posRow 行:2
posCol 列:4
result 共12片 其中3片 ng 9片ok
defectID 缺陷ID -1 36 44
"""

GUID = "AAAABBBBCCCCDDDD03"
MAXFRAMEID = 3
MAXPOSROW = 2
MAXPOSCOL = 4
UNITCODE = "U2222"
DEFECTIDLIST = [-1, 36, 44]
NGLEFT = 0  # 还剩下ng数量 先造ng
NULL = 'Null'

#  新建插入每一行的字典数据


def genInsertDataDict(frameID, posRow, posCol, result, defectID):
    global GUID, UNITCODE
    # `GUID`, `frameID`, `blockID`, `rowID`, `colID`, `unitCode`, `startTime`, `endTime`, `result`, `defectID`, `process`, `insertTime`, `updateTime`, `info` 
    insertDataDict = {
        'GUID': GUID,
        'frameID': frameID,
        'blockID': 1,
        'rowID': posRow,
        'colID': posCol,
        'unitCode': UNITCODE,
        'startTime': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        # 加2分钟
        'endTime': (datetime.now()+timedelta(minutes=2)).strftime('%Y-%m-%d %H:%M:%S'),
        'result': result,
        'defectID': defectID,
    }

    return insertDataDict


# 插入的每一行为字典
unitNu = 0
totoalDict = {}
for fid in range(1, MAXFRAMEID+1):  # 托盘 1~3

    for pr in range(1, MAXPOSROW+1):  # 行

        for pc in range(1, MAXPOSCOL+1):  # 列
            # print(f'托盘{fid}行{pr}列{pc}总数{unitNu}')

            idd = {}  # 每次进来 创建新字典

            # 确定 坏片ng defectID 与result 的值
            if NGLEFT < 3:  # 先造ng
                result = 1
                defectID = DEFECTIDLIST[NGLEFT]
                NGLEFT += 1
            else:  # 正常片
                result = 2  # reuslt为2 正常
                defectID = NULL

            idd = genInsertDataDict(fid, pr, pc, result, defectID)  # reuslt为2 正常
            unitNu += 1  # unit 总数加1
            totoalDict[unitNu] = idd # 插入总字典

# 写入文件查看数据
# with open("workspace/02MysqlInsertData/output.txt", "w", encoding="utf8") as f:
#     f.write(str(totoalDict))

cnx = mysql.connector.connect(
    host='192.168.0.23',       # 数据库主机地址
    user='user',    # 数据库用户名
    password='vatopaoi=',   # 数据库密码
    port='3306',
    database='vt_aoi'
)

cursor = cnx.cursor()

# 列记得对应
add_result = ("INSERT INTO rep_unit "
              "(GUID, frameID, blockID, rowID, colID, unitCode, startTime, endTime, result, defectID) "
              "VALUES (%(GUID)s, %(frameID)s, %(blockID)s, %(rowID)s, %(colID)s, %(unitCode)s, %(startTime)s, %(endTime)s, %(result)s, %(defectID)s)")

# 插入数据
for t, tdict in totoalDict.items():  # t 为序号 tdict 为字典
    # print(tdict)
    cursor.execute(add_result, tdict)


# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()


"""测试时间 
print(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print((datetime.now()+timedelta(minutes=10)).strftime('%Y-%m-%d %H:%M:%S')) """
