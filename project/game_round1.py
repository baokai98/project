"""
一个回合制游戏，每个角色都有hp 和power，
hp代表血量，power代表攻击力，hp的初始值为1000，
power的初始值为200。打斗多个回合
定义一个fight方法：
my_hp = hp - enemy_power
enemy_final_hp = enemy_hp - my_power
谁的hp先为0，那么谁就输了
"""
# 先定义一个函数
def fight():

    # 定义四个变量：分别为我的血量、我的攻击力、你的血量、你的攻击力
    my_hp = 1000
    my_pow = 200
    you_hp = 1000
    you_pow = 150
    # 为了实现多次对打，使用while循环
    while True:
        # 对打一次后我的血量=我原来的血量-你打我一次的攻击力
        my_hp = my_hp - you_pow
        # 对打一次后你的血量=你原来的血量-我打你一次的攻击力
        you_hp = you_hp - my_pow
        # 假如我的血量先小于0了，打印出我输了
        if my_hp < 0:

            print('我输了')
            # 终止对打，跳出循环
            break
        # 假如你的血量先小于0了，打印出我赢了
        elif you_hp < 0:

            print('我赢了')
            # 终止对打，跳出循环
            break
# 调用定义的函数
fight()

