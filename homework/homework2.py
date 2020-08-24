"""
定义一个天山童姥类 ，类名为TongLao，属性有血量，武力值（通过传入的参数得到）。TongLao类里面有2个方法，
see_people方法，需要传入一个name参数，如果传入”WYZ”（无崖子），则打印，“师弟！！！！”，如果传入“李秋水”，打印“呸，贱人”，如果传入“丁春秋”，打印“叛徒！我杀了你”
fight_zms方法（天山折梅手），调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血量。血多的一方获胜。
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造
"""


# 定义天山童姥的类型
class Tong_lao:
    # 构造一个特殊方法，类名Tong_lao后面加（），则该方法会自动执行,将变量打包，后面调用方法时可不用传递该参数
    def __init__(self, tl_hp, tl_pow):
        self.tl_hp = tl_hp
        self.tl_pow = tl_pow
        # 定义see_people方法，传入name参数

    def see_people(self, name):
        # 如果传入参数无崖子，则打印'师弟！！！你到底喜欢的人是谁？
        if name == '无崖子':
            print('师弟！！！你到底喜欢的人是谁？')
        # 如果传入参数'李秋水'则打印'呸，你这个死贱人'
        elif name == '李秋水':
            print('呸，你这个死贱人')
        # 如果传入参数'丁春秋'，则打印'叛徒!拿命来'
        elif name == '丁春秋':
            print('叛徒!拿命来')

    # 定义天山折梅手的方法，传入dr_hp,dr_pow参数
    def fight_zms(self, dr_hp, dr_pow):
        # 攻击力增强10倍，掉血一半
        self.tl_pow = self.tl_pow * 10
        self.tl_hp = self.tl_hp / 2
        # 进行一回合制对打
        self.tl_hp = self.tl_hp - dr_pow
        dr_hp = dr_hp - self.tl_pow
        # 假如天山童姥血量大于敌人血量，天山童姥赢
        if self.tl_hp > dr_hp:
            print('天山童姥的血量：', self.tl_hp)
            # 打印出敌人天山童姥血量和敌人血量
            print('敌人的血量：', dr_hp)
            print("天山童姥方赢了：哈哈，贱人！你还是没我厉害！")
        # 假如天山童姥血量小于敌人血量，天山童姥输
        elif self.tl_hp < dr_hp:
            # 打印出敌人天山童姥血量和敌人血量
            print('天山童姥的血量：', self.tl_hp)
            print('敌人的血量：', dr_hp)
            print('天山童姥方输了：贱人，没想到多年不见你这么厉害!')
        else:
            print('平局')


# 天山童姥实例化，传入tl_hp,tl_pow参数
tl = Tong_lao(1000, 200)
print("*" * 10, '看到无崖子', "*" * 10)
# 调用Tong_lao的see_people方法，传入name参数
tl.see_people('无崖子')
print("*" * 10, '遇到敌人', "*" * 10)
# 调用Tong_lao的天山折梅手方法，给敌人的dr_hp,dr_pow传递参数
tl.fight_zms(500, 200)
# 打到后面来了个蒙面高手
print("*" * 10, '来了个蒙面高手', "*" * 10)
# 给蒙面高手传递参数
tl.fight_zms(50000, 200)
