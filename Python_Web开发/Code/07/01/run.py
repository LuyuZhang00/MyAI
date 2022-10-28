from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    age = request.args.get('age')
    message = f'姓名:{name}\n年龄:{age}'
    return message

if __name__ == '__main__':
    app.run(debug=True)
