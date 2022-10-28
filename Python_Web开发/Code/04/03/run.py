import pymysql

connectiont = pymysql.connect(
    host = 'localhost', # 主机名
    user = 'root',      # 数据库用户名
    password = 'andy123456',  # 数据库密码
    db = 'mrsoft',      # 数据库名
    charset = 'utf8',   # 字符集编码
    cursorclass = pymysql.cursors.DictCursor # 游标类型
)

# SQL语句
sql = 'select * from books order by price '
with connectiont.cursor() as cursor:
    cursor.execute(sql)      # 执行SQL语句
    data = cursor.fetchall() # 获取全部数据

# 遍历图书数据
for book in data:
    print(f'图书:{book["name"]},价格:{book["price"]}')

connectiont.close() # 关闭连接
