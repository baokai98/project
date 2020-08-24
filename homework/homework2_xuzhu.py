'''
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
'''
# 导入homework2中的Tong_lao类
from homework2 import Tong_lao


# 定义一个xuzhu类并继承Tong_lao，xuzhu为子类，Tong_lao为父类
class Xuzhu(Tong_lao):
    # 定义read方法
    def read(self):
        print('虚竹：罪过罪过，你们别打了')


# 给xuzhu实例化
xz = Xuzhu(500, 100)
# 调用xuzhu的read方法
xz.read()
print("*" * 10, '虚竹觉醒，放下屠刀立地成佛，参加战斗', "*" * 10)
# 虚竹使用天山折梅手，给敌人传递参数
xz.fight_zms(1000, 200)
