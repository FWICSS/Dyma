#  Copyright (c) 2022. Code by Dimitri AIGLE
import unittest
from Dyma.intro_test.module_unitest.module import my_split,MyCustomTypeError

class TestMonModule(unittest.TestCase):
    def test_simplte_input(self):
        input = "salut ça va"
        output = my_split(input,' ')
        expected = ["salut", "ça", "va"]
        self.assertEqual(output,expected, "the string should be split with a space")

    # @unittest.skip('function non implémenter')
    def test_simplte_input(self):
        input = "salut ça va"
        output = my_split(input)
        expected = ["salut", "ça", "va"]

    def test_no_separator(self):
        input = "salut ça va"
        output = my_split(input)
        self.assertNotEqual(output,["salut", "ça", "va"])

    def test_is(self):
        a = [1, 2]
        b = [1, 2]
        c = a
        #self.assertIs(a, b)
        self.assertIs(a, c)
        self.assertIsNot(a, b)

    def test_true_false(self):
        a = [1, 2]
        b = True
        c = False
        d = "je suis une str"
        e = {}
        self.assertTrue(a)
        self.assertTrue(b)
        self.assertTrue(c)
        self.assertTrue(d)
        self.assertTrue(e)

    def test_none_not_none(self):
        self.assertIsNone(None)
        self.assertIsNotNone(1)

    def test_in_not_in(self):
        a = [1, 2, 3]
        self.assertIn(1, a)
        self.assertNotIn(5, a)

    def test_is_instance_not_is_instance(self):
        a = 1
        self.assertIsInstance(a,int)
        self.assertNotIsInstance(a,str)

    def test_error_if_not_str(self):
        a = 1
        self.assertRaises(MyCustomTypeError,my_split, a,' ')


if __name__ == "__main__":
    unittest.main()