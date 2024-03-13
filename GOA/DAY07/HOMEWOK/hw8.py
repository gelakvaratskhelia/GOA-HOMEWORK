# name = input("თქვენი სახელი! ")
# password = input("თქვენი პაროლი! ")

# confirm_password = "GelaK12"
# if confirm_password == password:
#     print("პაროლი სწორია")
# else:
#     confirm_password != password
#     print("პაროლი არასწორია")

name = input("თქვენი სახელი! ")
password = input("თქვენი პაროლი! ")

confirm_password = "GelaK12"

if confirm_password == password:
    print("პაროლი სწორია")
else:
    repeat_password = input("გთხოვთ, გადაამოწმოთ პაროლი: ")
    
    if repeat_password == password:
        print("თქვენ წარმატებით დარეგისტრირდით!")
    else:
        print("პაროლი არასწორია")
