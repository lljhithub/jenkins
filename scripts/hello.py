import pytest # 引入pytest包

def test_a(): # test开头的测试函数
    print("------->test_a")
    assert 1 # 断言成功
def test_b():
    print("------->test_b")
    assert 0 # 断言失败
if __name__ == '__main__':
    # pytest.main("-s  test_abc.py") # 调用pytest的main函数执行测试
    pytest.main(["-s", "login.py"])