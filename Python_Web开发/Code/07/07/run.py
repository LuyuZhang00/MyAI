from flask import Flask,request,render_template,make_response,session,redirect,url_for

app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login',methods=['GET','POST'])
def login():
    # 验证表单数据
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'mrsoft' and password == 'mrsoft':
            session['username'] = username  # 将用户名写入session
            session['logged_in'] = True     # 登录标识写入session
            return redirect(url_for('index'))
    return render_template('login.html') # 渲染表单页面

@app.route('/logout')
def logout():
    session.clear() # 清除Session
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
