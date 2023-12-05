import re

with open('05learnVatop/0501UPHanalyse/logs/VISION.log', 'r', encoding='gbk') as f:
    vision_logs = f.readlines()

vision_logs.reverse()

position_info_dict = {}
for log in vision_logs:  # 將相同的位置log整个到一起
    log = log.replace("\n", "")
    if '[pos:' in log:
        pos = re.findall(r'\[.*?\]', log)[0]
        if pos not in position_info_dict:
            position_info_dict[pos] = []
            position_info_dict[pos].append(log)
        else:
            position_info_dict[pos].append(log)

# print(position_info_dict)
for k,value in position_info_dict.items():
    with open('05learnVatop/0501UPHanalyse/out/out.log', "a", encoding="gbk") as f:
           f.write(k)
           f.write('\n')
    for v in value:
       with open('05learnVatop/0501UPHanalyse/out/out.log', "a", encoding="gbk") as f:
           f.write(v)
           f.write('\n')
