import unittest
from function_for_test import Function

clasa_test = Function()
class Tests(unittest.TestCase):
    def test_mutants(self):
        self.assertEqual(clasa_test.word_has_n_occurrences_in_text("test", "", -1, 'ds'), 1248)
        self.assertEqual(clasa_test.word_has_n_occurrences_in_text("cat cat", "catttttttt", 1, 'n'), 39)
        self.assertEqual(clasa_test.word_has_n_occurrences_in_text("cat Cat dog Dog", "cat", 3, 'n'), 69)
        self.assertEqual(clasa_test.word_has_n_occurrences_in_text("cat Cat dog Dog", "hat", 3, 'y'), 78)
        self.assertEqual(clasa_test.word_has_n_occurrences_in_text("cat Cat dog Dog", "cat", 2, 'n'), 59)
