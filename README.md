# Neural Estimation of Financial Agent-Based Models: A Comparative Study

Implementation of "Neural Estimation of Financial Agent-Based Models: A Comparative Study".

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
