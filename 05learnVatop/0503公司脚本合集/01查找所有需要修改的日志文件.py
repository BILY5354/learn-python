# 使用方法 放到主控跟目录下
import os

ALL_CONDITION = [
    'method.LogToLocal(ProdFlowTcpBLL.host,', 
    'method.Log(host', 'method.Log(ProdFlowTcpBLL.host,', 
    'method.LogToLocal(host,', 
    'method.Log(HostHelper.GetLocalMachineInfo(),', 
    'method.Log(IPHelper.GetLocalIP(),', 
    'method.LogToLocal(host: host,', 
    'method.LogEx(host,', 
    'method.Log("cfgTest",', 
    'method.Log(Host,', 
    'method.LogToLocal(Host,', 
    'method.Log(FrmLogin.LocalIP,'
]
files_path: list = []


for dirpath, dirnames, filenames in os.walk("."):
    """获取所有cs文件路径
    """
    if "HTMotion" in dirpath or "HTCommon" in dirpath or "HTWafer" in dirpath or "SecsGem" in dirpath:
        continue
    for filename in filenames:
        if filename.endswith(".cs"):
            fpath = os.path.join(dirpath, filename)
            files_path.append(fpath)

print(f'总共有{len(files_path)}个文件')

has_log_files_path = []


for current_fpath in files_path:
    """获取所有包含旧日志method.Log的cs文件路径
    """
    try:
        with open(fr'{current_fpath}', "r", encoding="utf8") as f:
            temp_str = f.read()
    except:
        with open(fr'{current_fpath}', "r", encoding="gbk") as f:
            temp_str = f.read()
        print(f'{current_fpath} 编码gbk')

    if "method.Log" in temp_str:
        has_log_files_path.append(current_fpath)

print(f'总共有{len(has_log_files_path)}个文件需求修改log')

update_log_files: dict = {}


for path in has_log_files_path:
    """读取所有需要修改日志的文件代码
    为什么不在上一个循环中读 因为可能有多个文件需要修改
    """
    try:
        with open(path, "r", encoding="utf8") as f:
            update_log_files[path] = f.readlines()
    except:
        with open(path, "r", encoding='gbk') as f:
            update_log_files[path] = f.readlines()


for i, v in enumerate(has_log_files_path):
    """创造所有需要修改log文件的新路径
    之后这些路径会保存创建对应层级的cs文件 以便存放修改过后的代码
    """

    temp_list = list(v)
    temp_list.insert(1, r"\Z")
    temp_str = ''.join(temp_list)
    has_log_files_path[i] = temp_str


for k, lines in update_log_files.items():
    """修改所有需要修改log文件的代码
    其中v是f.readlines()内容为一个list
    """
    for i, v in enumerate(lines):
        if "method.Log(" in v:

            line = lines[i]

            # for find_current in ALL_CONDITION:
            #     if find_current in line:
            #         lines[i] = lines[i].replace(find_current, 'MotionLog(')
            #         break

            if '(host' in line:
                lines[i] = lines[i].replace('method.Log(host, ', 'MotionLog(')
            elif '(Host' in line:
                lines[i] = lines[i].replace('method.Log(Host, ', 'MotionLog(')
            else:
                print(f'开头不一致！文件{k} {line}')
                break
    
            if 'LocalLogLevel.Error' in line:
                lines[i] = lines[i].replace('LocalLogLevel.Error', 'LogLevel.Error')
               
            elif 'LocalLogLevel.Warn' in line:
                lines[i] = lines[i].replace('LocalLogLevel.Warn', 'LogLevel.Warn')

            elif 'LocalLogLevel.Info' in line:
                lines[i] = lines[i].replace('LocalLogLevel.Info', 'LogLevel.Info')

            elif 'LocalLogLevel.Debug' in line:
                lines[i] = lines[i].replace('LocalLogLevel.Debug', 'LogLevel.Debug')

            elif 'LocalLogLevel.Fatal' in line:
                lines[i] = lines[i].replace('LocalLogLevel.Fatal', 'LogLevel.Fatal')

            elif 'LogLevel' in line:
                pass

            else:
                print(f'啥情况！文件{k} {line}')
        else:
            continue
            if 'LocalLogLevel.Error' in v:
                print(f'111！文件{k} {v}')
    update_log_files[k] = lines
   

for i, path in enumerate(has_log_files_path):
    """创建对应的文件并插入修改过后的代码
    """

    # 获取文件夹路径 并创建对应的层级
    folder_path = os.path.dirname(path)
    os.makedirs(folder_path, exist_ok=True)

    # 原来的地址
    old_path = path.replace(r".\Z", ".")

    for line in update_log_files[old_path]:
        #* 注意旧地址是为了拿字典中的值 而path是新地址 用于写在文件中
        with open(path, "a", encoding="utf8") as f:
            f.write(line)
