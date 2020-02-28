'''
    event线程同步互斥方法示例
'''
from threading import Event,Thread

s=None#在线程之间进行通信
e=Event()
def yzr():
    print('杨子荣前来拜山头')
    global s
    s='天王盖地虎'
    e.set()#解除阻塞
t = Thread(target=yzr)
t.start()

#主线程验证信息
print('说对口令就是自己人')
e.wait()
if s=='天王盖地虎':
    print('宝塔镇河妖')
    print('确认过眼神，你是对的人')
else:
    print('打死他，无情啊无情')

t.join()
