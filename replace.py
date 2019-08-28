def replace(mstring,sstring,str):
   return mstring.replace(sstring, str)




main_string=input("enter the  main string")
sub_string=input("enter the  string which is to be replaced in the main string")
str=input("enter the replaceable string ")

s=replace(main_string,sub_string,str)

print(s)