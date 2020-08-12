import pytest
import yaml

from pytest_homework2.calc import Calcu


@pytest.fixture(scope='class')
# 定义setup_class()方法，实现开通打印‘开始计算’，并将计算器实例化，后面不用多次调用，减少代码的重复使用
def get_calc():
    print('开始计算')
    calc = Calcu()
    yield calc
    print('结束计算')


# 打开caladatas.yml 文件,执行测试用例方法的参数化，文件中带有中文，需添加：encoding='utf-8'
with open('calc_datas.yml', encoding='utf-8') as f:
    # 命名一个变量来接读取出来的数据
    datas = yaml.safe_load(f)
    # 获取测试用例加法的参数# 获取测试用例加法的标题id
    adddatas = datas['add']['adddatas']
    addid = datas['add']['addid']
    divdatas = datas['div']['divdatas']
    divid = datas['div']['divid']
    subdatas = datas['sub']['subdatas']
    subid = datas['sub']['subid']
    muldatas = datas['mul']['muldatas']
    mulid = datas['mul']['mulid']


# 使定义的测试方法参数化
@pytest.fixture(params=adddatas, ids=addid)
def get_add(request):
    adddata = request.param
    return adddata


@pytest.fixture(params=subdatas, ids=subid)
def get_sub(request):
    subdata = request.param
    return subdata


@pytest.fixture(params=muldatas, ids=mulid)
def get_mul(request):
    muldata = request.param
    return muldata


@pytest.fixture(params=divdatas, ids=divid)
def get_div(request):
    divdata = request.param
    return divdata
