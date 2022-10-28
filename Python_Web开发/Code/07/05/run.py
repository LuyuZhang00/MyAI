from flask import Flask,request,render_template,make_response

app = Flask(__name__)

@app.route('/')
def index():
    # 判断Cookie是否存在
    if request.cookies.get('username'):
        return '欢迎来到首页!'
    else:
        return '请先登录!'

@app.route('/login',methods=['GET','POST'])
def login():
    # 验证表单数据
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'mrsoft' and password == 'mrsoft':
            # 如果用户名和密码正确，将用户名写入Cookie
            response = make_response(('登录成功!'))    # 获取response对象
            response.set_cookie('username', username) # 将用户名写入Cookie
            return response # 返回response对象
    return render_template('login.html') # 渲染表单页面


@app.route('/logout')
def logout():
    response = make_response(('退出登录!'))
    # 设置Cookie过期时间为0，即删除Cookie
    response.set_cookie('username', '', expires=0)
    return response

if __name__ == '__main__':
    app.run(debug=True)
