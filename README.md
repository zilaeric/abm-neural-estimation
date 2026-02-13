# Deep Neural Network Estimation of Financial Agent-Based Models: A Comparative Study

Implementation of "Deep Neural Network Estimation of Financial Agent-Based Models: 
A Comparative Study".

## Installation

### Dependencies

To set up virtual environment and install development version of the package, run:
```
conda create --name deepfabm python=3.14
conda activate deepfabm
pip install -r requirements.txt
pip install -e .
```

### (Optional) Weights & Biases

Optionally, you can use your Weights & Biases account to track neural network training 
progress. If you avoid using the corresponding CLI argument (`--wandb/-wb`) to configure
a Weights & Biases project, it is unnecessary to log into your account. Otherwise, log 
into your Weights & Biases account by running:
```
wandb login
```

### (Optional) Pre-commit checks

To install pre-commit hook that performs linting, formatting, and testing, run:
```
pre-commit install
```

The pre-commit hook can be also called at will by running:
```
pre-commit run --all-files
```

## Development

### Linting & formatting

Ruff is used for PEP 8 linting and formatting. To perform checks and reformat code, run:
```
ruff check . --fix
ruff format .
```

These checks run automatically if the pre-commit hook is installed as described in the
section before.

### Testing

Pytest is used for testing. To execute the full test suite, run:
```
python -m pytest tests
```

These tests run automatically if the pre-commit hook is installed as described in the
section before.

## Usage

The most straightforward way to use the package is through its command-line interface
(CLI). The package provides a unified entry-point via `deepfabm`.

### Training

The `deepfabm train` command can be used to train the neural network.

```
$ deepfabm train --help
usage: deepfabm train [--help] [--verbose] [--seed INT] [--wandb STR] --architecture {gru}

DeepFABM model training interface.

required arguments:
  --architecture, -a {gru}
                        choose network architecture to train

optional arguments:
  --help, -h            show this help message and exit
  --verbose, -v         set loglevel to DEBUG
  --seed, -s INT        set seed for reproducibility
  --wandb, -wb STR      set Weights & Biases project name to store experiment run to
```

### Evaluation

The `deepfabm evaluate` command can be used to perform inference using a trained neural
network.

```
$ deepfabm evaluate --help
usage: deepfabm evaluate [--help] [--verbose] [--seed INT] [--wandb STR] --folder STR [--data STR]

DeepFABM model evaluation interface.

required arguments:
  --folder, -f STR  choose results folder with trained weights to use for evaluation

optional arguments:
  --help, -h        show this help message and exit
  --verbose, -v     set loglevel to DEBUG
  --seed, -s INT    set seed for reproducibility
  --wandb, -wb STR  set Weights & Biases project name to store experiment run to
  --data, -d STR    choose empirical data to estimate model for, else use simulate data
```
