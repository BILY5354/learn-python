studentAges = ['小王:17', '小赵:16', '小李:17', '小孙:16', '小徐:18']

# enumerate (studentAges) 每次迭代返回 一个元组
# 里面有两个元素，依次是 元素的索引和元素本身 
for idx, student in enumerate(studentAges):
    print(idx)
    print(student)
    if int(student.split(':')[-1]) > 17:
        print(idx)