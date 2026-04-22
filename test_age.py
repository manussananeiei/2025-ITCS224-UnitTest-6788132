import unittest
from age import categorize_by_age

class TestCategorizeByAge(unittest.TestCase):
    def test_boundary_child_adolescent(self):
        self.assertEqual(categorize_by_age(9), "Child")
        self.assertEqual(categorize_by_age(10), "Adolescent")
    
    def test_boundary_adolescent_adult(self):
        self.assertEqual(categorize_by_age(18), "Adolescent")
        self.assertEqual(categorize_by_age(19), "Adult")

    def test_boundary_adult_golden_age(self):
        self.assertEqual(categorize_by_age(65), "Adult")
        self.assertEqual(categorize_by_age(66), "Golden age")

if __name__ == "__main__":
    unittest.main(verbosity=2)

