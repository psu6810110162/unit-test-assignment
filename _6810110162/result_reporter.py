def run_and_report(func, args: tuple, filepath: str) -> str:
    result = str(func(*args))
    with open(filepath, "w", encoding="utf-8") as fh:
        fh.write(result)
    return result


def read_result(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as fh:
        return fh.read()