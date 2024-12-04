"""Processing for Day 03"""

import re

def mull_it_over(memory: str, toggle: bool) -> int:
    """Take the memory and return the appropriate value"""

    output = 0

    enabled = True

    matches = re.findall(r"(do\(\)|don't\(\)|mul\([0-9]+,[0-9]+\))", memory)

    for match in matches:
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif enabled or not toggle:
            num1, num2 = match.split("(")[1].split(")")[0].split(",")
            output += int(num1) * int(num2)

    return output
