import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_FILLING, INGREDIENT_TYPE_SAUCE


@pytest.mark.parametrize('ingredient_type, name, price', [
    (INGREDIENT_TYPE_FILLING, 'Яйцо ЭГО', 600.0),
    (INGREDIENT_TYPE_SAUCE, '1000 астероидов', 80.6),
    (INGREDIENT_TYPE_FILLING, 'Марсианский бекон', 900.4)
])
def test_ingredient_getters(ingredient_type, name, price):
    ingredient = Ingredient(ingredient_type, name, price)

    assert ingredient.get_type() == ingredient_type
    assert ingredient.get_name() == name
    assert ingredient.get_price() == price