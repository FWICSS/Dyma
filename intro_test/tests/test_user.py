#  Copyright (c) 2022. Code by Dimitri AIGLE
import unittest
from Dyma.intro_test.module_unitest.adresse import Adresse
from Dyma.intro_test.module_unitest.User import User

class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("before starting any test")

    def setUp(self) -> None:
        print("setup")
        address = Adresse("Sainte-Rose", "Guadeloupe")
        self.user = User(address, "Dimitri")

    def test_greeting(self):
        output = self.user.greeting()
        expected = "Bonjour Dimitri"
        self.assertEqual(output,expected)

    def test_get_adresse(self):
        output = self.user.get_adresse()
        expected = "Guadeloupe : Sainte-Rose"
        self.assertEqual(output, expected)

    def tearDown(self) -> None:
        print("tear down")
        self.user = None

    @classmethod
    def tearDownClass(cls) -> None:
        print("At the end of all test")

