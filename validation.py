"""Write a function that takes input
Array of string "valid_array" e.g. ["name", "email", "password"]
Json object "data_for_validation"
Validate if all keys from "valid_array" are present in JSON Object "data_for_validation".
If all keys are present return true else return False.

Valid_arry = [“name”, “email_id”]
Case_1 data_for_validation: { “name”: “Saurabh”, “email_id”: “saurabh@learnerbee.in” }
Case_1 data_for_validation: { “email_id”: “saurabh@learnerbee.in” }
"""

arr=["karthik","karthikkashi98@gmail.com","123"]

def valid_length(json_input):
     if(len(json_input)==3):
         return True
     return False
def valid_name(json_input):
    if(json_input["name"]!=arr[0]):
        return True
    return False
def valid_mail(json_input):
    if(json_input["mail"]!=arr[1]):
        return True
    return False
def valid_pass(json_input):
    if(json_input["pass"]!=arr[2]):
        return True
    return False



found=1
json={"name":"karthik","mail":"karthikkashi98@gmail.com","pass":"123"}
if(valid_length(json)):
    if(valid_name(json)):
        print("name is not matching")
        found=0
    if(valid_mail(json)):
        print("mail adrress is not matching")
        found = 0
    if valid_pass(json):
        print("password is not matching")
        found = 0
else:
    print("u missed to fill some stuff")
    found = 0

if found==1:
    print("yours entry details are correct")










