"""this function takes integer no as a parameter  and checks whether it is prime or not and return boolean values"""
# this function works correctly only  when input no is less than 10,00,000



def isprime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(n/2+1)):
        if n%i == 0:
            return False
    return True


if __name__ == "__main__":

    n = int(input("enter the number"))
    if isprime(n):
        print("it is prime number")
    else:
        print("it is not a prime number")