
#Description
#"Write a Python function that takes three integers as input and adds addition and multiplication operators between the numbers to maximize the result value.

def expression(num1,num2,num3):
    result1 = num1 + num2 * num3
    result2 = num1 * (num2 + num3)
    result3 = num1 * num2 * num3
    result4 = (num1 + num2) * num3
    
    max1=max(result1,result2)
    max2=max(result3,result4)

    return max(max1,max2)
result = expression(1,2,3)
print(result)