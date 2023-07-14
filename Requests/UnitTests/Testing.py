import unittest


class TestSum(unittest.TestCase):

    def Test_Sum_is_correct(self):
        result = add(a, b)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
