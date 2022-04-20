
# 导入 flask 和 flask_sqlalchemy
# flask_restx支持RESTFul的风格，支持swagger文档
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api
from sqlalchemy.orm import Session

username = 'root'
password = '123456'
server = '47.106.133.253'
db = 'testplatform'

app = Flask(__name__)
api = Api(app)
CORS(app, supports_credentials=True) # 解决前端后端跨域访问问题,允许用户跨源发出Cookie或经过身份验证的请求

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{username}:{password}@{server}/{db}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # 解决FSADeprecationWarning异常
# SQLAlchemy绑定app
db = SQLAlchemy(app)

# 为了查询的时候IDE可以有对应的提示
db_session:Session = db.session



# 导包
def get_router():
    from router.testcase import case_ns
    api.add_namespace(case_ns, '/testcase')




if __name__ == '__main__':
    # 调用get_router方法，完成testcase路由注册
    get_router()
    app.run(debug=True)