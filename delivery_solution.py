# 141427376 - ID посылки
import sys


def get_number_of_platforms(data_in: list, limit: int) -> int:
    """The delivery service: main function."""
    data = sorted(data_in[:])
    platforms: int = 0
    left_pointer: int = 0
    right_pointer: int = len(data) - 1
    while left_pointer <= right_pointer:
        total: int = data[left_pointer] + data[right_pointer]
        platforms += 1
        right_pointer -= 1
        if total <= limit:
            left_pointer += 1
    return platforms


if __name__ == '__main__':
    data_in: list = [int(item) for item in
                     sys.stdin.readline().rstrip().split()]
    limit: int = int(sys.stdin.readline().rstrip())
    print(get_number_of_platforms(data_in, limit))
