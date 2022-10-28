import tornado.ioloop # 导入ioloop 模块
import tornado.web    # 导入web 模块
import os

class MainHandler(tornado.web.RequestHandler):
    ''' GET请求 '''
    def get(self):
        self.write("Hello World !") # 输出字符串

class LoginHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('login.html')

    def post(self):
        username = self.get_argument('username', '')    # 接收用户名参数
        password = self.get_argument('password', '')    # 接收密码参数
        self.write("username is {}, password is {}".format(username,password ))

def make_app():
    ''' 创建Tornado应用 '''
    return tornado.web.Application(
        handlers =[
            (r"/", MainHandler),        # 设置路由
            (r"/login",LoginHandler)],  # 设置登录页路由
        debug = True,  # 开启调试模式
        template_path=os.path.join(os.path.dirname(__file__), "templates"),  # 设置模板路径
    )

if __name__ == "__main__":
    app = make_app() # 创建Tornado应用
    app.listen(8888) # 设置监听端口
    print('Starting server on port 8888...') # 输出提示信息
    tornado.ioloop.IOLoop.current().start() # 启动服务