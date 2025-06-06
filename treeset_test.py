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

    def test_isEmpty(self):
        self.assertTrue(self.tree_set.isEmpty())
        self.tree_set.add(10)
        self.assertFalse(self.tree_set.isEmpty())
        self.tree_set.remove(10)
        self.assertTrue(self.tree_set.isEmpty())

    def test_first_and_last(self):
        self.tree_set.add(10)
        self.tree_set.add(20)
        self.tree_set.add(30)
        self.assertEqual(self.tree_set.first(), 10)
        self.assertEqual(self.tree_set.last(), 30)

    def test_addAll(self):
        self.tree_set.add(10)
        self.tree_set.add(20)
        self.tree_set.addAll([30, 40, 50])
        self.assertTrue(self.tree_set.contains(30))
        self.assertTrue(self.tree_set.contains(40))
        self.assertTrue(self.tree_set.contains(50))
        self.assertEqual(self.tree_set.size(), 5)

    def test_clear(self):
        self.tree_set.add(10)
        self.tree_set.add(20)
        self.tree_set.clear()
        self.assertTrue(self.tree_set.isEmpty())
        self.assertEqual(self.tree_set.size(), 0)
    
    def test_contains(self):
        self.tree_set.add(10)
        self.assertTrue(self.tree_set.contains(10))
        self.assertFalse(self.tree_set.contains(20))
    
    def test_size(self):
        self.assertEqual(self.tree_set.size(), 0)
        self.tree_set.add(10)
        self.assertEqual(self.tree_set.size(), 1)
        self.tree_set.add(20)
        self.assertEqual(self.tree_set.size(), 2)
        self.tree_set.remove(10)
        self.assertEqual(self.tree_set.size(), 1)
    
    def test_iterator(self):
        self.tree_set.add(10)
        self.tree_set.add(20)
        self.tree_set.add(30)
        iterator = iter(self.tree_set)
        elements = list(iterator)
        self.assertEqual(elements, [10, 20, 30])

    def test_long_size(self):
        # Test for a large number of elements
        for i in range(1000):
            self.tree_set.add(i)
        self.assertEqual(self.tree_set.size(), 1000)

    def test_floor_ceiling_higher_lower(self):
        for v in [10, 20, 30, 40, 50]:
            self.tree_set.add(v)

        self.assertEqual(self.tree_set.floor(25), 20)
        self.assertEqual(self.tree_set.floor(10), 10)
        self.assertIsNone(self.tree_set.floor(5))

        self.assertEqual(self.tree_set.ceiling(25), 30)
        self.assertEqual(self.tree_set.ceiling(50), 50)
        self.assertIsNone(self.tree_set.ceiling(55))

        self.assertEqual(self.tree_set.higher(25), 30)
        self.assertEqual(self.tree_set.higher(50), None)

        self.assertEqual(self.tree_set.lower(25), 20)
        self.assertEqual(self.tree_set.lower(10), None)

    def test_poll_first_and_last(self):
        for v in [10, 20, 30]:
            self.tree_set.add(v)

        self.assertEqual(self.tree_set.pollFirst(), 10)
        self.assertFalse(self.tree_set.contains(10))
        self.assertEqual(self.tree_set.pollLast(), 30)
        self.assertFalse(self.tree_set.contains(30))

    def test_clone(self):
        values = [10, 20, 30]
        for v in values:
            self.tree_set.add(v)

        clone_set = self.tree_set.clone()
        self.assertEqual(list(clone_set), values)
        self.assertNotEqual(id(self.tree_set), id(clone_set))
        clone_set.add(40)
        self.assertFalse(self.tree_set.contains(40))

    def test_type_enforcement(self):
        self.tree_set.add(10)
        with self.assertRaises(TypeError):
            self.tree_set.add("20")

    def test_is_empty_after_many_operations(self):
        for i in range(500):
            self.tree_set.add(i)
        for i in range(500):
            self.tree_set.remove(i)
        self.assertTrue(self.tree_set.isEmpty())


if __name__ == '__main__':
    unittest.main()