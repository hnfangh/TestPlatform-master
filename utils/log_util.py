
"""
log工具类
"""
import  logging
import os
from logging.handlers import RotatingFileHandler


# 获取句柄的logger对象,__name__是该模块在Python包命名空间中的名字，默认WARNING
logger = logging.getLogger(__name__)

# 获取当前工具文件所在的路径,绝对路径
root_path = os.path.dirname(os.path.abspath(__file__))

# os.sep.join智能地拼接一个或多个路径部分
# seq操作系统用来分隔路径不同部分的字符
# os.path.join(path, *paths)返回值是 path 和 *paths 的所有成员的拼接
log_dir_path = os.sep.join([root_path,f'/logs'])
# 判断是否有这个目录
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path) # 如果没有，则新增目录
"""
两个支持日志回滚的 FileHandler 类，分别是 RotatingFileHandler 和 TimedRotatingFileHandler
"""
# 创建日志记录器，指明日志保存路径，maxBytes每个日志的大小，backupCount保存日志文件数量上限
file_log_handler = RotatingFileHandler(os.sep.join([log_dir_path,'log.log']), maxBytes=1024*1024, backupCount=5)
# 设置日志的格式
date_string = '%Y-%m-%d %H:%M:%S'
# 日志格式化
formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(filename)s]/[line:%(lineno)d]/[%(funcName)s] %(message)s',date_string)

# 日志输出到控制台的句柄
stream_handler = logging.StreamHandler()

# 将日志记录器指定日志的格式
file_log_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)

# 为全局的日志工具对象添加日志记录器
# 绑定句柄到logger对象
logger.addHandler(file_log_handler)
logger.addHandler(stream_handler)

# 设置日志输出级别
logger.setLevel(level=logging.DEBUG)