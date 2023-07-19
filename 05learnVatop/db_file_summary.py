import re
import os
import sqlite3
import json
from pathlib import Path
from configparser import ConfigParser



def db_file_summary(ftype,db_name):
    
    # ftype = 1
    db_name_list = ['SimulRecipe1_20230626_105518.db3']
    db_file_path = '05learnVatop/db/' + db_name_list[0]
    db_file_Path = Path(db_file_path)
    if(not db_file_Path.exists()):
        print(db_name + ("mg_notfound","未找到该报告文件"))
        # return redirect(url_for('reportlist',ftype = ftype))

    sql = "select GUID,LotNo,machineId,startTime,endTime,defects,attrib,runAttrib from REP_INST LIMIT 1"
    result_sql = execute_sql(db_file_path, sql)[0]
    # 料片 块X行X列
    DIM = re.search(r'(?<=\<DIM\>).*?(?=\<\/DIM\>)',
                    str(result_sql[6])).group()
    RECIPE = re.search(r'(?<=\<RECIPE\>).*?(?=\<\/RECIPE\>)',
                    str(result_sql[6])).group()
    MOTION = "未记录"   
    if("MOTION" in str(result_sql[6])):
        MOTION = re.search(r'(?<=\<MOTION\>).*?(?=\<\/MOTION\>)',
                        str(result_sql[6])).group()
    # 封装类型
    try:
        PKG = re.search(r'(?<=\<PKG\>).*?(?=\<\/PKG\>)',str(result_sql[6])).group()
    except:
        PKG = ' '          
    # 产品名称
    try:
        DEV = re.search(r'(?<=\<DEV\>).*?(?=\<\/DEV\>)',str(result_sql[6])).group()
    except:
        DEV = ' '                 
    # 固晶机ID
    DBID = re.search(r'(?<=\<DBID\>).*?(?=\<\/DBID\>)',
                    str(result_sql[6])).group()
    # 焊线机ID
    WBID = re.search(r'(?<=\<WBID\>).*?(?=\<\/WBID\>)',
                    str(result_sql[6])).group()
    # 操作员ID
    OPER = re.search(r'(?<=\<OPER\>).*?(?=\<\/OPER\>)',
                    str(result_sql[6])).group()
    # 批次数量
    LOTSIZE = re.search(r'(?<=\<LOTSIZE\>).*?(?=\<\/LOTSIZE\>)',
                    str(result_sql[6])).group()
    # 料盒数量
    MAGCOUNT = re.search(r'(?<=\<MAGCOUNT\>).*?(?=\<\/MAGCOUNT\>)',
                    str(result_sql[6])).group()

    runAttrib_json = json.loads(result_sql[7])
    
    defects_dict = {}
    if(result_sql[5] == '' or result_sql[5] == None):
        print(db_name + ("mg_miss","报告非正常结束，defects 信息不全"))
        return 
    defects_list = result_sql[5].split(";")
    for defect in defects_list:
        defect_list = defect.split(",")
        if (defect_list[5] != '0'):
            # 这里有可能自定义的多个缺陷项 缺陷名字和缺陷代码 是一样的
            if (defect_list[3]+'('+defect_list[0]+')') in defects_dict:
                defects_dict[(defect_list[3]+'('+defect_list[0]+')')] += int(defect_list[5])
            else:
                defects_dict[(defect_list[3]+'('+defect_list[0]+')')] = int(defect_list[5])
    defects_sorted = sorted(defects_dict.items(),
                            key=lambda x: x[1], reverse=True)
    piedata = [
        {"value": (int(runAttrib_json["GOOD"]) + int(runAttrib_json['ASSISTPASS'])), "name":("mg_ok","良品")},
        # {"value": (int(runAttrib_json["FAIL"]) + int(runAttrib_json['ASSISTFAIL'])), "name":"次品"}
    ]
    for item in defects_sorted:
        piedata.append({"value":item[1],"name":item[0]})
    defects_names = [i[0] for i in defects_sorted]
    defect_counts = list(defects_dict.values())
    defect_counts.sort(reverse=True)
    defects_sum = sum(defect_counts)
    assist_list = [sum(defect_counts[:k])
                   for k, v in enumerate(defect_counts)]
    # defects_names.insert(0, "总缺陷数")
    defects_names.append(("mg_totaldef","总缺陷数"))
    # 第一列总数，不同颜色
    defect_counts_first = {'value': defects_sum,
                           'itemStyle': {'color': "#546570"}}
    # defect_counts.insert(0, defect_counts_first)
    defect_counts.append(defect_counts_first)
    # assist_list.insert(0, 0)
    assist_list.append(0)

    # demo1 弧高
    # all_item_value = []
    # hugao_value = get_item_all_value(ftype,db_name,"弧高")
    # key_word = ["弧高"]
    # for key in key_word:
    #     item_dict = {}
    #     item_value = get_item_all_value(ftype,db_name,key)
    #     item_dict[key] = item_value
    #     all_item_value.append(item_dict)

    print(f'{result_sql}')
    # return render_template("DbfileSummary.html",
    #                         ftype = ftype,
    #                         chartsPrint = contain_chart,
    #                         db_name=db_name,
    #                         GUID=result_sql[0],
    #                         lotNo=result_sql[1],
    #                         machineId=result_sql[2],
    #                         PKG = PKG,
    #                         DEV = DEV,
    #                         startTime=result_sql[3],
    #                         endTime=result_sql[4],
    #                         DIM=DIM,
    #                         DBID = DBID,
    #                         WBID = WBID,
    #                         OPER = OPER,
    #                         LOTSIZE = LOTSIZE,
    #                         MAGCOUNT = MAGCOUNT,
    #                         RECIPE=RECIPE.split("\\")[-1],
    #                         MOTION= MOTION.split("\\")[-1],
    #                         FCOUNT=runAttrib_json["FCOUNT"],
    #                         FAIL=(int(runAttrib_json["FAIL"]) + int(runAttrib_json['ASSISTFAIL'])),
    #                         GOOD=(int(runAttrib_json["GOOD"]) + int(runAttrib_json['ASSISTPASS'])),
    #                         piedata=piedata,
    #                         defects_names=defects_names,
    #                         defect_counts=defect_counts,
    #                         assist_list=assist_list
    #                         )


def execute_sql(db_file_path, sql):
    if(not os.path.isfile(db_file_path)):
        return False
    conn = sqlite3.connect(db_file_path)
    # 设置一个text_factory，告诉decode()忽略此类错误(utf-8无法解读  )
    conn.text_factory = lambda b: b.decode(errors='ignore')
    cursor = conn.cursor()
    try:
        cursor.execute(sql)
        sql_result = cursor.fetchall()
    except:
        print(db_file_path + ("mg_sql","执行sql有误"))
        print(("mg_sqlerror","数据库执行 SQL 有误，请确定数据库文件"+ db_file_path +"是否有内容"))
        return 
        # return redirect(url_for('index'))
    # 关闭游标：
    cursor.close()
    # 提交事务
    conn.commit()
    # 关闭连接
    conn.close()
    return sql_result


db_file_summary(1,'2023_0317_089_0.db3')