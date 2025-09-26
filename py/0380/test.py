import unittest
from main import RandomizedSet


class Test0380(unittest.TestCase):
    def test_case_1(self):
        operations = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
        params = [[], [1], [2], [2], [], [1], [2], []]
        expected = [None, True, False, True, 1, True, False, 2]

        rs = None
        for i, op in enumerate(operations):
            if op == "RandomizedSet":
                rs = RandomizedSet()
                actual = None
            elif op == "insert":
                actual = rs.insert(params[i][0])
            elif op == "remove":
                actual = rs.remove(params[i][0])
            elif op == "getRandom":
                actual = rs.getRandom()
                if i == 4:
                    self.assertIn(actual, [1, 2])
                    continue
                elif i == 7:
                    self.assertEqual(actual, 2)
                    continue

            if expected[i] is not None:
                self.assertEqual(expected[i], actual, f"Failed at operation {i}: {op}{params[i]}")

    def test_case_2(self):
        operations = ["RandomizedSet", "remove", "remove", "insert", "getRandom", "remove", "insert"]
        params = [[], [0], [0], [0], [], [0], [0]]
        expected = [None, False, False, True, 0, True, True]

        rs = None
        for i, op in enumerate(operations):
            if op == "RandomizedSet":
                rs = RandomizedSet()
                actual = None
            elif op == "insert":
                actual = rs.insert(params[i][0])
            elif op == "remove":
                actual = rs.remove(params[i][0])
            elif op == "getRandom":
                actual = rs.getRandom()
                self.assertEqual(actual, 0)
                continue

            if expected[i] is not None:
                self.assertEqual(expected[i], actual, f"Failed at operation {i}: {op}{params[i]}")

    def test_multiple_inserts_and_removes(self):
        rs = RandomizedSet()

        self.assertTrue(rs.insert(1))
        self.assertTrue(rs.insert(2))
        self.assertTrue(rs.insert(3))

        self.assertFalse(rs.insert(1))
        self.assertFalse(rs.insert(2))

        for _ in range(10):
            random_val = rs.getRandom()
            self.assertIn(random_val, [1, 2, 3])

        self.assertTrue(rs.remove(2))
        self.assertFalse(rs.remove(2))

        for _ in range(10):
            random_val = rs.getRandom()
            self.assertIn(random_val, [1, 3])

        self.assertTrue(rs.remove(1))
        self.assertTrue(rs.remove(3))

        self.assertFalse(rs.remove(1))

        self.assertTrue(rs.insert(4))
        self.assertEqual(rs.getRandom(), 4)

    def test_single_element(self):
        rs = RandomizedSet()
        self.assertTrue(rs.insert(5))
        self.assertEqual(rs.getRandom(), 5)
        self.assertTrue(rs.remove(5))
        self.assertTrue(rs.insert(10))
        self.assertEqual(rs.getRandom(), 10)


if __name__ == '__main__':
    unittest.main()
