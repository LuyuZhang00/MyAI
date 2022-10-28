from flask import Flask,render_template

def count_length(arg):#实现一个可以求长度的函数
    return len(arg)

app = Flask(__name__)
app.secret_key = 'mrsoft12345678' # 设置秘钥
app.add_template_filter(count_length,'count_length')

@app.route('/')
def index():
    content = """
    明日学院，是吉林省明日科技有限公司倾力打造的在线实用技能学习平台，该平台于2016年正式上线，主要为学习者提供海量、优质的课程，
    课程结构严谨，用户可以根据自身的学习程度，自主安排学习进度。我们的宗旨是，为编程学习者提供一站式服务，培养用户的编程思维。
    """
    return render_template('index.html',content=content)

if __name__ == '__main__':
    app.run(debug=True)
