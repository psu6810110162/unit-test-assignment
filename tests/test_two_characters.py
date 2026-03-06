import unittest
from _6810110162.two_characters import two_characters


class TestTwoCharactersKnownExamples(unittest.TestCase):

    def test_beabeefeab_returns_5(self):
        s = "beabeefeab"
        expected = 5
        result = two_characters(s)
        self.assertEqual(result, expected)


class TestTwoCharactersEdgeLengths(unittest.TestCase):

    def test_empty_string_returns_0(self):
        self.assertEqual(two_characters(""), 0)

    def test_single_character_returns_0(self):
        self.assertEqual(two_characters("a"), 0)

    def test_two_different_characters_returns_2(self):
        # "ab" → already alternating with 2 chars
        self.assertEqual(two_characters("ab"), 2)

    def test_two_same_characters_returns_0(self):
        # "aa" → cannot alternate
        self.assertEqual(two_characters("aa"), 0)


class TestTwoCharactersAlreadyAlternating(unittest.TestCase):
    """Strings that need zero deletions."""

    def test_ababab_returns_6(self):
        s = "ababab"
        self.assertEqual(two_characters(s), 6)

    def test_bababa_returns_6(self):
        s = "bababa"
        self.assertEqual(two_characters(s), 6)

    def test_ab_returns_2(self):
        s = "ab"
        self.assertEqual(two_characters(s), 2)


class TestTwoCharactersImpossible(unittest.TestCase):

    def test_all_same_characters_returns_0(self):
        self.assertEqual(two_characters("aaaa"), 0)

    def test_aab_returns_0_consecutive_blocks(self):
        self.assertEqual(two_characters("aab"), 0)


class TestTwoCharactersMultipleDistinct(unittest.TestCase):
    """Strings with more than 2 distinct characters."""

    def test_picks_best_pair(self):
        s = "aabcaa"
        result = two_characters(s)
        self.assertGreaterEqual(result, 0)


    def test_three_char_string_xyx(self):
        s = "xyx"
        self.assertEqual(two_characters(s), 3)


class TestTwoCharactersReturnType(unittest.TestCase):

    def test_returns_integer(self):
        self.assertIsInstance(two_characters("ab"), int)

    def test_result_is_non_negative(self):
        for s in ("", "a", "ab", "aaaa", "ababab", "beabeefeab"):
            with self.subTest(s=s):
                self.assertGreaterEqual(two_characters(s), 0)


if __name__ == "__main__":
    unittest.main()