# Fibonacci Sequence Generator

def gen_fibonacci(n):
    '''Generates a fibonacci sequence
    with n size
    '''
    i = 0
    j = 1
    res = []
    a = 0
    while(a < n):
        res.append(i)
        x = j
        j = i+j
        i = x
        a += 1
    return (res)

def main():
    print(gen_fibonanacci(int(input('How many fib numbers are needed? '))))
    
if __name__ == '__main__':
    main()