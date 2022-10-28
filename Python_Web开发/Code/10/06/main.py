import tornadoredis


CONNECTION_POOL = tornadoredis.ConnectionPool(max_connections=100, wait_for_available=True)
c = tornadoredis.Client(host="127.0.0.1", port="6379", connection_pool=CONNECTION_POOL)
# 测试是否连接成功，写一个key，并查看redis数据库是否存在该key
c.set("age",18)