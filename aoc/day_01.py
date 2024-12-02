"""Processing for Day 01"""

def historian_hysteria(lists: str, similarity_score: bool) -> int:
    """Take the lists and return the appropriate value"""

    list_1 = []
    list_2 = []

    for items in lists.splitlines():
        item_1_str, item_2_str = items.split("   ")
        list_1.append(int(item_1_str))
        list_2.append(int(item_2_str))

    if similarity_score:
        similarity = 0

        for item_1 in list_1:
            for item_2 in list_2:
                if item_1 == item_2:
                    similarity += item_1

        return similarity

    list_1.sort()
    list_2.sort()

    diffs = 0

    for idx, item_2 in enumerate(list_2):
        diffs += abs(list_1[idx] - item_2)

    return diffs
