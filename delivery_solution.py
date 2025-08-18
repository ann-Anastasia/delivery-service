# 141045603 - ID посылки
import sys
data: list = list(map(int, sys.stdin.readline().rstrip().split()))
limit: int = int(sys.stdin.readline().rstrip())


def main(data: list, limit: int) -> int:
    """The delivery service: main function"""
    platforms: int = 0
    data_equal_limit: list = [item for item in data if item == limit]
    data_other: list = [item for item in data if item < limit]
    data_other.sort()
    platforms += len(data_equal_limit)
    left_pointer: int = 0
    right_pointer: int = len(data_other) - 1
    while left_pointer <= right_pointer:
        if left_pointer != right_pointer:
            total: int = data_other[left_pointer] + data_other[right_pointer]
        else:
            total: int = data_other[left_pointer]
        if total <= limit:
            platforms += 1
            left_pointer += 1
            right_pointer -= 1
        elif total > limit:
            platforms += 1
            right_pointer -= 1
        else:
            left_pointer += 1
    return platforms


if __name__ == '__main__':
    print(main(data, limit))
