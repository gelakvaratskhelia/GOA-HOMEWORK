numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


print("გამრავლება:")
for num in numbers:
    result = num * 2
    print(f"{num} * 2 = {result}")



print("გაყოფა:")
for num in numbers:
    result = num / 2
    print(f"{num} / 2 = {result}")



print("მიმატება:")
for num in numbers:
    result = num + 5
    print(f"{num} + 5 = {result}")



print("გამოკლება:")
for num in numbers:
    result = num - 3
    print(f"{num} - 3 = {result}")





#TASK2
numbers = [10, 20, 30, 40, 50]


print("სია თითოეული მნიშვნელობით:")
for num in numbers:
    print(num)


new_numbers = [num * 2 for num in numbers]

print("სია თითოეული მნიშვნელობის ჩანაცვლებით:")
for new_num in new_numbers:
    print(new_num)

my_list = [10, 20, 30, 40, 50]

desired_value = int(input("შეიყვანეთ სასურველი მნიშვნელობა: "))

if desired_value in my_list:
    print("შეტანილი მნიშვნელობა მოიძებნა სიაში.")
else:
    print("შეტანილი მნიშვნელობა არ მოიძებნა სიაში.")
