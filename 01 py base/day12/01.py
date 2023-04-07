import dateutil.parser

# 字符串时间 转化为 datetime 对象
dt = dateutil.parser.isoparse('2008-09-03T20:56:35.450686+00:00')

# 转化为本地时区的 datetime 对象
localdt = dt.astimezone(tz=None)
# 产生本地格式 字符串
print(localdt.strftime('%Y-%m-%d %H:%M:%S'))