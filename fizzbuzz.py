# Get integer from user
user_num =  int(input("Hello, there! Enter some positive integer: "))

# Print user_num for debugging
# print(user_num)

# Iteration
for i in range (1, user_num+1):
    if i % 15 == 0:
        print('fizzbuzz')
    elif i % 3 == 0:
        print('fizz')
    elif i % 5 == 0:
        print('buzz')
    else:
        print(f"{i} ")
