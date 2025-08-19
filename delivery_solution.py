# 141325975 - ID посылки
import sys


def get_number_of_platforms(data: list, limit: int) -> int:
    """The delivery service: main function."""
    platforms: int = 0
    data.sort()
    left_pointer: int = 0
    right_pointer: int = len(data) - 1

    def get_step_left(platforms: int, right_pointer: int) -> tuple:
        """Takes a step to the left."""
        platforms += 1
        right_pointer -= 1
        return platforms, right_pointer

    def get_step_right(left_pointer: int) -> int:
        """Takes a step to the right."""
        left_pointer += 1
        return left_pointer

    while left_pointer <= right_pointer:
        total: int = data[left_pointer] + data[right_pointer]
        if total <= limit:
            platforms, right_pointer = get_step_left(platforms, right_pointer)
            left_pointer = get_step_right(left_pointer)
        elif total > limit:
            platforms, right_pointer = get_step_left(platforms, right_pointer)
        else:
            left_pointer = get_step_right(left_pointer)
    if left_pointer == right_pointer:
        platforms += 1
    return platforms


if __name__ == '__main__':
    data: list = [int(item) for item in sys.stdin.readline().rstrip().split()]
    limit: int = int(sys.stdin.readline().rstrip())
    print(get_number_of_platforms(data, limit))
