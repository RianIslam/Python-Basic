def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

even_number = []
starting = 0
user_input = int(input("Limit : "))

for num in range(0,user_input):
    if is_even(num):
        even_number.append(num)

print(f"Even numbers : {even_number}")
print(f"Finish")