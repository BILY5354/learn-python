# 创建最后一个表的数据
from random import randint, uniform
import mysql.connector
""" #todo 缩进为此表新增
1*3托盘*8unit*6视角*3配方应用*3测量项
GUID AAAABBBBCCCCDDDD03
framID 托盘数:3
posBlock 固定为1
posRow 行:2
posCol 列:4
    objID 视角 1 2 3 4 5 6
    appID 检测应用ID
    taskID 检测项ID
result 共12片 其中3片 ng 9片ok
defectID 缺陷ID -1 36 44
"""

GUID = "AAAABBBBCCCCDDDD03"
MAXFRAMEID = 3  # 托盘数
MAXPOSROW = 2  # 行
MAXPOSCOL = 4  # 列
MAXPOSOBJ = 6  # 视角
MAXAPPID = 3  # app检测数量
DEFECTIDLIST = [-1, 36, 44]
NGLEFT = 0  # 还剩下ng数量 先造ng
APPIDLIST = [1001, 1002, 2001]  # 配方应用列表
TASKDICT = {  # 配方所对应的测量项列表
    1001: 1002001,
    1002: 1002002,
    2001: 2001001
}

LOGDICT = {  # 用于 长宽高的 log 需要拼接 一共3部分 ？  =1(1nd Bd)B1 宽度 = ;
    0: "=1(1nd Bd)B1 宽度 = ",
    1: "=1(1nd Bd)B1 长度 = ",
    2: "=1(1nd Bd)B1 焊盘*距离 = ",
}
NULL = 'Null'


#  新建插入每一行的字典数据
def genInsertDataDict(frameID, posRow, posCol, posObj, appID, taskID, result, defectID, isMeasure, meaValue, log):
    global GUID, NULL
    insertDataDict = {
        # GUID, frameID, blockID, rowID, colID, objID, appID, taskID, result, defectID, draw, duration, type, isMeasure, meaValue, log, info
        'GUID': GUID,
        'frameID': frameID,
        'blockID': 1,
        'rowID': posRow,
        'colID': posCol,
        'objID': posObj,  # 6个视角
        'appID': appID,
        'taskID': taskID,
        'result': result,
        'defectID': defectID,
        'draw': "{}",
        'duration': randint(0, 500),
        'type': '1',
        'isMeasure': isMeasure,
        'meaValue': meaValue,  # task 项数据
        'log': log,  # log数据
        # 'insertTime': NULL,
        # 'updateTime': NULL,
        # 'info': NULL
    }

    return insertDataDict


# 插入的每一行为字典
unitNu = 0
totoalDict = {}
for fid in range(1, MAXFRAMEID+1):  # 托盘 1~3

    for pr in range(1, MAXPOSROW+1):  # 行

        for pc in range(1, MAXPOSCOL+1):  # 列

            # 确定 坏片ng defectID 与result 的值
            if NGLEFT < 3:  # 先造ng
                result = 1
                defectID = DEFECTIDLIST[NGLEFT]
            else:  # 正常片
                result = 2  # reuslt为2 正常
                defectID = NULL

            for po in range(1, MAXPOSOBJ+1):  # 相机 6个角度

                for ai in range(1, MAXAPPID+1):  # appid 按顺序拿

                    if NGLEFT < 3:  # ng片 log信息第一位为0 正常为1
                        logTag = '0'
                    else:  # 正常片
                        logTag = '1'

                    idd = {}  # 每次进来 创建新字典
                    meaValue = 0.0
                    log = ""
                    isMeasure = 0  # 是否有测量值
                    if randint(0, 1) == 1:  # * 1为测量项 0不是
                        isMeasure = 1
                        meaValue = uniform(1, 500)
                        log = logTag + \
                            LOGDICT[randint(0, 2)] + str(meaValue) + ";"
                    else:  # 不是检测项
                        meaValue = 0.0
                        isMeasure = 0
                        # 不是检测项 没有数据
                        log = logTag + LOGDICT[randint(0, 2)] + ";"

                    idd = genInsertDataDict(
                        fid, pr, pc, po, APPIDLIST[ai-1], TASKDICT[APPIDLIST[ai-1]], result, defectID, isMeasure, meaValue, log)

                    unitNu += 1
                    totoalDict[unitNu] = idd

            NGLEFT += 1  # ng unit 加1
            # print(NGLEFT)

with open("my fun/02MysqlInsertData/output.txt", "w", encoding="utf8") as f:
    f.write(str(totoalDict))


cnx = mysql.connector.connect(
    host='192.168.0.23',       # 数据库主机地址
    user='user',    # 数据库用户名
    password='vatopaoi=',   # 数据库密码
    port='3306',
    database='vt_aoi'
)

cursor = cnx.cursor()

add_result = ("INSERT INTO rep_result "
              "(GUID, frameID, blockID, rowID, colID, objID, appID, taskID, result, defectID, draw, duration, type, isMeasure, meaValue, log) "
              "VALUES (%(GUID)s, %(frameID)s, %(blockID)s, %(rowID)s, %(colID)s, %(objID)s, %(appID)s, %(taskID)s, %(result)s, %(defectID)s, %(draw)s, %(duration)s, %(type)s, %(isMeasure)s, %(meaValue)s, %(log)s)")


# 插入数据
for t, tdict in totoalDict.items():  # t 为序号 tdict 为字典
    print(tdict)
    cursor.execute(add_result, tdict)


# Make sure data is committed to the database
cnx.commit()
cursor.close()
cnx.close()