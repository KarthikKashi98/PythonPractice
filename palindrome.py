"""this function takes string as a parameter then checks whether it is a palindrome or not and return boolean result"""

def isPalindrome(str):

    r=list(str)
    r.reverse()

    rev="".join(r)


    if str == rev:
        return 1
    else:

        return 0


str=input("enter a valid string")
if isPalindrome(str):
    print(str," is a palindrome")
else:
    print(str," is not a palindrome")