from server import db
from sqlalchemy import *

from dao import testcase_model
from dao import plan_model

testcase_plan_rel = db.Table(

    # 中间表名称
    'testcase_plan_rel',
    # Column('id', Integer, primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试用例表的id
    Column('testcase_id', Integer, ForeignKey('testcase.id'), primary_key=True),
    # 其中一张表的描述，作为一个外键指向测试计划表的id
    Column('plan_id', Integer, ForeignKey('plan.id'), primary_key=True)

)


# from dao.testcase_model import *
# from dao.plan_model import *
# class Testcase_Plan_Rel_Model(db.Model):
#     __tablename__ = 'testcase_plan_rel'
#     testcase_id = db.Column(db.Integer, db.ForeignKey('testcase.id'), primary_key=True)
#     plan_id = db.Column(db.Integer, db.ForeignKey('plan.id'), primary_key=True)

# if __name__ ==  '__main__':
#     db.create_all()

