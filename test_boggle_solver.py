import unittest
import sys

sys.path.append("/home/codio/workspace/")

from boogle_solver import Boggle


def normalize(words):
    if not words:
        return []
    return sorted([w.upper() for w in words])


# -------------------------------------------------
# Scalability Tests (3x3 → 6x6 example)
# -------------------------------------------------

class TestSuite_Alg_Scalability_Cases(unittest.TestCase):

    def test_Normal_case_3x3(self):
        grid = [
            ["A", "B", "C"],
            ["D", "E", "F"],
            ["G", "H", "I"]
        ]

        dictionary = ["abc", "abdhi", "abi", "ef", "cfi", "dea"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        expected = normalize(["abc", "abdhi", "cfi", "dea"])
        self.assertEqual(expected, solution)

    def test_4x4_case(self):
        grid = [
            ["T", "E", "S", "T"],
            ["A", "B", "C", "D"],
            ["E", "F", "G", "H"],
            ["I", "J", "K", "L"]
        ]

        dictionary = ["test", "abcd", "afkp", "teba", "ghl"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        expected = normalize(["test", "abcd", "teba", "ghl"])
        self.assertEqual(expected, solution)

    def test_5x5_large_dictionary(self):
        grid = [
            ["C", "A", "T", "S", "D"],
            ["D", "O", "G", "S", "E"],
            ["B", "I", "R", "D", "F"],
            ["F", "I", "S", "H", "G"],
            ["L", "I", "O", "N", "H"]
        ]

        dictionary = [
            "cats", "dogs", "bird", "fish", "lion",
            "cat", "dog", "cow", "tiger", "bear"
        ]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        # At least these must exist
        for word in ["cats", "dogs", "bird"]:
            self.assertIn(word.upper(), solution)


# -------------------------------------------------
# Simple Edge Cases
# -------------------------------------------------

class TestSuite_Simple_Edge_Cases(unittest.TestCase):

    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["a", "aa", "aaa"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        expected = []
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = []
        dictionary = ["hello", "there"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        expected = []
        self.assertEqual(expected, solution)

    def test_Invalid_Dictionary_Type(self):
        grid = [["A", "B"], ["C", "D"]]
        dictionary = "abcd"

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        expected = []
        self.assertEqual(expected, solution)

    def test_Non_Square_Grid(self):
        grid = [["A", "B", "C"], ["D", "E", "F"]]
        dictionary = ["abe"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        expected = []
        self.assertEqual(expected, solution)


# -------------------------------------------------
# Complex Coverage Cases
# -------------------------------------------------

class TestSuite_Complete_Coverage(unittest.TestCase):

    def test_reuse_cell_not_allowed(self):
        grid = [
            ["A", "B"],
            ["C", "D"]
        ]

        dictionary = ["ABA"]  # would require reusing A

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        self.assertEqual([], solution)

    def test_diagonal_complex_path(self):
        grid = [
            ["A", "X", "X"],
            ["X", "B", "X"],
            ["X", "X", "C"]
        ]

        dictionary = ["abc"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        self.assertIn("ABC", solution)

    def test_long_snake_path(self):
        grid = [
            ["A", "B", "C"],
            ["H", "I", "D"],
            ["G", "F", "E"]
        ]

        dictionary = ["abcdefghi"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        self.assertIn("ABCDEFGHI", solution)


# -------------------------------------------------
# Qu and St Tile Tests
# -------------------------------------------------

class TestSuite_Qu_and_St(unittest.TestCase):

    def test_Qu_tile(self):
        grid = [
            ["Qu", "A"],
            ["R", "T"]
        ]

        dictionary = ["quart", "qua", "qu"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        self.assertIn("QUA", solution)
        self.assertIn("QUART", solution)
        self.assertNotIn("QU", solution)  # too short

    def test_St_tile(self):
        grid = [
            ["St", "A"],
            ["R", "T"]
        ]

        dictionary = ["start", "star", "st"]

        game = Boggle(grid, dictionary)
        solution = normalize(game.getSolution())

        self.assertIn("START", solution)
        self.assertIn("STAR", solution)
        self.assertNotIn("ST", solution)


if __name__ == '__main__':
    unittest.main()
