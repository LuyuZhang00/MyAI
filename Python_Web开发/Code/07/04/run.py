from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    print('视图函数执行')
    return 'index page'

# 在第一次请求之前运行.
@app.before_first_request
def before_first_request():
    print('before_first_request')

# 在每一次请求前都会执行
@app.before_request
def before_request():
    print('before_request')

# 在请求之后运行
@app.after_request
def after_request(response):
    # response: 就是前面的请求处理完毕之后, 返回的响应数据，前提是视图函数没有出现异常
    # response.headers["Content-Type"] = "application/json"
    print('after_request')
    return response

# 无论视图函数是否出现异常，每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(error):
    print('teardown_request: error %s' % error)

if __name__ == '__main__':
    app.run(debug=True)
