# 作者: 王道 龙哥
# 2022年03月25日10时01分17秒
import logging

logging.basicConfig(level=logging.DEBUG, #大于等于这里级别的日志才会输出
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')


# 开始使用log功能, 传递的参数会替换message
logging.debug('这是 loggging debug message')
logging.info('这是 loggging info message')
logging.warning('这是 loggging a warning message')
logging.error('这是 an loggging error message')
logging.critical('这是 loggging critical message')