import sqlite3
from pathlib import Path
import os
import re


# db_file_path = '\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_095927.db3'
# db_file_path_list = [
#     '\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230522\\SimulRecipe1_20230523_031903.db3', 
#     '\\\\192.168.0.11\\Data\\GeRun\\SecondaryWire\\4#\\VT报告文件db3\\20230626-T9-test\\SimulRecipe1_20230627_095927.db3'
# ]
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


# 构建缺陷整体字典 {'缺陷id': '106','缺陷名字': '塌线缺陷(SW)', 'ver': [最小单位(空)]}
# 没有 version_name 因为其是用于 append 的
def build_one_defect_unit(defect_id, defect_name, defect_code):
    return {
        'id' : defect_id,
        'name' : defect_name + f'({defect_code})' ,
        'ver' : []
    }


# 构建缺陷-数量字典 插入最小单位 {'版本号' : 数量}
def build_ver_nu_of_defect_unit(version_name, number):
    return {
        version_name : number
    }



#* 程序开始
total_batch_name = [i for i in data.keys()]
total_version_defects_dict = {}  # 总字典 所有版本批次号的缺陷 

for current_batch_name in total_batch_name:
    db_file_path_list = data[current_batch_name]

    # 在一开始便判断总字典是否存在此批次号
    if current_batch_name not in total_version_defects_dict:
        total_version_defects_dict[current_batch_name] = []
        current_batch_defect_id_list = [] # 保存本批次的所有缺陷id 且该id顺序与字典中相同

    for db_file_path in db_file_path_list:

        db_file_path = Path(db_file_path)
        version_name = re.findall(r'VT报告文件db3\\(.*?)\\',str(db_file_path))[0]  # ver_id

        query_sql = "select defects from REP_INST LIMIT 1"
        query_sql_result = execute_sql(db_file_path,query_sql)[0][0] # 拿字符
        if query_sql_result is None:
            print('报告非正常结束,defects 信息不全') 
        if not query_sql_result.endswith(';'): # 在最后加分号方便re分组
            query_sql_result += ";"
        one_batch_defects_list = re.findall(r'(.*?;)', query_sql_result)
        
        for defect in one_batch_defects_list:
            split_defect_list = defect.split(',')
            # 存在大于0的缺陷 
            if int(split_defect_list[1]) == 1 and int(split_defect_list[5]) > 0:

                # 统一生成本次 {'版本号' : 数量} 用于加入
                current_ver_nu_of_defect = build_ver_nu_of_defect_unit(version_name, split_defect_list[5])
                current_defect_id = split_defect_list[2]

                # 无此缺陷信息 需要构建
                if current_defect_id not in current_batch_defect_id_list: 
                    current_batch_defect_dict = build_one_defect_unit(split_defect_list[2],
                                                                    split_defect_list[3],
                                                                    split_defect_list[0])
                    
                    current_batch_defect_dict['ver'].append(current_ver_nu_of_defect)
                    current_batch_defect_id_list.append(current_defect_id)
                    
                    # 将首次创建单个缺陷的字典加入该批次的列表中 如果已有此id直接append
                    total_version_defects_dict[current_batch_name].append(current_batch_defect_dict)

                else:  # 有此缺陷字典 直接加入 {'版本号' : 数量} 首先找此缺陷在列表的位置
                    try:
                        # 该索引是当前缺陷在该批次列表中的下标
                        current_index = current_batch_defect_id_list.index(current_defect_id)
                    except:
                        #! 是否需要加入信息插入Excel表中
                        print("没有此defrct Id信息")
                        break

                    defect_of_specific_id_dict = total_version_defects_dict[current_batch_name][current_index]
                    defect_of_specific_id_dict["ver"].append(current_ver_nu_of_defect)

            else: # 本缺陷数为0 看下一个
                continue
    

with open('05learnVatop\output.json', 'w',encoding='utf8') as f:
    f.write(str(total_version_defects_dict))
# print(total_version_defects_dict)
