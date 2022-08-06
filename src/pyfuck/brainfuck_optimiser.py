import re

TOLERANCE = 15
CHUNK_SIZE = 5

consecutive_chars = re.compile(r"(([+-])\2*)")


def invalid_string(s: str) -> bool:
    return s not in [
        len(s) * "+",
        len(s) * "-"
    ]


def optimise_operators(operators: str) -> str:
    trailing = "[<+++++>-]<"

    n = len(operators)

    if n < TOLERANCE or invalid_string(operators):
        return operators

    # Number of chunks
    n //= CHUNK_SIZE

    # Add remainder to trailing chars
    trailing = "".join([trailing, *([operators[0]] * (n % CHUNK_SIZE))])

    output = "".join([">", *([operators[0] * n]), trailing, "-"])

    return output


def optimise_line(operators: str) -> str:
    if "." in operators:
        return ".".join(map(optimise_line, operators.split(".")))

    char_sequences = list(map(lambda x: x[0], consecutive_chars.findall(operators)))

    return "".join(map(optimise_operators, char_sequences))



def optimise_script(filename: str, new_file: str = None) -> None:
    new_file = new_file or f"optimised-{filename}"

    with open(filename, "r+") as f:
        lines = f.readlines()
        optimised_lines = list(map(optimise_line, lines))

    with open(new_file, "w") as f:
        f.write("\n".join(optimised_lines))
