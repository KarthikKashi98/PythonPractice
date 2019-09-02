

"""this fun will returns list of all divisors of a number
:param: an integer number"""


def divisor(n):
    a=[]
    a.append(1)
    print("list of divisor of a number are\n")
    for i in range(int(n/2)+1):
        for j in range(int(n/2+1)):
            if(i*j == n):
                a.append(i)
    return a


if __name__ == '__main__':
    print("enter one number ")
    n = int(input())
    # fun call

    a=divisor(n)
    print(a)

