import unittest
from _6810110162.alternating_characters import alternating_characters


class TestAlternatingCharactersZeroDeletions(unittest.TestCase):

    def test_already_alternating_ab(self):
        s = "ABABAB"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_already_alternating_ba(self):
        s = "BABABA"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_single_character_a(self):
        s = "A"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_single_character_b(self):
        s = "B"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_two_different_characters(self):
        s = "AB"
        expected = 0
        result = alternating_characters(s)
        self.assertEqual(result, expected)


class TestAlternatingCharactersMultipleDeletions(unittest.TestCase):
    

    def test_aabaab_requires_2(self):
        s = "AABAAB"
        expected = 2
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_all_a_requires_n_minus_1(self):
        s = "AAAA"
        expected = 3  # len - 1
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_all_b_requires_n_minus_1(self):
        s = "BBBB"
        expected = 3
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_aabbaabb_requires_4(self):
        s = "AABBAABB"
        expected = 4
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_aab_requires_1(self):
        s = "AAB"
        expected = 1
        result = alternating_characters(s)
        self.assertEqual(result, expected)


    def test_abb_requires_1(self):
        s = "ABB"
        expected = 1
        result = alternating_characters(s)
        self.assertEqual(result, expected)


class TestAlternatingCharactersReturnType(unittest.TestCase):

    def test_returns_integer(self):
        result = alternating_characters("AABB")
        self.assertIsInstance(result, int)

    def test_result_is_non_negative(self):
        for s in ("A", "AB", "AAAB", "BBBB", "ABAB"):
            with self.subTest(s=s):
                self.assertGreaterEqual(alternating_characters(s), 0)

    def test_result_never_exceeds_len_minus_1(self):
        for s in ("A", "AAA", "AAAA", "ABAB"):
            with self.subTest(s=s):
                self.assertLessEqual(alternating_characters(s), len(s) - 1)


if __name__ == "__main__":
    unittest.main()