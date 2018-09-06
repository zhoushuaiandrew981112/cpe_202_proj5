from graphwit import *
import unittest

class TestGraphWit(unittest.TestCase):


    def test_bfs_dfs(self):
    
        adj_list = {"a" : [("b", 1)], "b" : [("c", 1)], "c": [] }
        self.assertEqual(order_bfs(adj_list, "a"), ["a", "b", "c"])
        self.assertEqual(order_dfs(adj_list, "a"), ["a", "b", "c"])

        adj_list = {"a" : [("b", 1), ("c", 1)], "b" : [("c", 1)], "c": [("a", 1)] }
        self.assertEqual(order_bfs(adj_list, "b"), ["b", "c", "a"])
        self.assertEqual(order_dfs(adj_list, "b"), ["b", "c", "a"])

        adj_list = {"a" : [("b", 1), ("c", 1)], "b" : [], "c": [] }
        self.assertEqual(order_bfs(adj_list, "a"), ["a", "b", "c"])
        self.assertEqual(order_dfs(adj_list, "a"), ["a", "b", "c"])

        adj_list = {"a" : [("b", 1), ("d", 1)], "b" : [("c", 1)], "c": [], "d" : [("a", 1), ("b", 1)] }
        self.assertEqual(order_bfs(adj_list, "a"), ["a", "b", "d", "c"])
        self.assertEqual(order_dfs(adj_list, "a"), ["a", "b", "c", "d"])

        adj_list = {"a" : [("b", 1), ("d", 1)], "b" : [("c", 1)], "c": [], "d" : [("a", 1), ("b", 1)] }
        self.assertEqual(order_bfs(adj_list, "d"), ["d", "a", "b", "c"])
        self.assertEqual(order_dfs(adj_list, "d"), ["d", "a", "b", "c"])


if __name__ == '__main__':
    unittest.main()
