from langgraph.checkpoint.base import EmptyChannelError


class GraphRecursionError(RecursionError):
    """Raised when the graph has exhausted the maximum number of steps.

    This prevents infinite loops. To increase the maximum number of steps,
    run your graph with a config specifying a higher `recursion_limit`.

    Examples:

        graph = builder.compile()
        graph.invoke(
            {"messages": [("user", "Hello, world!")]},
            # The config is the second positional argument
            {"recursion_limit": 1000},
        )
    """

    pass


class InvalidUpdateError(Exception):
    """Raised when attempting to update a channel with an invalid sequence of updates."""

    pass


class GraphInterrupt(Exception):
    """Raised when a subgraph is interrupted."""

    pass


class EmptyInputError(Exception):
    """Raised when graph receives an empty input."""

    pass


__all__ = [
    "GraphRecursionError",
    "InvalidUpdateError",
    "GraphInterrupt",
    "EmptyInputError",
    "EmptyChannelError",
]
