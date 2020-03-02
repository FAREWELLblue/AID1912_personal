'''
 对不同的请求情形进行分类
'''
from view import *

urls = [
    ('/time',get_time),
    ('/hello',hello),
    ('/bye',bye)
]