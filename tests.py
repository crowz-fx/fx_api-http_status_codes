import handler
import json
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class StatusAPITests(unittest.TestCase):
    def test_return_all_codes_count(self):
        self.assertTrue(len(handler.return_all_codes()) == 63)

    def test_return_one_code_count(self):
        code_to_get = 200
        response = handler.return_one_code(code_to_get)
        self.assertEqual(3, len(response))
        self.assertIsNotNone(response)
        self.assertTrue(response["name"] == "OK")
        self.assertTrue(response["code"] == code_to_get)

    def test_non_existent_code(self):
        code_to_get = 20000
        try:
            handler.return_one_code(code_to_get)
            self.fail()
        except Exception as e:
            self.assertIsNone(e.__dict__["response"])
            self.assertEqual(e.__dict__["description"], 
                "HTTP Status code for [{code_to_get}] was not found!".format(code_to_get = code_to_get))

if __name__ == "__main__":
    unittest.main()
