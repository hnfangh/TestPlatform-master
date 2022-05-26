from sqlalchemy.orm import relationship

from dao import testcase_plan_rel
from server import db
from utils.log_util import logger

class PlanModel(db.Model):
    # 表名
    __tablename__ = 'plan'
    # 防止多个定义映射到同一个表所导致的冲突
    __table_args__ = {'extend_existing': True}
    # 计划ID,主键标识
    id = db.Column(db.Integer, primary_key=True)
    # 计划名称
    name = db.Column(db.String(80), nullable=False, unique=True)
    # relationship不影响数据库架构。它提供了访问相关对象的方便方法
    testcases = relationship('TestcaseModel', secondary=testcase_plan_rel,backref='plancase')

    @classmethod
    def get_all(cls):
        return db.session.query(cls).all()


    @classmethod
    def get_filter_by(cls, **kwargs):
        return db.session.query(cls).filter_by(**kwargs).all


    @classmethod
    def create(cls, name, case_objs):
        '''
        name: 测试计划名称
        testcase_objs: 测试用例对象列表[tetscase1, testcase2]
        :return:
        '''
        instance = cls(name=name)
        db.session.add(instance)
        instance.testcase = case_objs
        db.session.commit()

        plan_id = instance.id
        logger.info(f'创建的测试计划的ID为 <===== {plan_id}')
        db.session.close()
        return plan_id

# if __name__ == '__main__':
#     db.create_all()


'''
常用的SQLAlchemy关系选项

选项名	说明
backref	在关系的另一模型中添加反向引用,用于设置外键名称,在1查多的
primary join	明确指定两个模型之间使用的连表条件
lazy	指定如何加载关联模型数据的方式。参数值:
select（立即加载，查询所有相关数据显示，相当于lazy=True）
subquery（立即加载，但使用子查询）
dynamic（不加载记录，但提供加载记录的查询对象）
uselist	如果为False，不使用列表，而使用标量值。一对一关系中，需要设置relationship中的uselist=Flase，其他数据库操作一样。
secondary	指定多对多关系中关系表的名字。
多对多关系中，需建立关系表，设置 secondary=关系表  
secondary join	在SQLAlchemy中无法自行决定时，指定多对多关系中的二级连表条件

'''