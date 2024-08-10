import unittest
import numpy as np
from python.shape_finder import find_shapes

class TestFindShapes(unittest.TestCase):

    def test_empty_image(self):
        image = np.zeros((5, 5), dtype=int)
        num_shapes, shapes = find_shapes(image)
        self.assertEqual(num_shapes, 0)
        self.assertEqual(shapes, [])

    def test_single_shape(self):
        image = np.array([
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ])
        num_shapes, shapes = find_shapes(image)
        self.assertEqual(num_shapes, 1)
        self.assertEqual(len(shapes), 1)
        self.assertIn([(0, 0), (1, 0), (1, 1), (0, 1)], shapes)

    def test_multiple_shapes(self):
        image = np.array([
            [1, 0, 0, 1],
            [0, 0, 0, 0],
            [0, 1, 1, 0],
            [1, 0, 0, 1]
        ])
        num_shapes, shapes = find_shapes(image)
        self.assertEqual(num_shapes, 5)
        self.assertEqual(len(shapes), 5)

    def test_all_ones(self):
        image = np.ones((5, 5), dtype=int)
        num_shapes, shapes = find_shapes(image)
        self.assertEqual(num_shapes, 1)
        self.assertEqual(len(shapes), 1)
        self.assertEqual(len(shapes[0]), 25)

    def test_single_shape_border(self):
        image = np.array([
            [1, 1, 1],
            [1, 0, 1],
            [1, 1, 1]
        ])
        num_shapes, shapes = find_shapes(image)
        self.assertEqual(num_shapes, 1)
        self.assertEqual(len(shapes), 1)
        self.assertEqual(len(shapes[0]), 8)
    
    def test_diagonal_shape(self):
        image = np.array([
            [1, 0, 1],
            [0, 1, 0],
            [1, 0, 1]
        ])
        num_shapes, shapes = find_shapes(image)
        self.assertEqual(num_shapes, 5)
        self.assertEqual(len(shapes), 5)

if __name__ == '__main__':
    unittest.main()