#When executing these tests, the terminal outputs that there is a failure in the code somewhere among the assertion statements.
#Looking through the two statements, the fractions don't add up to 1, meaning that that was our error.
#If the statement in the assertEqual was true, then we'd have 0 failures, but with the numbers we have, thats the one failure we have.
#Used "python -m unittest test" to run
import unittest
from fractions import Fraction


from my_sum import sum


class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == "__main_":
    unittest.main()

