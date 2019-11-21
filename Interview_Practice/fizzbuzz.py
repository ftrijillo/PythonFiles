numbers = [45,22,14,65,97,72]

for item,num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[item] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[item] = 'fizz'
    elif num % 5 == 0:
        numbers[item] = 'buzz'

print(numbers)
