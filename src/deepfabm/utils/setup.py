from .parser import TrainParser, EvaluateParser
from .logger import LOGGER, setup_logging, setup_wandb, terminate_wandb
from .seed import set_seed


PARSER_MAP = {
    "train": TrainParser,
    "evaluate": EvaluateParser,
}


def initialize_run(script: str, args: dict):
    """
    Initializes run by setting up results directory and initializing all services.
    
    :param command: Invoked script, either `"train"` or `"evaluate"`
    :type command: str
    :param args: CLI arguments passed during invocation
    :type args: dict
    """
    # Parse the command-line arguments
    try:
        parser = PARSER_MAP[script]()
    except:
        raise KeyError(f"No parser found for the invoked script '{script}'")
    
    args = parser.parse_args(args)

    # Set up logging
    setup_logging(args.loglevel)
    LOGGER.info(f"Dictionary of parsed arguments: {vars(args)}")

    # Set up Weights & Biases logging
    if args.wandb:
        setup_wandb(project=args.wandb_project, config=vars(args))

    # Set up the random seed
    set_seed(args.seed)


def terminate_run(args: dict):
    """
    Finalizes run by stopping all running services.
    
    :param args: CLI arguments passed during invocation
    :type args: dict
    """
    # Terminate Weights & Biases logging
    if args.wandb:
        terminate_wandb()
