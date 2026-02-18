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
usage: deepfabm train [--seed INT] [--verbose] [--wandb STR] [--help] experiment

DeepFABM model training interface.

positional arguments:
  experiment        path to experiment configuration in the '/experiments' folder

optional arguments:
  --seed, -s INT    reproducibility seed number
  --verbose, -v     set loglevel to DEBUG
  --wandb, -wb STR  Weights & Biases project name; do not use W&B if not set
  --help, -h        show this help message and exit
```

### Evaluation

The `deepfabm evaluate` command can be used to perform inference using a trained neural
network.

```
$ deepfabm evaluate --help
usage: deepfabm evaluate [--data STR] [--seed INT] [--verbose] [--help] folder

DeepFABM model evaluation interface.

positional arguments:
  folder          path to results folder with trained weights in the '/results' folder

optional arguments:
  --data, -d STR  path to empirical data in the '/data' folder, else simulate data
  --seed, -s INT  reproducibility seed number
  --verbose, -v   set loglevel to DEBUG
  --help, -h      show this help message and exit
```

### Plotting

The `deepfabm plot` command can be used to plot model realizations and empirical data.

#### Empirical data

```
$ deepfabm plot emp --help
usage: deepfabm emp --data STR [--help]

DeepFABM empirical data plotting interface.

required arguments:
  --data, -d STR  path to empirical data in the '/data' folder

optional arguments:
  --help, -h      show this help message and exit
```

#### Simulated data

```
$ deepfabm plot sim --help
usage: deepfabm sim --model STR --parametrization STR --obs INT --burn INT [--seed INT] [--help]

DeepFABM simulated data plotting interface.

required arguments:
  --model, -m STR       simulation model identifier
  --parametrization, -p STR
                        simulation model parametrization identifier
  --obs INT             number of observations
  --burn INT            burn-in period length

optional arguments:
  --seed, -s INT        reproducibility seed number
  --help, -h            show this help message and exit
```
