def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 0:
        return 0
    if n == 1:
        return 1

    return fib_recursive(n-1) + fib_recursive(n-2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm
    n>=0
    :param n: number of item
    :return: Fibonacci number
    """

    if n == 0:       # first fibonacci number
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(n - 1):
        a, b = b, a + b

    return b


def generator_fib(n):
    """
    возвращает первые n чисел фибоначи
    :param n:
    :return:
    """
    a = 0
    yield a

    b = 1
    yield b

    for _ in range(n - 2):
        a, b = b, a + b
        yield b
N = 10

list_fib_iterative = [fib_iterative(i) for i in range(N)]
list_generator = [num for num in generator_fib(N)]

if __name__ == '__main__':
    fib_recursive(8)