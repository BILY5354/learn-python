# 查询excel文件中查询数据库缺陷信息的代码
from pathlib import Path
import os
import sqlite3

data = {
    "EP2303003GMK125": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230522\\SimulRecipe1_20230523_031903.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_024615.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_044738.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_033515.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_040027.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_021924.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_031546.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_111004.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_095927.db3"
    ],
    "EP2303003GMK126": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230522\\SimulRecipe1_20230523_032027.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_024739.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_044859.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_033828.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_040341.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_022052.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_031716.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_112206.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_101145.db3"
    ],
    "EP2304005GMK042": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\EP2304005GMK042_20230525_021601.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\EP2304005GMK042_20230525_054848.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\EP2304005GMK042_20230529_025800.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\EP2304005GMK042_20230531_032320.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\EP2304005GMK042_20230614_015150.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\EP2304005GMK042_20230615_024515.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\EP2304005GMK042_20230626_101931.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\EP2304005GMK042_20230627_085917.db3"
    ],
    "EP2304005GMK048": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\EP2304005GMK048_20230525_022927.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\EP2304005GMK048_20230525_043055.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\EP2304005GMK048_20230529_031152.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\EP2304005GMK048_20230531_033658.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\EP2304005GMK048_20230614_020328.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\EP2304005GMK048_20230615_025725.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\EP2304005GMK048_20230626_103214.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\EP2304005GMK048_20230627_091149.db3"
    ],
    "EP2302093GMK115": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_024110.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_044236.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_032444.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_034951.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_021410.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_030851.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_104342.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_092339.db3"
    ],
    "EP2302093GMK141": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_024224.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_044349.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_032746.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_035254.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_021525.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_031021.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_105518.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_093523.db3"
    ],
    "EP2302093GMK142": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_024335.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_044459.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_033045.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_035554.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_021638.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_031150.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_110607.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_094656.db3"
    ],
    "EP2303009GMK028": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_030000.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_050106.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_035142.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_041734.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_023309.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_032924.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_113418.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_102405.db3"
    ],
    "EP2303009GMK125": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_031230.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_051312.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_040459.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_043137.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_024519.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_034132.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_114657.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_103629.db3"
    ],
    "EP2303016GMK020": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_032421.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_052444.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_041736.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_044445.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_025709.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_035336.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_115839.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_104814.db3"
    ],
    "EP2303011GMK080": [
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525\\SimulRecipe1_20230525_033637.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230525-1\\SimulRecipe1_20230525_053654.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529\\SimulRecipe1_20230529_043037.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230529-T8\\SimulRecipe1_20230531_045834.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230614-T9\\SimulRecipe1_20230614_030931.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230615-T9\\SimulRecipe1_20230615_040627.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230616-T9\\SimulRecipe1_20230626_121037.db3",
        "\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_110031.db3"
    ]
}

def execute_sql(db_file_path, sql):
    if (not os.path.isfile(db_file_path)):
        return False
    conn = sqlite3.connect(db_file_path)
    # 设置一个text_factory，告诉decode()忽略此类错误(utf-8无法解读)
    conn.text_factory = lambda b: b.decode(errors='ignore')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        sql_result = cursor.fetchall()
    except:
        print('数据库执行 SQL 有误，请确定数据库文件是否有内容')
    # 关闭游标：
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()

    return sql_result



data_set = 'EP2303003GMK125'
total_version_defects_dict = {}

total_batch_name = [i for i in data.keys()]

for current_batch_name in total_batch_name:
    dbFile_path_list = data[current_batch_name]


for db_file_path in dbFile_path_list:
    db_file_path_split = db_file_path.split('\\')
    # 版本号
    ver_id = db_file_path_split[-2]
    db_file_path = Path(db_file_path)
    sql = "select defects from REP_INST LIMIT 1"
    if data_set not in total_version_defects_dict:
        result_sql = execute_sql(db_file_path, sql)[0]
        file_defects_list = []
        defects = result_sql[0]
        if (defects == '' or defects == None):
            print('报告非正常结束,defects 信息不全')
            break
        defects_list = defects.split(";")
        for defect in defects_list:
            defect_list = defect.split(",")
            if (defect_list[5] != '0'):
                defect_dict = {}
                ver_name_count_dict = {}
                ver_defect_list = []
                defect_code = defect_list[0]
                defect_name = defect_list[3]
                defect_id = defect_list[2]
                name_code = defect_name + '(' + defect_code + ')'
                # {'id': '1', 'name': '基准点(REF)', 'ver': [{ghgh:3}, {gfgff:3}]}
                defect_dict['id'] = defect_id
                defect_dict['name'] = name_code
                defect_count = int(defect_list[5])
                ver_name_count_dict[ver_id] = defect_count
                ver_defect_list.append(ver_name_count_dict)
                defect_dict['ver'] = ver_defect_list
                file_defects_list.append(defect_dict)
        total_version_defects_dict[data_set] = file_defects_list
    else:
        file_defect_data_list = []
        db_file_path = Path(db_file_path)
        result_sql = execute_sql(db_file_path, sql)[0]
        file_defects_list = []
        defect_id_list = []
        defects = result_sql[0]
        if (defects == '' or defects == None):
            print('报告非正常结束,defects 信息不全')
            break
        defects_list = defects.split(";")
        for defect in defects_list:
            defect_list = defect.split(",")
            if (defect_list[5] != '0'):
                defect_code = defect_list[0]
                defect_name = defect_list[3]
                defect_id = defect_list[2]
                defect_id_list.append(defect_id)
                name_code = defect_name + '(' + defect_code + ')'
                defect_count = defect_list[5]
                id_name_count = defect_id + ',' + name_code + ',' + defect_count
                file_defect_data_list.append(id_name_count)
        pre_defects_list = total_version_defects_dict[data_set]
        for def_dict in pre_defects_list:
            pre_id = def_dict['id']
            pre_ver_list = def_dict['ver']
            if pre_id not in defect_id_list:
                zero_dict = {}
                zero_dict[ver_id] = 0
                pre_ver_list.append(zero_dict)
            else:
                for defect_list in file_defect_data_list:
                    ver_name_count_dict = {}
                    defect_split = defect_list.split(',')
                    id = defect_split[0]
                    count = int(defect_split[2])
                    if (pre_id == id):
                        ver_name_count_dict[ver_id] = count
                        pre_ver_list.append(ver_name_count_dict)

print(total_version_defects_dict)
