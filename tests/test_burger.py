from unittest.mock import Mock
from praktikum.burger import Burger


class TestBurger:

    def test_set_buns(self):
        mock_bun = Mock()
        burger = Burger()
        burger.set_buns(mock_bun)

        assert burger.bun == mock_bun

    def test_add_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        assert burger.ingredients == [mock_ingredient]

    def test_remove_ingredient(self):
        mock_ingredient = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient)

        burger.remove_ingredient(0)

        assert burger.ingredients == []

    def test_move_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_2 = Mock()
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        burger.move_ingredient(0, 1)

        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100

        mock_ingredient_1 = Mock()
        mock_ingredient_1.get_price.return_value = 40

        mock_ingredient_2 = Mock()
        mock_ingredient_2.get_price.return_value = 60

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)

        assert burger.get_price() == 100 * 2 + 40 + 60

    def test_get_receipt(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100
        mock_bun.get_name.return_value = 'Булка'

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 50
        mock_ingredient.get_name.return_value = 'Сыр'
        mock_ingredient.get_type.return_value = 'FILLING'

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)

        receipt = burger.get_receipt()

        assert '(==== Булка ====)' in receipt
        assert '= filling Сыр =' in receipt
        assert 'Price: 250' in receipt
