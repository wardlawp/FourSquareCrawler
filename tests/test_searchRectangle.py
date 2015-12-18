import unittest
from SearchRectangle import SearchRectangle

class TestSearchRectangle(unittest.TestCase):


    def test_subdivision(self):
        searchRect = SearchRectangle([0,0], [2,2], 4)
        subRects = searchRect.subdivisions()
        
        self.assertEqual(subRects[0].NW, [0,0])
        self.assertEqual(subRects[0].SE, [1,1])
        
        self.assertEqual(subRects[1].NW, [0,1])
        self.assertEqual(subRects[1].SE, [1,2])
        
        self.assertEqual(subRects[2].NW, [1,0])
        self.assertEqual(subRects[2].SE, [2,1])
        
        self.assertEqual(subRects[3].NW, [1,1])
        self.assertEqual(subRects[3].SE, [2,2])
        
    """def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')
    
    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())
        
    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)"""