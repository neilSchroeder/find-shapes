"""Main control script for shape finding."""

import argparse
import os
import sys

import numpy as np

from python.shape_finder import find_shapes


def main():
    """
    Main control function for shape finding.

    This function parses command line arguments, loads an input file,
    and finds shapes in the image.

    Args:
        --input-file: Path to the input file.

    Returns:
        None
    """

    # Parse command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('--input-file', help='Input file', dest='input_file', required=True)

    args = parser.parse_args()

    # Check input file exists
    if not os.path.exists(args.input_file):
        print('Input file not found')
        sys.exit(1)

    # Load input file
    with open(args.input_file, 'r') as f:
        input_data = f.read()

    # Convert input data to an image
    image = np.array([[int(x) for x in line] for line in input_data.strip().split('\n')])

    # Find shapes
    num_shapes, shapes = find_shapes(image)

    print(f'Number of shapes in {args.input_file}: {num_shapes}')


if __name__ == '__main__':
    main()