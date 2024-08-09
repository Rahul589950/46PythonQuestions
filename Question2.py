# Define a function max_of_three()that takes three numbers as arguments and returns the largest of them.

def max_of_three(num1,num2,num3):
    max = 0
    if (num1 >= num2):
        max = num1
    else:
        max = num2
    
    if num3 >= max:
        return num3
    else:
        return max
    

print(max_of_three(1,5,8))
print(max_of_three(0,2,1))
print(max_of_three(1,2,3))

