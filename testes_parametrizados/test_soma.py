import pytest

def soma(a, b):
    return a + b


@pytest.mark.parametrize("a,b,esperado",
                         [
                          (10,12,22),
                          (2,3,5)
                         ]
                        )
def test_soma(a,b,esperado):
    assert soma(a,b) == esperado