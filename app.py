

def fibo(x: int) -> int:
    if x == 0:
        return 0
    elif x <= 2:
        return 1
    return fibo(x-1) + fibo(x-2)

print(fibo(19))