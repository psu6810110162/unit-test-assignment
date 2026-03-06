import unittest
from _6810110162.caesar_cipher import caesar_cipher


class TestCaesarCipherKnownExamples(unittest.TestCase):
    

    def test_middle_outz_shift_2(self):
        s, k = "middle-Outz", 2
        expected = "okffng-Qwvb"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)


    def test_hello_world_shift_3(self):
        s, k = "Hello, World!", 3
        expected = "Khoor, Zruog!"
        result = caesar_cipher(s, k)
        self.assertEqual(result, expected)


class TestCaesarCipherWrapAround(unittest.TestCase):
   

    def test_xyz_lowercase_wraps_to_abc(self):
        s, k = "xyz", 3
        self.assertEqual(caesar_cipher(s, k), "abc")

    def test_XYZ_uppercase_wraps_to_ABC(self):
        s, k = "XYZ", 3
        self.assertEqual(caesar_cipher(s, k), "ABC")

    def test_z_shifts_to_a(self):
        s, k = "z", 1
        self.assertEqual(caesar_cipher(s, k), "a")

    def test_Z_shifts_to_A(self):
        s, k = "Z", 1
        self.assertEqual(caesar_cipher(s, k), "A")

    def test_a_shifts_to_z_with_k_25(self):
        s, k = "a", 25
        self.assertEqual(caesar_cipher(s, k), "z")


class TestCaesarCipherNonAlpha(unittest.TestCase):
   

    def test_digits_preserved(self):
        s, k = "abc123", 1
        result = caesar_cipher(s, k)
        self.assertEqual(result, "bcd123")

    def test_spaces_preserved(self):
        s, k = "a b c", 1
        result = caesar_cipher(s, k)
        self.assertEqual(result, "b c d")

    def test_punctuation_preserved(self):
        s, k = "a!b@c#", 1
        result = caesar_cipher(s, k)
        self.assertEqual(result, "b!c@d#")

    def test_all_symbols_unchanged(self):
        s, k = "1234!@#$", 10
        result = caesar_cipher(s, k)
        self.assertEqual(result, s)


class TestCaesarCipherEdgeCases(unittest.TestCase):
    

    def test_shift_zero_returns_same(self):
        s, k = "abcABC", 0
        self.assertEqual(caesar_cipher(s, k), "abcABC")

    def test_shift_26_full_rotation_returns_same(self):
        s, k = "HelloWorld", 26
        self.assertEqual(caesar_cipher(s, k), "HelloWorld")

    def test_shift_52_double_rotation_returns_same(self):
        s, k = "abcXYZ", 52
        self.assertEqual(caesar_cipher(s, k), "abcXYZ")

    def test_empty_string_returns_empty(self):
        self.assertEqual(caesar_cipher("", 5), "")

    def test_preserves_mixed_case_independently(self):
        # 'a' → 'b', 'A' → 'B'
        s, k = "aA", 1
        self.assertEqual(caesar_cipher(s, k), "bB")


if __name__ == "__main__":
    unittest.main()