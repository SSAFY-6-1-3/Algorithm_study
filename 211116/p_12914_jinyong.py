memo = [0] * 2001
memo[1], memo[2] = 1, 2


def solution(n):
    """
    1 칸을 뛰어야 하는 경우 : (1) => 1가지 방법
    2 칸을 뛰어야 하는 경우 : (1, 1), (2) => 2가지 방법
    3 칸을 뛰어야 하는 경우 : (1, 1, 1), (1, 2), (2, 1) => 3가지 방법
    4 칸을 뛰어야 하는 경우 : (1, 1, 1, 1), (1, 2, 1), (2, 1, 1), (1, 1, 2), (2, 2) => 5가지 방법
    즉, n 칸을 뛰어야 하는 경우의 수는 n-1 칸의 경우의 수 + n-2 칸의 경우의 수가 된다.
    """
    if memo[n]:
        return memo[n]

    for i in range(3, n+1):
        memo[i] = (memo[i-1] + memo[i-2]) % 1234567

    return memo[n]


print(solution(5))