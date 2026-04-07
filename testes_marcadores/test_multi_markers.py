import pytest
import time


# pegar testes por marcadores pytest -m "[nome marcador]"
# pode utilizar lógica booleana pytest -m "not [nome marcador] or [nome segundo marcador] and not [nome terceiro marcador]"
# pegar parte do nome do marcador pytest -k "[parte desejada]"


@pytest.mark.rapida
def test_soma_rapida():
    assert  1 + 2 == 3

@pytest.mark.lento
def test_soma_lenta():
    time.sleep(2)
    assert  1 + 2 == 3

@pytest.mark.rapida
@pytest.mark.lento
def test_soma_mista():
    time.sleep(1)
    assert  1 + 2 == 3