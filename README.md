# Find Shapes Project

This code is a simple implementation of a shape search on binary text images.
This work is to be submitted to MaestroAI as demonstration of coding ability
for an application to their Senior AI Engineer position.

## Motivation

This project is motivated by the desire to demonstrate a competency with 
coding.

## Features

The shape finding algorithm implements a simple depth first search for shapes.

## Setup/Installation

```
git clone https://github.com/nschroed/find_shapes.git
cd find_shapes
conda env create -f environment.yml
conda activate find_shapes
```

## Running

```
python run_shape_find.py --input-file data/data_small.txt
python run_shape_file.py --input-file data/data_large.txt
```

## Tests

### Run unit tests
`python -m unittest test_shape_finder.py`