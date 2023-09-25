#Description
"""
Build a function that receives an integer and a string.
The purpose of the function is to calculate the sum of even or odd numbers up to
the entered integer based on the specified category (even or odd) and return the total sum.
"""

def SumNumber(num,category):
    total=0
    if category=='even':
        for i in range(num):
            if i%2==0:
                total+=i
        return total

    if category=='odd':
        for i in range(num):
            if i%2==1:
                total+=i
            return total
        
result = SumNumber(11,'even')
print(result)