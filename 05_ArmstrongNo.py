class Solution
def arms(self,num):
    original=num
    temp=num
    total=0
    count = len(str(num))
    while num>0:
        digit=temp%10
        total = total + pow(digit,count)
        temp=temp//10
    if original==total:
        print("It is an Armstrong Number")
    else:
        print("Not an Armstrong Number")
