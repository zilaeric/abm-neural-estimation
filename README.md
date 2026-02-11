# Neural Estimation of Financial Agent-Based Models: A Comparative Study

Implementation of "Neural Estimation of Financial Agent-Based Models: A Comparative
Study".

## Installation

To set up virtual environment and install development version of the package, run:
```
conda create --name deepfabm python=3.14
conda activate deepfabm
pip install -r requirements.txt
pip install -e .
```

To log into your Weights & Biases account, run:
```
wandb login
```

Finally, you can validate the installation with the test suite by running:
```
python -m pytest tests
```

## Usage

The most straightforward way to employ the package is through its command-line interface
(CLI).

### Training

The `deepfabm-train` command can be used to train the neural network.

```
$ deepfabm-train --help
usage: deepfabm-train [--help] [--verbose] [--seed INT] [--wandb STR] --architecture {gru}

Parser for training

Required arguments:
  --architecture, -a {gru}
                        choose network architecture to train

Optional arguments:
  --help, -h            show this help message and exit
  --verbose, -v         set loglevel to INFO
  --seed, -s INT        set seed for reproducibility
  --wandb, -wb STR      set Weights & Biases project to store training run progress
```

### Evaluation

The `deepfabm-evaluate` command can be used to perform inference using a trained neural
network.

```
$ deepfabm-evaluate --help
usage: deepfabm-evaluate [--help] [--verbose] [--seed INT] [--wandb STR] --folder STR [--data STR]

Parser for evaluation

Required arguments:
  --folder, -f STR  choose results folder containing trained network weights to use for evaluation

Optional arguments:
  --help, -h        show this help message and exit
  --verbose, -v     set loglevel to INFO
  --seed, -s INT    set seed for reproducibility
  --wandb, -wb STR  set Weights & Biases project to store training run progress
  --data, -d STR    choose empirical dataset to estimate model for, otherwise use simulated dataset
```
