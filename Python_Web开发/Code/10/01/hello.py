import tornado.ioloop # 导入ioloop 模块
import tornado.web    # 导入web 模块

class MainHandler(tornado.web.RequestHandler):
    ''' GET请求 '''
    def get(self):
        self.write("Hello World !") # 输出字符串

def make_app():
    ''' 创建Tornado应用 '''
    return tornado.web.Application([
        (r"/", MainHandler),   # 设置路由
    ])

if __name__ == "__main__":
    app = make_app() # 创建Tornado应用
    app.listen(8888) # 设置监听端口
    print('Starting server on port 8888...') # 输出提示信息
    tornado.ioloop.IOLoop.current().start() # 启动服务
