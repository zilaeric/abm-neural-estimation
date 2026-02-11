from __future__ import annotations

from deepfabm.utils import LOGGER

from .base import Network

_NETWORK_REGISTRY: dict[str, type[Network]] = {}
_IMPLEMENTATIONS_IMPORTED: bool = False


def _register_implementations() -> None:
    """
    Ensure all network implementations have been imported at least once.

    Importing the implementations package triggers decorator-based registration.
    This function is safe to call multiple times.
    """

    global _IMPLEMENTATIONS_IMPORTED
    if _IMPLEMENTATIONS_IMPORTED:
        return

    from . import implementations  # noqa: F401

    _IMPLEMENTATIONS_IMPORTED = True

    LOGGER.debug(
        f"Network registry contains the following networks: {list_networks()}."
    )


def register_network(name: str):
    """
    Class decorator to register a network implementation.

    :param name: Network identifier to use for the network class
    :type name: str
    """

    def decorator(network_class: type[Network]) -> type[Network]:
        if name in _NETWORK_REGISTRY and _NETWORK_REGISTRY[name] is not network_class:
            raise ValueError(f"Network '{name}' already registered.")

        if not issubclass(network_class, Network):
            raise TypeError(
                f"Trying to add network '{name}' which is not of the 'Network' class."
            )

        # Add network to network registry
        _NETWORK_REGISTRY[name] = network_class

        return network_class

    return decorator


def list_networks() -> list[str]:
    """
    List all networks registered in the network registry.

    :return: List of all identifiers from the network registry
    :rtype: list[str]
    """

    _register_implementations()
    return sorted(_NETWORK_REGISTRY)


def load_network(network: str, **kwargs) -> Network:
    """
    Load specified network. Preferred way of loading networks.

    :param network: Network identifier of the network to be loaded
    :type network: str
    :return: Instance of the loaded network
    :rtype: Network
    """
    _register_implementations()

    try:
        network_class = _NETWORK_REGISTRY[network]
        LOGGER.info(f"Loaded network '{network}' from network registry.")
    except KeyError as e:
        raise ValueError(
            f"No network found for '{network}'. Available: {list_networks()}."
        ) from e

    return network_class(**kwargs)
