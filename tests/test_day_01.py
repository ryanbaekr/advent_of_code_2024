"""Testing for Day 01"""

import os
import aoc

FIXTURE = os.path.join(os.path.dirname(os.path.realpath(__file__)), "fixtures", "day_01")

def test_diffs() -> None:
    """Test historian_hysteria with similarity_score=False"""

    with open(FIXTURE, encoding="utf-8") as f:
        lists = f.read()

    diffs = aoc.historian_hysteria(lists, similarity_score=False)

    assert diffs == 1938424


def test_similarity() -> None:
    """Test historian_hysteria with similarity_score=True"""

    with open(FIXTURE, encoding="utf-8") as f:
        lists = f.read()

    similarity = aoc.historian_hysteria(lists, similarity_score=True)

    assert similarity == 22014209
