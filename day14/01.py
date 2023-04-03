# 调用其它程序 课后作业 有空格需要转义 
#! 用 os.system 会遇到空格问题 显示没有此文件夹 因此改用 
import os
videoFiles = '''
bandicam 2020-01-10 10-45-13-679.mp4
bandicam 2020-01-06 11-01-35-020.mp4
bandicam 2020-01-06 11-05-11-334.mp4
'''

nvfList = [] # 新的视频列表 包含空格
vfList = videoFiles.splitlines()
for vf in vfList:
    if vf:  # 判断不为空
        tvfList = vf.split(' ') # tvfList 是一开始的路径在删除空格后的列表
        newvf = '' # 新的视频名字
        for tvf in tvfList:
            if "mp4" in tvf: # 分裂包含 mp4 字符 加 new
                newvf += tvf.split('.')[0] + '.new.' + tvf.split('.')[1]
                break # 最后部分执行完可以退出了
            newvf += tvf + ' '
            
        nvfList.append(newvf) # 加入包含空格新的列表里
    

ovfList = [] # 旧的视频列表 包含空格
for tt in nvfList:
    tt2 = tt.replace(".new","")
    ovfList.append(tt2)

print(ovfList)
print(nvfList)

for ovf in ovfList:
    if ovf:
        for nvf in nvfList:
            cmd = f'ffmpeg.exe -i {ovf} -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy {nvf}'
            # print(cmd)
            # os.system(cmd)
    else:
        continue