import unittest
from SearchRectangle import SearchRectangle


class TestSearchRectangle(unittest.TestCase):

    def test_subdivision(self):
        searchRect = SearchRectangle([0, 0], [2, 2], 4)
        subRects = searchRect.subdivisions()

        self.assertEqual(subRects[0].NE, [0, 0])
        self.assertEqual(subRects[0].SW, [1, 1])

        self.assertEqual(subRects[1].NE, [0, 1])
        self.assertEqual(subRects[1].SW, [1, 2])

        self.assertEqual(subRects[2].NE, [1, 0])
        self.assertEqual(subRects[2].SW, [2, 1])

        self.assertEqual(subRects[3].NE, [1, 1])
        self.assertEqual(subRects[3].SW, [2, 2])
