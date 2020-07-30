import random
# 先定义一个函数
def fight():
    # 定义四个变量：分别为我的血量、我的攻击力、你的血量、你的攻击力

    my_hp = 1000
    my_pow = 200
    you_hp = 1000
    you_pow = 200
    pow_qx = random.randint(0,1)

    # 为了实现多次对打，使用while循环
    while True:
        # 对打一次后我的血量=我原来的血量-你打我一次的攻击力
        if pow_qx = 0:
            my_hp = my_hp - you_pow
        # 对打一次后你的血量=你原来的血量-我打你一次的攻击力
            you_hp = you_hp - my_pow
        else:
            you_hp =you_hp - my_pow
            my_hp = my_hp - you_pow
        # 假如我的血量先小于0了，打印出我输了
        if my_hp < 0 :
            print('我输了')
            # 终止对打，跳出循环
            break
        # 假如你的血量先小于0了，打印出我赢了
         elif you_hp < 0 :
            print('我赢了')
            # 终止对打，跳出循环
            break
# 调用定义的函数
fight()