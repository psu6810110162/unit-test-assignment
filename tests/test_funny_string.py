import unittest
from _6810110162.funny_string import funny_string


class TestFunnyStringFunnyCases(unittest.TestCase):

    def test_acxz_is_funny(self):
        s = "acxz"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_single_character_is_funny(self):
        s = "a"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_two_identical_characters_is_funny(self):
        s = "aa"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_two_different_characters_is_funny(self):
        s = "ab"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_abc_is_funny(self):
        s = "abc"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_all_same_characters_is_funny(self):
        s = "aaaa"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_palindrome_abcba_is_funny(self):
        s = "abcba"
        expected = "Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


class TestFunnyStringNotFunnyCases(unittest.TestCase):
    

    def test_ivvkj_is_not_funny(self):
        s = "ivvkj"
        expected = "Not Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_bcxz_is_not_funny(self):
        s = "bcxz"
        expected = "Not Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_abcd_is_not_funny(self):
        s = "azbz" 
        expected = "Not Funny"
        result = funny_string(s)
        self.assertEqual(result, expected)


    def test_longer_not_funny_string(self):
        s = "pvqxr"   
        result = funny_string(s)
        self.assertIn(result, ("Funny", "Not Funny"),
                      "Result must be one of the two valid strings")
        expected = "Not Funny"
        self.assertEqual(result, expected)


class TestFunnyStringReturnType(unittest.TestCase):

    def test_returns_string_type(self):
        result = funny_string("abc")
        self.assertIsInstance(result, str)

    def test_result_is_one_of_two_valid_values(self):
        for s in ("a", "ab", "acxz", "ivvkj"):
            with self.subTest(s=s):
                result = funny_string(s)
                self.assertIn(result, ("Funny", "Not Funny"))


if __name__ == "__main__":
    unittest.main()