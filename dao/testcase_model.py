
from server import db
from utils.log_util import logger

"""
Dao只负责与DB交互
"""

class TestcaseModel(db.Model):
    # 表名
    __tablename__ = 'testcase'
    # 用例ID，主键标识
    id = db.Column(db.Integer, primary_key=True)
    # 用例标题，限定80字符，不为空，且唯一
    case_title = db.Column(db.String(80), nullable=False, unique=True)
    # 备注
    remark = db.Column(db.String(100))



    # 查询用例不带条件
    @classmethod
    def get_all(cls):
        return cls.query.all()

    # 查询用例带条件
    @classmethod
    def get_filter_by(cls,**kwargs):
        return cls.query.filter_by(**kwargs).first()



    # 新增用例
    @classmethod
    def create(cls, id, case_title,remark):
        result = cls(id=id, case_title=case_title, remark=remark)
        logger.info(f'将要新增的内容为 <===== {result}')
        db.session.add(result)
        db.session.commit()
        db.session.close()



    # 更新用例
    @classmethod
    def update(cls,id,case_title,remark):
        update_data = cls(id=id,case_title=case_title,remark=remark)
        logger.info(f'将要更新的内容为 <===== {update_data}')
        cls.query.filter_by(id=id).update({'id': id,'case_title':case_title,'remark':remark})
        # 提交更新内容
        db.session.commit()
        db.session.close()


    # 删除用例
    @classmethod
    def delete(cls, id):
        TestcaseModel.query.filter_by(id=id).delete()
        logger.info(f'将要删除的内容为 <===== {id}')
        db.session.commit()
        db.session.close()



# if __name__ == '__main__':
# #     新增testcase表字段
# #     db.create_all()
