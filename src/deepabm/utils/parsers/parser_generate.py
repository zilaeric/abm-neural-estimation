from .parser_base import BaseParser


class GenerateParser(BaseParser):
    def __init__(self):
        super().__init__(description="Parser for data generation")

        self.required.add_argument(
            "--environment",
            "-env",
            dest="environment",
            help="choose environment to generate data from",
            type=str,
            choices=["diamonds", "fruits", "levers", "smac"],
            required=True,
        )

        self.required.add_argument(
            "--policy",
            "-pol",
            dest="policy",
            help="choose policy to use for data generation",
            type=str,
            choices=["astar", "random", "trained"],
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

        self.command.add_argument(
            "--identifier",
            "-id",
            dest="identifier",
            help="specify identifier to add to saved dataset's foldername",
            type=str,
            metavar="STR",
        )

    def parse_args(self, args):
        args = self.parser.parse_args(args)

        # Check that weights are selected when using trained policy
        if args.policy == "trained" and args.weights is None:
            self.parser.error("Trained policy requires --weights!")

        return args
