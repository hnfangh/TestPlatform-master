from dao.testcase_model import TestcaseModel
from utils.log_util import logger


class Testcase:

    # 查询用例处理逻辑
    def get(self,id=None):

        if id:
            # 如果id不为空，查询操作
            case_data = TestcaseModel.get_filter_by(id=id)
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
            case_datas = TestcaseModel.get_all()
            datas = [{'id': case_data.id,
                      'case_title': case_data.case_title,
                      'remark': case_data.remark} for case_data in case_datas]
        logger.info(f'要返回数据为<====={datas}')
        # 返回数据,保证路由有要返回的数据
        return datas


    # 新增用例处理逻辑
    def create(self, id, case_title, remark):
        # 查询数据库是否有存在的数据记录
        exists = TestcaseModel.get_filter_by(id=id)
        logger.info(f'新增前查询的结果 <===== {exists}')
        # 如果数据存在就新增数据
        if not exists:
            TestcaseModel.create(id=id, case_title=case_title, remark=remark)
            return True
        else:
            return False



    # 更新用例处理逻辑
    def update(self,id,case_title,remark):
        # 查询数据库是否有存在的数据记录
        exists = TestcaseModel.get_filter_by(id=id)
        logger.info(f'更新前查询的结果 <===== {exists}')
        #
        if exists:
            TestcaseModel.update(id=id, case_title=case_title, remark=remark)
            return True
        else:
            return False

    # 删除用例处理逻辑
    def delete(self,id):
        # 查询数据库是否有存在的数据记录
        exists = TestcaseModel.get_filter_by(id=id)
        logger.info(f'删除前查询的结果 <===== {exists}')
        # 如果数据存在，删除数据
        if exists:
            TestcaseModel.delete(id=id)
            return True
        # 不存在，返回false
        else:
            return False