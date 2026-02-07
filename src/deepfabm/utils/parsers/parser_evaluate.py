from .parser_base import BaseParser


class EvaluateParser(BaseParser):
    def __init__(self):
        super().__init__(description="Parser for model evaluation")

        self.required.add_argument(
            "--environment",
            "-env",
            dest="environment",
            help="choose the environment to evaluate policy in",
            type=str,
            choices=["levers", "fruits", "diamonds", "smac"],
            required=True,
        )

        self.required.add_argument(
            "--policy",
            "-pol",
            dest="policy",
            help="choose policy to evaluate",
            type=str,
            choices=["random", "astar", "trained"],
            required=True,
        )

        self.command.add_argument(
            "--weights",
            "-wgt",
            dest="weights",
            help="specify policy weights' foldername for trained policy",
            type=str,
            metavar="STR",
        )

    def parse_args(self, args):
        args = self.parser.parse_args(args)

        # Check that weights are selected when using trained policy
        if args.policy == "trained" and args.weights is None:
            self.parser.error("Trained policy requires --weights!")

        return args
