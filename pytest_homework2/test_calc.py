'''
1、补全计算器（加减乘除）的测试用例
2、使用fixture方法，完成加减乘除用例的自动生成，添加别名
3、修改测试用例的收集规则，执行所有以 check_开头和test_ 开头的测试用例
4、创建 Fixture 方法实现执行测试用例前打印【开始计算】，执行测试用例之后打印【计算结束】
5、将 Fixture 方法存放在conftest.py ，灵活设置scope的级别
'''

import pytest
import yaml
from pytest_homework2.calc import Calcu


# 打开caladatas.yml 文件,执行测试用例方法的参数化，文件中带有中文，需添加：encoding='utf-8'
# with open('calc_datas.yml', encoding='utf-8') as f:
#     # 命名一个变量来接读取出来的数据
#     datas = yaml.safe_load(f)
#     # 获取测试用例加法的参数# 获取测试用例加法的标题id
#     adddatas = datas['add']['adddatas']
#     addid = datas['add']['addid']
#     divdatas = datas['div']['divdatas']
#     divid = datas['div']['divid']
#     subdatas = datas['sub']['subdatas']
#     subid = datas['sub']['subid']
#     muldatas = datas['mul']['muldatas']
#     mulid = datas['mul']['mulid']


# 定义测试计算机的类
class TestCalcu:
    def setup(self):
        print("开始执行测试用例")

    # 在每条测试用例后执行
    def teardown(self):
        print("测试用例执行完毕")

    # @pytest.fixture(scope='class')
    # # 定义setup_class()方法，实现开通打印‘开始计算’，并将计算器实例化，后面不用多次调用，减少代码的重复使用
    # def get_calc(self):
    #     print('开始计算')
    #     calc = Calcu()
    #     yield calc
    #     print('结束计算')
    #
    # # 使定义的测试方法参数化
    # @pytest.fixture(params=adddatas, ids=addid)
    # def get_add(self, request):
    #     data = request.param
    #     return data

    # 定义一个add的测试方法
    def test_add(self, get_calc, get_add):
        # 调用计算器的add方法
        result = get_calc.add(get_add[0], get_add[1])
        # 判断计算结果的类型（二进制计算可能产生浮点数）
        if isinstance(result, float):
            # 将结果四舍五入
            result = round(result, 8)
            # 断言计算结果==预期结果
        assert result == get_add[2]

    # @pytest.fixture(params=subdatas, ids=subid)
    # def get_sub(self, request):
    #     data = request.param
    #     return data

    def check_sub(self, get_calc, get_sub):
        if isinstance(get_sub[0], str):
            return get_sub[2]

        result = get_calc.sub(get_sub[0], get_sub[1])
        if isinstance(result, float):
            result = round(result, 8)
        # 断言计算结果==预期结果
        assert result == get_sub[2]

    # @pytest.fixture(params=muldatas, ids=mulid)
    # def get_mul(self, request):
    #     data = request.param
    #     return data

    def test_mul(self, get_calc, get_mul):
        if isinstance(get_mul[0], str):
            return get_mul[2]
        result = get_calc.mul(get_mul[0], get_mul[1])
        if isinstance(result, float):
            result = round(result, 8)

        # 断言计算结果==预期结果
        assert result == get_mul[2]

    # 定义测试div的方法并参数化
    # @pytest.fixture(params=divdatas, ids=divid)
    # def get_div(self, request):
    #     data = request.param
    #     return data

    def test_div(self, get_calc, get_div):
        if get_div[1] == 0:
            return get_div[2]
        # 调用计算器div方法计算
        result = get_calc.div(get_div[0], get_div[1])

        if isinstance(result, float):
            result = round(result, 8)
        # 断言计算结果==预期结果
        assert result == get_div[2]
