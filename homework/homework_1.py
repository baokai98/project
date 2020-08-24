# 作业1
# 用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
# 1:定义个动物
# 定义一只狗的类
class Dog:
    # 定义这只狗的属性
    name = '旺财'
    breed = '中华田园犬'
    gender = '公'
    color = '黄'

    # 定义这只狗的方法
    def jiao(self):
        print("能旺旺叫")

    def eat(self):
        print("能吃")

    def pick_up(self):
        print("能捡棍子")


# 打印定义这只狗的属性
print(Dog.name, Dog.breed, Dog.gender, Dog.color)
# 给狗实例化（旺财）
wc = Dog()
# 调用旺财的方法
wc.eat()
wc.jiao()


# 2：定义个英雄
# 定义英雄的类
class Hero:
    # 打印英雄的属性
    name = '皇子'
    skin = '黄金甲'
    gender = '男'
    guojia = '德玛西亚'

    # 定义英雄的方法
    def q(self):
        print('巨龙撞击')

    def w(self):
        print('黄金圣盾')

    def e(self):
        print('德邦军旗')

    def r(self):
        print('天崩地裂')


# 打印英雄的属性
print('英雄的属性：', Hero.name, Hero.guojia)
# 实例化
hz = Hero()
# 实力调用方法
hz.e(), hz.q()
hz.r()
print(hz.name)


# 定义一辆车
# 定义一辆车的类
class Car:
    # 定义车的属性
    pingpai = '奥迪'
    chexing = 'A4'
    lunzi = '四个'
    color = '骚红'

    # 定义车的方法
    def zd(self):
        print('这款车是自动挡')

    def js(self):
        print('这辆车真好开')


# 打印车的属性
print(Car.pingpai)
# 实例化
che = Car()
che.js()
print(che.color)


# 定义一部手机
# 定义一个类
class Phone:
    # 定义属性
    name = 'vivo'
    xinghao = 'Z5X'
    color = '激光蓝'

    # 定义方法
    def photo(self):
        print('拍照片')

    def music(self):
        print('播放音乐')

    def messige(self):
        print('打开微信')


# 打印属性
print(Phone.name)
# 实例化
sj = Phone()
# 调用方法
sj.music()
