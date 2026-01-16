import unittest
from main import LRUCache

class Test0146(unittest.TestCase):
    def run_operations(self, operations, values):
        """Helper to run a sequence of LRU cache operations"""
        results = []
        cache = None

        for op, val in zip(operations, values):
            if op == "LRUCache":
                cache = LRUCache(val[0])
                results.append(None)
            elif op == "put":
                cache.put(val[0], val[1])
                results.append(None)
            elif op == "get":
                results.append(cache.get(val[0]))

        return results

    def test_basic_lru_eviction(self):
        """Test basic LRU eviction with capacity 2"""
        operations = ["LRUCache","put","put","get","put","get","put","get","get","get"]
        values = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
        expected = [None,None,None,1,None,-1,None,-1,3,4]

        actual = self.run_operations(operations, values)
        self.assertEqual(expected, actual)

    def test_single_capacity(self):
        """Test LRU cache with minimal capacity of 1"""
        operations = ["LRUCache","put","get","put","get","get"]
        values = [[1],[2,1],[2],[3,2],[2],[3]]
        expected = [None,None,1,None,-1,2]

        actual = self.run_operations(operations, values)
        self.assertEqual(expected, actual)

    def test_larger_capacity_with_updates(self):
        """Test LRU cache with capacity 3, including key updates"""
        operations = ["LRUCache","put","put","put","put","get","get","get","get","put","get","get"]
        values = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[5]]
        expected = [None,None,None,None,None,4,3,2,-1,None,-1,5]

        actual = self.run_operations(operations, values)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
