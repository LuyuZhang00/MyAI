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
sql = """
CREATE TABLE books (
id int NOT NULL AUTO_INCREMENT,
name varchar(255) NOT NULL,
category varchar(50) NOT NULL,
price decimal(10,2) DEFAULT '0',
publish_time date DEFAULT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
"""
cursor = connectiont.cursor() # 获取游标对象
cursor.execute(sql) # 执行SQL语句
cursor.close()      # 关闭游标
connectiont.close() # 关闭连接
