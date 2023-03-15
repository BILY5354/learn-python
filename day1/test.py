upChars = '零壹贰叁肆伍陆柒捌玖' 
def change(): 
    # upChars = '...' 直接使用错误 效果新建一个同名局部变量
    upChars = '零一二三四五六七八九' 
    print(upChars)

change() 
print(upChars)