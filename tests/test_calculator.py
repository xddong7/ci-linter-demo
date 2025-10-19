# 导入pytest测试框架和我们写的add函数
import pytest
from calculator import add

# 测试1：正常场景——两个正数相加
def test_add_positive_numbers():
    assert add(2, 3) == 5  # 断言结果是否符合预期，不符合则测试失败

# 测试2：边界场景——包含0和负数
def test_add_boundary_cases():
    assert add(0, 5) == 5
    assert add(-1, -1) == -2
    assert add(1000, -500) == 500

# 测试3：异常场景——传入非数字类型（预期会报错，验证函数是否能正确处理）
def test_add_invalid_input():
    with pytest.raises(TypeError):  # 预期触发TypeError异常
        add(2, "3")  # 传入字符串和数字，正常应报错