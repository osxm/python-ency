import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 4)

if __name__ == '__main__':
    unittest.main()