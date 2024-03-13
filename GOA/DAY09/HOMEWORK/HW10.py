programming_languages = ["Python", "Java", "JavaScript", "CSS", "C+"]

print("პროგრამირების ენების სია:", programming_languages)
print("ბოლო ენა სიაში:", programming_languages[-1])


mixed_list = ["რაიმე",   42, 3.14, True]
string_element = mixed_list[0]
integer_element = mixed_list[1]
float_element = mixed_list[2]
boolean_element = mixed_list[3]
print("სტრინგის ელემენტი:", string_element)
print("მთელი რიცხვის ელემენტი:", integer_element)
print("წილადი რიცხვის ელემენტი:", float_element)
print("ლოგიკური მნიშვნელობის ელემენტი:", boolean_element)


multiples_of_4 = [i for i in range(0, 21, 4)]
largest_multiple_of_4 = max(multiples_of_4)
print("4-ის ჯერადი რიცხვები 0-დან 20-მდე:", multiples_of_4)
print("უდიდესი რიცხვი 4-ის ჯერადი სიისაში:", largest_multiple_of_4)


odd_numbers = [num for num in range(30, 51) if num % 2 != 0]
odd_numbers.sort()
sum_of_smallest_three = sum(odd_numbers[:3])
print("30-დან 50-მდე ლუწი რიცხვების სია:", odd_numbers)
print("სამი უმცირესი ელემენტის ჯამი:", sum_of_smallest_three)

multiples_of_three = [num for num in odd_numbers if num % 3 == 0]
print("3-ის ჯერადი რიცხვები:", multiples_of_three)