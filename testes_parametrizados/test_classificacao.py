import pytest

def classifica_idade(idade):
    if idade < 12:
        return 'Criança'
    elif idade > 12 and idade < 18:
        return 'Adolescente'
    elif idade > 18 and idade < 65:
        return 'Adulto'
    else:
        return 'Idoso'
    
@pytest.mark.parametrize("idade, categoria_esperada", [
    (15, 'Adolescente'), 
    (5,'Criança'), 
    (20, 'Adulto'), 
    (100,'Idoso')
])
def test_classifica_idade(idade, categoria_esperada):
    assert classifica_idade(idade) == categoria_esperada