"""Testing for Day 03"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_03")

def test_normal() -> None:
    """Test mull_it_over with toggle=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        memory = f.read()

    output = aoc.mull_it_over(memory, toggle=False)

    assert output == 153469856


def test_toggle() -> None:
    """Test mull_it_over with toggle=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        memory = f.read()

    output = aoc.mull_it_over(memory, toggle=True)

    assert output == 77055967
