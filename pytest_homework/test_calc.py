'''
1、补全计算器（加法 除法）的测试用例
2、使用参数化完成测试用例的自动生成
3、在调用测试方法之前打印【开始计算】，在调用测试方法之后打印【计算结束】
注意：
    使用等价类，边界值，因果图等设计测试用例
    测试用例中添加断言，验证结果
    灵活使用 setup(), teardown() , setup_class(), teardown_class()
'''

import pytest
import yaml

from pytest_homework.calc import Calcu

# 打开caladatas.yml 文件,执行测试用例方法的阐述化，文件中带有中文，需添加：encoding='utf-8'
with open('calc_datas.yml', encoding='utf-8') as f:
    # 命名一个变量来接读取出来的数据
    data = yaml.safe_load(f)
    # 获取测试用例加法的参数
    adddatas = data['add']['datas']
    print(adddatas)
    # 获取测试用例加法的标题id
    addmyid = data['add']['myid']
    print(addmyid)
    divdatas = data['div']['datas']
    print(divdatas)
    divmyid = data['div']['myid']
    print(divmyid)


# 定义测试计算机的类
class TestCalcu:
    # 定义setup_class()方法，实现开通打印‘开始计算’，并将计算器实例化，后面不用多次调用，减少代码的重复使用
    def setup_class(self):
        print("开始计算")
        # 实例化计算器
        self.calc = Calcu()

    # 定义teardown_class()，在结尾打印一次结束计算
    def teardown_class(self):
        print("结束计算")

    # 在每条测试用例前后执行
    def setup(self):
        print("开始执行测试用例")

    def teardown(self):
        print("结束测试用例")

    # 使定义的测试方法参数化
    @pytest.mark.parametrize('a,b,expect', adddatas, ids=addmyid)
    # 定义一个add的测试方法
    def test_add(self, a, b, expect):
        # 调用计算器的add方法
        result = self.calc.add(a, b)
        # 判断计算结果的类型（二进制计算可能产生浮点数）
        if isinstance(result, float):
            # 将结果四舍五入
            result = round(result, 2)
            # 断言计算结果==预期结果
        assert result == expect

    # 定义测试div的方法并参数化
    @pytest.mark.parametrize('a,b,expect', divdatas, ids=divmyid)
    def test_div(self, a, b, expect):
        # 判断分母是否为0
        if b == 0:
            return expect
        # 调用计算器div方法计算
        result = self.calc.div(a, b)
        # 断言计算结果==预期结果
        assert result == expect
