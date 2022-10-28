from flask import Flask,request,render_template

app = Flask(__name__)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        message = f'用户名是:{username}</br>密码是:{password}'
        return message

    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
