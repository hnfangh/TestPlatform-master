from jenkinsapi.jenkins import Jenkins


class JenkinsUtils:

    BASE_URL = 'http://47.106.133.253:8080' # Jenkins服务地址
    USERNAME = 'hnfangh'
    PASSWORD = 123456
    JOB = 'testplatform'

    @classmethod
    def invoke(cls, **kwargs):
        jenkins_testplatform = Jenkins(cls.BASE_URL, cls.USERNAME, cls.PASSWORD)
        # 获取jenkins的job对象
        tp_job = jenkins_testplatform.get_job(cls.JOB)
        # 构建job
        # 获取当前job最后一次完成构建的编号
        # build_params
        tp_job.invoke(build_params=kwargs)
        first_build_number = tp_job.get_last_buildnumber()

        # 获取测试报告的多种方式
        # 1. 自己解析测试报告数据，自己完成测试报告的UI模板展示。渲染到前端生成
        # 2. 直接使用allure的测试报告

        # http://47.106.133.253:8080/job/testplatform/4/allure/
        report = f"{cls.BASE_URL}/job/{cls.JOB}/{first_build_number+1}/allure"

        return report


if __name__ == '__main__':
    JenkinsUtils.invoke(task='test_wework_case.py')