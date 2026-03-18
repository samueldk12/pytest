import pytest

@pytest.fixture
def soma_dobro(numeros):
    yield sum(x * 2 for x in numeros)


@pytest.mark.parametrize('numeros', [[1,3]])
def test_soma_dobro(soma_dobro):
    result_soma_dobro = soma_dobro
    assert result_soma_dobro == 8