def fectorial(n):
    print(n, '*', end=' ')
    if n == 0:
        return 1
    else:
        return n * fectorial(n - 1)
    
if __name__ == '__main__':  
    print('\n',fectorial(10))