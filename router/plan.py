import json

from flask import request
from flask_restx import Namespace, Resource

from server import api
from service.plan import Plan
from utils.log_util import logger

plan_ns = Namespace('plan', description='测试计划管理')

@plan_ns.route('')
class PlanServer(Resource):

    get_parser = api.parser()
    get_parser.add_argument('id', type=int, locations='args')

    '''
       查询构建记录接口，可传ID，也可以不传
       传则查询对应的记录，不传则查询所有
       如果为查询到，返回空列表
    '''

    @plan_ns.expect(get_parser)
    def get(self):
        '''
        测试计划查询
        :return:
        '''

        # 获取请求数据
        plan_id = request.args.get('plan_id')
        logger.info(f'type(request.args) <===== {type(request.args)}')
        logger.info(f"测试计划获取接口接收到的参数 <===== {plan_id}")

        # 调用service层的plan业务逻辑
        plan = Plan()
        datas = plan.get(plan_id)

        # 接口返回内容
        return {'code': 0, 'msg': {'status': 'sucess', 'data': datas}}




    '''
       新增构建记录接口，可传name，testcase
    '''

    post_parser = api.parser()
    post_parser.add_argument('name', type=str, required=True, locations='json')
    post_parser.add_argument('testcases', locations='json')

    @plan_ns.expect(post_parser)
    def post(self):
        '''
        新增测试计划
        :return:
        '''
        plan_data = request.json
        logger.info(f"测试计划新增接口接收到的参数<====== {plan_data}")

        name = plan_data.get('name')
        testcases = plan_data.get('testcases')
        testcases = json.loads(testcases) if isinstance(testcases, str) else testcases

        # 调用service层的plan业务逻辑
        plan = Plan()
        plan.create(name, testcases)

        return {"code": 0, "msg": f"plan {name}  add success"}