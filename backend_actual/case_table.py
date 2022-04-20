"""
backend_actual.py
实际业务代码和DB操作代码放到一起严重耦合，可测试性差
"""
# 导入 flask 和 flask_sqlalchemy
# flask_restx支持RESTFul的风格，支持swagger文档
import yaml
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, Namespace

# 读取DB配置yaml文件
from backend_actual.log_util import logger

with open('db.yaml') as f:
    dbconfig = yaml.safe_load(f)
    username = dbconfig.get('database').get('username')
    password = dbconfig.get('database').get('password')
    serverip = dbconfig.get('database').get('serverip')
    db = dbconfig.get('database').get('db')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymsql://{username}:{password}@{serverip}/{db}?charset=utf-8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # 解决FSADeprecationWarning异常
# SQLAlchemy绑定app
db = SQLAlchemy(app)

# swagger文档接口的命名空间
case_ns = Namespace('case', description='用例管理')

# 创建用例表
class TestCase(db.Model):
    # 表名
    __tablename__ = 'testcase'
    # 用例ID，主键标识
    id = db.Column(db.Integer, primary_key=True)
    # 用例标题，限定80字符，不为空，且唯一
    case_title = db.Column(db.String(80), nullable=False, unique=True)
    # 备注
    remark = db.Column(db.String(100))


# 测试用例管理
@case_ns.route('')
class TestCaseSever(Resource):
    """
    查询接口：可以传ID，可以不传id
    不传ID：返回全部数据
    传ID：返回查询到对应数据，如果未查询到则返回空列表
    """

    def get(self):
        """
        测试用例查询
        :return:
        """
        # 获取接受的参数
        case_id = request.args.get('id')

        logger.info(f'type(request.args) <====={type(request.args)}')
        logger.info(f'接收到的参数 <====== {case_id}')

        if case_id:
            # 如果id不为空，查询操作
            case_data = TestCase.query.filter_by(id=case_id).first()
            logger.info(f'{case_data}')
            # 如果查询有数据，查询操作
            if case_data:
               datas = [{'id': case_data.id,
                        'case_title': case_data.case_title,
                         'remark': case_data.remark}]
               logger.info(f'查询返回的数据为：<====={datas}')
            # 如果查不出数据，返回空
            else:
                datas = []

        else:
            # 如果为空，返回所有数据
            case_datas = TestCase.query.all()
            datas = [{'id': case_data.ase_id,
            'case_title': case_data.cas_date,
            'remark': case_data.remake} for case_data in case_datas]

        return datas


    def post(self):
        pass


    def put(self):
        pass


    def delete(self):
        pass



if __name__ == '__main__':
    # db.create_all() //创建生成表
    app.run(debug=True)