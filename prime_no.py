"""this function takes integer no as a parameter  and checks whether it is prime or not and return boolean values"""
# this function works correctly only  when input no is less than 10,00,000



def isprime(n):

    for i in range(2,int(n/2+1)):
        if n%i == 0:
            return False
    return True

def isprime1(n):
    if(n==0 or n==1):
        return False
    if(n==3 or n==5 or n==2):
        return True
    if(n%6==5) or (n%6==1):
        b=(isprime(n))
        return b

    return False



if __name__ == "__main__":

    n = int(input("enter the number"))
    count=0
    for i in range(n):
        if isprime1(i):
            print(i)
            count+=1
    print(count)


