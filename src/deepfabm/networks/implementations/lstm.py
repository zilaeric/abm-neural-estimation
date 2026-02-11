from ..base import Network
from ..registry import register_network


@register_network("lstm")
class LSTM(Network):
    def forward(self, *args, **kwargs):
        raise NotImplementedError(
            f"{self.__class__} forward pass has not been implemented yet!"
        )
