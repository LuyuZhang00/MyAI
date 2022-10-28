from flask import Flask,request,render_template,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥

@app.route('/login',methods=['GET','POST'])
def login():
    # 验证表单数据
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'mrsoft' and password == 'mrsoft':
            flash('恭喜您登录成功','success')
        else:
            flash('用户名或密码错误', 'error')
        return redirect(url_for('login'))
    return render_template('login.html') # 渲染表单页面

if __name__ == '__main__':
    app.run(debug=True)
