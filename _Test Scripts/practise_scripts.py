#fibonacci

def print_fibo(n):
    
    if n < 0:
        print("cannot print fibonacci series for a negative number")
        return
    elif n == 0:
        print(0)
        return
    else:
        a = 0
        b = 1
        print(a)
        for _ in range(n):
            print(b)
            b,a = a + b, b

def print_fibo_rec(n):
    if n <= 1:
        return n
    else:
        return print_fibo_rec(n-1) + print_fibo_rec(n-2)

if __name__ == "__main__":
    print_fibo(10)
    for i in range(10):
        print(print_fibo_rec(i))
    