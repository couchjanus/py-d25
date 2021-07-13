# app.py
# import the fibbonacci module
import fibbonacci
# import peculiar_lib.factorial
import peculiar_lib.factorial as fac

def main():
    res = fibbonacci.fibb(3)
    print("fibbonacci = ", res)

    # res = peculiar_lib.factorial.factorial(3)
    res = fac.factorial(3)
    print("factorial = ", res)


# this means that if this script is executed, then 
# main() will be executed
if __name__ == '__main__':
    main()



