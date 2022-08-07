import os
from typing import Callable, Protocol, TypeAlias

Hook: TypeAlias = Callable[[int, int], None]


class ContextError(Exception): ...


class ContextEnsurable(Protocol):
    @property
    def in_context(self) -> bool: ...


class Cursor:
    def __init__(self, hooks: list[Hook]) -> None:
        self.pos = 0
        self.hooks = hooks

    def _notify_hooks(self, prev_pos: int, new_pos: int):
        for hook in self.hooks:
            hook(prev_pos, new_pos)

    def move_to(self, new_pos: int) -> None:
        self._notify_hooks(self.pos, new_pos)

        if (not isinstance(new_pos, int)) or new_pos > 30000:
            raise ValueError("Position must be an integer <= 30000")

        self.pos = new_pos


def ensure_context(func: Callable):
    def wrapper(self: ContextEnsurable, *args, **kwargs):
        if not self._in_context:
            raise ContextError(f"Function {func.__name__} not using in a `with` block / context manager")
        return func(*args, **kwargs)
    return wrapper


class OptimisedGenerator:
    def __init__(self, source: str, output: str = None) -> None:
        # If output is none, set to source
        output = output or source

        # Check files exist
        if not (os.path.exists(source) and os.path.exists(output)):
            not_existing = []

            if not os.path.exists(source):
                not_existing.append(source)
            if not os.path.exists(output):
                not_existing.append(output)

            file_str = ', '.join(not_existing)
            file_number = len(not_existing)

            raise FileNotFoundError(f"{file_str} | {file_number} file{'s' if file_number > 1 else ''} do{'es' if not (file_number - 1) else ''} not exist")  # noqa

        # Assign filepaths
        self.source_filepath = source
        self.output_filepath = output

        # Initaialise file objects as None with not in context
        self.source_file = None
        self.output_file = None

        # Create cursor with move hook
        self.cursor = Cursor([self.on_move_operation])

        self._in_context = False

    def __enter__(self) -> "OptimisedGenerator":
        self._in_context = True

        self.source_file = open(self.source_filepath)
        self.output_file = open(self.output_filepath)

        return self

    def __exit__(self, *_):
        self.source_file.close()
        self.output_file.close()

        self.source_file = None
        self.output_file = None

        self._in_context = False

    def _check_context(self, f=None):
        if not self._in_context:
            b = "\b"
            raise ContextError(f"Function {f or b} must be used in `with` statement")

    @ensure_context
    def on_move_operation(self, old_pos: int, new_pos: int):
        """Function to be hooked to an event manager (Cursor)"""
        diff = new_pos - old_pos
        fill_char = "+" if diff > 0 else "-"



        print(f"Move Operation: Δ{diff}")

    @ensure_context
    def write_loop(self, n: int):
        """"""


OptimisedGenerator("hello.world", "output.file")
