import unittest
from unittest.mock import patch, mock_open, MagicMock, call

from _6810110162.result_reporter import run_and_report, read_result
from _6810110162.funny_string import funny_string
from _6810110162.caesar_cipher import caesar_cipher
from _6810110162.alternating_characters import alternating_characters
from _6810110162.two_characters import two_characters
from _6810110162.grid_challenge import grid_challenge


# ---------------------------------------------------------------------------
# 1. STUB — replace file-system with a controlled in-memory object
# ---------------------------------------------------------------------------

class TestRunAndReportStub(unittest.TestCase):

    def test_funny_string_result_written_to_file(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            result = run_and_report(funny_string, ("acxz",), "output.txt")
        self.assertEqual(result, "Funny")
        fake_file.assert_called_once_with("output.txt", "w", encoding="utf-8")
        

    def test_caesar_cipher_result_written_to_file(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
    
            result = run_and_report(caesar_cipher, ("middle-Outz", 2), "cipher.txt")
        # assert
        self.assertEqual(result, "okffng-Qwvb")
        fake_file.assert_called_once_with("cipher.txt", "w", encoding="utf-8")


    def test_grid_challenge_result_written_to_file(self):
        # arrange
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            result = run_and_report(grid_challenge, (grid,), "grid.txt")
        # assert
        self.assertEqual(result, "YES")


    def test_alternating_characters_result_written_to_file(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            result = run_and_report(alternating_characters, ("AABAAB",), "alt.txt")
        self.assertEqual(result, "2")


    def test_two_characters_result_written_to_file(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            result = run_and_report(two_characters, ("beabeefeab",), "two.txt")
        self.assertEqual(result, "5")


# ---------------------------------------------------------------------------
# 2. MOCK — verify interaction / behaviour (not just state)
# ---------------------------------------------------------------------------

class TestRunAndReportMock(unittest.TestCase):

    def test_write_called_with_correct_content_funny(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            run_and_report(funny_string, ("acxz",), "out.txt")
        fake_file().write.assert_called_once_with("Funny")


    def test_write_called_with_correct_content_cipher(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            run_and_report(caesar_cipher, ("xyz", 3), "out.txt")
        # assert
        fake_file().write.assert_called_once_with("abc")


    def test_write_called_with_no_result_result(self):
        # arrange
        fake_file = mock_open()
        with patch("builtins.open", fake_file):
            run_and_report(grid_challenge, (["ba", "cd"],), "out.txt")
        fake_file().write.assert_called_once_with("YES")


class TestReadResultMock(unittest.TestCase):

    def test_read_result_returns_stubbed_content(self):
        fake_file = mock_open(read_data="Funny")
        with patch("builtins.open", fake_file):
            content = read_result("output.txt")
        # assert
        self.assertEqual(content, "Funny")
        fake_file.assert_called_once_with("output.txt", "r", encoding="utf-8")


    def test_read_result_returns_numeric_string(self):
        # arrange
        fake_file = mock_open(read_data="5")
        with patch("builtins.open", fake_file):
            content = read_result("two.txt")
        self.assertEqual(content, "5")


# ---------------------------------------------------------------------------
# 3. SPY — wrap a real function to record calls while keeping real logic
# ---------------------------------------------------------------------------

class TestSpyOnAlgorithm(unittest.TestCase):
    def test_spy_records_funny_string_call(self):
        spy = MagicMock(wraps=funny_string)
        result = spy("acxz")
        self.assertEqual(result, "Funny")
        spy.assert_called_once_with("acxz")


    def test_spy_records_caesar_cipher_call(self):
        # arrange
        spy = MagicMock(wraps=caesar_cipher)
        result = spy("xyz", 3)
        self.assertEqual(result, "abc")
        spy.assert_called_once_with("xyz", 3)


    def test_spy_records_multiple_calls(self):
        # arrange
        spy = MagicMock(wraps=alternating_characters)
        spy("AABAAB")
        spy("ABABAB")
        # assert – called exactly twice
        self.assertEqual(spy.call_count, 2)
        spy.assert_any_call("AABAAB")
        spy.assert_any_call("ABABAB")


    def test_spy_records_grid_challenge_call(self):
        # arrange
        spy = MagicMock(wraps=grid_challenge)
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        result = spy(grid)
        # assert
        self.assertEqual(result, "YES")
        spy.assert_called_once_with(grid)


    def test_spy_records_two_characters_call(self):
        # arrange
        spy = MagicMock(wraps=two_characters)
        result = spy("beabeefeab")
        # assert
        self.assertEqual(result, 5)
        spy.assert_called_once_with("beabeefeab")


if __name__ == "__main__":
    unittest.main()