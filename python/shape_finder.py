"""Function for finding shapes in an image."""

import numpy as np
import numba


def find_shapes(image):
    """
    Find shapes in an image.

    By shape, we mean a group of connected pixels with the same value.
    This is a simple implementation that uses a depth-first search.

    Args:
        image: 2D numpy array of integers.
    Returns:
        A tuple of the number of shapes and a list of shapes.
        Each shape is a list of (x, y) coordinates.
    """

    def _is_valid(x, y):
        return 0 <= x < image.shape[0] and 0 <= y < image.shape[1]

    def _dfs(x, y, shape):
        if not _is_valid(x, y) or visited[x, y] or image[x, y] == 0:
            return
        visited[x, y] = True
        shape.append((x, y))
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            _dfs(x + dx, y + dy, shape)

    visited = np.zeros_like(image, dtype=bool)
    shapes = []
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            if not visited[x, y] and image[x, y] == 1:
                shape = []
                _dfs(x, y, shape)
                shapes.append(shape)

    return len(shapes), shapes