from flask import request
from flask_restx import Resource, Namespace

from server import api
from service.testcase import Testcase
from utils.log_util import logger



case_ns = Namespace('case', description='用例管理')

@case_ns.route('')
class TestCaseServer(Resource):

    ### 查询用例相关
    get_parser = api.parser()
    get_parser.add_argument('id', type=int, location="args")

    @case_ns.expect(get_parser)
    def get(self):
        """
        查询测试用例
        :return:
        """
        # 获取前端的参数
        case_id = request.args.get('id')
        logger.info(f'type(request.args) <===== {type(request.args)}')
        logger.info(f'查询用例接收到的参数 <===== {case_id}')

        # 调用service层的具体查询业务逻辑
        testcase = Testcase()
        datas = testcase.get(case_id)

        # 给接口的响应内容
        return {'code':0, 'msg':{'status': 'success', 'data': datas}}




    ## 新增用例相关
    post_parser = api.parser()
    post_parser.add_argument('id', type=int, location='json')
    post_parser.add_argument('case_title', type=str, required=True, location='json')
    post_parser.add_argument('remark', type=str, location='json')

    @case_ns.expect(post_parser)
    def post(self):
        '''
        新增测试用例
        :return:
        '''

        # 获取请求数据
        case_data = request.json
        logger.info(f'新增用例接收到的参数 <===== {case_data}')
        id = case_data.get('id')
        case_title = case_data.get('case_title')
        remark = case_data.get('remark')

        # 调用service层的具体新增逻辑
        testcase = Testcase()
        tc = testcase.create(id, case_title, remark)
        if tc:
            return {'code': 0, 'msg': f'用例{id}新增成功'}
        else:
            return {'code': 40001, 'msg': f'用例{id}已存在，新增失败'}




    # 删除用例相关
    del_parser = api.parser()
    del_parser.add_argument('id', type=int, required=True, location='json')

    @case_ns.expect(post_parser)
    def delete(self):
        '''
        删除测试用例
        :return:
        '''
        case_data = request.json
        logger.info(f'删除用例接收到的参数 <===== {case_data}')
        id = case_data.get('id')

        # 调用service层的具体删除逻辑
        testcase = Testcase()
        td = testcase.delete(id)
        if td:
            return {'code': 0, 'msg': f'用例{id}删除成功'}
        else:
            return {'code': 40001, 'msg': f'用例{id}查询不到数据，删除失败'}



     # 更新用例相关
    update_parser = api.parser()
    update_parser.add_argument('id', type=int, required=True, location='json')
    update_parser.add_argument('case_title', type=str, required=True, location='json')
    update_parser.add_argument('remark', type=str, required=True, location='json')

    @case_ns.expect(update_parser)
    def put(self):
        '''
        更新测试用例
        :return:
        '''
        case_data = request.json
        logger.info(f'更新用例接收到的参数 <===== {case_data}')
        id = case_data.get('id')
        case_title = case_data.get('case_title')
        remark = case_data.get('remark')

        # 调用service层的具体更新逻辑
        testcase = Testcase()
        tc = testcase.update(id, case_title, remark)
        if tc:
            return {'code': 0, 'msg': f'用例{id}更新成功'}
        else:
            return {'code': 40001, 'msg': f'用例{id}重复，更新失败'}