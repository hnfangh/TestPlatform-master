from flask import request
from flask_restx import Resource, Namespace

from server import api
from service.build import Build
from utils.log_util import logger

build_ns = Namespace('build', description='构建记录管理')


@build_ns.route('')
class BuildServer(Resource):
    '''
    查询构建记录接口，可传ID，也可以不传
    传则查询对应的记录，不传则查询所有
    如果为查询到，返回空列表
    '''
    get_parser = api.parser()
    get_parser.add_argument('plan_id', type=int, location='args')

    @build_ns.expect(get_parser)
    def get(self):
        '''
        构建记录查询
        :return:
        '''
        plan_id = request.args.get('plan_id')
        logger.info(f"测试计划获取接口接收到的参数 <===== {plan_id}")

        # 调用service层到build业务逻辑
        build = Build()
        datas = build.get(plan_id)

        # 接口返回内容
        return {'code': 0, 'msg': {'status': 'sucess', 'data': datas}}