from typing import Tuple


def get_items() -> Tuple[str]:
    user_input = input().split(",")
    return tuple(user_input)


if __name__ == "__main__":
    items = get_items()
    print(items)