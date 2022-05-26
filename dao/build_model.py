import datetime

from sqlalchemy import Integer, ForeignKey, String

from server import db
from dao import plan_model

class BuildModel(db.Model):
    # 表名
    __tablename__ = 'build'
    # 构建ID， 主键
    id = db.Column(Integer, primary_key=True)
    # 外键指向测试计划的id
    plan_id = db.Column(Integer, ForeignKey('plan.id'))
    # 测试报告链接
    report = db.Column(String(120), nullable=False, unique=True)
    # 创建时间，无需传值，自动生成
    created_at = db.Column(db.DateTime, default=datetime.datetime.now())

    # 新增构建记录
    @classmethod
    def create(cls, plan_id, report):
        instance = cls(plan_id=plan_id, report=report)
        db.session.add(instance)
        db.session.commit()
        db.session.close()

    # 查询构建记录
    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()

    @classmethod
    def get_filter_by(cls, **kwargs):
        return db.session.query(cls).filter_by(kwargs).all



# if __name__ == '__main__':
#     db.create_all()

"""
建新表出现：sqlalchemy.exc.NoReferencedTableError: Foreign key associated with column
解决方案：导入dao层对应的包，from dao import testcase_plan_model
"""