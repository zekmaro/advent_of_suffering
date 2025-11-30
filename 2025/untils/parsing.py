def ints(line):
    """Extract all integers from a string."""
    import re
    return list(map(int, re.findall(r"-?\d+", line)))


def chunks(lst, n):
    """Yield chunks of size n."""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]
