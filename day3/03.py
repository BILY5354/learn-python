# 对象方法补充练习 email 邮箱地址 输入合法性验证

def validate_email(emailaddr):
    if((emailaddr.count(' ')==0) and (emailaddr.count('@')==1) and (emailaddr.find('@')!=0)):
        # 现在来判断@后面部分有且仅有一个点 且前后必须有字符 .可不止一个
        tag1=emailaddr.find('@')
        temailaddr=emailaddr[tag1:] #复制@后面的字符串
        tlen=len(temailaddr) #判断最后一位
        if((temailaddr.count('.')==1) and (temailaddr.find('.')!=1) and (temailaddr.find('.')!=(tlen-1))): #@后只能有一个.
            # print(temailaddr) 测试用
            return True
        else:
            return False
    else:
        return False
    

if(validate_email('jolo.smith.email@com.')):
    print("正确")
else:
    print("错误")