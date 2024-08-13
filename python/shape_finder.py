"""Function for finding shapes in an image."""

import numpy as np


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
    min_x, min_y = 0, 0
    max_x, max_y = image.shape[0], image.shape[1]
    cell_shifts = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def _is_valid(x, y):
        """Private function to check if a cell is valid."""
        return min_x <= x < max_x and min_y <= y < max_y

    def _dfs(x, y, shape):
        """Private function to perform depth-first search."""
        if not _is_valid(x, y) or visited[x, y] or image[x, y] == 0:
            return
        visited[x, y] = True
        shape.append((x, y))
        for dx, dy in cell_shifts:
            _dfs(x + dx, y + dy, shape)

    visited = np.zeros_like(image, dtype=bool)
    shapes = []
    # iterate over all cells
    for x in range(image.shape[0]):
        for y in range(image.shape[1]):
            # skip zeros and already visited cells
            if not visited[x, y] and image[x, y] == 1:
                shape = []
                # perform depth-first search
                # to find all cells connected to the current cell
                _dfs(x, y, shape)
                shapes.append(shape)

    return len(shapes), shapes