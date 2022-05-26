from service.build import Build

from dao.plan_model import PlanModel
from dao.testcase_model import TestcaseModel
from utils.jenkins_util import JenkinsUtils
from utils.log_util import logger


class Plan:


    def execute(self, plan_id, case_titles):
        """
        执行测试用例，需要传入计划的id，以及对应的具体的用例信息
        test_demo.py
        :return:
        """
        # ['testcase1.py', 'testcase2.py']  -> pytest testcase1.py testcase2.py
        # 完成格式转换，jenkins可以直接调用

        case_title = ' '.join(case_titles)
        logger.debug(f"测试计划{plan_id}",f"要执行的的测试用例内容{case_titles}")

        # 调用执行器执行测试用例
        report = JenkinsUtils.invoke(task=case_title)

        # 写入构建记录
        build = Build()
        build.create(plan_id, report)



    def create(self,name, case_id_lists):
        '''
        1. 获取关联的测试用例，创建对应的测试计划
        2. 执行测试计划，生产一条构建记录
            - 执行了哪些用例
            - 关联的测试计划是什么
        :return:
        '''

        case_objects = [TestcaseModel.get_filter_by(id=id) for id in case_id_lists]
        logger.debug(f'测试列表{case_id_lists}',f'获取到测试用例对象为{case_objects}')

        # 在创建过程中，需要传入测试计划的名称，并且指出关联哪些测试用例
        plan_id = PlanModel.create(name, case_objects)
        # 直接调用get方法，获取转换后的测试数据的格式
        case_titles = self.get(plan_id[0]['testcase_info'])
        self.execute(plan_id, case_titles)



    def get(self, plan_id=None):
        '''

        :param plan_id:
        :return:
        '''

        plan_objects = self.get_objs(plan_id)

        plan_datas = [{'id': plan_objects.id,
          'name': plan_objects.name,
          'testcase_info':[
            testcase.case_title for testcase in plan_object.testcase]}
          for plan_object in plan_objects]
        logger.info(f"获取到的测试计划的数据为->{plan_datas}")
        return plan_datas


    def get_objs(self,plan_id=None):
        if plan_id:
            r = PlanModel.get_filter_by(id=plan_id)
        else:
            r = PlanModel.get_all()
        logger.debug(f"获取到的测试计划的列表为{r}")
        return r

