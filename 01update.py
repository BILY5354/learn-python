# 调用其它程序 课后作业 有空格需要转义
from subprocess import PIPE, Popen

videoFiles = '''
bandicam 2020-01-10 10-45-13-679.mp4
bandicam 2020-01-06 11-01-35-020.mp4
bandicam 2020-01-06 11-05-11-334.mp4
'''

vfList = videoFiles.splitlines()
for vf in vfList:
    if vf:  # 判断不为空
        tvfList = vf.splitlines()
        newvf = ''  # 新的视频名字
        for tvf in tvfList:
            if "mp4" in tvf:  # 分裂包含 mp4 字符 加 new
                newvf += tvf.split('.')[0] + '.new.' + tvf.split('.')[1]
                break  # 最后部分执行完可以退出了
            newvf += tvf

        proc = Popen(
            f'ffmpeg.exe -i {vf} -af asetrate=44100*8.9/10,atempo=10/8.9 -c:v copy {newvf}',
            stdin=None,
            stdout=PIPE,
            stderr=PIPE,
            shell=True)

        outinfo, errinfo = proc.communicate()
        outinfo = outinfo.decode('gbk')
        errinfo = errinfo.decode('gbk')
        print(outinfo)
        print('-------------')
        print(errinfo)