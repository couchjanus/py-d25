def fibb(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)

if __name__ == "__main__":
   n = int(input())
   print(fibb(n))
