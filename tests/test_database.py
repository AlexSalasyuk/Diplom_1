from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING

class TestDatabase:

    def test_available_buns_returns_expected_buns(self):
        db = Database()
        buns = db.available_buns()

        assert len(buns) == 3
        assert [bun.get_name() for bun in buns] == ['black bun', 'white bun', 'red bun']
        assert [bun.get_price() for bun in buns] == [100, 200, 300]

    def test_available_ingredients_returns_expected_ingredients(self):
        db = Database()
        ingredients = db.available_ingredients()

        assert len(ingredients) == 6

        sauces = ingredients[:3]
        fillings = ingredients[3:]

        assert [i.get_type() for i in sauces] == [INGREDIENT_TYPE_SAUCE] * 3
        assert [i.get_name() for i in sauces] == ['hot sauce', 'sour cream', 'chili sauce']
        assert [i.get_price() for i in sauces] == [100, 200, 300]

        assert [i.get_type() for i in fillings] == [INGREDIENT_TYPE_FILLING] * 3
        assert [i.get_name() for i in fillings] == ['cutlet', 'dinosaur', 'sausage']
        assert [i.get_price() for i in fillings] == [100, 200, 300]
