try:
    import unittest2 as unittest
except ImportError:
    import unittest

class StatusAPITests(unittest.TestCase):
    def test_true(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
