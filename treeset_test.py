import unittest
from treeset import TreeSet

# Implementación de los tests para el tree_set.py
class TestTreeSet(unittest.TestCase):
    def setUp(self):
        self.tree_set = TreeSet()

    def test_add_elements(self):
        self.tree_set.add(10)
        self.tree_set.add(20)
        self.tree_set.add(30)
        self.assertTrue(self.tree_set.contains(10))
        self.assertTrue(self.tree_set.contains(20))
        self.assertTrue(self.tree_set.contains(30))
        self.assertEqual(self.tree_set.size(), 3)

    def test_remove_elements(self):
        self.tree_set.add(10)
        self.tree_set.add(20)
        self.tree_set.remove(10)
        self.assertFalse(self.tree_set.contains(10))
        self.assertTrue(self.tree_set.contains(20))
        self.assertEqual(self.tree_set.size(), 1)

    def test_duplicate_addition(self):
        self.tree_set.add(10)
        self.tree_set.add(10)
        self.assertEqual(self.tree_set.size(), 1)

    def test_remove_non_existent(self):
        self.tree_set.add(10)
        self.tree_set.remove(20)  # Removing non-existent element
        self.assertTrue(self.tree_set.contains(10))
        self.assertEqual(self.tree_set.size(), 1)

if __name__ == '__main__':
    unittest.main()