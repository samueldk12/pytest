import pytest

def calcula_total(price, discount_rate, tax_rate):
    discount = price * discount_rate
    tax = (price - discount) * tax_rate
    total = price - discount + tax
    return round(total,2)

@pytest.mark.parametrize('price', [10.00,50.00,30.00])
@pytest.mark.parametrize('discount_rate', [0,0.1,0.25])
@pytest.mark.parametrize('tax_rate', [0,0.05,0.1])
def test_calcula_total(price, discount_rate, tax_rate):
    discount = price * discount_rate
    tax = (price - discount) * tax_rate
    total = price - discount + tax
    assert calcula_total(price,discount_rate, tax_rate) ==  round(total,2)