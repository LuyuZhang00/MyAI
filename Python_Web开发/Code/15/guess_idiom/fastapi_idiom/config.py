class Config:
    SECRET_KEY = 'mrsoft'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:andy123456@localhost/idiom?charset=utf8mb4"

    # 小程序配置信息
    AppID = '*****'     # 小程序的AppID
    AppSecret = '*****' # 小程序的AppSecret