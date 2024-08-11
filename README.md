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

This project uses `conda` for version control, specifically `conda 23.7.4` but
any modern version should do the job. To install `conda`, follow the
instructions here: [install conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

Once installed, use the following command line instructions to set up this
repo:

```
git clone https://github.com/neilSchroeder/find-shapes.git
cd find-shapes
conda env create -f environment.yml
conda activate find_shapes
```

## Running

```
python run_shape_find.py --input-file data/data_small.txt
python run_shape_find.py --input-file data/data_large.txt
```

## Tests

### Run unit tests
`python -m unittest python/test/test_shape_finder.py`