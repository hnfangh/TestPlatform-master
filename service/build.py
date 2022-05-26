from dao.build_model import BuildModel
from utils.log_util import logger


class Build:


    def get_objs_by_plan_id(self, plan_id=None):
        if plan_id:
            b = BuildModel.get_filter_by(plan_id=plan_id)
        else:
            b = BuildModel.get_all()
        logger.debug(f"获取到的构建记录的列表为{b}")
        return b


    def get(self, plan_id=None):
        '''

        :return:
        '''

        build_objects = self.get_objs_by_plan_id(plan_id)
        build_datas = [
            {
                "plan_id": build_objects.plan_id,
                "report": build_objects.report,
                # 把创建时间转换为string类型
                "created_at": str(build_objects.created_at)
            }for build_objects in build_objects ]
        logger.info(f"获取到的构建记录的数据为->{build_datas}")
        return build_datas



    def create(self, plan_id, report):
        """
        :param plan_id:
        :param report:
        :return:
        """
        logger.debug(f"创建构建记录对应的计划id为{plan_id}， 测试报告为{report}")
        BuildModel.create(plan_id,report)