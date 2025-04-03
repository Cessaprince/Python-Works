#PRACTICE ASSIGNMENT

"""Program that returns the lcm of two numbers"""

num1 = int(input('Enter a number :'))
num2 = int(input('Enter another number :'))



for num in range(2, 1000):
    if num % num1 == 0 and num % num2 == 0:
        smallest_multiple = num
        break

print(f'The LCM of {num1} and {num2} is {smallest_multiple}') 


"""Program that returns hcf of two numbers"""


num1 = int(input('Enter a number :'))
num2 = int(input('Enter another number :'))

for num in range(2, 1000):
    if num1 % num == 0 and num2 % num == 0: 
        result = True
        if result is True:
            result = num
        elif num > result:
            result = num    
print(f'The HCF of {num1} and {num2} is {result}')