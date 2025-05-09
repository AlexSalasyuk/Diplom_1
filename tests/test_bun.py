import pytest
from praktikum.bun import Bun


@pytest.mark.parametrize('name, price',[
    ('Плутоневая', 300.0),
    ('Марсианская', 666.6),
    ('Нептуная', 456.77)
])
def test_bun_initialization(name, price):
    bun = Bun(name, price)

    assert bun.get_name() == name
    assert bun.get_price() == price