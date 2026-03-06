import unittest
from _6810110162.grid_challenge import grid_challenge


class TestGridChallengeYesCases(unittest.TestCase):
    """Grids that should return 'YES'."""

    def test_known_example_returns_yes(self):
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        result = grid_challenge(grid)
        self.assertEqual(result, "YES")


    def test_single_row_always_yes(self):
        grid = ["dcba"]
        self.assertEqual(grid_challenge(grid), "YES")


    def test_single_column_sorted_ascending(self):
        grid = ["a", "b", "c", "d"]
        self.assertEqual(grid_challenge(grid), "YES")


    def test_already_sorted_grid(self):
        grid = ["abc", "bcd", "cde"]
        self.assertEqual(grid_challenge(grid), "YES")


    def test_all_same_characters(self):
        grid = ["aaa", "aaa", "aaa"]
        self.assertEqual(grid_challenge(grid), "YES")


    def test_single_cell(self):
        grid = ["z"]
        self.assertEqual(grid_challenge(grid), "YES")


    def test_two_rows_sortable(self):
        grid = ["ba", "cd"]
        self.assertEqual(grid_challenge(grid), "YES")


    def test_rectangular_grid_yes(self):
        # 2 rows × 3 cols
        grid = ["cba", "fed"]
        self.assertEqual(grid_challenge(grid), "YES")


class TestGridChallengeNoCases(unittest.TestCase):
    """Grids that should return 'NO'."""

    def test_unsortable_two_by_two(self):
        grid = ["zb", "aa"]
        self.assertEqual(grid_challenge(grid), "NO")


    def test_column_not_ascending(self):
        grid = ["cb", "aa"]
        self.assertEqual(grid_challenge(grid), "NO")


    def test_larger_unsortable_grid(self):
        grid = ["abc", "aaa", "zzz"]
        self.assertEqual(grid_challenge(grid), "NO")
        

    def test_single_column_descending(self):
        grid = ["c", "b", "a"]
        self.assertEqual(grid_challenge(grid), "NO")


class TestGridChallengeReturnType(unittest.TestCase):

    def test_returns_string(self):
        result = grid_challenge(["abc"])
        self.assertIsInstance(result, str)

    def test_result_is_yes_or_no(self):
        cases = [
            ["abc"],
            ["cba"],
            ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"],
            ["zb", "aa"],
        ]
        for grid in cases:
            with self.subTest(grid=grid):
                self.assertIn(grid_challenge(grid), ("YES", "NO"))


if __name__ == "__main__":
    unittest.main()