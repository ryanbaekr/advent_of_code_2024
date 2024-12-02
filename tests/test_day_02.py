"""Testing for Day 02"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_02")

def test_normal() -> None:
    """Test red_nosed_reports with dampener=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        data = f.read()

    safe = aoc.red_nosed_reports(data, dampener=False)

    assert safe == 598


def test_dampener() -> None:
    """Test red_nosed_reports with dampener=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        data = f.read()

    safe = aoc.red_nosed_reports(data, dampener=True)

    assert safe == 634
