import unittest
from Test_swapping_key_and_value import swap_key_value

from unittest.mock import patch, Mock

def swap_dict_keys_values(d):
    return {v: k for k, v in d.items()}

class TestSwapDictKeysValues(unittest.TestCase):

    def test_swap_dict_keys_values(self):
        # Test avec un dictionnaire contenant des clés de type string et des valeurs de type integer
        d = {'a': 1, 'b': 2, 'c': 3}
        expected_result = {1: 'a', 2: 'b', 3: 'c'}

        # Simulation du dictionnaire entier pour renvoyer une copie modifiable avec les mêmes éléments
        with patch.dict(d, {'items.return_value': [('a', 1), ('b', 2), ('c', 3)]}):
            self.assertEqual(swap_dict_keys_values(d), expected_result)

        # Test avec un dictionnaire vide
        d = {}
        expected_result = {}

        # Simulation du dictionnaire entier pour renvoyer une copie modifiable avec une liste de tuples vide
        with patch.dict(d, {'items.return_value': []}):
            self.assertEqual(swap_dict_keys_values(d), expected_result)

        # Test avec un dictionnaire contenant des clés de type integer et des valeurs de type string
        d = {1: 'a', 2: 'b', 3: 'c'}
        expected_result = {'a': 1, 'b': 2, 'c': 3}

        # Simulation du dictionnaire entier pour renvoyer une copie modifiable avec les mêmes éléments
        with patch.dict(d, {'items.return_value': [(1, 'a'), (2, 'b'), (3, 'c')]}):
            self.assertEqual(swap_dict_keys_values(d), expected_result)

        # Test avec un dictionnaire contenant des valeurs en doublon
        d = {'a': 1, 'b': 2, 'c': 1}
        expected_result = {1: 'c', 2: 'b'}

        # Simulation du dictionnaire entier pour renvoyer une copie modifiable avec une liste de tuples contenant des valeurs en doublon
        with patch.dict(d, {'items.return_value': [('a', 1), ('b', 2), ('c', 1)]}):
            self.assertEqual(swap_dict_keys_values(d), expected_result)
