import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    n = int(input_data[0])
    a = list(map(int, input_data[1:n+1]))

    last_pos = {}
    max_len = 0
    left = 0

    for right in range(n):
        val = a[right]
        if val in last_pos and last_pos[val] >= left:
            left = last_pos[val] + 1

        last_pos[val] = right
        max_len = max(max_len, right - left + 1)

    print(max_len)

if __name__ == '__main__':
    main()