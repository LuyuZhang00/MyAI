import os
import uuid

from flask import send_from_directory
from flask import Flask,request,render_template,redirect,url_for

app = Flask(__name__)
UPLOAD_FOLDER = os.path.join(app.root_path,'uploads')
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """
    判断上传文件类型是否允许
    :param filename: 文件名
    :return: 布尔值True或False
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

def random_file(filename):
    """
    生成随机文件
    :param filename: 文件名
    :return: 随机文件名
    """
    # 获取文件后缀
    ext = os.path.splitext(filename)[1]
    # 使用uuid生成随机字符
    new_filename = uuid.uuid4().hex+ext
    return new_filename

@app.route('/upload',methods=['GET','POST'])
def upload():
    """
    头像上传表单页面
    :return:
    """
    if request.method == 'POST':
        # 接受头像字段
        avatar = request.files['avatar']
        # 判断文件是否上传，已经上传文件类型是否正确
        if avatar and allowed_file(avatar.filename):
            # 生成一个随机文件名
            filename = random_file(avatar.filename)
            # 保存文件
            avatar.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file',filename=filename))

    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    """
    显示上传头像
    :param filename: 文件名
    :return: 真实文件路径
    """
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

if __name__ == '__main__':
    app.run(debug=True)
