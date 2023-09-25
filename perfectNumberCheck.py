"""
"اكتب دالة تستقبل عددًا صحيحًا موجبًا وتحدد ما إذا كان هذا العدد مثاليًا أم لا. 
العدد المثالي يكون مجموع قواسمه الصحيحة (باستثناء الرقم نفسه)
"""

def perfectNumberCheck(number):
    divisorSum= 0
    for i in range(1,number+1):
        if i!=number:
            if number%i==0:
                divisorSum +=i
    if number == divisorSum:
        return True
    else:
        return False
result = perfectNumberCheck(28)
print(result)