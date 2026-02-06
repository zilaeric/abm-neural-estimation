# Neural Estimation of Financial Agent-Based Models: A Comparative Study

Implementation of "Neural Estimation of Financial Agent-Based Models: A Comparative Study".

## Installation

To install the package and the corresponding virtual environment, run:
```
conda env create -f deepabm.yaml
conda activate deepabm
pip install -e .
```

To log into your Weights and Biases account, run:
```
wandb login
```

To confirm that installation was successful by completing unit tests, run:
```
python -m pytest tests
```