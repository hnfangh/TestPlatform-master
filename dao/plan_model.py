from sqlalchemy.orm import relationship

from server import db


class PlanModel(db.model):
    # 表名
    __tablename__ = 'plan'
    # 计划ID,主键标识
    id = db.Colunm(db.Integer, primary_key=True)
    # 计划名称
    name = db.Colunm(db.String(80), nullable=False, unique=True)

    # testcase = relationship('TestcaseModel', secondary=testcase_plan_rel,backref='plancase')