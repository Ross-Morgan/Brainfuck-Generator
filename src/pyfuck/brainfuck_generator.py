def generate_script() -> str:
    filename = input("What do you want your file to be called? ")
    prompt_chars = list(input("What do you want to print? "))

    prompt_ascii_codes = list(map(ord, prompt_chars))

    current_index = 0
    output = []

    for char in prompt_ascii_codes:
        while current_index < char:
            output.append("+")
            current_index += 1

        while current_index > char:
            output.append("-")
            current_index -= 1

        output.append(".\n")

    print(*output, sep="", file=open(filename, "w+"))

    return filename
