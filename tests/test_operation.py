from src.math_operations import add,sub 


def test_add():
    assert add(2,3)==5
    assert add(-1,1)==0
    assert add(5,3)==8
    
    
def test_sub():
    assert sub(10,6)==4
    assert sub(13,15)==-2
    assert sub(34,31)==3 