from .parser_base import BaseParser


class TrainParser(BaseParser):
    def __init__(self):
        super().__init__(description="Parser for model training")

        self.required.add_argument(
            "--dataset",
            "-d",
            dest="dataset",
            help="specify dataset's foldername to get training data",
            type=str,
            metavar="STR",
            required=True,
        )

        self.required.add_argument(
            "--model",
            "-m",
            dest="model",
            help="choose model to train",
            type=str,
            choices=["cdt", "idt", "kddt"],
            required=True,
        )

        self.required.add_argument(
            "--identifier",
            "-id",
            dest="identifier",
            help="specify identifier to add to saved policy weights' foldername",
            type=str,
            metavar="STR",
        )
